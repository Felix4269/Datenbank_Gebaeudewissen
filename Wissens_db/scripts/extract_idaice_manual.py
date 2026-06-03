"""
extract_idaice_manual.py

Extrahiert Text aus IDAICE_Manual.pdf und befüllt die .md-Dateien
unter data/IDAICE_Manual/.

Das PDF verwendet ein proprietäres CID-Font-Encoding.
Dekodierung: Zeichen = chr(cid_wert + 29)
"""

import re
import sys
from pathlib import Path

try:
    import pdfplumber
except ImportError:
    print("pdfplumber nicht installiert. Bitte: pip install pdfplumber")
    sys.exit(1)

PDF_PATH = Path(r"C:\Users\schin\Downloads\IDAICE_Manual.pdf")
OUT_DIR = Path(__file__).parent.parent / "data" / "IDAICE_Manual"


# ── CID-Decoder ───────────────────────────────────────────────────────────────
def decode_cid(text):
    def replace(m):
        cid = int(m.group(1))
        ch = cid + 29
        if 32 <= ch <= 126:
            return chr(ch)
        if cid == 139:
            return "©"
        return " "
    return re.sub(r"\(cid:(\d+)\)", replace, text)


def clean(text):
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" \n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    # Seitenkopf (Header) entfernen: "IDA Indoor Climate and Energy 4.8 ..."
    text = re.sub(
        r"IDA Indoor Climate and Energy 4\.8\s+©\s+EQUA Simulation AB 2018\s*\n",
        "",
        text,
    )
    return text.strip()


# ── Kapitel-Konfiguration ─────────────────────────────────────────────────────
# pages: (erste, letzte) – 1-basiert, inklusiv
CHAPTERS = [
    {
        "file":      "01_About_the_Manual.md",
        "kap":       "Kap. 1",
        "title":     "About the Manual",
        "tags":      "[IDA-ICE, Manual, Simulation, Gebäudesimulation]",
        "pages":     (6, 7),
        "prev":      "*(Anfang)*",
        "prev_link": None,
        "next":      "Kap. 2",
        "next_link": "02_Basic_Principles",
    },
    {
        "file":      "02_Basic_Principles.md",
        "kap":       "Kap. 2",
        "title":     "Basic Principles of IDA ICE",
        "tags":      "[IDA-ICE, Simulation, Grundlagen, Architektur]",
        "pages":     (8, 10),
        "prev":      "Kap. 1",
        "prev_link": "01_About_the_Manual",
        "next":      "Kap. 3.1",
        "next_link": "03_1_Model_Description_Intro",
    },
    {
        "file":      "03_1_Model_Description_Intro.md",
        "kap":       "Kap. 3.1",
        "title":     "Model Description – Introduction & Primary System",
        "tags":      "[IDA-ICE, Modell, Primärsystem, Wärmepumpe, Kessel]",
        "pages":     (11, 11),
        "prev":      "Kap. 2",
        "prev_link": "02_Basic_Principles",
        "next":      "Kap. 3.2",
        "next_link": "03_2_Primary_System_Plant",
    },
    {
        "file":      "03_2_Primary_System_Plant.md",
        "kap":       "Kap. 3.2",
        "title":     "Model Description – Primary System Plant (Detail)",
        "tags":      "[IDA-ICE, ESBO, Wärmeanlage, Lüftungsanlage, Anlagentechnik]",
        "pages":     (12, 22),
        "prev":      "Kap. 3.1",
        "prev_link": "03_1_Model_Description_Intro",
        "next":      "Kap. 3.3",
        "next_link": "03_3_Zone_Models_HVAC",
    },
    {
        "file":      "03_3_Zone_Models_HVAC.md",
        "kap":       "Kap. 3.3",
        "title":     "Model Description – Zone Models & HVAC",
        "tags":      "[IDA-ICE, Zonenmodell, HVAC, Strahlung, Hydronik]",
        "pages":     (23, 32),
        "prev":      "Kap. 3.2",
        "prev_link": "03_2_Primary_System_Plant",
        "next":      "Kap. 3.4",
        "next_link": "03_4_Building_Geometry",
    },
    {
        "file":      "03_4_Building_Geometry.md",
        "kap":       "Kap. 3.4",
        "title":     "Building Geometry – CAD & Image Import",
        "tags":      "[IDA-ICE, CAD, IFC, Geometrie, Import]",
        "pages":     (33, 38),
        "prev":      "Kap. 3.3",
        "prev_link": "03_3_Zone_Models_HVAC",
        "next":      "Kap. 4",
        "next_link": "04_Getting_Started_Advanced",
    },
    {
        "file":      "04_Getting_Started_Advanced.md",
        "kap":       "Kap. 4",
        "title":     "Getting Started – Advanced Level",
        "tags":      "[IDA-ICE, Advanced, Equationsystem, Beispiel]",
        "pages":     (39, 43),
        "prev":      "Kap. 3.4",
        "prev_link": "03_4_Building_Geometry",
        "next":      "Kap. 5",
        "next_link": "05_Tips_Tricks",
    },
    {
        "file":      "05_Tips_Tricks.md",
        "kap":       "Kap. 5",
        "title":     "Tips & Tricks / Numerical Instabilities",
        "tags":      "[IDA-ICE, Tipps, Numerik, Performance, Instabilität]",
        "pages":     (44, 46),
        "prev":      "Kap. 4",
        "prev_link": "04_Getting_Started_Advanced",
        "next":      "*(Ende)*",
        "next_link": None,
    },
]


# ── Heading-Formatierung ──────────────────────────────────────────────────────
CLAUSE_STARTERS_EN = (
    "The ", "A ", "An ", "This ", "These ", "In ", "For ", "With ",
    "If ", "When ", "Each ", "All ", "It ", "As ", "By ", "On ",
    "At ", "To ", "From ", "After ", "Before ", "During ", "Both ",
    "There ", "Most ", "Some ", "One ", "Many ", "Note ", "See ",
    "Since ", "However ", "Although ", "Because ", "Due ",
)
CONTINUATION_ENDINGS = (" or", " and", " as", " of", " the", " a", " an", " is")
NUM_RE = re.compile(r"^(\d+(?:\.\d+)*)\.\s+(.+)$")
LEVELS = {1: "##", 2: "###", 3: "####", 4: "#####"}


def apply_headings(text):
    lines = text.splitlines()
    result = []
    for i, line in enumerate(lines):
        m = NUM_RE.match(line.strip())
        if not m:
            result.append(line)
            continue
        number, txt = m.group(1), m.group(2).strip()
        orig = line.strip()
        if len(orig) > 80 or txt.endswith(".") or ". " in txt:
            result.append(line)
            continue
        if any(orig.endswith(e) for e in CONTINUATION_ENDINGS):
            result.append(line)
            continue
        if any(txt.startswith(s) for s in CLAUSE_STARTERS_EN):
            result.append(line)
            continue
        next_l = lines[i + 1].strip() if i + 1 < len(lines) else ""
        if next_l and next_l[0].islower():
            result.append(line)
            continue
        depth = number.count(".") + 1
        prefix = LEVELS.get(depth, "#####")
        result.append(f"{prefix} {orig}")
    return "\n".join(result)


# ── .md-Datei schreiben ───────────────────────────────────────────────────────
def write_md(chap, content):
    if chap["prev_link"]:
        prev_part = f"[[{chap['prev_link']}|◀ {chap['prev']}]]"
    else:
        prev_part = f"◀ {chap['prev']}"
    if chap["next_link"]:
        next_part = f"[[{chap['next_link']}|{chap['next']} ▶]]"
    else:
        next_part = f"{chap['next']} ▶"
    nav = f"> {prev_part}  ·  [[_IDAICE_Manual_MOC|↑ Inhaltsverzeichnis]]  ·  {next_part}"

    md = f"""---
tags: {chap['tags']}
normnummer: "IDAICE Manual v4.8"
gueltig_ab: "2018-01-01"
kapitel: "{chap['kap']}"
titel: "{chap['title']}"
---

# {chap['kap']} – {chap['title']}

{nav}

---

{content}
"""
    path = OUT_DIR / chap["file"]
    path.write_text(md, encoding="utf-8")
    print(f"  OK {chap['file']}  ({len(content):,} Zeichen)")


# ── Hauptprogramm ─────────────────────────────────────────────────────────────
def main():
    print(f"Lese: {PDF_PATH}")
    pages_raw = {}
    with pdfplumber.open(PDF_PATH) as pdf:
        total = len(pdf.pages)
        print(f"  {total} Seiten gefunden.")
        for i, page in enumerate(pdf.pages):
            raw = page.extract_text() or ""
            pages_raw[i + 1] = decode_cid(raw)

    print("\nErstelle .md-Dateien …")
    for chap in CHAPTERS:
        p_start, p_end = chap["pages"]
        texts = [pages_raw.get(p, "") for p in range(p_start, p_end + 1)]
        combined = "\n\n".join(texts)
        content = apply_headings(clean(combined))
        write_md(chap, content)

    print("\nFertig.")


if __name__ == "__main__":
    main()
