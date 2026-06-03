# Wissensdatenbank – CLAUDE.md

## Projektziel

Lokale Wissensdatenbank für Bauingenieurwesen / Gebäudetechnik (ZHAW, Prof. Markus Hubbuch).
Quellen: Schweizer SIA-Normen, EN-Normen, Simulationssoftware-Dokumentation und Vorlesungsskripte.
Format: Strukturierte Markdown-Dateien, optimiert für Obsidian und Claude-Zugriff.
Ziel: schnelles Nachschlagen von Definitionen, Formeln, Konzepten und Normanforderungen.

---

## Projektstruktur

```
Wissens_db/
├── CLAUDE.md                          # Diese Datei
├── data/
│   ├── 00_Wissensbank_Index.md        # Haupt-Index aller Themengebiete
│   │
│   ├── IDAICE_Manual/                 # IDA ICE User Manual v4.8 (EN)
│   │   ├── _IDAICE_Manual_MOC.md
│   │   └── *.md                       # 14 Kapitel-Dateien
│   │
│   ├── IDA_ICE_Tutorial/              # IDA ICE Tutorial ZHAW (DE)
│   │   ├── _IDA_ICE_Tutorial_MOC.md
│   │   └── *.md                       # 12 Kapitel-Dateien
│   │
│   ├── SIA_384-6_2021/                # Norm: Erdwärmesonden
│   │   ├── _SIA_384-6_2021_MOC.md
│   │   └── *.md
│   │
│   ├── SIA_385-2_2025/                # Norm: Warmwasser
│   │   ├── _SIA_385-2_2025_MOC.md
│   │   └── *.md
│   │
│   ├── SIA_387-4_2023/                # Norm: Beleuchtung / Elektrizität
│   │   ├── _SIA_387-4_2023_MOC.md
│   │   └── *.md
│   │
│   ├── SN_EN_380_1993/                # Norm: Holzbau / Prüfverfahren
│   │   ├── _SN_EN_380_1993_MOC.md
│   │   └── *.md
│   │
│   ├── NEST_Sprint_Simulation/        # Simulationsprojekt: NEST (Empa)
│   │   └── *.md
│   │
│   ├── Skript_Bauphysik/              # Vorlesungsskript Bauphysik 2026
│   │   └── *.md
│   │
│   ├── Skript_Energie/                # Vorlesungsskript Energieflüsse 2026
│   │   └── *.md
│   │
│   ├── Skript_Lueftung/               # Vorlesungsskript Lüftungstechnik
│   │   └── *.md
│   │
│   ├── assets/                        # Extrahierte Bilder aus PDFs
│   │   ├── IDAICE_Manual/             # fig_X_Y.png (23 Abbildungen)
│   │   ├── Skript_Bauphysik/
│   │   ├── Skript_Energie/
│   │   └── Skript_Lueftung/
│   │
│   └── raw/                           # Original-PDFs (Zwischenablage)
│       ├── IDAICE_Manual.pdf
│       └── IDA_ICE_Tutorial_brdj.pdf
│
└── scripts/                           # Verarbeitungs-Skripte (Python)
```

---

## Quell-Dokumente

### Vorlesungsskripte (Prof. Markus Hubbuch, ZHAW)

| Datei | Thema | Pfad |
|---|---|---|
| Skript Lüftung.pdf | Lüftungstechnik, Luftwechsel, Ventilationssysteme | `C:/Users/schin/Downloads/Skript Lüftung.pdf` |
| Skript Bauphysik 2026.pdf | Wärmeschutz, Feuchteschutz, Schallschutz, U-Werte | `C:/Users/schin/Downloads/Skript Bauphysik 2026.pdf` |
| Skript Energie im Gebäude 2026.pdf | Energiebilanz, Heizlast, Kühllast, Primärenergie | `C:/Users/schin/Downloads/Skript Energie im Gebäude 2026.pdf` |

### Simulationssoftware

| Datei | Thema | Pfad |
|---|---|---|
| IDAICE_Manual.pdf | IDA ICE v4.8 – Modelle, HVAC, Geometrie, Advanced Level | `C:/Users/schin/Downloads/IDAICE_Manual.pdf` |
| IDA_ICE_Tutorial_brdj.pdf | IDA ICE Tutorial ZHAW – Varianten, Heizlast, SIA 380/1 | `C:/Users/schin/Downloads/IDA_ICE_Tutorial_brdj.pdf` |

### Normen (PDFs in Downloads)

| Norm | Thema |
|---|---|
| SIA 384/6:2021 | Geothermie, Erdwärmesonden, Planung & Ausführung |
| SIA 385/2:2025 | Sanitär, Warmwasser, Auslegung & Energiebedarf |
| SIA 387/4:2023 | Beleuchtung, Elektrizitätsbedarf, Berechnungsmethoden |
| SN EN 380:1993 | Holzbau, Prüfverfahren für statische Belastungen |

Neue PDFs kommen nach `C:/Users/schin/Downloads/`.

---

## Tech-Stack

- **Python 3.8** (Windows: `py`-Launcher)
- **pdfplumber** – PDF-Textextraktion (Layouts, Formeln, Tabellen)
- **pypdf** – Bild-Extraktion aus PDFs
- **Pillow (PIL)** – Bildkonvertierung (CMYK → RGB, PNG-Export)
- **Markdown (.md)** – Speicherformat für alle Wissensinhalte
- **Obsidian** – Lesen, Navigieren, Graph-Ansicht

```
Abhängigkeiten:
pdfplumber>=0.10.0
pypdf>=3.0.0
Pillow>=9.0.0
pymupdf>=1.23.0   (PyMuPDF / fitz – für Skript-PDFs und Tutorial)
```

---

## Datenformat

Jede Themensektion hat:
- Eine **MOC-Datei** (`_<Name>_MOC.md`) als Inhaltsverzeichnis
- **Kapitel-Dateien** mit YAML-Frontmatter, Navigationsleiste und Textinhalt
- Obsidian-Verlinkungen (`[[Dateiname|Anzeigetext]]`) für Navigation

### Frontmatter-Schema

```yaml
---
tags: [IDA-ICE, Simulation, Grundlagen]
normnummer: "IDAICE Manual v4.8"
gueltig_ab: "2018-01-01"
kapitel: "Kap. 2"
titel: "Basic Principles of IDA ICE"
---
```

### Bilder

Extrahierte Abbildungen liegen unter `data/assets/<Sektion>/`.
Einbindung in Markdown: `![[../assets/IDAICE_Manual/fig_3_5.png]]`

---

## Skripte (scripts/)

Alle Skripte werden mit `py scripts/<name>.py` ausgeführt.

| Skript | Zweck |
|---|---|
| `extract_idaice_manual.py` | IDAICE_Manual.pdf → .md-Dateien (CID-Decoder) |
| `insert_images_idaice.py` | Bilder aus IDAICE_Manual.pdf extrahieren + in .md einfügen |
| `insert_images_tutorial.py` | Bilder aus IDA_ICE_Tutorial_brdj.pdf extrahieren + in .md einfügen |
| `extract_images.py` | Bilder aus beliebigen PDFs extrahieren |
| `create_idaice_files.py` | Initiale .md-Dateistruktur für IDA ICE |
| `create_chapter_files.py` | Kapitel-Dateien für neue Sektionen anlegen |
| `create_hubbuch_files.py` / `create_hubbuch_vault.py` | Skripte für Hubbuch-Skripte |
| `create_nest_sprint_files.py` | NEST-Sprint-Dateien anlegen |
| `add_obsidian_links.py` | Obsidian-Links nachträglich einfügen |
| `format_headings.py` | Überschriften-Formatierung normalisieren |
| `fix_subscripts.py` | Tiefgestellte Zeichen korrigieren |
| `_fix_quotes_tutorial.py` | Verwaiste typografische Anführungszeichen aus Tutorial .md entfernen |
| `_fix_merged_words_tutorial.py` | Zusammengewachsene Wörter (fehlende Leerzeichen aus PDF-Extraktion) reparieren |
| `fix_*.py` | Dokumentspezifische Korrekturen |
| `dedup_images.py` | Doppelte Bilder entfernen |
| `convert_to_latex.py` | Formeln → LaTeX-Format |
| `_inspect_pdfs.py` | PDF-Struktur analysieren |

---

## Navigationskonzept

Einstieg über `data/00_Wissensbank_Index.md` → MOC-Datei der Sektion → Kapitel-Dateien.

```
00_Wissensbank_Index.md
 └─► _<Sektion>_MOC.md
      └─► Kapitel-Dateien (navigierbar per ◀ / ▶ in der Datei)
```

---

## Neue PDFs hinzufügen

1. PDF nach `C:/Users/schin/Downloads/` legen
2. Passendes Extraktions-Skript ausführen (oder neues erstellen)
3. `data/00_Wissensbank_Index.md` um die neue Sektion ergänzen

---

## Konventionen

- Skripte: `py` (Windows Python-Launcher), Encoding immer `utf-8`
- Dateinamen: `lowercase_mit_unterstrichen.md`, keine Umlaute
- MOC-Dateien: Präfix `_`, z.B. `_IDAICE_Manual_MOC.md`
- Bilder: `fig_X_Y.png` (IDAICE) oder `abb<N>_<slug>.jpg` (Skripte)
- Keine Cloud-Dienste, keine externen Datenbanken — alles lokal

---

## Bekannte Lücken

- [ ] `data/chunks/` und `data/raw/*.txt` – geplante Pipeline nie umgesetzt, Ordner leer
- [ ] Skript_Bauphysik / Skript_Energie / Skript_Lueftung – .md vorhanden, aber keine MOC-Verlinkung im Index geprüft
- [ ] Formelerkennung / LaTeX-Export – `convert_to_latex.py` existiert, noch nicht vollständig
- [ ] Semantische Suche (Embeddings) – nicht implementiert
