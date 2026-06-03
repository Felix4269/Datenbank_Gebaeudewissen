"""
insert_images_idaice.py

1. Extrahiert alle echten Figures aus IDAICE_Manual.pdf
2. Speichert sie als PNG in data/assets/IDAICE_Manual/
3. Fügt ![[...]] Bild-Referenzen in die .md-Dateien ein

Duplikate / Icons die übersprungen werden:
  Im1  (17×17 px)  = kleines Icon
  Im4  = PNG-Kopie von Im3 (gleiche Pixeldimensionen)
  Im6  = PNG-Kopie von Im5 (gleiche Pixeldimensionen)
  Im16 = TIF-Kopie von Im15 (gleiche Dimensionen)
  Im21 = exaktes Duplikat von Im20 (gleiche Dimensionen + Dateigröße)

Mapping-Logik (basiert auf Seitenzuordnung + Textanalyse):
  Im2  p8  → Fig 2.1  (ESBO-Tab)
  Im3  p9  → Fig 2.2  (Standard-Level Main Form)
  Im5  p10 → Fig 2.3  (Advanced-Level Main Form)
  Im7  p11 → Fig 3.1  (Primary system default config)
  Im8  p13 → Fig 3.2  (ESBO Plant General view)
  Im9  p17 → Fig 3.4  (ESBO Plant Advanced Level schematic)
             (Fig 3.3 = Vektorgrafik im PDF, kein Rasterbild)
             (Fig 3.4 = Vektorgrafik im PDF, kein Rasterbild)
  Im10 p21 → Fig 3.5  (Default AHU)
  Im11 p24 → Fig 3.6  (Climate zone model schematic)
  Im12 p26 → Fig 3.7  (Zone form)
  Im13 p26 → Fig 3.8  (Control setpoints)
  Im14 p29 → Fig 3.9  (Radiator on wall)
  Im15 p30 → Fig 3.10 (Cooling panel)
  Im17 p31 → Fig 3.11 (Active beam form)
  Im18 p32 → Fig 3.12 (Floor heating form)
  Im19 p35 → Fig 4.1  (IFC Mapping dialog)
  Im20 p36 → Fig 4.2  (IFC model + ICE zone)
  Im22 p40 → Fig 5.1  (AHU at advanced level)
  Im23 p41 → Fig 5.2  (Variable browser)
  Im24 p42 → Fig 5.3  (Window form + external blind)
  Im25 p42 → Fig 5.4  (Shade control macro)
  Im26 p43 → Fig 5.5  (Thermostat setpoint)
  Im27 p45 → Fig 6.1  (Time-split parallelization checkbox)
  Im28 p45 → Fig 6.2  (Simulation preferences)
"""

import re
from pathlib import Path

try:
    from pypdf import PdfReader
except ImportError:
    raise SystemExit("pypdf fehlt – bitte: pip install pypdf")

PDF_PATH  = Path(r"C:\Users\schin\Downloads\IDAICE_Manual.pdf")
ASSETS    = Path(r"C:\Users\schin\OneDrive\Desktop\Wissens_db\data\assets\IDAICE_Manual")
MD_DIR    = Path(r"C:\Users\schin\OneDrive\Desktop\Wissens_db\data\IDAICE_Manual")

# PDF-Bildname (ohne Extension) → (Figurbezeichnung, Ausgabedateiname)
FIGURE_MAP = {
    "Im2":  ("2.1",  "fig_2_1.png"),
    "Im3":  ("2.2",  "fig_2_2.png"),
    "Im5":  ("2.3",  "fig_2_3.png"),
    "Im7":  ("3.1",  "fig_3_1.png"),
    "Im8":  ("3.2",  "fig_3_2.png"),
    "Im9":  ("3.4",  "fig_3_4.png"),
    "Im10": ("3.5",  "fig_3_5.png"),
    "Im11": ("3.6",  "fig_3_6.png"),
    "Im12": ("3.7",  "fig_3_7.png"),
    "Im13": ("3.8",  "fig_3_8.png"),
    "Im14": ("3.9",  "fig_3_9.png"),
    "Im15": ("3.10", "fig_3_10.png"),
    "Im17": ("3.11", "fig_3_11.png"),
    "Im18": ("3.12", "fig_3_12.png"),
    "Im19": ("4.1",  "fig_4_1.png"),
    "Im20": ("4.2",  "fig_4_2.png"),
    "Im22": ("5.1",  "fig_5_1.png"),
    "Im23": ("5.2",  "fig_5_2.png"),
    "Im24": ("5.3",  "fig_5_3.png"),
    "Im25": ("5.4",  "fig_5_4.png"),
    "Im26": ("5.5",  "fig_5_5.png"),
    "Im27": ("6.1",  "fig_6_1.png"),
    "Im28": ("6.2",  "fig_6_2.png"),
}

# Figurnummer → Dateiname (wird nach Extraktion gefüllt)
NUM_TO_FILE = {}  # type: dict


# ── 1. Bilder extrahieren ────────────────────────────────────────────────────
def extract_images() -> None:
    ASSETS.mkdir(parents=True, exist_ok=True)
    reader = PdfReader(str(PDF_PATH))

    for page in reader.pages:
        for img in page.images:
            stem = img.name.rsplit(".", 1)[0]          # "Im2", "Im3", …
            if stem not in FIGURE_MAP:
                continue
            fig_num, out_name = FIGURE_MAP[stem]
            out_path = ASSETS / out_name

            pil_img = img.image                        # PIL Image
            if pil_img.mode not in ("RGB", "RGBA", "L", "LA"):
                pil_img = pil_img.convert("RGB")
            pil_img.save(str(out_path), "PNG")
            NUM_TO_FILE[fig_num] = out_name
            print(f"  {out_name:<20}  Fig {fig_num:<5}  {pil_img.width}×{pil_img.height}")


# ── 2. Figure-Captions in .md-Dateien durch Bild + Beschriftung ersetzen ────
# Jeder Eintrag: (Datei, exakter Such-String, Figurnummer, Beschriftungstext)
CAPTIONS = [
    # 02_Basic_Principles.md
    ("02_Basic_Principles.md",
     "Figure 2.1 The Building tab of IDA ESBO",
     "2.1", "The Building tab of IDA ESBO"),
    ("02_Basic_Principles.md",
     "Figure 2.2 Main form for the building at standard level",
     "2.2", "Main form for the building at standard level"),
    ("02_Basic_Principles.md",
     "Figure 2.3 Main Form for the building at the advanced level",
     "2.3", "Main Form for the building at the advanced level"),

    # 03_1_Model_Description_Intro.md
    ("03_1_Model_Description_Intro.md",
     "Figure 3.1 The primary system in the default configuration",
     "3.1", "The primary system in the default configuration"),

    # 03_2_2_esbo_plant.md  (Fig 3.4 = Vektorgrafik → kein Bild)
    ("03_2_2_esbo_plant.md",
     "Figure 3.2 The ESBO Plant General view",
     "3.2", "The ESBO Plant General view"),
    ("03_2_2_esbo_plant.md",
     "Figure 3.3 An example of the General tab of the ESBO Plant populated with models",
     "3.3", "An example of the General tab of the ESBO Plant populated with models"),
    ("03_2_2_esbo_plant.md",
     "Figure 3.4 The ESBO Plant of Fig. 3.3 viewed at Advanced level of IDA ICE",
     "3.4", "The ESBO Plant of Fig. 3.3 viewed at Advanced level of IDA ICE"),

    # 03_2_3_air_handling.md
    ("03_2_3_air_handling.md",
     "Figure 3.5 Default air handling unit",
     "3.5", "Default air handling unit"),

    # 03_3_1_zone_intro_solar.md
    ("03_3_1_zone_intro_solar.md",
     "Figure 3.6 Schematic view (advanced level) of Climate zone model",
     "3.6", "Schematic view (advanced level) of Climate zone model"),

    # 03_3_2_airflows.md
    ("03_3_2_airflows.md",
     "Figure 3.7 The zone form.",
     "3.7", "The zone form"),
    ("03_3_2_airflows.md",
     "Figure 3.8 Control setpoints",
     "3.8", "Control setpoints"),

    # 03_3_5_6_fan_coil_hydronic.md
    ("03_3_5_6_fan_coil_hydronic.md",
     "Figure 3.9 A radiator on an external wall, its standard form, and a dialog for the Device type.",
     "3.9", "A radiator on an external wall, its standard form, and a dialog for the Device type"),

    # 03_3_7_cooling_units.md
    ("03_3_7_cooling_units.md",
     "Figure 3.10 A cooling panel on the ceiling surface, its standard form, and a dialog for the\nDevice type.",
     "3.10", "A cooling panel on the ceiling surface, its standard form, and a dialog for the Device type"),
    ("03_3_7_cooling_units.md",
     "Figure 3.11 Active beam form",
     "3.11", "Active beam form"),
    ("03_3_7_cooling_units.md",
     "Figure 3.12 Floor heating form",
     "3.12", "Floor heating form"),

    # 03_4_Building_Geometry.md
    ("03_4_Building_Geometry.md",
     "Figure 4.1 IFC Mapping dialog",
     "4.1", "IFC Mapping dialog"),
    ("03_4_Building_Geometry.md",
     "Figure 4.2 IFC model with an ICE zone, a selected IFC space and unselected IFC spaces.",
     "4.2", "IFC model with an ICE zone, a selected IFC space and unselected IFC spaces"),

    # 04_Getting_Started_Advanced.md
    ("04_Getting_Started_Advanced.md",
     "Figure 5.1 The air handling unit.",
     "5.1", "The air handling unit"),
    ("04_Getting_Started_Advanced.md",
     "Figure 5.2",
     "5.2", ""),
    ("04_Getting_Started_Advanced.md",
     "Figure 5.3",
     "5.3", ""),
    ("04_Getting_Started_Advanced.md",
     "Figure 5.4",
     "5.4", ""),
    ("04_Getting_Started_Advanced.md",
     "Figure 5.5",
     "5.5", ""),

    # 05_Tips_Tricks.md  – zwei Figuren auf einer Zeile
    ("05_Tips_Tricks.md",
     "Figure 6.1 Figure 6.2",
     "6.1+6.2", ""),
]


def make_replacement(fig_num: str, caption: str) -> str:
    """Baut den Ersatzstring: Bild-Embed + kursive Beschriftung."""
    if fig_num == "6.1+6.2":
        parts = []
        for n in ("6.1", "6.2"):
            if n in NUM_TO_FILE:
                parts.append(f"![[../assets/IDAICE_Manual/{NUM_TO_FILE[n]}]]")
            parts.append(f"*Abb. {n}*")
        return "\n\n".join(parts)

    lines = []
    if fig_num in NUM_TO_FILE:
        lines.append(f"![[../assets/IDAICE_Manual/{NUM_TO_FILE[fig_num]}]]")

    if caption:
        lines.append(f"*Abb. {fig_num} – {caption}*")
    else:
        lines.append(f"*Abb. {fig_num}*")

    return "\n".join(lines)


def insert_image_refs() -> None:
    for md_file, search_str, fig_num, caption in CAPTIONS:
        md_path = MD_DIR / md_file
        if not md_path.exists():
            print(f"  FEHLT: {md_file}")
            continue

        content = md_path.read_text(encoding="utf-8")

        if search_str not in content:
            print(f"  NICHT GEFUNDEN in {md_file}: {search_str[:50]!r}")
            continue

        replacement = make_replacement(fig_num, caption)
        new_content = content.replace(search_str, replacement, 1)
        md_path.write_text(new_content, encoding="utf-8")
        has_img = fig_num in NUM_TO_FILE or (
            fig_num == "6.1+6.2" and ("6.1" in NUM_TO_FILE or "6.2" in NUM_TO_FILE)
        )
        status = "[Bild]" if has_img else "[Text]"
        print(f"  {status} Fig {fig_num:<6} -> {md_file}")


# ── Hauptprogramm ─────────────────────────────────────────────────────────────
def main() -> None:
    print(f"PDF:  {PDF_PATH}")
    print(f"Bilder -> {ASSETS}")
    print()

    print("=== 1. Bilder extrahieren ===")
    extract_images()
    print(f"  {len(NUM_TO_FILE)} Bilder gespeichert.\n")

    print("=== 2. Bild-Referenzen einfügen ===")
    insert_image_refs()
    print("\nFertig.")


if __name__ == "__main__":
    main()
