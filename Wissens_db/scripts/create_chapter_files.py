"""
Liest extrahierte JSON-Rohdaten und erstellt pro Kapitel eine saubere .md-Datei.
"""

import json, os, re

BASE = r"C:\Users\schin\OneDrive\Desktop\Wissens_db\data"

def load(name):
    path = os.path.join(BASE, f"raw_{name}.json")
    with open(path, encoding="utf-8") as f:
        return json.load(f)

NOISE_PATTERNS = [
    r"\d{4}:\d[-/]\d+-\d+-\d+",           # Datum-Wasserzeichen wie 1202:6-483645
    r"^NS\s*$", r"^NE\s*$",
    r"kehtoilbibluhcshcoH",
    r"neideM-E",
    r"^WAHZ",
    r"\d{8}\s+ot\s+desnecil",
    r"^228501S\s*$",
    r"^VNS\s*$",
    r"^Norm \d+.*\.indd",
    r"SIA \d+/\d+, Copyright",
    r"SIA \d+/\d+ Copyright",
    r"\.hcsnessiW",
    r"rehcr.Z",
    r"^desnecil\s*$",
    r"^ot\s+desnecil",
    r"^48226417",
    r"^eluhcshcoH",
    r"^\.\w{1,2}\s*$",                     # einzelne Punkte-Abkürzungen wie ".A" ".f"
    r"^\d{2}:\d{2}_\d{2}-\d{2}-\d{4}",   # Datumformat-Noise
    r"^[A-Z]{2,3}\s*$",                    # einzelne Großbuchstaben-Zeilen (NS, NE, VNS)
    r"^\d{4}:\d",                           # alle vierstelligen Jahreszahl-Noise
    r"^/\s*$",                              # einzelner Slash
    r"^-\s*$",                              # einzelner Strich
    r"^ot\s*$",                             # "ot" als Wasserzeichen-Rest
    r"^\d{1,2}\s*$",                        # einzelne Seitenzahlen
]

def clean_page(text):
    lines = text.split("\n")
    cleaned = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        skip = any(re.search(p, stripped) for p in NOISE_PATTERNS)
        if not skip:
            cleaned.append(stripped)
    return "\n".join(cleaned)

def get_pages(pages, start, end):
    parts = []
    for p in range(start, end + 1):
        raw = pages.get(str(p), "").strip()
        if raw:
            c = clean_page(raw)
            if c:
                parts.append(c)
    return "\n\n".join(parts)

def write_md(folder, filename, content):
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    rel = os.path.relpath(path, BASE)
    print(f"  ✓ {rel}")

def header(normnummer, kap, titel, tags, gueltig):
    return f"""---
tags: {tags}
normnummer: {normnummer}
gueltig_ab: "{gueltig}"
kapitel: "{kap}"
titel: "{titel}"
---

# {kap} – {titel}

"""


# ═══════════════════════════════════════════════════════════════
# SN EN 380:1993
# ═══════════════════════════════════════════════════════════════
print("\n▶ SN EN 380:1993 – Holzbauwerke Prüfverfahren")
F380 = os.path.join(BASE, "SN_EN_380_1993")

import pdfplumber, warnings
warnings.filterwarnings("ignore")
en380 = {}
with pdfplumber.open(r"C:\Users\schin\OneDrive\Desktop\snen380_1993_d.pdf") as pdf:
    for i, page in enumerate(pdf.pages):
        t = page.extract_text()
        if t:
            en380[i + 1] = t.strip()

def en380_clean(pages_list):
    parts = [clean_page(en380.get(p, "")) for p in pages_list]
    return "\n\n".join(p for p in parts if p)

write_md(F380, "01_Anwendungsbereich.md",
    header("SN EN 380:1993", "Kap. 1–2", "Anwendungsbereich und normative Verweisungen",
           "[Norm, Holzbau, Prüfverfahren]", "1995-10-01") +
    en380_clean([5]))

write_md(F380, "03_04_Definitionen_Symbole.md",
    header("SN EN 380:1993", "Kap. 3–4", "Definitionen und Symbole",
           "[Norm, Holzbau, Prüfverfahren, Definitionen]", "1995-10-01") +
    en380_clean([5]))

write_md(F380, "05_Allgemeine_Anforderungen.md",
    header("SN EN 380:1993", "Kap. 5", "Allgemeine Anforderungen",
           "[Norm, Holzbau, Prüfverfahren, Anforderungen]", "1995-10-01") +
    en380_clean([6]))

write_md(F380, "06_Pruefverfahren.md",
    header("SN EN 380:1993", "Kap. 6", "Prüfverfahren für statische Belastungen",
           "[Norm, Holzbau, Prüfverfahren, Statik, Belastung, Tabelle]", "1995-10-01") +
    en380_clean([6, 7, 8, 9]))

write_md(F380, "06_7_Pruefbericht.md",
    header("SN EN 380:1993", "Kap. 6.7", "Prüfbericht",
           "[Norm, Holzbau, Prüfverfahren, Dokumentation]", "1995-10-01") +
    en380_clean([9, 10]))


# ═══════════════════════════════════════════════════════════════
# SIA 384/6:2021
# ═══════════════════════════════════════════════════════════════
print("\n▶ SIA 384/6:2021 – Erdwärmesonden")
p384 = load("384_6")
F384 = os.path.join(BASE, "SIA_384-6_2021")
T384 = "[Norm, Geothermie, Erdwärmesonde, SIA384-6, Gebäudetechnik]"
N384 = "SN 546384/6:2021"
G384 = "2021-05-01"

for fname, kap, titel, s, e in [
    ("00_Geltungsbereich.md",       "Kap. 0", "Geltungsbereich",                              5,  5),
    ("01_Begriffe_Definitionen.md", "Kap. 1", "Verständigung – Begriffe und Definitionen",    6, 11),
    ("01_Symbole_Indizes.md",       "Kap. 1", "Verständigung – Symbole und Indizes",         12, 13),
    ("02_Strategische_Planung.md",  "Kap. 2", "Strategische Planung",                        14, 17),
    ("03_Projektierung.md",         "Kap. 3", "Projektierung",                               18, 25),
    ("04_Baustoffe.md",             "Kap. 4", "Anforderungen an Baustoffe und Konstruktion", 26, 29),
    ("05_Ausfuehrung.md",           "Kap. 5", "Ausführung",                                  30, 32),
    ("06_Pruefungen.md",            "Kap. 6", "Prüfungen",                                   33, 34),
    ("07_Dokumentation.md",         "Kap. 7", "Dokumentation",                               35, 37),
    ("08_Betrieb_Wartung.md",       "Kap. 8", "Betrieb und Wartung",                         38, 38),
]:
    write_md(F384, fname,
        header(N384, kap, titel, T384, G384) + get_pages(p384, s, e))


# ═══════════════════════════════════════════════════════════════
# SIA 385/2:2025
# ═══════════════════════════════════════════════════════════════
print("\n▶ SIA 385/2:2025 – Trinkwarmwasser")
p385 = load("385_2")
F385 = os.path.join(BASE, "SIA_385-2_2025")
T385 = "[Norm, Trinkwarmwasser, Sanitär, SIA385-2, Gebäudetechnik, Warmwasser]"
N385 = "SN 546385/2:2025"
G385 = "2025-02-01"

for fname, kap, titel, s, e in [
    ("00_Geltungsbereich.md",              "Kap. 0", "Geltungsbereich und normative Verweisungen",       5,  7),
    ("01_Begriffe_Definitionen.md",         "Kap. 1", "Verständigung – Begriffe und Definitionen",       8, 13),
    ("01_Symbole_Indizes.md",               "Kap. 1", "Verständigung – Symbole, Indizes, Abkürzungen",  14, 16),
    ("02_Projektierung.md",                 "Kap. 2", "Projektierung",                                  17, 18),
    ("03_Grobauslegung.md",                 "Kap. 3", "Grobauslegung – Optimierung in der Vorprojektphase", 19, 22),
    ("04_Feinplanung.md",                   "Kap. 4", "Feinplanung – Auslegung der Warmwasserversorgung", 23, 28),
    ("05_Waermebedarf_Hilfsenergie.md",     "Kap. 5", "Wärmebedarf und Hilfsenergie",                   29, 29),
]:
    write_md(F385, fname,
        header(N385, kap, titel, T385, G385) + get_pages(p385, s, e))


# ═══════════════════════════════════════════════════════════════
# SIA 387/4:2023
# ═══════════════════════════════════════════════════════════════
print("\n▶ SIA 387/4:2023 – Beleuchtung")
p387 = load("387_4")
F387 = os.path.join(BASE, "SIA_387-4_2023")
T387 = "[Norm, Beleuchtung, Elektrizität, SIA387-4, Gebäudetechnik, Licht, Energiebedarf]"
N387 = "SN 565387/4:2023"
G387 = "2023-08-01"

for fname, kap, titel, s, e in [
    ("00_Geltungsbereich.md",                "Kap. 0", "Geltungsbereich und normative Verweisungen",    5,  6),
    ("01_Begriffe_Definitionen.md",           "Kap. 1", "Verständigung – Begriffe und Definitionen",    7, 11),
    ("01_Symbole_Indizes.md",                 "Kap. 1", "Verständigung – Symbole, Indizes, Darstellung", 12, 14),
    ("02_Projektierung.md",                   "Kap. 2", "Projektierung",                               15, 16),
    ("03_1_Allgemeines_Grundlagen.md",        "Kap. 3.1", "Berechnung – Allgemeines und Grundlagen",   17, 18),
    ("03_2_Spezifische_Leistung.md",          "Kap. 3.2", "Berechnung – Spezifische Leistung",         19, 21),
    ("03_3_Volllaststunden_Methode1.md",      "Kap. 3.3", "Berechnung – Volllaststunden (Methode 1)",  22, 26),
    ("03_4_Stundenschritt_Methode2.md",       "Kap. 3.4", "Berechnung – Jahresenergie im Stundenschritt (Methode 2)", 27, 30),
    ("04_Anforderungen.md",                   "Kap. 4", "Anforderungen",                               31, 34),
]:
    write_md(F387, fname,
        header(N387, kap, titel, T387, G387) + get_pages(p387, s, e))

print("\n✓ Alle Kapitel-Dateien erstellt.")
