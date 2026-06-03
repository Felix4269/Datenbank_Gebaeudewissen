"""
fix_sia_384_correct_files.py

Korrigiert die Figur-Zuordnung in SIA 384-6:
Die Figuren wurden ursprünglich den falschen Dateien zugeordnet.

PDF-Seitenstruktur:
  Kap. 3.2–3.4 (S. 18–25): KEINE eigenen Figuren (nur Verweise auf Anhänge)
  Kap. 6       (S. 33–34): KEINE eigenen Figuren (nur Verweise auf Anhang B)
  Anhang B     (S. 46–54): Figuren 4, 5, 6, 7
  Anhang C     (S. 55–60): Figur 8 (korrekt)
  Anhang D     (S. 61–85): Figuren 9–23, 24–29
  Anhang F     (S. 89–97): Figuren 30–33 (korrekt)

Schritt 1: Falsch eingefügte Bilder entfernen
Schritt 2: Bilder an richtiger Stelle einfügen (vor > **Figur X** Zeile)

Ausführung: py scripts/fix_sia_384_correct_files.py
"""

import re, sys, io
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

SIA_DIR   = Path("C:/Users/schin/OneDrive/Desktop/Wissens_db/data/SIA_384-6_2021")
ASSETS    = Path("C:/Users/schin/OneDrive/Desktop/Wissens_db/data/assets/SIA_384-6_2021")


# ──────────────────────────────────────────────────────────────
# Hilfsfunktionen
# ──────────────────────────────────────────────────────────────

def remove_image_lines(md_path: Path, filenames) -> int:
    """
    Entfernt alle Zeilen, die einen der angegebenen Dateinamen enthalten.
    Gibt die Anzahl entfernter Blöcke zurück.
    """
    text = md_path.read_text(encoding="utf-8")
    removed = 0
    for fname in filenames:
        if fname not in text:
            continue
        # Entferne Zeile mit ![[fname]] und optionale Caption-Zeile davor/danach
        # Muster: optionale Leerzeile + ![[fname]] + optionale *caption* Zeile(n)
        pattern = re.compile(
            r'\n+!\[\[' + re.escape(fname) + r'\]\]'    # ![[fname]]
            r'(?:\n\*[^\n]*\*)?'                         # optionale *caption*
            r'(?:\n[^\n!>*#\-].*?)?'                     # ggf. weiterer Caption-Text
        )
        new_text, n = pattern.subn('', text)
        if n:
            text = new_text
            removed += n
    # Mehrfache Leerzeilen normalisieren (max. 2)
    text = re.sub(r'\n{3,}', '\n\n', text)
    md_path.write_text(text, encoding="utf-8")
    return removed


def insert_before_line(md_path: Path, search_text: str, img_filename: str) -> bool:
    """
    Sucht die erste Zeile, die search_text enthält, und fügt
    ![[img_filename]] direkt davor ein.
    Überspringt, wenn img_filename bereits im Dokument.
    """
    text = md_path.read_text(encoding="utf-8")
    if img_filename in text:
        return False   # bereits vorhanden

    lines = text.splitlines(keepends=True)
    for i, line in enumerate(lines):
        if search_text in line:
            lines.insert(i, f"![[{img_filename}]]\n")
            md_path.write_text("".join(lines), encoding="utf-8")
            return True
    return False


def insert_group_before_line(md_path: Path, search_text: str, img_filenames) -> bool:
    """
    Fügt mehrere Bilder vor der Zeile mit search_text ein.
    """
    text = md_path.read_text(encoding="utf-8")
    # Prüfe ob schon eingefügt
    if all(f in text for f in img_filenames):
        return False

    lines = text.splitlines(keepends=True)
    for i, line in enumerate(lines):
        if search_text in line:
            block = "".join(f"![[{f}]]\n" for f in img_filenames)
            lines.insert(i, block)
            md_path.write_text("".join(lines), encoding="utf-8")
            return True
    return False


# ──────────────────────────────────────────────────────────────
# Schritt 1: Falsch platzierte Bilder entfernen
# ──────────────────────────────────────────────────────────────

def step1_remove_wrong_images():
    print("\n── Schritt 1: Falsch platzierte Bilder entfernen ──")

    # Kap. 3.2-3.4: Figuren 4, 5, 9-21, 23 entfernen (gehören nach Anhang B/D)
    path = SIA_DIR / "03_2_3_4_systemoptimierung_berechnung.md"
    wrong = [
        "figur_4_druckverlust_ews_kreis.png",
        "figur_5_druckverlust_faktor.png",
        "figur_9_normleistung_de32.png",
        "figur_10_normleistung_de40.png",
        "figur_11_zuschlag_simplex.png",
        "figur_12_volllaststunden.png",
        "figur_13_zuschlag_volllaststunden.png",
        "figur_14_zuschlag_volllaststunden.png",
        "figur_15_zuschlag_volllaststunden.png",
        "figur_16_zuschlag_volllaststunden.png",
        "figur_17_zuschlag_volllaststunden.png",
        "figur_18_zuschlag_volllaststunden.png",
        "figur_19_zuschlag_volllaststunden.png",
        "figur_20_zuschlag_volllaststunden.png",
        "figur_21_zuschlag_volllaststunden.png",
        "figur_23_lastprofil_ews.png",
    ]
    n = remove_image_lines(path, wrong)
    print(f"  {path.name}: {n} Bilder entfernt")

    # Kap. 6: Figuren 6, 7 entfernen (gehören nach Anhang B)
    path = SIA_DIR / "06_Pruefungen.md"
    wrong = [
        "figur_6_dichtheitspruefung_ews.png",
        "figur_7_langzeitpruefung.png",
    ]
    n = remove_image_lines(path, wrong)
    print(f"  {path.name}: {n} Bilder entfernt")

    # Anhang C: Figuren 24-29 entfernen (gehören nach Anhang D)
    path = SIA_DIR / "Anhang_C_Kennwerte.md"
    wrong = [
        "figur_24_druckverlust_glycol.png",
        "figur_25_druckverlust_glycol_visk.png",
        "figur_26_hydraulische_leistung_ews.png",
        "figur_27_druckverlust_pe_rohr.png",
        "figur_28_hydraulische_leistung_pe.png",
        "figur_29_druckverlust_faktor_glycol.png",
    ]
    n = remove_image_lines(path, wrong)
    print(f"  {path.name}: {n} Bilder entfernt")


# ──────────────────────────────────────────────────────────────
# Schritt 2: Bilder in richtige Dateien einfügen
# ──────────────────────────────────────────────────────────────

def step2_insert_into_anhang_b():
    print("\n── Schritt 2a: Anhang B – Figuren 4, 5, 6, 7 einfügen ──")
    path = SIA_DIR / "Anhang_B_Pruefungen.md"

    insertions = [
        # (search_text_in_caption_line, img_filename)
        ("> **Figur 4**",  "figur_4_druckverlust_ews_kreis.png"),
        ("> **Figur 5**",  "figur_5_druckverlust_faktor.png"),
        ("> **Figur 6**",  "figur_6_dichtheitspruefung_ews.png"),
        ("> **Figur 7**",  "figur_7_langzeitpruefung.png"),
    ]

    for search, fname in insertions:
        if not (ASSETS / fname).exists():
            print(f"  WARNUNG: Asset fehlt: {fname}")
            continue
        ok = insert_before_line(path, search, fname)
        status = "✓ eingefügt" if ok else "· bereits vorhanden"
        print(f"  {status}: {fname}")


def step2_insert_into_anhang_d():
    print("\n── Schritt 2b: Anhang D – Figuren 9–23, 24–29 einfügen ──")
    path = SIA_DIR / "Anhang_D_Projektierungshinweise.md"

    # Einzelne Figuren
    single_insertions = [
        ("> **Figur 9**",   "figur_9_normleistung_de32.png"),
        ("> **Figur 10**",  "figur_10_normleistung_de40.png"),
        ("> **Figur 11**",  "figur_11_zuschlag_simplex.png"),
        ("> **Figur 12**",  "figur_12_volllaststunden.png"),
        ("> **Figur 23**",  "figur_23_lastprofil_ews.png"),
        ("> **Figur 24**",  "figur_24_druckverlust_glycol.png"),
        ("> **Figur 25**",  "figur_25_druckverlust_glycol_visk.png"),
        ("> **Figur 26**",  "figur_26_hydraulische_leistung_ews.png"),
        ("> **Figur 27**",  "figur_27_druckverlust_pe_rohr.png"),
        ("> **Figur 28**",  "figur_28_hydraulische_leistung_pe.png"),
        ("> **Figur 29**",  "figur_29_druckverlust_faktor_glycol.png"),
    ]

    for search, fname in single_insertions:
        if not (ASSETS / fname).exists():
            print(f"  WARNUNG: Asset fehlt: {fname}")
            continue
        ok = insert_before_line(path, search, fname)
        status = "✓ eingefügt" if ok else "· bereits vorhanden"
        print(f"  {status}: {fname}")

    # Figuren 13–21 als Gruppe vor "> **Figuren 13–21**"
    group_fnames = [
        "figur_13_zuschlag_volllaststunden.png",
        "figur_14_zuschlag_volllaststunden.png",
        "figur_15_zuschlag_volllaststunden.png",
        "figur_16_zuschlag_volllaststunden.png",
        "figur_17_zuschlag_volllaststunden.png",
        "figur_18_zuschlag_volllaststunden.png",
        "figur_19_zuschlag_volllaststunden.png",
        "figur_20_zuschlag_volllaststunden.png",
        "figur_21_zuschlag_volllaststunden.png",
    ]
    missing = [f for f in group_fnames if not (ASSETS / f).exists()]
    if missing:
        print(f"  WARNUNG: Assets fehlen: {missing}")
    else:
        ok = insert_group_before_line(path, "> **Figuren 13–21**", group_fnames)
        status = "✓ eingefügt (Figuren 13–21)" if ok else "· bereits vorhanden (Figuren 13–21)"
        print(f"  {status}")


# ──────────────────────────────────────────────────────────────
# Hauptprogramm
# ──────────────────────────────────────────────────────────────

def main():
    print(f"\n{'═'*60}")
    print(f"  SIA 384-6 – Figuren an richtigen Ort verschieben")
    print(f"{'═'*60}")

    step1_remove_wrong_images()
    step2_insert_into_anhang_b()
    step2_insert_into_anhang_d()

    print(f"\n  Fertig. Bitte Obsidian neu laden (Ctrl+R).\n")


if __name__ == "__main__":
    main()
