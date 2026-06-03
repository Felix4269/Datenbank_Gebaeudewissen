# -*- coding: utf-8 -*-
"""
create_hubbuch_files.py
Extrahiert die drei Hubbuch-Vorlesungsskripte vollständig (kein Wort gekürzt)
in Kapitel-MD-Dateien mit Obsidian-Verlinkungen und Navigation.
"""

import os
import re
import pdfplumber

BASE = r"C:\Users\schin\OneDrive\Desktop\Wissens_db\data"
INDEX = r"C:\Users\schin\OneDrive\Desktop\Wissens_db\data\00_Wissensbank_Index.md"

# ---------------------------------------------------------------------------
# Konfiguration der drei Skripte
# (start_page und end_page sind 0-basierte pdfplumber-Seitenindizes)
# ---------------------------------------------------------------------------

SKRIPTE = [
    {
        "pdf":    r"C:\Users\schin\Downloads\Skript Energie im Gebäude 2026.pdf",
        "folder": "Skript_Energie",
        "titel":  "Energieflüsse im Gebäude",
        "kurz":   "Skript_Energie",
        "autor":  "Prof. Markus Hubbuch",
        "jahr":   "2026",
        "tags":   ["Energie", "Heizwärmebedarf", "Wärmegewinne", "Gebäudetechnik"],
        "header_strip": ["Energieflüsse im Gebäude"],
        "footer_re":    r"©\s*20\d\d.*?Hubbuch.*?Seite\s+\d+\s*/\s*\d+",
        "kapitel": [
            # (filename, kap_nr, titel, start_idx, end_idx)
            ("00_Titelseite_TOC",    "0",   "Titelseite und Inhaltsverzeichnis",                0,   2),
            ("01_Grundlagen",        "1",   "Grundlagen",                                       3,   3),
            ("02_Waermeverluste",    "2",   "Wärmeverluste",                                    4,   7),
            ("03_Waermegewinne",     "3",   "Wärmegewinne",                                     8,  17),
            ("04_Heizwaermebedarf",  "4",   "Heizwärmebedarf",                                 18,  24),
            ("05_Warmwasser",        "5",   "Wärmebedarf Warmwasser",                          25,  29),
            ("06_Energiebedarf",     "6",   "Energiebedarf des Gebäudes",                      30,  47),
            ("07_Sommerlicher_Waermeschutz", "7", "Sommerlicher Wärmeschutz",                 48,  58),
            ("08_Anhang",            "8",   "Anhang",                                          59,  60),
        ],
    },
    {
        "pdf":    r"C:\Users\schin\Downloads\Skript Lüftung.pdf",
        "folder": "Skript_Lueftung",
        "titel":  "Lüftungstechnik",
        "kurz":   "Skript_Lueftung",
        "autor":  "Prof. Markus Hubbuch",
        "jahr":   "2022",
        "tags":   ["Lüftung", "Raumlufttechnik", "Klimaanlage", "Gebäudetechnik"],
        "header_strip": ["ZHAW, Institut für Facility Management Lüftungstechnik"],
        "footer_re":    r"©\s*20\d\d\s*M\.\s*Hubbuch.*?Seite\s+\d+\s*/\s*\d+",
        "kapitel": [
            ("00_Titelseite_TOC",    "0",   "Titelseite und Inhaltsverzeichnis",                0,   2),
            ("01_Aufgaben_Einteilung","1",  "Aufgaben und Einteilung der Lüftungstechnik",      3,   5),
            ("02_Bedarfsermittlung", "2",   "Bedarfsermittlung, Luftraten",                     6,  14),
            ("03_Lueftungssysteme",  "3",   "Lüftungssysteme",                                 15,  24),
            ("04_Bauarten",          "4",   "Bauarten von Lüftungs- und Klimaanlagen",          25,  31),
            ("05_Komponenten",       "5",   "Komponenten der Lüftungs- und Klimatechnik",       32,  46),
            ("06_Schallanforderungen","6",  "Schallanforderungen",                             47,  48),
        ],
    },
    {
        "pdf":    r"C:\Users\schin\Downloads\Skript Bauphysik 2026.pdf",
        "folder": "Skript_Bauphysik",
        "titel":  "Bauphysik",
        "kurz":   "Skript_Bauphysik",
        "autor":  "Prof. Markus Hubbuch",
        "jahr":   "2026",
        "tags":   ["Bauphysik", "Wärmeschutz", "Feuchteschutz", "U-Wert", "Gebäudetechnik"],
        "header_strip": ["Skript Bauphysik"],
        "footer_re":    r"©\s*20\d\d.*?Hubbuch.*?Seite\s+\d+\s*/\s*\d+",
        "kapitel": [
            ("00_Titelseite_TOC",       "0",  "Titelseite und Inhaltsverzeichnis",              0,   1),
            ("01_Grundlagen",           "1",  "Grundlagen Bauphysik",                           2,   3),
            ("02_Waermeverluste_Trans", "2",  "Verringerung der Wärmeverluste durch Transmission", 4, 9),
            ("03_Theorie_Waermedurchgang","3","Theorie Wärmedurchgang",                        10,  16),
            ("04_Theorie_Feuchte",      "4",  "Theorie der feuchten Luft",                     17,  20),
            ("05_Luftdichtheit",        "5",  "Luftdichtheit eines Gebäudes",                  21,  32),
        ],
    },
]

# ---------------------------------------------------------------------------
# Cross-Link-Map zwischen den drei Skripten (für Inline-Verlinkung)
# ---------------------------------------------------------------------------
CROSS_LINKS = {
    "Skript Bauphysik": "[[_Skript_Bauphysik_MOC|Skript Bauphysik]]",
    "Skript Lüftung":   "[[_Skript_Lueftung_MOC|Skript Lüftung]]",
    "Skript Energie":   "[[_Skript_Energie_MOC|Skript Energie]]",
}

# ---------------------------------------------------------------------------
# Hilfsfunktionen
# ---------------------------------------------------------------------------

def clean_page_text(text, header_strips, footer_re_str):
    """Entfernt seitenspezifische Kopf- und Fusszeilen ohne Inhalt zu kürzen."""
    if not text:
        return ""
    lines = text.splitlines()
    cleaned = []
    footer_re = re.compile(footer_re_str, re.IGNORECASE | re.DOTALL)
    for line in lines:
        stripped = line.strip()
        # Kopfzeile entfernen
        if stripped in header_strips:
            continue
        # Fusszeile entfernen
        if footer_re.search(stripped):
            continue
        cleaned.append(line)
    return "\n".join(cleaned)


def extract_chapter(pdf, start_idx, end_idx, header_strips, footer_re_str):
    """Extrahiert alle Seiten eines Kapitels und gibt den vollständigen Text zurück."""
    pages_text = []
    for i in range(start_idx, end_idx + 1):
        if i >= len(pdf.pages):
            break
        raw = pdf.pages[i].extract_text() or ""
        cleaned = clean_page_text(raw, header_strips, footer_re_str)
        if cleaned.strip():
            pages_text.append(cleaned.strip())
    return "\n\n".join(pages_text)


def build_nav(prev_link, next_link, moc_name):
    parts = []
    if prev_link:
        parts.append(f"◀ {prev_link}")
    parts.append(f"[[_{moc_name}_MOC|↑ MOC]]")
    if next_link:
        parts.append(f"{next_link} ▶")
    return "> " + " · ".join(parts) + "\n\n---\n\n"


def add_cross_links(text):
    """Verlinkt Querverweise auf andere Hubbuch-Skripte."""
    for phrase, link in CROSS_LINKS.items():
        text = re.sub(
            r'(?<!\[\[)' + re.escape(phrase) + r'(?!\]\])',
            link,
            text
        )
    return text


def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"    OK: {os.path.basename(path)}")


# ---------------------------------------------------------------------------
# Hauptverarbeitung
# ---------------------------------------------------------------------------

for skript in SKRIPTE:
    folder_path = os.path.join(BASE, skript["folder"])
    os.makedirs(folder_path, exist_ok=True)
    kurz    = skript["kurz"]
    titel   = skript["titel"]
    kapitel = skript["kapitel"]
    header_s = skript["header_strip"]
    footer_r = skript["footer_re"]
    tags_str = ", ".join(skript["tags"])

    print(f"\n{'='*60}")
    print(f"Verarbeite: {titel}")
    print(f"  Zielordner: {folder_path}")

    with pdfplumber.open(skript["pdf"]) as pdf:
        total_pages = len(pdf.pages)
        print(f"  Seiten gesamt: {total_pages}")

        # Kapitel extrahieren
        chapters_data = []  # (filename, kap_nr, titel, text)
        for (fname, kap_nr, kap_titel, s_idx, e_idx) in kapitel:
            text = extract_chapter(pdf, s_idx, e_idx, header_s, footer_r)
            chapters_data.append((fname, kap_nr, kap_titel, text))
            n_pages = e_idx - s_idx + 1
            print(f"    Kap {kap_nr}: '{kap_titel}' ({n_pages} Seiten, {len(text)} Zeichen)")

    # MD-Dateien schreiben
    n = len(chapters_data)
    for idx, (fname, kap_nr, kap_titel, text) in enumerate(chapters_data):

        # Navigation
        prev_link = None
        next_link = None
        if idx > 0:
            pf, _, pt, _ = chapters_data[idx - 1]
            prev_link = f"[[{pf}|← {pt[:35]}]]"
        if idx < n - 1:
            nf, _, nt, _ = chapters_data[idx + 1]
            next_link = f"[[{nf}|{nt[:35]} →]]"

        nav = build_nav(prev_link, next_link, kurz)

        # Querverweise verlinken
        text_linked = add_cross_links(text)

        content = f"""\
---
tags: [{tags_str}]
skript: "{titel}"
autor: "{skript['autor']}"
version: "{skript['jahr']}"
kapitel: "{kap_nr}"
---

{nav}# {titel} – Kapitel {kap_nr}: {kap_titel}

{text_linked}

---

{nav}"""

        out_path = os.path.join(folder_path, f"{fname}.md")
        write_file(out_path, content)

    # MOC-Datei erstellen
    moc_rows = "\n".join(
        f"| [[{fname}|Kap. {kap_nr}: {kap_titel}]] | {kap_titel} |"
        for fname, kap_nr, kap_titel, _ in chapters_data
    )
    moc_content = f"""\
---
tags: [{tags_str}, MOC]
skript: "{titel}"
autor: "{skript['autor']}"
---

# {titel} – MOC

**Autor:** {skript["autor"]}
**Version:** {skript["jahr"]}

---

## Kapitelübersicht

| Datei | Inhalt |
|---|---|
{moc_rows}

---

*Zurück zum Hauptindex: [[00_Wissensbank_Index]]*
"""
    moc_path = os.path.join(folder_path, f"_{kurz}_MOC.md")
    write_file(moc_path, moc_content)
    print(f"  MOC erstellt: _{kurz}_MOC.md")

# ---------------------------------------------------------------------------
# Master-Index aktualisieren
# ---------------------------------------------------------------------------
print("\nAktualisiere 00_Wissensbank_Index.md ...")

with open(INDEX, encoding="utf-8") as f:
    index_text = f.read()

HUBBUCH_SECTION = """
---

## Vorlesungsskripte (Prof. Markus Hubbuch)

> Vorlesungsskripte für Energie- und Gebäudemanagement / Gebäudetechnik, ZHAW

| Skript | Inhalt |
|---|---|
| [[_Skript_Energie_MOC\\|Energieflüsse im Gebäude (2026)]] | Wärmeverluste, Wärmegewinne, Heizwärmebedarf, Energiebedarf, sommerlicher Wärmeschutz |
| [[_Skript_Lueftung_MOC\\|Lüftungstechnik]] | Bedarfsermittlung, Lüftungssysteme, Bauarten, Komponenten, Schall |
| [[_Skript_Bauphysik_MOC\\|Bauphysik (2026)]] | Wärmedämmung, Wärmebrücken, U-Wert, Feuchte, Luftdichtheit |
"""

if "Vorlesungsskripte" not in index_text:
    index_text = index_text.rstrip() + "\n" + HUBBUCH_SECTION + "\n"
    with open(INDEX, 'w', encoding='utf-8') as f:
        f.write(index_text)
    print("  Index aktualisiert.")
else:
    print("  Vorlesungsskripte bereits im Index – übersprungen.")

print("\nFertig! Alle drei Hubbuch-Skripte verarbeitet.")
