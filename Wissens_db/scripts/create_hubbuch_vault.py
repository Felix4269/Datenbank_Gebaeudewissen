# -*- coding: utf-8 -*-
"""
create_hubbuch_vault.py
Erstellt ein eigenständiges Obsidian-Vault "Wissens_db_Hubbuch" auf dem Desktop
mit den drei Hubbuch-Vorlesungsskripten – vollständig, kein Wort gekürzt.
"""

import os
import re
import pdfplumber

VAULT = r"C:\Users\schin\OneDrive\Desktop\Wissens_db_Hubbuch"
os.makedirs(VAULT, exist_ok=True)

# ---------------------------------------------------------------------------
# Konfiguration der drei Skripte
# (start_idx / end_idx = 0-basierte pdfplumber-Seitenindizes)
# ---------------------------------------------------------------------------

SKRIPTE = [
    {
        "pdf":    r"C:\Users\schin\Downloads\Skript Energie im Gebäude 2026.pdf",
        "folder": "Skript_Energie",
        "titel":  "Energieflüsse im Gebäude",
        "kurz":   "Skript_Energie",
        "autor":  "Prof. Markus Hubbuch",
        "jahr":   "2026",
        "tags":   ["Energie", "Heizwärmebedarf", "Wärmegewinne", "Gebäudetechnik", "Hubbuch"],
        "header_strip": ["Energieflüsse im Gebäude"],
        "footer_re":    r"©\s*20\d\d.*?Hubbuch.*?Seite\s+\d+\s*/\s*\d+",
        "kapitel": [
            # (filename, kap_nr, titel, start_idx, end_idx)
            ("00_Titelseite_TOC",             "0", "Titelseite und Inhaltsverzeichnis",       0,   2),
            ("01_Grundlagen",                 "1", "Grundlagen",                               3,   3),
            ("02_Waermeverluste",             "2", "Wärmeverluste",                            4,   7),
            ("03_Waermegewinne",              "3", "Wärmegewinne",                             8,  17),
            ("04_Heizwaermebedarf",           "4", "Heizwärmebedarf",                         18,  24),
            ("05_Warmwasser",                 "5", "Wärmebedarf Warmwasser",                  25,  29),
            ("06_Energiebedarf",              "6", "Energiebedarf des Gebäudes",               30,  47),
            ("07_Sommerlicher_Waermeschutz",  "7", "Sommerlicher Wärmeschutz",                48,  58),
            ("08_Anhang",                     "8", "Anhang",                                  59,  60),
        ],
    },
    {
        "pdf":    r"C:\Users\schin\Downloads\Skript Lüftung.pdf",
        "folder": "Skript_Lueftung",
        "titel":  "Lüftungstechnik",
        "kurz":   "Skript_Lueftung",
        "autor":  "Prof. Markus Hubbuch",
        "jahr":   "2022",
        "tags":   ["Lüftung", "Raumlufttechnik", "Klimaanlage", "Gebäudetechnik", "Hubbuch"],
        "header_strip": ["ZHAW, Institut für Facility Management Lüftungstechnik"],
        "footer_re":    r"©\s*20\d\d\s*M\.\s*Hubbuch.*?Seite\s+\d+\s*/\s*\d+",
        "kapitel": [
            ("00_Titelseite_TOC",     "0", "Titelseite und Inhaltsverzeichnis",               0,   2),
            ("01_Aufgaben_Einteilung","1", "Aufgaben und Einteilung der Lüftungstechnik",      3,   5),
            ("02_Bedarfsermittlung",  "2", "Bedarfsermittlung, Luftraten",                     6,  14),
            ("03_Lueftungssysteme",   "3", "Lüftungssysteme",                                 15,  24),
            ("04_Bauarten",           "4", "Bauarten von Lüftungs- und Klimaanlagen",          25,  31),
            ("05_Komponenten",        "5", "Komponenten der Lüftungs- und Klimatechnik",       32,  46),
            ("06_Schallanforderungen","6", "Schallanforderungen",                             47,  48),
        ],
    },
    {
        "pdf":    r"C:\Users\schin\Downloads\Skript Bauphysik 2026.pdf",
        "folder": "Skript_Bauphysik",
        "titel":  "Bauphysik",
        "kurz":   "Skript_Bauphysik",
        "autor":  "Prof. Markus Hubbuch",
        "jahr":   "2026",
        "tags":   ["Bauphysik", "Wärmeschutz", "Feuchteschutz", "U-Wert", "Gebäudetechnik", "Hubbuch"],
        "header_strip": ["Skript Bauphysik"],
        "footer_re":    r"©\s*20\d\d.*?Hubbuch.*?Seite\s+\d+\s*/\s*\d+",
        "kapitel": [
            ("00_Titelseite_TOC",          "0", "Titelseite und Inhaltsverzeichnis",           0,   1),
            ("01_Grundlagen",              "1", "Grundlagen Bauphysik",                        2,   3),
            ("02_Waermeverluste_Trans",    "2", "Verringerung der Wärmeverluste durch Transmission", 4, 9),
            ("03_Theorie_Waermedurchgang", "3", "Theorie Wärmedurchgang",                     10,  16),
            ("04_Theorie_Feuchte",         "4", "Theorie der feuchten Luft",                  17,  20),
            ("05_Luftdichtheit",           "5", "Luftdichtheit eines Gebäudes",               21,  32),
        ],
    },
]

# Cross-Links zwischen den Skripten
CROSS_LINKS = {
    "Skript Bauphysik": "[[_Skript_Bauphysik_MOC|Skript Bauphysik]]",
    "Skript Lüftung":   "[[_Skript_Lueftung_MOC|Skript Lüftung]]",
    "Skript Energie":   "[[_Skript_Energie_MOC|Skript Energie]]",
}

# ---------------------------------------------------------------------------
# Hilfsfunktionen
# ---------------------------------------------------------------------------

def clean_page(text, header_strips, footer_re_str):
    if not text:
        return ""
    footer_re = re.compile(footer_re_str, re.IGNORECASE)
    cleaned = []
    for line in text.splitlines():
        s = line.strip()
        if s in header_strips:
            continue
        if footer_re.search(s):
            continue
        cleaned.append(line)
    return "\n".join(cleaned)


def extract_chapter(pdf, s_idx, e_idx, header_strips, footer_re_str):
    pages = []
    for i in range(s_idx, min(e_idx + 1, len(pdf.pages))):
        raw  = pdf.pages[i].extract_text() or ""
        text = clean_page(raw, header_strips, footer_re_str).strip()
        if text:
            pages.append(text)
    return "\n\n".join(pages)


def nav_line(prev_link, next_link, moc_name):
    parts = []
    if prev_link:
        parts.append(f"◀ {prev_link}")
    parts.append(f"[[_{moc_name}_MOC|↑ MOC]]")
    if next_link:
        parts.append(f"{next_link} ▶")
    return "> " + " · ".join(parts) + "\n\n---\n\n"


def add_cross_links(text):
    for phrase, link in CROSS_LINKS.items():
        text = re.sub(r'(?<!\[\[)' + re.escape(phrase) + r'(?!\]\])', link, text)
    return text


def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"    OK  {os.path.basename(path)}")

# ---------------------------------------------------------------------------
# Alle drei Skripte verarbeiten
# ---------------------------------------------------------------------------

all_mocs = []   # für den Master-Index

for skript in SKRIPTE:
    folder_path = os.path.join(VAULT, skript["folder"])
    os.makedirs(folder_path, exist_ok=True)

    kurz    = skript["kurz"]
    titel   = skript["titel"]
    kapitel = skript["kapitel"]
    tags_str = ", ".join(skript["tags"])

    print(f"\n{'='*60}")
    print(f"Verarbeite: {titel}")

    with pdfplumber.open(skript["pdf"]) as pdf:
        total = len(pdf.pages)
        print(f"  Seiten: {total}")

        chapters_data = []
        for (fname, kap_nr, kap_titel, s_idx, e_idx) in kapitel:
            text = extract_chapter(pdf, s_idx, e_idx, skript["header_strip"], skript["footer_re"])
            chapters_data.append((fname, kap_nr, kap_titel, text))
            print(f"  Kap {kap_nr}: {kap_titel[:50]}  ({len(text):,} Zeichen)")

    # ---- Kapitel-Dateien schreiben ----
    n = len(chapters_data)
    for idx, (fname, kap_nr, kap_titel, text) in enumerate(chapters_data):

        prev_link = next_link = None
        if idx > 0:
            pf, _, pt, _ = chapters_data[idx - 1]
            prev_link = f"[[{pf}|← {pt[:40]}]]"
        if idx < n - 1:
            nf, _, nt, _ = chapters_data[idx + 1]
            next_link = f"[[{nf}|{nt[:40]} →]]"

        nav = nav_line(prev_link, next_link, kurz)
        text_linked = add_cross_links(text)

        content = (
            f"---\n"
            f"tags: [{tags_str}]\n"
            f"skript: \"{titel}\"\n"
            f"autor: \"{skript['autor']}\"\n"
            f"version: \"{skript['jahr']}\"\n"
            f"kapitel: \"{kap_nr}\"\n"
            f"---\n\n"
            f"{nav}"
            f"# {titel} – Kapitel {kap_nr}: {kap_titel}\n\n"
            f"{text_linked}\n\n"
            f"---\n\n"
            f"{nav}"
        )

        write_file(os.path.join(folder_path, f"{fname}.md"), content)

    # ---- MOC-Datei ----
    moc_rows = "\n".join(
        f"| [[{fname}|Kap. {kap_nr}: {kap_titel}]] | {kap_titel} |"
        for fname, kap_nr, kap_titel, _ in chapters_data
    )
    moc = (
        f"---\n"
        f"tags: [{tags_str}, MOC]\n"
        f"skript: \"{titel}\"\n"
        f"autor: \"{skript['autor']}\"\n"
        f"---\n\n"
        f"# {titel}\n\n"
        f"**Autor:** {skript['autor']}  \n"
        f"**Version:** {skript['jahr']}\n\n"
        f"---\n\n"
        f"## Kapitel\n\n"
        f"| Datei | Inhalt |\n"
        f"|---|---|\n"
        f"{moc_rows}\n\n"
        f"---\n\n"
        f"*Zurück: [[00_Index|Hauptindex]]*\n"
    )
    moc_path = os.path.join(folder_path, f"_{kurz}_MOC.md")
    write_file(moc_path, moc)
    all_mocs.append((kurz, titel, skript["autor"], skript["jahr"], moc_path))

# ---------------------------------------------------------------------------
# Master-Index im Vault-Wurzelverzeichnis
# ---------------------------------------------------------------------------

index_rows = "\n".join(
    f"| [[_{kurz}_MOC|{titel}]] | {autor} | {jahr} |"
    for kurz, titel, autor, jahr, _ in all_mocs
)

# Kapitelübersicht aller drei Skripte für den Index
detail_blocks = []
for skript in SKRIPTE:
    rows = "\n".join(
        f"| [[{fname}|Kap. {kap_nr}]] | {kap_titel} |"
        for fname, kap_nr, kap_titel, _, __ in [
            (f, k, t, s, e) for (f, k, t, s, e) in skript["kapitel"]
        ]
    )
    detail_blocks.append(
        f"### [[_{skript['kurz']}_MOC|{skript['titel']}]]\n\n"
        f"| Kapitel | Inhalt |\n"
        f"|---|---|\n"
        f"{rows}\n"
    )

index_content = (
    f"---\n"
    f"tags: [Hubbuch, Wissensdatenbank, MOC, Index]\n"
    f"---\n\n"
    f"# Wissensdatenbank – Prof. Markus Hubbuch\n\n"
    f"Vorlesungsskripte für Energie- und Gebäudemanagement / Gebäudetechnik  \n"
    f"ZHAW, Institut für Facility Management\n\n"
    f"---\n\n"
    f"## Skripte\n\n"
    f"| Skript | Autor | Version |\n"
    f"|---|---|---|\n"
    f"{index_rows}\n\n"
    f"---\n\n"
    f"## Kapitelübersicht\n\n"
    + "\n".join(detail_blocks) +
    f"\n---\n\n"
    f"*Alle Inhalte © Prof. Markus Hubbuch, ZHAW*\n"
)

index_path = os.path.join(VAULT, "00_Index.md")
write_file(index_path, index_content)
print(f"\n  Master-Index: 00_Index.md")

# ---------------------------------------------------------------------------
# Obsidian .obsidian/app.json  (minimale Vault-Einstellungen)
# ---------------------------------------------------------------------------

obsidian_dir = os.path.join(VAULT, ".obsidian")
os.makedirs(obsidian_dir, exist_ok=True)

app_json = '{\n  "legacyEditor": false,\n  "livePreview": true\n}\n'
with open(os.path.join(obsidian_dir, "app.json"), 'w', encoding='utf-8') as f:
    f.write(app_json)

# Obsidian workspace – öffnet 00_Index.md als Starttab
workspace_json = """{
  "main": {
    "id": "main",
    "type": "split",
    "children": [
      {
        "id": "tab1",
        "type": "tabs",
        "children": [
          {
            "id": "leaf1",
            "type": "leaf",
            "state": {
              "type": "markdown",
              "state": {
                "file": "00_Index.md",
                "mode": "preview"
              }
            }
          }
        ]
      }
    ],
    "direction": "vertical"
  },
  "left": { "id": "left", "type": "split", "children": [], "direction": "horizontal", "width": 300 },
  "right": { "id": "right", "type": "split", "children": [], "direction": "horizontal", "width": 300 },
  "active": "leaf1",
  "lastOpenFiles": ["00_Index.md"]
}
"""
with open(os.path.join(obsidian_dir, "workspace.json"), 'w', encoding='utf-8') as f:
    f.write(workspace_json)

print(f"\n  Obsidian-Konfiguration erstellt (.obsidian/)")
print(f"\nFertig!  Vault: {VAULT}")
print(f"In Obsidian: 'Open folder as vault' → Desktop/Wissens_db_Hubbuch")
