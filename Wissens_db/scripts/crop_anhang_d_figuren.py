"""
crop_anhang_d_figuren.py

Schneidet alle 21 Figuren aus Anhang D (SIA 384-6) präzise aus dem PDF heraus.
Jede Figur wird ohne Bildunterschrift (nur Diagrammbereich) als PNG gespeichert.
Die Bildunterschriften sind bereits im Markdown-Text vorhanden.
"""
import fitz, io, sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

PDF_PATH = Path(r"C:/Users/schin/Downloads/SN 546384-6 SIA 384-6_2021_d.pdf")
ASSETS   = Path(r"C:/Users/schin/OneDrive/Desktop/Wissens_db/data/assets/SIA_384-6_2021")

doc = fitz.open(str(PDF_PATH))
mat = fitz.Matrix(3, 3)  # 3× Zoom für hohe Auflösung

# (Dateiname, Seiten-Index 0-basiert, y_top, y_bot)
# y-Werte in PDF-Punkten (Seite 63 = Index 62, A4 = 842 pt hoch)
# Bildunterschriften werden NICHT eingeschlossen (bereits im Markdown)
figures = [
    # Seite 63 (idx 62): Figur 9 + 10
    ("figur_9_normleistung_de32.png",              62, 115, 392),
    ("figur_10_normleistung_de40.png",             62, 502, 800),

    # Seite 64 (idx 63): Figur 11
    ("figur_11_zuschlag_simplex.png",              63, 212, 520),

    # Seite 65 (idx 64): Figur 12
    ("figur_12_volllaststunden.png",               64, 280, 580),

    # Seite 67 (idx 66): Figur 13
    ("figur_13_zuschlag_volllaststunden.png",      66, 274, 575),

    # Seite 68 (idx 67): Figur 14 + 15
    ("figur_14_zuschlag_volllaststunden.png",      67, 103, 395),
    ("figur_15_zuschlag_volllaststunden.png",      67, 434, 720),

    # Seite 69 (idx 68): Figur 16 + 17
    ("figur_16_zuschlag_volllaststunden.png",      68, 103, 408),
    ("figur_17_zuschlag_volllaststunden.png",      68, 448, 740),

    # Seite 70 (idx 69): Figur 18 + 19
    ("figur_18_zuschlag_volllaststunden.png",      69, 103, 388),
    ("figur_19_zuschlag_volllaststunden.png",      69, 427, 730),

    # Seite 71 (idx 70): Figur 20 + 21
    ("figur_20_zuschlag_volllaststunden.png",      70, 103, 397),
    ("figur_21_zuschlag_volllaststunden.png",      70, 436, 725),

    # Seite 77 (idx 76): Figur 22
    ("figur_22_temperaturabkuehlung_nachbar.png",  76, 486, 738),

    # Seite 78 (idx 77): Figur 23
    ("figur_23_lastprofil_ews.png",                77, 575, 790),

    # Seite 80 (idx 79): Figur 24 + 25
    ("figur_24_druckverlust_glycol.png",           79,  92, 400),
    ("figur_25_druckverlust_glycol_visk.png",      79, 428, 745),

    # Seite 81 (idx 80): Figur 26 + 27
    ("figur_26_hydraulische_leistung_ews.png",     80,  92, 405),
    ("figur_27_druckverlust_pe_rohr.png",          80, 433, 700),

    # Seite 82 (idx 81): Figur 28 + 29
    ("figur_28_hydraulische_leistung_pe.png",      81,  92, 355),
    ("figur_29_druckverlust_faktor_glycol.png",    81, 460, 700),
]

for fname, page_idx, y_top, y_bot in figures:
    page = doc[page_idx]
    w    = page.rect.width
    clip = fitz.Rect(22, y_top, w - 22, y_bot)
    pix  = page.get_pixmap(matrix=mat, clip=clip, colorspace=fitz.csRGB)
    out  = ASSETS / fname
    pix.save(str(out))
    print(f"Seite {page_idx+1:3d}: {fname}  ({pix.width}x{pix.height} px)")

doc.close()
print("\nFertig.")
