"""
Fügt Obsidian-Links zu allen Kapitel-.md-Dateien hinzu:
- _MOC.md pro Norm-Ordner (Map of Content)
- 00_Index.md als Master-Index
- Navigation (vorheriges / nächstes Kapitel) in jeder Datei
- Automatische Umwandlung von (siehe X) / (Kapitel X) zu [[Wiki-Links]]
"""

import os, re

BASE = r"C:\Users\schin\OneDrive\Desktop\Wissens_db\data"

# ─── Normen-Definition ─────────────────────────────────────────────────────────
NORMS = {
    "SN_EN_380_1993": {
        "titel":      "SN EN 380:1993 – Holzbauwerke: Prüfverfahren unter statischen Belastungen",
        "kurz":       "SN EN 380:1993",
        "thema":      "Holzbau · Prüfverfahren · Statik",
        "kapitel": [
            ("01_Anwendungsbereich",       "Kap. 1–2",  "Anwendungsbereich & normative Verweisungen"),
            ("03_04_Definitionen_Symbole",  "Kap. 3–4",  "Definitionen und Symbole"),
            ("05_Allgemeine_Anforderungen", "Kap. 5",    "Allgemeine Anforderungen"),
            ("06_Pruefverfahren",           "Kap. 6",    "Prüfverfahren für statische Belastungen"),
            ("06_7_Pruefbericht",           "Kap. 6.7",  "Prüfbericht"),
        ],
        # Kapitel-Präfix → Dateiname (für (siehe X) Auflösung)
        "ref_map": {
            "1": "01_Anwendungsbereich",
            "2": "01_Anwendungsbereich",
            "3": "03_04_Definitionen_Symbole",
            "4": "03_04_Definitionen_Symbole",
            "5": "05_Allgemeine_Anforderungen",
            "6": "06_Pruefverfahren",
            "6.7": "06_7_Pruefbericht",
        },
    },
    "SIA_384-6_2021": {
        "titel":      "SIA 384/6:2021 – Erdwärmesonden",
        "kurz":       "SIA 384/6:2021",
        "thema":      "Geothermie · Erdwärmesonden · Planung & Ausführung",
        "kapitel": [
            ("00_Geltungsbereich",       "Kap. 0",   "Geltungsbereich"),
            ("01_Begriffe_Definitionen", "Kap. 1a",  "Begriffe und Definitionen"),
            ("01_Symbole_Indizes",       "Kap. 1b",  "Symbole und Indizes"),
            ("02_Strategische_Planung",  "Kap. 2",   "Strategische Planung"),
            ("03_Projektierung",         "Kap. 3",   "Projektierung"),
            ("04_Baustoffe",             "Kap. 4",   "Baustoffe und Konstruktion"),
            ("05_Ausfuehrung",           "Kap. 5",   "Ausführung"),
            ("06_Pruefungen",            "Kap. 6",   "Prüfungen"),
            ("07_Dokumentation",         "Kap. 7",   "Dokumentation"),
            ("08_Betrieb_Wartung",       "Kap. 8",   "Betrieb und Wartung"),
        ],
        "ref_map": {
            "0": "00_Geltungsbereich",
            "1": "01_Begriffe_Definitionen",
            "1.1": "01_Begriffe_Definitionen", "1.2": "01_Begriffe_Definitionen",
            "1.3": "01_Symbole_Indizes",       "1.4": "01_Symbole_Indizes",
            "2": "02_Strategische_Planung",
            "3": "03_Projektierung",
            "4": "04_Baustoffe",
            "5": "05_Ausfuehrung",
            "6": "06_Pruefungen",
            "7": "07_Dokumentation",
            "8": "08_Betrieb_Wartung",
        },
    },
    "SIA_385-2_2025": {
        "titel":      "SIA 385/2:2025 – Trinkwarmwasseranlagen in Gebäuden",
        "kurz":       "SIA 385/2:2025",
        "thema":      "Sanitär · Warmwasser · Auslegung & Energiebedarf",
        "kapitel": [
            ("00_Geltungsbereich",          "Kap. 0",  "Geltungsbereich"),
            ("01_Begriffe_Definitionen",    "Kap. 1a", "Begriffe und Definitionen"),
            ("01_Symbole_Indizes",          "Kap. 1b", "Symbole, Indizes und Abkürzungen"),
            ("02_Projektierung",            "Kap. 2",  "Projektierung"),
            ("03_Grobauslegung",            "Kap. 3",  "Grobauslegung – Vorprojektphase"),
            ("04_Feinplanung",              "Kap. 4",  "Feinplanung – Auslegung"),
            ("05_Waermebedarf_Hilfsenergie","Kap. 5",  "Wärmebedarf und Hilfsenergie"),
        ],
        "ref_map": {
            "0": "00_Geltungsbereich",
            "1": "01_Begriffe_Definitionen",
            "1.1": "01_Begriffe_Definitionen", "1.2": "01_Symbole_Indizes",
            "1.3": "01_Symbole_Indizes",       "1.4": "01_Symbole_Indizes",
            "2": "02_Projektierung",
            "3": "03_Grobauslegung",
            "4": "04_Feinplanung",
            "5": "05_Waermebedarf_Hilfsenergie",
        },
    },
    "SIA_387-4_2023": {
        "titel":      "SIA 387/4:2023 – Elektrizität in Gebäuden: Beleuchtung",
        "kurz":       "SIA 387/4:2023",
        "thema":      "Beleuchtung · Elektrizitätsbedarf · Berechnung & Anforderungen",
        "kapitel": [
            ("00_Geltungsbereich",            "Kap. 0",   "Geltungsbereich"),
            ("01_Begriffe_Definitionen",      "Kap. 1a",  "Begriffe und Definitionen"),
            ("01_Symbole_Indizes",            "Kap. 1b",  "Symbole, Indizes und Darstellung"),
            ("02_Projektierung",              "Kap. 2",   "Projektierung"),
            ("03_1_Allgemeines_Grundlagen",   "Kap. 3.1", "Berechnung – Allgemeines"),
            ("03_2_Spezifische_Leistung",     "Kap. 3.2", "Berechnung – Spezifische Leistung"),
            ("03_3_Volllaststunden_Methode1", "Kap. 3.3", "Berechnung – Volllaststunden (Methode 1)"),
            ("03_4_Stundenschritt_Methode2",  "Kap. 3.4", "Berechnung – Stundenschritt (Methode 2)"),
            ("04_Anforderungen",              "Kap. 4",   "Anforderungen"),
        ],
        "ref_map": {
            "0": "00_Geltungsbereich",
            "1": "01_Begriffe_Definitionen",
            "1.1": "01_Begriffe_Definitionen", "1.2": "01_Symbole_Indizes",
            "1.3": "01_Symbole_Indizes",       "1.4": "01_Symbole_Indizes",
            "2": "02_Projektierung",
            "3": "03_1_Allgemeines_Grundlagen",
            "3.1": "03_1_Allgemeines_Grundlagen",
            "3.2": "03_2_Spezifische_Leistung",
            "3.3": "03_3_Volllaststunden_Methode1",
            "3.4": "03_4_Stundenschritt_Methode2",
            "4": "04_Anforderungen",
        },
    },
}

# Norm-Kurzbezeichnungen → Ordnernamen (für Querverweise zwischen Normen)
NORM_LINK_MAP = {
    "SIA 384/6":  "SIA_384-6_2021",
    "SIA 385/2":  "SIA_385-2_2025",
    "SIA 387/4":  "SIA_387-4_2023",
    "SN EN 380":  "SN_EN_380_1993",
    "SIA 380/1":  None,  # nicht in DB
    "SIA 384/1":  None,
    "SIA 384/2":  None,
    "SIA 384/3":  None,
    "SIA 385/1":  None,
    "SIA 380/2":  None,
    "SIA 382/1":  None,
    "SIA 382/2":  None,
    "SIA 387/4":  "SIA_387-4_2023",
}


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()

def write(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✓ {os.path.relpath(path, BASE)}")


# ─── (1) Kapitel-Verweise im Text zu [[Links]] umwandeln ──────────────────────
def add_inline_links(text, ref_map, folder):
    """
    Ersetzt Muster wie (siehe 3.2.1), (Kapitel 3), (3.2), gemäss 3.4.2
    durch Obsidian-[[Links]] auf die passende Kapiteldatei.
    """
    def resolve(kap_str):
        """Gibt Dateinamen zurück oder None wenn nicht auflösbar."""
        # direkte Übereinstimmung
        if kap_str in ref_map:
            return ref_map[kap_str]
        # nur ersten zwei Teile (z.B. "3.4.2" → "3.4" → "3")
        parts = kap_str.split(".")
        for depth in range(len(parts) - 1, 0, -1):
            key = ".".join(parts[:depth])
            if key in ref_map:
                return ref_map[key]
        return None

    def replacer(m):
        prefix = m.group(1) or ""  # "siehe ", "Kapitel ", etc.
        kap = m.group(2)
        target = resolve(kap)
        if target:
            return f"({prefix}[[{target}|{kap}]])"
        return m.group(0)

    # Pattern: (siehe X.X.X), (Kapitel X), (Abschnitt X.X)
    text = re.sub(
        r"\(((?:siehe |Kapitel |Abschnitt |gemäss )?)"
        r"(\d+(?:\.\d+){0,3})\)",
        replacer, text
    )
    # Pattern: gemäss X.X.X (ohne Klammern, am Satzende oder vor Komma)
    def replacer2(m):
        kap = m.group(1)
        target = resolve(kap)
        if target:
            return f"gemäss [[{target}|{kap}]]"
        return m.group(0)
    text = re.sub(r"gemäss (\d+(?:\.\d+){1,3})(?=[\s,\.])", replacer2, text)

    return text


# ─── (2) Nav-Leiste für jede Kapitel-Datei ────────────────────────────────────
def build_nav(folder_key, idx, chapters):
    parts = []
    if idx > 0:
        prev_file, prev_kap, prev_titel = chapters[idx - 1]
        parts.append(f"◀ [[{prev_file}|{prev_kap} {prev_titel}]]")
    else:
        parts.append("◀ *(erstes Kapitel)*")

    parts.append(f"[[_{folder_key}_MOC|↑ Inhaltsverzeichnis]]")

    if idx < len(chapters) - 1:
        nxt_file, nxt_kap, nxt_titel = chapters[idx + 1]
        parts.append(f"[[{nxt_file}|{nxt_kap} {nxt_titel}]] ▶")
    else:
        parts.append("*(letztes Kapitel)* ▶")

    return "> " + "  ·  ".join(parts) + "\n\n---\n\n"


# ─── (3) _MOC.md pro Norm-Ordner ──────────────────────────────────────────────
def create_moc(folder_key, norm):
    lines = [
        f"---",
        f"tags: [MOC, Norm, Index]",
        f"normnummer: \"{norm['kurz']}\"",
        f"---",
        f"",
        f"# {norm['titel']}",
        f"",
        f"**Thema:** {norm['thema']}",
        f"",
        f"## Kapitel",
        f"",
    ]
    for fname, kap, titel in norm["kapitel"]:
        lines.append(f"- [[{fname}|{kap} – {titel}]]")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("[[00_Wissensbank_Index|↑ Zurück zum Hauptindex]]")
    lines.append("")

    path = os.path.join(BASE, folder_key, f"_{folder_key}_MOC.md")
    write(path, "\n".join(lines))


# ─── (4) Jede Kapitel-Datei aktualisieren ─────────────────────────────────────
def update_chapter(folder_key, norm, idx):
    fname, kap, titel = norm["kapitel"][idx]
    path = os.path.join(BASE, folder_key, fname + ".md")
    if not os.path.exists(path):
        print(f"  ⚠ Nicht gefunden: {path}")
        return

    content = read(path)

    # Frontmatter Ende finden
    fm_end = content.find("\n---\n", 4)  # zweites ---
    if fm_end == -1:
        body = content
        frontmatter = ""
    else:
        frontmatter = content[:fm_end + 5]
        body = content[fm_end + 5:]

    # Nav einfügen (bestehende Nav-Zeile ersetzen falls vorhanden)
    nav = build_nav(folder_key, idx, norm["kapitel"])
    body = re.sub(r"^> ◀.*?\n\n---\n\n", "", body, flags=re.DOTALL)
    body = nav + body.lstrip()

    # Inline-Links im Body einfügen
    body = add_inline_links(body, norm["ref_map"], folder_key)

    write(path, frontmatter + body)


# ─── (5) Master-Index ─────────────────────────────────────────────────────────
def create_master_index():
    lines = [
        "---",
        "tags: [MOC, Index, Wissensdatenbank]",
        "---",
        "",
        "# Wissensbank – Hauptindex",
        "",
        "Lokale Wissensdatenbank aus Schweizer SIA-Normen und EN-Normen (Bauingenieurwesen / Gebäudetechnik).",
        "",
        "## Normen",
        "",
    ]
    for folder_key, norm in NORMS.items():
        moc_file = f"_{folder_key}_MOC"
        lines.append(f"### [[{moc_file}|{norm['kurz']}]]")
        lines.append(f"*{norm['thema']}*")
        lines.append("")
        for fname, kap, titel in norm["kapitel"]:
            lines.append(f"- [[{fname}|{kap} – {titel}]]")
        lines.append("")
    lines.append("---")
    lines.append("*Generiert mit `scripts/create_chapter_files.py` + `scripts/add_obsidian_links.py`*")
    lines.append("")

    path = os.path.join(BASE, "00_Wissensbank_Index.md")
    write(path, "\n".join(lines))


# ─── Alles ausführen ──────────────────────────────────────────────────────────
print("Erstelle Obsidian-Links und MOC-Dateien...\n")

for folder_key, norm in NORMS.items():
    print(f"▶ {norm['kurz']}")
    create_moc(folder_key, norm)
    for idx in range(len(norm["kapitel"])):
        update_chapter(folder_key, norm, idx)

create_master_index()
print("\n✓ Fertig.")
