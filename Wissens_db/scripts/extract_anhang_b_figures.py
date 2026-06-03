"""
extract_anhang_b_figures.py

Korrekt zugeschnittene Figuren 4, 5, 6, 7 und B.1.1.4-Illustration
aus Anhang B der SIA 384-6 PDF.
"""
import fitz, sys, io
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

PDF_PATH = Path(r"C:/Users/schin/Downloads/SN 546384-6 SIA 384-6_2021_d.pdf")
ASSETS   = Path(r"C:/Users/schin/OneDrive/Desktop/Wissens_db/data/assets/SIA_384-6_2021")

doc = fitz.open(str(PDF_PATH))
mat = fitz.Matrix(3, 3)

# (page_index, y_top, y_bottom, filename)
CROPS = [
    # Figur 4: nur Chart (Caption im MD separat), Seite 46, Index 45
    (45, 415, 715, "figur_4_druckverlust_ews_kreis.png"),
    # Figur 5: Caption + Chart, Seite 47, Index 46
    (46, 258, 506, "figur_5_druckverlust_faktor.png"),
    # B.1.1.4 Illustration: Schematic + 2 Charts, Seite 48, Index 47
    (47, 55, 372, "figur_b114_beispiel_ews.png"),
    # Figur 6: nur Chart (Caption im MD separat), Seite 51, Index 50
    (50, 230, 478, "figur_6_dichtheitspruefung_ews.png"),
    # Figur 7: Caption + Chart, Seite 53, Index 52
    (52, 248, 514, "figur_7_langzeitpruefung.png"),
]

for idx, y_top, y_bot, fname in CROPS:
    page = doc[idx]
    w    = page.rect.width
    clip = fitz.Rect(22, y_top, w - 22, y_bot)
    pix  = page.get_pixmap(matrix=mat, clip=clip, colorspace=fitz.csRGB)
    out  = ASSETS / fname
    pix.save(str(out))
    print(f"  Seite {idx+1}: {fname}  ({pix.width}x{pix.height} px)")

doc.close()
print("Fertig.")
