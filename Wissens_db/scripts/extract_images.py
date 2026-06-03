"""
extract_images.py

Extracts all images from the three Skript-PDFs and inserts them into the
corresponding Obsidian markdown files.

Strategy:
  - Pages with 1–3 images : extract embedded JPEG/PNG objects directly.
  - Pages with 4+ images  : render the full page as PNG (2× zoom).
  - Images smaller than MIN_DIM px in either dimension are skipped.
  - When multiple images on one page share a caption, a numeric suffix is added.
  - Image links are inserted directly after the matching "Abbildung X:" /
    "Tabelle X:" caption line in the target .md file.
  - Already-inserted images are never inserted twice.

Run:
    py scripts/extract_images.py
"""

import re
import sys
import io
from pathlib import Path

import fitz  # PyMuPDF

# ── Global settings ─────────────────────────────────────────────────────────────

DATA_ROOT  = Path(__file__).parent.parent / "data"
MIN_DIM    = 80    # skip images smaller than this in either axis

# ── Umlaut-safe filename helper ─────────────────────────────────────────────────

_UMLAUT = str.maketrans("äöüÄÖÜß", "aoeuOUs")  # simple ASCII transliteration

def _safe(text: str, maxlen: int = 42) -> str:
    t = text.translate(_UMLAUT)
    t = re.sub(r"[^a-z0-9]+", "_", t.lower())
    return t[:maxlen].strip("_")


def caption_filename(caption: str, suffix: str = "") -> str:
    """'Abbildung 11: Energieflussdiagramm…' → 'abb11_energieflussdiagramm…'"""
    m = re.match(r"(Abbildung|Tabelle)\s+(\d+)[:\s]*(.*)", caption, re.I)
    if m:
        kind = "abb" if m.group(1).lower() == "abbildung" else "tab"
        num  = m.group(2)
        desc = _safe(m.group(3))
        base = f"{kind}{num}_{desc}" if desc else f"{kind}{num}"
    else:
        base = _safe(caption) or "img"
    return base + suffix


# ── Caption extraction from a PDF page ─────────────────────────────────────────

def page_captions(page):
    caps = []
    for line in page.get_text().splitlines():
        s = line.strip()
        if re.match(r"^(Abbildung|Tabelle)\s+\d+\s*[:\.]", s):
            caps.append(s)
    return caps


# ── Markdown insertion ──────────────────────────────────────────────────────────

def _search_key(caption: str) -> str:
    m = re.match(r"((?:Abbildung|Tabelle)\s+\d+)", caption, re.I)
    return m.group(1) if m else caption[:30]


def insert_image(md_path: Path, caption: str, filename: str):
    """Insert ![[filename]] after the caption line; append if not found."""
    text = md_path.read_text(encoding="utf-8")
    if filename in text:          # already inserted
        return
    lines = text.splitlines(keepends=True)
    key   = _search_key(caption)
    block = f"\n![[{filename}]]\n*{caption}*\n"

    for i, line in enumerate(lines):
        if key in line:
            lines.insert(i + 1, block)
            md_path.write_text("".join(lines), encoding="utf-8")
            return

    # Caption not found → append
    with md_path.open("a", encoding="utf-8") as f:
        f.write(f"\n\n## Abbildungen\n{block}")


# ── Per-page extraction ─────────────────────────────────────────────────────────

def extract_page(doc, page_num: int, md_path: Path, assets_dir: Path) -> int:
    """Extract images from one page and insert links. Returns count saved."""
    page = doc[page_num - 1]
    imgs = page.get_images(full=True)

    # Filter out images below minimum size
    valid_imgs = []
    for img in imgs:
        xref = img[0]
        pix  = fitz.Pixmap(doc, xref)
        if pix.width >= MIN_DIM and pix.height >= MIN_DIM:
            valid_imgs.append((xref, pix.width, pix.height))
        pix = None
    if not valid_imgs:
        return 0

    captions = page_captions(page)
    saved = 0

    # Pages with 4+ images → render full page as PNG
    if len(valid_imgs) >= 4:
        cap      = captions[0] if captions else f"Seite {page_num}"
        fname    = caption_filename(cap) + ".png"
        out_path = assets_dir / fname
        mat = fitz.Matrix(2.0, 2.0)
        pix = page.get_pixmap(matrix=mat)
        pix.save(str(out_path))
        pix = None
        insert_image(md_path, cap, fname)
        print(f"    [render] {fname}")
        return 1

    # 1–3 images → extract individually
    # Build caption list: if fewer captions than images, repeat last caption
    cap_list = list(captions)
    while len(cap_list) < len(valid_imgs):
        cap_list.append(cap_list[-1] if cap_list else f"Seite {page_num} Bild {len(cap_list)+1}")

    # Track used filenames to add suffix when same caption repeats
    used: dict[str, int] = {}
    for idx, (xref, w, h) in enumerate(valid_imgs):
        cap   = cap_list[idx]
        base  = caption_filename(cap)
        used[base] = used.get(base, 0) + 1
        suffix = f"_{used[base]}" if used[base] > 1 else ""
        # Check ahead: will this base appear again?
        future = sum(1 for j in range(idx + 1, len(valid_imgs))
                     if caption_filename(cap_list[j]) == base)
        if used[base] == 1 and future > 0:
            suffix = "_1"    # first of a group → also get suffix

        pix = fitz.Pixmap(doc, xref)
        if pix.n > 4:
            pix = fitz.Pixmap(fitz.csRGB, pix)
        ext   = "png" if pix.n == 4 else "jpg"
        fname = f"{base}{suffix}.{ext}"
        pix.save(str(assets_dir / fname))
        pix = None
        insert_image(md_path, cap, fname)
        print(f"    [{w}×{h}] {fname}")
        saved += 1

    return saved


# ── PDF definitions ─────────────────────────────────────────────────────────────

PDFS = [
    {
        "slug": "Skript_Bauphysik",
        "pdf":  "C:/Users/schin/Downloads/Skript Bauphysik 2026.pdf",
        "page_map": {
            4:  "01_Grundlagen.md",
            5:  "02_Waermeverluste_Trans.md",
            6:  "02_Waermeverluste_Trans.md",
            7:  "02_Waermeverluste_Trans.md",
            9:  "02_Waermeverluste_Trans.md",
            10: "02_Waermeverluste_Trans.md",
            17: "03_6_u_wert_berechnung.md",
            21: "04_Theorie_Feuchte.md",
            23: "05_1_2_grundlagen_natuerliche_lueftung.md",
            25: "05_3_4_lufterneuerung_radon.md",
            26: "05_5_luftfeuchtigkeit.md",
            27: "05_6_7_ueberpruefung_anforderungen.md",
            28: "05_6_7_ueberpruefung_anforderungen.md",
            30: "05_8_9_mechanische_lueftung.md",
            31: "05_8_9_mechanische_lueftung.md",
            32: "05_8_9_mechanische_lueftung.md",
        },
    },
    {
        "slug": "Skript_Lueftung",
        "pdf":  "C:/Users/schin/Downloads/Skript Lüftung.pdf",
        "page_map": {
            1:  "00_Titelseite_TOC.md",
            5:  "01_Aufgaben_Einteilung.md",
            6:  "01_Aufgaben_Einteilung.md",
            8:  "02_1_schadstoffabfuhr_luftfuehrung.md",
            9:  "02_1_schadstoffabfuhr_luftfuehrung.md",
            10: "02_1_schadstoffabfuhr_luftfuehrung.md",
            12: "02_1_schadstoffabfuhr_luftfuehrung.md",
            16: "03_1_freie_lueftung.md",
            17: "03_2_mechanische_lueftung.md",
            18: "03_2_mechanische_lueftung.md",
            19: "03_2_mechanische_lueftung.md",
            20: "03_2_mechanische_lueftung.md",
            21: "04_1_nur_luft_anlagen.md",
            28: "04_2_kombinierte_anlagen.md",
            29: "04_2_kombinierte_anlagen.md",
            30: "04_2_kombinierte_anlagen.md",
            31: "04_2_kombinierte_anlagen.md",
            35: "05_1_filter.md",
            36: "05_1_filter.md",
            38: "05_2_ventilatoren.md",
            39: "05_2_ventilatoren.md",
            41: "05_3_waermerueckgewinnung.md",
            42: "05_3_waermerueckgewinnung.md",
            43: "05_4_lufterhitzer_kuehler.md",
        },
    },
    {
        "slug": "Skript_Energie",
        "pdf":  "C:/Users/schin/Downloads/Skript Energie im Gebäude 2026.pdf",
        "page_map": {
            4:  "01_Grundlagen.md",
            5:  "02_Waermeverluste.md",
            6:  "02_Waermeverluste.md",
            9:  "03_1_interne_waermegewinne.md",
            10: "03_1_interne_waermegewinne.md",
            13: "03_2_solare_waermegewinne.md",
            14: "03_2_solare_waermegewinne.md",
            17: "03_2_solare_waermegewinne.md",
            19: "04_Heizwaermebedarf.md",
            21: "04_Heizwaermebedarf.md",
            25: "05_Warmwasser.md",
            27: "05_Warmwasser.md",
            31: "06_1_berechnung_energiebedarf.md",
            33: "06_2_primaerenergie.md",
            34: "06_3_deckung_energiebedarf.md",
            35: "06_3_deckung_energiebedarf.md",
            41: "06_4_vorschriften.md",
            43: "06_5_standards_labels.md",
            44: "06_5_standards_labels.md",
            47: "06_7_nutzereinfluss.md",
            48: "06_7_nutzereinfluss.md",
            51: "07_1_bauweise_beschattung.md",
            59: "08_Anhang.md",
        },
    },
]


# ── Main ────────────────────────────────────────────────────────────────────────

def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

    grand_total = 0
    for cfg in PDFS:
        slug      = cfg["slug"]
        pdf_path  = cfg["pdf"]
        page_map  = cfg["page_map"]
        md_dir    = DATA_ROOT / slug
        assets    = DATA_ROOT / "assets" / slug
        assets.mkdir(parents=True, exist_ok=True)

        print(f"\n{'═'*60}")
        print(f"  {slug}")
        print(f"{'═'*60}")

        doc   = fitz.open(pdf_path)
        total = 0
        for page_num in sorted(page_map):
            md_file = md_dir / page_map[page_num]
            if not md_file.exists():
                print(f"  S.{page_num:3d}  SKIP (Datei fehlt: {md_file.name})")
                continue
            print(f"  S.{page_num:3d} → {page_map[page_num]}")
            n = extract_page(doc, page_num, md_file, assets)
            total += n
        doc.close()

        print(f"\n  → {total} Bilder in {assets.relative_to(DATA_ROOT.parent)}")
        grand_total += total

    print(f"\n{'═'*60}")
    print(f"  Gesamt: {grand_total} Bilder extrahiert und verlinkt.")
    print(f"{'═'*60}")


if __name__ == "__main__":
    main()
