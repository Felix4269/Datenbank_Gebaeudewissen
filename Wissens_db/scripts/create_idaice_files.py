"""
Erstellt Kapitel-.md-Dateien für IDAICE_Manual und IDA_ICE_Tutorial
inklusive Obsidian-Links, Navigation und MOC.
"""

import json, os, re

BASE    = r"C:\Users\schin\OneDrive\Desktop\Wissens_db\data"
F_MAN   = os.path.join(BASE, "IDAICE_Manual")
F_TUT   = os.path.join(BASE, "IDA_ICE_Tutorial")

# ─── Rohdaten laden ───────────────────────────────────────────────────────────
with open(os.path.join(BASE, "raw_idaice_manual.json"),   encoding="utf-8") as f:
    MANUAL = json.load(f)
with open(os.path.join(BASE, "raw_idaice_tutorial.json"), encoding="utf-8") as f:
    TUTORIAL = json.load(f)


# ─── Hilfsfunktionen ──────────────────────────────────────────────────────────
NOISE = [
    r"^IDA Indoor Climate and Energy",
    r"^EQUA Simulation AB",
    r"^Kapitel \d+\. Simulation Vorgehen\s*$",
    r"^ICP intern:",
    r"^\d+/\d+\s*$",
]

def clean(text):
    lines = [l.strip() for l in text.split("\n")]
    out = []
    for l in lines:
        if not l:
            continue
        if any(re.search(p, l) for p in NOISE):
            continue
        out.append(l)
    return "\n".join(out)

def get_pages(src, start, end):
    parts = []
    for p in range(start, end + 1):
        raw = src.get(str(p), "").strip()
        c = clean(raw)
        if c:
            parts.append(c)
    return "\n\n".join(parts)

def write(folder, fname, content):
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, fname)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"  ✓ {os.path.relpath(path, BASE)}")

def nav(folder_key, idx, chapters):
    prev = f"◀ [[{chapters[idx-1][0]}|{chapters[idx-1][1]}]]" if idx > 0 else "◀ *(Anfang)*"
    moc  = f"[[_{folder_key}_MOC|↑ Inhaltsverzeichnis]]"
    nxt  = f"[[{chapters[idx+1][0]}|{chapters[idx+1][1]}]] ▶" if idx < len(chapters)-1 else "*(Ende)* ▶"
    return f"> {prev}  ·  {moc}  ·  {nxt}\n\n---\n\n"

def header(fname, kap, titel, tags, normnummer, gueltig):
    return f"""---
tags: {tags}
normnummer: "{normnummer}"
gueltig_ab: "{gueltig}"
kapitel: "{kap}"
titel: "{titel}"
---

# {kap} – {titel}

"""

def moc_file(folder, folder_key, titel, thema, normnummer, chapters):
    lines = [
        "---",
        "tags: [MOC, IDA-ICE, Index]",
        f'normnummer: "{normnummer}"',
        "---",
        "",
        f"# {titel}",
        "",
        f"**Thema:** {thema}",
        "",
        "## Kapitel",
        "",
    ]
    for fname, kap, desc in chapters:
        lines.append(f"- [[{fname}|{kap} – {desc}]]")
    lines += ["", "---", "", "[[00_Wissensbank_Index|↑ Zurück zum Hauptindex]]", ""]
    write(folder, f"_{folder_key}_MOC.md", "\n".join(lines))


# ═══════════════════════════════════════════════════════════════════════════════
# IDAICE_Manual (EN)
# ═══════════════════════════════════════════════════════════════════════════════
print("\n▶ IDAICE User Manual")
TAGS_M = "[IDA-ICE, Manual, Simulation, Gebäudesimulation, HVAC]"
NR_M   = "IDAICE Manual v4.8"
GU_M   = "2018-01-01"

CHAPTERS_M = [
    ("01_About_the_Manual",          "Kap. 1",   "About the Manual",                    6,  7),
    ("02_Basic_Principles",          "Kap. 2",   "Basic Principles of IDA ICE",         8, 10),
    ("03_1_Model_Description_Intro", "Kap. 3.1", "Model Description – Introduction",   11, 11),
    ("03_2_Primary_System_Plant",    "Kap. 3.2", "Model Description – Primary System Plant", 12, 17),
    ("03_3_Zone_Models_HVAC",        "Kap. 3.3", "Model Description – Zone Models & HVAC",  18, 30),
    ("03_4_Building_Geometry",       "Kap. 3.4", "Model Description – Building Geometry & Zones", 31, 38),
    ("04_Getting_Started_Advanced",  "Kap. 4",   "Getting Started – Advanced Level",   39, 43),
    ("05_Tips_Tricks",               "Kap. 5",   "Tips & Tricks / Numerical Instabilities", 44, 46),
]
CHAPTERS_M_NAV = [(f, k, d) for f, k, d, *_ in CHAPTERS_M]

moc_file(F_MAN, "IDAICE_Manual", "IDA ICE – User Manual (v4.8)",
         "Gebäudesimulation · Raumklima · Energiebedarf · HVAC", NR_M, CHAPTERS_M_NAV)

for idx, (fname, kap, titel, s, e) in enumerate(CHAPTERS_M):
    body = nav("IDAICE_Manual", idx, CHAPTERS_M_NAV) + get_pages(MANUAL, s, e)
    write(F_MAN, fname + ".md",
          header(fname, kap, titel, TAGS_M, NR_M, GU_M) + body)


# ═══════════════════════════════════════════════════════════════════════════════
# IDA_ICE_Tutorial (DE – ZHAW)
# ═══════════════════════════════════════════════════════════════════════════════
print("\n▶ IDA ICE Tutorial (ZHAW)")
TAGS_T = "[IDA-ICE, Tutorial, Simulation, Gebäudesimulation, SIA, ZHAW, Deutsch]"
NR_T   = "IDA ICE Tutorial ZHAW v1.1"
GU_T   = "2024-01-01"

CHAPTERS_T = [
    ("00_Glossar_Konstanten",       "Vorwort",  "Glossar und Physikalische Konstanten",           6,  7),
    ("01_1_Modell_Grundsaetzliches","Kap. 1.1", "Modell Aufbau – Grundsätzliches",               8, 11),
    ("01_2a_Variante0_Schritte1_7", "Kap. 1.2a","Variante 0 Step-by-Step – Schritte 1–7 (Eingaben, Hülle, Klima)", 12, 18),
    ("01_2b_Variante0_Geometrie",   "Kap. 1.2b","Variante 0 Step-by-Step – Gebäudegeometrie & Zonen", 19, 29),
    ("01_2c_Variante0_Simulation",  "Kap. 1.2c","Variante 0 Step-by-Step – Simulation & Auswertung", 30, 33),
    ("01_2d_Kalibrieren",           "Kap. 1.2.1","Modell kalibrieren",                           34, 35),
    ("01_3a_Varianten_Erstellen",   "Kap. 1.3", "Varianten Erstellen – Grundlagen & Projektmanager", 36, 39),
    ("01_3b_Basisvarianten",        "Kap. 1.3.2","Basisvarianten 1, 2, 3 und 4",                 40, 42),
    ("01_3c_Untervarianten",        "Kap. 1.3.3","Untervarianten l, s, hl, hs, fl und fs",       43, 48),
    ("01_4a_Heizlast_Systemnachweis","Kap. 1.4.1–2","Heizlastermittlung & Systemnachweis SIA 380/1", 49, 50),
    ("01_4b_Jahresenergiebedarf",   "Kap. 1.4.3","Jahresenergiebedarf",                          51, 51),
    ("99_Literatur_Versionshistorie","Anhang",   "Literaturverzeichnis & Versionshistorie",       52, 53),
]
CHAPTERS_T_NAV = [(f, k, d) for f, k, d, *_ in CHAPTERS_T]

moc_file(F_TUT, "IDA_ICE_Tutorial", "IDA ICE – Tutorial (ZHAW, Deutsch)",
         "Gebäudesimulation · Varianten · Heizlast · SIA 380/1", NR_T, CHAPTERS_T_NAV)

for idx, (fname, kap, titel, s, e) in enumerate(CHAPTERS_T):
    body = nav("IDA_ICE_Tutorial", idx, CHAPTERS_T_NAV) + get_pages(TUTORIAL, s, e)
    write(F_TUT, fname + ".md",
          header(fname, kap, titel, TAGS_T, NR_T, GU_T) + body)

print("\n✓ Fertig.")
