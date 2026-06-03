"""
extract_sia_384_6.py

Rendert alle Figuren aus der SIA 384-6:2021 PDF als hochauflösende PNGs
und fügt sie in die entsprechenden Markdown-Dateien ein.

Ausführung:  py scripts/extract_sia_384_6.py
"""

import re, sys, io
from pathlib import Path
import fitz  # PyMuPDF

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

DATA_ROOT = Path(__file__).parent.parent / "data"
ASSETS    = DATA_ROOT / "assets" / "SIA_384-6_2021"
MD_DIR    = DATA_ROOT / "SIA_384-6_2021"
PDF_PATH  = "C:/Users/schin/Downloads/SN 546384-6 SIA 384-6_2021_d.pdf"

ASSETS.mkdir(parents=True, exist_ok=True)

# Seite (1-basiert) → Liste von (Dateiname, Ziel-md, Suchschlüssel-für-Einfügepunkt)
PAGE_MAP = {
     6: [("figur_1_uebersicht_erdwaermenutzung.png",       "00_Geltungsbereich.md",                   "Figur 1")],
    25: [("Figur_2_GSF_eff.png",                           "03_5_nachbarsonden.md",                   "Figur 2"),
         ("Figur_3_Temperaturabkuehlung.png",              "03_5_nachbarsonden.md",                   "Figur 3")],
    46: [("figur_4_druckverlust_ews_kreis.png",            "03_2_3_4_systemoptimierung_berechnung.md","Figur 4")],
    47: [("figur_5_druckverlust_faktor.png",               "03_2_3_4_systemoptimierung_berechnung.md","Figur 5")],
    51: [("figur_6_dichtheitspruefung_ews.png",            "06_Pruefungen.md",                        "Figur 6")],
    53: [("figur_7_langzeitpruefung.png",                  "06_Pruefungen.md",                        "Figur 7")],
    56: [("figur_8_bodenoberflaeche.png",                  "Anhang_C_Kennwerte.md",                   "Figur 8")],
    63: [("figur_9_normleistung_de32.png",                 "03_2_3_4_systemoptimierung_berechnung.md","Figur 9"),
         ("figur_10_normleistung_de40.png",                "03_2_3_4_systemoptimierung_berechnung.md","Figur 10")],
    64: [("figur_11_zuschlag_simplex.png",                 "03_2_3_4_systemoptimierung_berechnung.md","Figur 11")],
    65: [("figur_12_volllaststunden.png",                  "03_2_3_4_systemoptimierung_berechnung.md","Figur 12")],
    67: [("figur_13_zuschlag_volllaststunden.png",         "03_2_3_4_systemoptimierung_berechnung.md","Figur 13")],
    68: [("figur_14_zuschlag_volllaststunden.png",         "03_2_3_4_systemoptimierung_berechnung.md","Figur 14"),
         ("figur_15_zuschlag_volllaststunden.png",         "03_2_3_4_systemoptimierung_berechnung.md","Figur 15")],
    69: [("figur_16_zuschlag_volllaststunden.png",         "03_2_3_4_systemoptimierung_berechnung.md","Figur 16"),
         ("figur_17_zuschlag_volllaststunden.png",         "03_2_3_4_systemoptimierung_berechnung.md","Figur 17")],
    70: [("figur_18_zuschlag_volllaststunden.png",         "03_2_3_4_systemoptimierung_berechnung.md","Figur 18"),
         ("figur_19_zuschlag_volllaststunden.png",         "03_2_3_4_systemoptimierung_berechnung.md","Figur 19")],
    71: [("figur_20_zuschlag_volllaststunden.png",         "03_2_3_4_systemoptimierung_berechnung.md","Figur 20"),
         ("figur_21_zuschlag_volllaststunden.png",         "03_2_3_4_systemoptimierung_berechnung.md","Figur 21")],
    77: [("figur_22_temperaturabkuehlung_nachbar.png",     "03_5_nachbarsonden.md",                   "Figur 22")],
    78: [("figur_23_lastprofil_ews.png",                   "03_2_3_4_systemoptimierung_berechnung.md","Figur 23")],
    80: [("figur_24_druckverlust_glycol.png",              "Anhang_C_Kennwerte.md",                   "Figur 24"),
         ("figur_25_druckverlust_glycol_visk.png",         "Anhang_C_Kennwerte.md",                   "Figur 25")],
    81: [("figur_26_hydraulische_leistung_ews.png",        "Anhang_C_Kennwerte.md",                   "Figur 26"),
         ("figur_27_druckverlust_pe_rohr.png",             "Anhang_C_Kennwerte.md",                   "Figur 27")],
    82: [("figur_28_hydraulische_leistung_pe.png",         "Anhang_C_Kennwerte.md",                   "Figur 28"),
         ("figur_29_druckverlust_faktor_glycol.png",       "Anhang_C_Kennwerte.md",                   "Figur 29")],
    94: [("figur_30_prinzipschema_einzelsonde.png",        "Anhang_F_Ausfuehrung.md",                 "Figur 30")],
    95: [("figur_31_prinzipschema_y.png",                  "Anhang_F_Ausfuehrung.md",                 "Figur 31"),
         ("figur_32_prinzipschema_ohne_y.png",             "Anhang_F_Ausfuehrung.md",                 "Figur 32")],
    96: [("figur_33_geocooling.png",                       "Anhang_F_Ausfuehrung.md",                 "Figur 33")],
}


def render_page(doc, page_num: int, out_path: Path, zoom: float = 2.0):
    """Rendert eine PDF-Seite als PNG."""
    if out_path.exists():
        return False   # bereits vorhanden
    mat = fitz.Matrix(zoom, zoom)
    pix = doc[page_num - 1].get_pixmap(matrix=mat)
    pix.save(str(out_path))
    pix = None
    return True


def insert_into_md(md_path: Path, filename: str, search_key: str, caption: str):
    """
    Fügt ![[filename]] und *caption* nach der ersten Zeile ein,
    die search_key enthält. Wird übersprungen wenn filename schon im Text.
    """
    if not md_path.exists():
        print(f"    SKIP (Datei nicht gefunden): {md_path.name}")
        return

    text = md_path.read_text(encoding="utf-8")
    if filename in text:
        return   # bereits eingefügt

    lines = text.splitlines(keepends=True)
    block = f"\n![[{filename}]]\n*{caption}*\n"

    # Suche nach der Figur-Referenz im Text
    for i, line in enumerate(lines):
        if search_key in line:
            lines.insert(i + 1, block)
            md_path.write_text("".join(lines), encoding="utf-8")
            print(f"    ✓ eingefügt nach Zeile {i+1} in {md_path.name}")
            return

    # Nicht gefunden → am Ende anhängen
    with md_path.open("a", encoding="utf-8") as f:
        f.write(f"\n\n{block}")
    print(f"    ✓ am Ende angehängt in {md_path.name}")


def main():
    doc = fitz.open(PDF_PATH)
    total = 0
    rendered_pages = {}   # page_num → rendered pixmap path (für Seiten mit mehreren Figuren)

    print(f"\n{'═'*60}")
    print(f"  SIA 384-6:2021 — {len(PAGE_MAP)} Seiten mit Figuren")
    print(f"{'═'*60}")

    for page_num in sorted(PAGE_MAP.keys()):
        entries = PAGE_MAP[page_num]
        page = doc[page_num - 1]

        # Seite einmal rendern (erste Datei)
        first_fname = entries[0][0]
        first_path  = ASSETS / first_fname
        rendered = render_page(doc, page_num, first_path)

        # Für weitere Figuren auf derselben Seite: Datei kopieren
        import shutil
        for i, (fname, md_name, search_key) in enumerate(entries):
            out_path = ASSETS / fname
            if i > 0 and not out_path.exists():
                shutil.copy(str(first_path), str(out_path))
                print(f"  S.{page_num:3d} kopiert → {fname}")
            elif i == 0:
                status = "neu" if rendered else "vorhanden"
                print(f"  S.{page_num:3d} [{status}] → {fname}")

            # Figur-Caption aus PDF-Text ermitteln
            page_text = page.get_text()
            cap_match = re.search(
                rf"{re.escape(search_key)}\s*[:\–\—]?\s*(.{{0,120}})", page_text
            )
            caption = cap_match.group(0).strip() if cap_match else search_key

            # In Markdown-Datei einfügen
            md_path = MD_DIR / md_name
            insert_into_md(md_path, fname, search_key, caption)
            total += 1

    doc.close()
    print(f"\n  → {total} Figuren verarbeitet")
    print(f"  → Assets in: data/assets/SIA_384-6_2021/")


if __name__ == "__main__":
    main()
