"""
insert_images_tutorial.py

1. Extrahiert alle Figures aus IDA_ICE_Tutorial_brdj.pdf (PyMuPDF)
2. Speichert sie als PNG in data/assets/IDA_ICE_Tutorial/
3. Ersetzt "Abbildung 1.X: ..." Zeilen in den .md-Dateien durch
   ![[...]] Bild-Embed + kursive Beschriftung

Hinweise:
  - Abbildung 1.4 (Wählen Bestandsgebäude) ist im PDF nur als Vektorgrafik
    vorhanden (dünner Toolbar-Strip, 1189×75 px) – wird übersprungen.
  - Alle anderen 56 Figures (1.1–1.3, 1.5–1.57) werden extrahiert.

Figure-zu-Seite-Mapping (aus Scan ermittelt):
  S. 9 → 1.1, 1.2       S.10 → 1.3         S.12 → 1.5, 1.6
  S.13 → 1.7, 1.8       S.14 → 1.9, 1.10   S.15 → 1.11, 1.12
  S.16 → 1.13           S.17 → 1.14         S.18 → 1.15
  S.19 → 1.16           S.20 → 1.17         S.21 → 1.18, 1.19
  S.22 → 1.20           S.23 → 1.21, 1.22   S.24 → 1.23
  S.25 → 1.24           S.26 → 1.25         S.27 → 1.26
  S.28 → 1.27           S.29 → 1.28, 1.29   S.30 → 1.30, 1.31
  S.31 → 1.32           S.32 → 1.33, 1.34, 1.35
  S.33 → 1.36, 1.37     S.34 → 1.38         S.35 → 1.39, 1.40
  S.36 → 1.41           S.37 → 1.42, 1.43   S.38 → 1.44
  S.39 → 1.45           S.41 → 1.46         S.44 → 1.47, 1.48
  S.45 → 1.49           S.46 → 1.50         S.47 → 1.51
  S.48 → 1.52           S.49 → 1.53, 1.54   S.50 → 1.55, 1.56
  S.51 → 1.57
"""

import re
import sys
import io
from pathlib import Path

try:
    import fitz  # PyMuPDF
except ImportError:
    raise SystemExit("PyMuPDF fehlt – bitte: pip install pymupdf")

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

PDF_PATH = Path(r"C:\Users\schin\Downloads\IDA_ICE_Tutorial_brdj.pdf")
MD_DIR   = Path(r"C:\Users\schin\OneDrive\Desktop\Wissens_db\data\IDA_ICE_Tutorial")
ASSETS   = Path(r"C:\Users\schin\OneDrive\Desktop\Wissens_db\data\assets\IDA_ICE_Tutorial")
MIN_DIM  = 100  # minimale Pixelgrösse (überspringt Icons & Trennleisten)


# ── Figure-Nummer → .md-Datei ─────────────────────────────────────────────────

FIGURE_FILE = {
    **{f"1.{n}": "01_1_Modell_Grundsaetzliches.md"       for n in range(1,  5)},
    **{f"1.{n}": "01_2a_Variante0_Schritte1_7.md"        for n in range(5,  16)},
    **{f"1.{n}": "01_2b_Variante0_Geometrie.md"          for n in range(16, 30)},
    **{f"1.{n}": "01_2c_Variante0_Simulation.md"         for n in range(30, 38)},
    **{f"1.{n}": "01_2d_Kalibrieren.md"                  for n in range(38, 41)},
    **{f"1.{n}": "01_3a_Varianten_Erstellen.md"          for n in range(41, 46)},
    "1.46":      "01_3b_Basisvarianten.md",
    **{f"1.{n}": "01_3c_Untervarianten.md"               for n in range(47, 53)},
    **{f"1.{n}": "01_4a_Heizlast_Systemnachweis.md"      for n in range(53, 57)},
    "1.57":      "01_4b_Jahresenergiebedarf.md",
}


# ── Seite → [Figure-Nummern in visueller Reihenfolge] ────────────────────────

PAGE_FIGURES = {
    9:  ["1.1", "1.2"],
    10: ["1.3"],               # Abb 1.4 = Vektorgrafik (kein Rasterbild)
    12: ["1.5", "1.6"],
    13: ["1.7", "1.8"],
    14: ["1.9", "1.10"],
    15: ["1.11", "1.12"],
    16: ["1.13"],
    17: ["1.14"],
    18: ["1.15"],
    19: ["1.16"],
    20: ["1.17"],
    21: ["1.18", "1.19"],
    22: ["1.20"],
    23: ["1.21", "1.22"],
    24: ["1.23"],
    25: ["1.24"],
    26: ["1.25"],
    27: ["1.26"],
    28: ["1.27"],
    29: ["1.28", "1.29"],
    30: ["1.30", "1.31"],
    31: ["1.32"],
    32: ["1.33", "1.34", "1.35"],
    33: ["1.36", "1.37"],
    34: ["1.38"],
    35: ["1.39", "1.40"],
    36: ["1.41"],
    37: ["1.42", "1.43"],
    38: ["1.44"],
    39: ["1.45"],
    41: ["1.46"],
    44: ["1.47", "1.48"],
    45: ["1.49"],
    46: ["1.50"],
    47: ["1.51"],
    48: ["1.52"],
    49: ["1.53", "1.54"],
    50: ["1.55", "1.56"],
    51: ["1.57"],
}


# ── Hilfsfunktionen ───────────────────────────────────────────────────────────

def fig_filename(fig_num: str) -> str:
    """'1.5' → 'fig_1_5.png'"""
    return "fig_" + fig_num.replace(".", "_") + ".png"


def get_images_sorted(doc, page_num: int):
    """
    Gibt Liste von (xref, width, height) zurück, sortiert nach
    vertikaler Position (oben → unten).
    Bilder kleiner als MIN_DIM werden übersprungen.
    """
    page = doc[page_num - 1]

    # Positionen aus rawdict holen
    pos_map = {}  # xref → y0
    try:
        raw = page.get_text("rawdict", flags=0)
        for block in raw.get("blocks", []):
            if block.get("type") == 1:   # Bildblock
                xref = block.get("xref")
                if xref:
                    pos_map[xref] = block["bbox"][1]
    except Exception:
        pass  # falls rawdict nicht verfügbar, ohne Sortierung weiter

    result = []
    seen = set()
    for img in page.get_images(full=True):
        xref, w, h = img[0], img[2], img[3]
        if xref in seen:
            continue
        seen.add(xref)
        if w < MIN_DIM or h < MIN_DIM:
            continue
        y0 = pos_map.get(xref, 99999)
        result.append((y0, xref, w, h))

    result.sort(key=lambda t: t[0])
    return [(xref, w, h) for _, xref, w, h in result]


def save_image(doc, xref: int, out_path: Path) -> None:
    """Speichert ein PDF-Bild als PNG (konvertiert CMYK/CMYK+Alpha → RGB)."""
    pix = fitz.Pixmap(doc, xref)
    if pix.n > 4:
        pix = fitz.Pixmap(fitz.csRGB, pix)
    pix.save(str(out_path))
    pix = None


def insert_in_md(md_path: Path, fig_num: str, filename: str) -> bool:
    """
    Sucht die Zeile 'Abbildung 1.X: ...' im .md-File und ersetzt sie durch
      ![[../assets/IDA_ICE_Tutorial/<filename>]]
      *Abbildung 1.X: ...*
    Gibt True zurück wenn erfolgreich.
    """
    text = md_path.read_text(encoding="utf-8")
    rel  = f"../assets/IDA_ICE_Tutorial/{filename}"

    if filename in text:
        return False  # bereits eingefügt

    pattern = rf"^(Abbildung\s+{re.escape(fig_num)}\s*:.*?)$"

    def replacer(m):
        cap = m.group(1).strip()
        return f"![[{rel}]]\n*{cap}*"

    new_text, n = re.subn(pattern, replacer, text, count=1, flags=re.MULTILINE)
    if n:
        md_path.write_text(new_text, encoding="utf-8")
        return True
    return False


# ── Hauptprogramm ─────────────────────────────────────────────────────────────

def main() -> None:
    ASSETS.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(str(PDF_PATH))

    saved    = 0
    inserted = 0
    skipped  = 0

    print(f"PDF : {PDF_PATH.name}  ({len(doc)} Seiten)")
    print(f"Bilder -> {ASSETS.relative_to(ASSETS.parent.parent)}")
    print()

    for page_num in sorted(PAGE_FIGURES):
        fig_list = PAGE_FIGURES[page_num]
        imgs     = get_images_sorted(doc, page_num)

        print(f"S.{page_num:2d}  {len(imgs)} Bild(er) -> {fig_list}")

        for i, fig_num in enumerate(fig_list):
            if i >= len(imgs):
                print(f"  [FEHLT]  Abb {fig_num} – kein Bild auf Seite {page_num}")
                skipped += 1
                continue

            xref, w, h = imgs[i]
            fname      = fig_filename(fig_num)
            out_path   = ASSETS / fname

            save_image(doc, xref, out_path)
            saved += 1
            print(f"  [{w:4d}x{h:<4d}]  {fname}")

            md_file = FIGURE_FILE.get(fig_num)
            if not md_file:
                print(f"  [WARN]   Kein md-Mapping für {fig_num}")
                continue

            md_path = MD_DIR / md_file
            if insert_in_md(md_path, fig_num, fname):
                inserted += 1
                print(f"           -> in {md_file}")
            else:
                print(f"           -> bereits vorhanden oder Caption nicht gefunden")

    doc.close()

    print()
    print(f"{'='*55}")
    print(f"  {saved} Bilder gespeichert")
    print(f"  {inserted} .md-Eintraege aktualisiert")
    if skipped:
        print(f"  {skipped} Figures ohne Rasterbild (Vektorgrafik)")
    print(f"{'='*55}")
    print()
    print("Hinweis: Abbildung 1.4 (Wählen Bestandsgeb.) ist im PDF")
    print("         nur als Vektorgrafik – kein PNG extrahierbar.")


if __name__ == "__main__":
    main()
