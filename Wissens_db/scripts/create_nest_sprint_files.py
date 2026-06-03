# -*- coding: utf-8 -*-
"""
create_nest_sprint_files.py
Processes the NEST Sprint simulation .md files into the knowledge base
with Obsidian wiki-links, YAML frontmatter and a MOC file.
"""

import os
import re

SRC = r"C:\Users\schin\Downloads"
DST = r"C:\Users\schin\OneDrive\Desktop\Wissens_db\data\NEST_Sprint_Simulation"
INDEX = r"C:\Users\schin\OneDrive\Desktop\Wissens_db\data\00_Wissensbank_Index.md"

os.makedirs(DST, exist_ok=True)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def add_schedule_links(text):
    """Replace bare schedule names with [[09_Schedules|name]] links."""
    schedules = [
        "schedule_office_occupancy",
        "schedule_ventilation_fans",
        "schedule_heat_recovery",
        "schedule_heating_availability",
        "schedule_cooling_availability",
        "schedule_shading",
        "schedule_temperature_control",
        "schedule_office",
    ]
    for s in schedules:
        # Replace only when not already inside [[ ]]
        text = re.sub(
            r'(?<!\[\[)(?<!\|)' + re.escape(s) + r'(?!\]\])',
            f'[[09_Schedules|{s}]]',
            text
        )
    return text

def add_param_links(text):
    """Replace file references with wiki links."""
    replacements = {
        '"03_parameter_catalog.md"': '[[03_Parameter_Catalog]]',
        '"09_schedules.md"':         '[[09_Schedules]]',
        '"08_baseline_model.md"':    '[[08_Baseline_Model]]',
        '"02_building_model_overview.md"': '[[02_Building_Overview]]',
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  Erstellt: {os.path.basename(path)}")

def nav(prev_link, moc_link, next_link):
    parts = []
    if prev_link:
        parts.append(f"◀ {prev_link}")
    parts.append(f"[[_NEST_Sprint_MOC|↑ MOC]]")
    if next_link:
        parts.append(f"{next_link} ▶")
    return "> " + " · ".join(parts) + "\n\n---\n\n"

# ---------------------------------------------------------------------------
# 02_Building_Overview.md
# ---------------------------------------------------------------------------

building_content = """\
---
tags: [NEST, Sprint, Simulation, Gebäudemodell]
projekt: NEST Unit Sprint
etage: 1. Obergeschoss
tool: IDA ICE 5.1.1
---

""" + nav(None, "_NEST_Sprint_MOC", "[[08_Baseline_Model|08 Baseline →]]") + """\
# Gebäudemodell – NEST Sprint

## Gebäude

* Name: NEST
* Unit: Sprint
* Etage: 1. Obergeschoss
* Standort: Schweiz (Empa Dübendorf)

## Simulationstool

* Software: IDA ICE 5.1.1

## Fokuszonen

* [[08_Baseline_Model|Büro 172]]
* [[08_Baseline_Model|Büro 176]]
* [[08_Baseline_Model|Büro 185]]

Weitere Zonen:

* Korridorzonen
* Technikräume

## HLK-System

### Büros

* Heizung und Kühlung über aktive Deckensysteme (KVS)
* Temperatursollwerte → siehe [[09_Schedules|schedule_temperature_control]]

### Lüftung

* Mechanische Lüftungsanlage (Zu- und Abluft)
* Wärmerückgewinnung → [[09_Schedules|schedule_heat_recovery]]

### Sonstige Zonen

* Korridore und Technikräume: Ideale Heizung, keine aktive Kühlung

## Wetterdaten

* Quelle: MeteoSchweiz
* Station: Zürich Fluntern (SMA)
* Jahr: 2022
* Format: EPW (konvertiert für IDA ICE)

## Messdaten

### Temperatur

* Raumlufttemperatur aus Sensoren in Büros
* Zeitauflösung: stündlich (aggregiert)

### CO₂ (optional)

* Deckenmontiertes Sensorsystem
* Zur Analyse des Belegungsverhaltens

### Energie (optional)

* Thermische Energie und Leistung aus Gebäudetechnik
* Messung über Energieventil (Belimo)

## Simulationsausgaben

Hauptausgaben für den Vergleich:

* Raumlufttemperatur (stündlich)
* ggf. CO₂-Konzentration
* Energie (Heizen / Kühlen)

## Vergleichsansatz

* Zeitauflösung: stündlich
* Fokus auf Übereinstimmung gemessener Raumtemperaturen für 2022
* Besonderes Augenmerk auf:
  * Wochenendverhalten
  * Heizbetrieb an Werktagen
  * Mittagstemperaturspitzen
  * saisonale Unterschiede

---

""" + nav(None, "_NEST_Sprint_MOC", "[[08_Baseline_Model|08 Baseline →]]")

write_file(os.path.join(DST, "02_Building_Overview.md"), building_content)

# ---------------------------------------------------------------------------
# 08_Baseline_Model.md
# ---------------------------------------------------------------------------

baseline_content = """\
---
tags: [NEST, Sprint, Simulation, Baseline, IDA-ICE]
projekt: NEST Unit Sprint
tool: IDA ICE 5.1.1
---

""" + nav("[[02_Building_Overview|← 02 Gebäude]]", "_NEST_Sprint_MOC", "[[03_Parameter_Catalog|03 Parameter →]]") + """\
# Baseline-Modell – NEST Sprint

## Beschreibung

Diese Datei definiert den strukturellen Aufbau des Baseline-Modells.
Alle Parameterwerte und Zeitpläne sind definiert in:

* [[03_Parameter_Catalog]] – Parameterkatalog
* [[09_Schedules]] – Zeitpläne

Diese Datei beschreibt nur die Modellstruktur und Systemkonfiguration.

## Allgemeine Modellinformationen

* Projekt: NEST Unit Sprint
* Fokus: 1. Obergeschoss
* Simulationstool: IDA ICE 5.1.1

## Zonen

### Bürozonen

* Büro 171 – 176
* Büro 181 – 186

### Sonstige Zonen

* Technikraum 170
* Technikraum 180
* Gang 177
* Gang 187

Zonen gesamt: 16

## Zonengeometrie

### Bürozonen

* Typische Raumhöhe: 3,21 m
* Typische Grundfläche: ca. 8,11 – 13,13 m²

Ausgewählte Zonen:

| Zone | Fläche | Höhe |
|---|---|---|
| Büro 185 | 9,212 m² | 3,21 m |
| Büro 176 | 12,88 m² | 3,21 m |
| Büro 172 | 9,212 m² | 3,21 m |

### Sonstige Zonen

| Zone | Fläche | Höhe |
|---|---|---|
| Technikraum 180 | 10,61 m² | 3,21 m |
| Technikraum 170 | 10,07 m² | 3,21 m |
| Gang 187 | 19,44 m² | 3,21 m |
| Gang 177 | 19,36 m² | 3,21 m |

### Gesamt

* Konditionierte Grundfläche gesamt: 172,9 m²
* Zonenvolumen gesamt: ca. 555 m³

## HLK-System

### Lüftung

* Zentrales Lüftungsgerät: Lüftungsgerät
* Angeschlossene Zonen: alle Zonen
* Gesamtzuluft: 187 L/s
* Gesamtabluft: 187 L/s

### Bürozonen

* Systemtyp: KVS
* Lokale Heiz-/Kühlelemente (Deckensystem)

### Technikräume & Korridore

* Ideale Heizelemente
* Keine aktive Kühlung

## Interne Lasten

* Gesteuert über [[09_Schedules|schedule_office_occupancy]]
* Enthält:
  * Belegung
  * Beleuchtung
  * Geräte

## HLK-Steuerung

* Lüftung, Heizung und Kühlung über Zeitpläne gesteuert
* Siehe:
  * [[09_Schedules|schedule_ventilation_fans]]
  * [[09_Schedules|schedule_heating_availability]]
  * [[09_Schedules|schedule_cooling_availability]]

## Solarsteuerung & Verschattung

* Verschattung gesteuert durch:
  * [[09_Schedules|schedule_shading]]
  * [[03_Parameter_Catalog|shading_threshold]] (Einstrahlungsschwellenwert)

## Parameterverweis

Alle anpassbaren Modellparameter → [[03_Parameter_Catalog]]

## Zeitplanverweis

Alle zeitabhängigen Verhalten → [[09_Schedules]]

## Aktuelle Modellmerkmale

* Bürobasierte interne Lasten
* Zeitabhängige Lüftung
* Saisonale Heiz- und Kühlverfügbarkeit
* Strahlungsbasierte Verschattung mit Zeitplanbeschränkung
* Mehrzonige thermische Interaktion

---

""" + nav("[[02_Building_Overview|← 02 Gebäude]]", "_NEST_Sprint_MOC", "[[03_Parameter_Catalog|03 Parameter →]]")

write_file(os.path.join(DST, "08_Baseline_Model.md"), baseline_content)

# ---------------------------------------------------------------------------
# 03_Parameter_Catalog.md
# ---------------------------------------------------------------------------

param_content = """\
---
tags: [NEST, Sprint, Simulation, Parameter, HLK]
projekt: NEST Unit Sprint
---

""" + nav("[[08_Baseline_Model|← 08 Baseline]]", "_NEST_Sprint_MOC", "[[09_Schedules|09 Zeitpläne →]]") + """\
# Parameterkatalog – NEST Sprint

Alle anpassbaren Modellparameter der Baseline-Simulation.
Zeitplanreferenzen → [[09_Schedules]] | Modellstruktur → [[08_Baseline_Model]]

---

## ventilation_flow_offices

* Kategorie: HLK / Lüftung
* Ort: Zone – Lüftung – Zu-/Abluftvolumenstrom
* Einheit: l/(s·m²)
* Basiswert: **0,6**
* Erlaubter Bereich: 0,1 – 3,0
* Priorität: mittel

### Einfluss

* beeinflusst Wärmeverlust im Winter
* beeinflusst Kühlpotenzial im Sommer
* beeinflusst CO₂-Konzentration

---

## ventilation_flow_Technikräume_Korridor

* Kategorie: HLK / Lüftung
* Ort: Zone – Lüftung – Zu-/Abluftvolumenstrom
* Einheit: l/(s·m²)
* Basiswert: **2,0**
* Erlaubter Bereich: 0,1 – 3,0
* Priorität: mittel

### Einfluss

* beeinflusst Wärmeverlust im Winter
* beeinflusst Kühlpotenzial im Sommer
* beeinflusst CO₂-Konzentration

---

## ventilation_schedule

* Kategorie: HLK / Zeitplan
* Ort: Lüftungssteuerung
* Einheit: Zeitplan
* Basiswert: [[09_Schedules|schedule_ventilation_fans]]
* Priorität: mittel

### Einfluss

* definiert, wann Luftaustausch stattfindet
* beeinflusst Wärmeverlust und Kühlpotenzial
* beeinflusst CO₂-Dynamik

### Haupteffekt im Modell

* keine Lüftung nachts
* keine Lüftung am Wochenende

---

## heat_recovery_efficiency

* Kategorie: HLK / Lüftung
* Ort: Lüftungsanlage – Wärmetauscher
* Einheit: Zeitplan
* Basiswert: [[09_Schedules|schedule_heat_recovery]]
* Priorität: mittel

### Einfluss

* reduziert Lüftungswärmeverluste im Winter
* beeinflusst Zulufttemperatur
* wirkt sich auf Heizenergiebedarf aus

---

## heating_availability

* Kategorie: HLK / Steuerung
* Ort: Heizanlage – Verfügbarkeitszeitplan
* Einheit: Zeitplan
* Basiswert: [[09_Schedules|schedule_heating_availability]]
* Priorität: **hoch**

### Einfluss

* bestimmt, wann Heizen erlaubt ist
* verhindert Heizen im Sommer

### Haupteffekt im Modell

* keine Heizung im Sommer
* vermeidet gleichzeitiges Heizen und Kühlen

---

## heating_setpoint_offices

* Kategorie: HLK / Steuerung
* Ort: Zone – Sollwerte
* Einheit: °C
* Basiswert: [[09_Schedules|schedule_temperature_control]] → Heizungssollwert
* Priorität: **hoch**

### Einfluss

* wirkt sich direkt auf die Innentemperatur in der Heizperiode aus
* bestimmt minimale Komforttemperatur

---

## cooling_availability

* Kategorie: HLK / Steuerung
* Ort: Kühlanlage – Verfügbarkeitszeitplan
* Einheit: Zeitplan
* Basiswert: [[09_Schedules|schedule_cooling_availability]]
* Priorität: **hoch**

### Einfluss

* bestimmt, wann Kühlen erlaubt ist
* verhindert Kühlen im Winter

### Haupteffekt im Modell

* keine Kühlung im Winter
* verhindert unrealistische Winterkühlung

---

## cooling_setpoint_offices

* Kategorie: HLK / Steuerung
* Ort: Zone – Sollwerte
* Einheit: °C
* Basiswert: [[09_Schedules|schedule_temperature_control]] → Kühlungssollwert
* Priorität: **hoch**

### Einfluss

* bestimmt maximale Innentemperatur
* definiert Kühlungsaktivierungsschwelle

---

## cooling_capacity_offices

* Kategorie: HLK / System
* Ort: Zone – Kühlanlage
* Einheit: W
* Basiswert: **500 W**
* Erlaubter Bereich: 100 – 1200 W
* Priorität: **hoch**

### Einfluss

* begrenzt Kühlleistung
* beeinflusst Spitzentemperaturreduktion

---

## heating_capacity_offices

* Kategorie: HLK / System
* Ort: Zone – Heizanlage
* Einheit: W
* Basiswert: **500 W**
* Erlaubter Bereich: 100 – 1200 W
* Priorität: **hoch**

### Einfluss

* begrenzt Heizleistung
* beeinflusst Fähigkeit, Sollwert zu halten

---

## occupancy_density

* Kategorie: Interne Lasten
* Ort: Zone – Personen
* Einheit: Zeitplan
* Basiswert: [[09_Schedules|schedule_office_occupancy]]
* Priorität: mittel

### Einfluss

* beeinflusst interne Wärmegewinne
* beeinflusst CO₂-Erzeugung

---

## lighting_load

* Kategorie: Interne Lasten
* Ort: Zone – Beleuchtung
* Einheit: Zeitplan
* Basiswert: [[09_Schedules|schedule_office_occupancy]]
* Priorität: mittel

### Einfluss

* trägt zu internen Wärmegewinnen bei

---

## equipment_load

* Kategorie: Interne Lasten
* Ort: Zone – Geräte
* Einheit: Zeitplan
* Basiswert: [[09_Schedules|schedule_office_occupancy]]
* Priorität: mittel

### Einfluss

* trägt zu internen Wärmegewinnen bei

---

## shading_threshold

* Kategorie: Solar / Fassade
* Ort: Fenster – Verschattungssteuerung
* Einheit: W/m²
* Basiswert: **200 W/m²**
* Erlaubter Bereich: 100 – 600 W/m²
* Priorität: **hoch**

### Einfluss

* bestimmt, ab welchem Strahlungsniveau die Verschattung aktiviert wird
* niedriger Schwellenwert → frühere Aktivierung → reduzierte Solargewinne
* hoher Schwellenwert → verzögerte Aktivierung → erhöhte Solargewinne

---

## shading_schedule

* Kategorie: Solar / Steuerung
* Ort: Fenster – Verschattungszeitplan
* Einheit: Zeitplan
* Basiswert: [[09_Schedules|schedule_shading]] (im Baseline **nicht aktiviert**)
* Priorität: **hoch**

### Einfluss

* definiert, wann Verschattung aktiviert werden darf
* beschränkt Verschattung auf bestimmte Zeitfenster
* kann Verschattung trotz hoher Einstrahlung verhindern

### Haupteffekt im Modell

* Verschattungszeitplan ist im Baseline **nicht aktiviert**

---

""" + nav("[[08_Baseline_Model|← 08 Baseline]]", "_NEST_Sprint_MOC", "[[09_Schedules|09 Zeitpläne →]]")

write_file(os.path.join(DST, "03_Parameter_Catalog.md"), param_content)

# ---------------------------------------------------------------------------
# 09_Schedules.md
# ---------------------------------------------------------------------------

schedules_content = """\
---
tags: [NEST, Sprint, Simulation, Zeitplan, HLK]
projekt: NEST Unit Sprint
---

""" + nav("[[03_Parameter_Catalog|← 03 Parameter]]", "_NEST_Sprint_MOC", "[[05a_Calibration_Office_172|05a Kalibrierung 172 →]]") + """\
# Zeitpläne – NEST Sprint

Alle zeitabhängigen Steuerungen des IDA-ICE-Modells.
Parameter-Referenzen → [[03_Parameter_Catalog]] | Modellstruktur → [[08_Baseline_Model]]

---

## schedule_office_occupancy

* Name in IDA ICE: `08-17 wochentags1 (Sprint)`

### Werktage

| Zeitfenster | Wert |
|---|---|
| 08:00 – 12:00 | 1 |
| 12:00 – 13:00 | 0 (Mittagspause) |
| 13:00 – 17:00 | 1 |
| Restliche Zeit | 0 |

### Wochenende & Feiertage

* Samstag → 0
* Sonntag → 0
* Feiertage → 0

### Angewendet auf

* Belegung / Occupancy
* Beleuchtung / Lighting
* Geräte / Equipment

### Interpretation

* Typisches Büronutzungsprofil
* Keine internen Gewinne am Wochenende
* Mittagspause reduziert interne Gewinne

---

## schedule_ventilation_fans

* Name in IDA ICE: `06-18 wochentags`

### Werktage

| Zeitfenster | Wert |
|---|---|
| 06:00 – 18:00 | 1 |
| Restliche Zeit | 0 |

### Wochenende

* Aus (Off)

### Angewendet auf

* Lüftungsventilatoren

### Interpretation

* Lüftung nur tagsüber aktiv
* Keine mechanische Lüftung nachts oder am Wochenende

---

## schedule_heat_recovery

* Name in IDA ICE: (implizit / immer aktiv)

### Verhalten

* 24h aktiv
* Keine Zeitplanbeschränkung

### Angewendet auf

* Wärmetauscher

### Interpretation

* Konstante Wärmerückgewinnung
* Reduziert Wärmeverluste im Winter

---

## schedule_heating_availability

* Name in IDA ICE: `HeizungSommer_inaktiv`

### Verhalten

| Zeitraum | Wert |
|---|---|
| 1. Juni – 31. August | 0 (inaktiv) |
| Restliches Jahr | 1 (aktiv) |

### Angewendet auf

* Heizanlage

### Interpretation

* Heizung im Sommer deaktiviert
* Verhindert Heizen in warmen Monaten

---

## schedule_cooling_availability

* Name in IDA ICE: `KühlungSommer_aktiv`

### Verhalten

| Zeitraum | Wert |
|---|---|
| 1. Oktober – 1. April | 0 (inaktiv) |
| Restliches Jahr | 1 (aktiv) |

### Angewendet auf

* Kühlanlage

### Interpretation

* Kühlung im Winter deaktiviert
* Nur in wärmeren Perioden aktiv

---

## schedule_shading

* Name in IDA ICE: `Verschattung_Test2`
* **Im Baseline-Modell nicht aktiviert**

### Zusatzbedingung

* Solare Einstrahlung ≥ 200 W/m² (→ [[03_Parameter_Catalog|shading_threshold]])

### Angewendet auf

* Fensterverschattung (Lamellen)

### Steuerlogik

Verschattung aktiviert sich nur, wenn:
1. Zeitplan = 1
   **UND**
2. Solare Einstrahlung > 200 W/m²

### Interpretation

* Verschattung auf Mittagsstunden beschränkt
* Keine Verschattung morgens oder abends
* Kann zu erhöhten Solargewinnen außerhalb des aktiven Fensters führen

---

## schedule_temperature_control

* (implizit)

### Heizungssollwert

| Zeitraum | Sollwert |
|---|---|
| Standard | 21 °C |
| 1. Juli – 31. August | 15 °C |

### Kühlungssollwert

| Zeitraum | Sollwert |
|---|---|
| Juni | 25 °C |
| Restliches Jahr | 24 °C |

### Interpretation

* Saisonale Anpassung der Sollwerte
* Heizung im Sommer durch niedrigen Sollwert faktisch deaktiviert
* Kühlverhalten variiert leicht im Juni

---

""" + nav("[[03_Parameter_Catalog|← 03 Parameter]]", "_NEST_Sprint_MOC", "[[05a_Calibration_Office_172|05a Kalibrierung 172 →]]")

write_file(os.path.join(DST, "09_Schedules.md"), schedules_content)

# ---------------------------------------------------------------------------
# Split calibration history by office
# ---------------------------------------------------------------------------

print("\nLese 05_calibration_history.md ...")
with open(os.path.join(SRC, "05_calibration_history.md"), encoding="utf-8") as f:
    cal_raw = f.read()

# Split into sections: preamble + office blocks
# Each office block starts with "## Run 001 office XXX"
office_pattern = re.compile(r'(?=^## Run 001 office (\d+))', re.MULTILINE)
parts = office_pattern.split(cal_raw)

# parts[0] = preamble text before first office block
# Then alternating: office_number, block_text
preamble = parts[0].strip()

office_blocks = {}
i = 1
while i < len(parts):
    office_num = parts[i].strip()
    block = parts[i + 1].strip()
    office_blocks[office_num] = block
    i += 2

print(f"  Gefundene Büros: {list(office_blocks.keys())}")

# ---------------------------------------------------------------------------
# Build calibration file for one office
# ---------------------------------------------------------------------------

OFFICE_LABELS = {
    "172": ("05a_Calibration_Office_172", "05a", "a"),
    "176": ("05b_Calibration_Office_176", "05b", "b"),
    "185": ("05c_Calibration_Office_185", "05c", "c"),
}

NAV_CAL = {
    "172": ("[[09_Schedules|← 09 Zeitpläne]]",   "[[05b_Calibration_Office_176|05b Büro 176 →]]"),
    "176": ("[[05a_Calibration_Office_172|← 05a Büro 172]]", "[[05c_Calibration_Office_185|05c Büro 185 →]]"),
    "185": ("[[05b_Calibration_Office_176|← 05b Büro 176]]", None),
}

PARAM_LINK_MAP = {
    "ventilation_flow_offices":           "[[03_Parameter_Catalog|ventilation_flow_offices]]",
    "cooling_capacity_offices":           "[[03_Parameter_Catalog|cooling_capacity_offices]]",
    "heating_capacity_offices":           "[[03_Parameter_Catalog|heating_capacity_offices]]",
    "heating_availability":               "[[03_Parameter_Catalog|heating_availability]]",
    "cooling_availability":               "[[03_Parameter_Catalog|cooling_availability]]",
    "ventilation_schedule":               "[[03_Parameter_Catalog|ventilation_schedule]]",
    "shading_schedule":                   "[[03_Parameter_Catalog|shading_schedule]]",
    "shading_threshold":                  "[[03_Parameter_Catalog|shading_threshold]]",
    "occupancy_schedule":                 "[[03_Parameter_Catalog|occupancy_density]]",
}

def linkify_cal(text):
    """Replace bare parameter names in calibration text with wiki links."""
    for param, link in PARAM_LINK_MAP.items():
        text = re.sub(
            r'(?<!\[\[)(?<!\|)' + re.escape(param) + r'(?!\]\])',
            link,
            text
        )
    # Also link schedule names
    text = add_schedule_links(text)
    return text

for office_num, (filename, label, letter) in OFFICE_LABELS.items():
    if office_num not in office_blocks:
        print(f"  WARNUNG: Büro {office_num} nicht gefunden – übersprungen.")
        continue

    prev_nav, next_nav = NAV_CAL[office_num]
    block = office_blocks[office_num]
    block_linked = linkify_cal(block)

    content = f"""\
---
tags: [NEST, Sprint, Kalibrierung, Büro{office_num}, Simulation]
projekt: NEST Unit Sprint
büro: "{office_num}"
---

""" + nav(prev_nav, "_NEST_Sprint_MOC", next_nav) + f"""\
# Kalibrierung – Büro {office_num}

## Auswertungsansatz

{preamble}

---

## Parametertests

{block_linked}

---

""" + nav(prev_nav, "_NEST_Sprint_MOC", next_nav)

    write_file(os.path.join(DST, f"{filename}.md"), content)

# ---------------------------------------------------------------------------
# _NEST_Sprint_MOC.md
# ---------------------------------------------------------------------------

moc_content = """\
---
tags: [NEST, Sprint, Simulation, MOC]
projekt: NEST Unit Sprint
---

# NEST Sprint – Simulationsprojekt (MOC)

Kalibrierungsstudie einer Büroetage im NEST-Gebäude (Empa Dübendorf)
Simuliert mit IDA ICE 5.1.1 | Messjahr 2022 | Wetter: MeteoSchweiz Zürich Fluntern

---

## Dokumente

| Datei | Inhalt |
|---|---|
| [[02_Building_Overview]] | Gebäude, Zonen, Messdaten, Wetterdaten |
| [[08_Baseline_Model]] | Modellstruktur, Zonen, HLK-System, Schedules |
| [[03_Parameter_Catalog]] | Alle 14 Modellparameter mit Einfluss und Basiswerten |
| [[09_Schedules]] | Alle 7 Zeitpläne (Belegung, Lüftung, Heizung, Kühlung, Verschattung) |
| [[05a_Calibration_Office_172]] | Parametertests Büro 172 – Run 001–009 |
| [[05b_Calibration_Office_176]] | Parametertests Büro 176 – Run 001–009 |
| [[05c_Calibration_Office_185]] | Parametertests Büro 185 – Run 001–009 |

---

## Fokuszonen

* [[05a_Calibration_Office_172|Büro 172]] – 9,212 m²
* [[05b_Calibration_Office_176|Büro 176]] – 12,88 m²
* [[05c_Calibration_Office_185|Büro 185]] – 9,212 m²

## Bewertungsperioden

* **Winter**: Dezember – Februar
* **Sommer**: Juni – August
* **Übergang**: März – Mai, September – November

## Metriken

* MAE – Mean Absolute Error
* MBE – Mean Bias Error
* RMSE – Root Mean Square Error

## Getestete Parameter

| Run | Parameter | Kategorie |
|---|---|---|
| 001 | [[03_Parameter_Catalog|ventilation_flow_offices]] | Lüftung |
| 002 | [[03_Parameter_Catalog|cooling_capacity_offices]] | Kühlung |
| 003 | [[03_Parameter_Catalog|heating_capacity_offices]] | Heizung |
| 004 | [[03_Parameter_Catalog|heating_availability]] | Steuerung |
| 005 | [[03_Parameter_Catalog|cooling_availability]] | Steuerung |
| 006 | [[03_Parameter_Catalog|ventilation_schedule]] | Zeitplan |
| 007 | [[03_Parameter_Catalog|shading_schedule]] | Verschattung |
| 008 | [[03_Parameter_Catalog|shading_threshold]] | Verschattung |
| 009 | [[03_Parameter_Catalog|occupancy_density]] | Interne Lasten |

---

*Zurück zum Hauptindex: [[00_Wissensbank_Index]]*
"""

write_file(os.path.join(DST, "_NEST_Sprint_MOC.md"), moc_content)

# ---------------------------------------------------------------------------
# Update 00_Wissensbank_Index.md
# ---------------------------------------------------------------------------

print("\nAktualisiere 00_Wissensbank_Index.md ...")

with open(INDEX, encoding="utf-8") as f:
    index_text = f.read()

NEST_SECTION = """
---

## Simulationsprojekte

### NEST Sprint – IDA ICE Kalibrierungsstudie

> Thermische Gebäudesimulation einer Büroetage im NEST-Gebäude (Empa Dübendorf, 2022)

| Datei | Inhalt |
|---|---|
| [[_NEST_Sprint_MOC\\|NEST Sprint MOC]] | Übersicht und Navigation |
| [[02_Building_Overview\\|Gebäudemodell]] | Zonen, HVAC, Wetterdaten |
| [[08_Baseline_Model\\|Baseline-Modell]] | Modellstruktur und Systemkonfiguration |
| [[03_Parameter_Catalog\\|Parameterkatalog]] | 14 Simulationsparameter |
| [[09_Schedules\\|Zeitpläne]] | 7 Steuerungszeitpläne |
| [[05a_Calibration_Office_172\\|Kalibrierung Büro 172]] | Run 001–009 |
| [[05b_Calibration_Office_176\\|Kalibrierung Büro 176]] | Run 001–009 |
| [[05c_Calibration_Office_185\\|Kalibrierung Büro 185]] | Run 001–009 |
"""

# Avoid duplicates
if "NEST Sprint" not in index_text:
    index_text = index_text.rstrip() + "\n" + NEST_SECTION + "\n"
    with open(INDEX, 'w', encoding='utf-8') as f:
        f.write(index_text)
    print("  Index aktualisiert.")
else:
    print("  NEST Sprint bereits im Index – übersprungen.")

print("\nFertig! Alle NEST-Sprint-Dateien erstellt.")
