"""
extract_figur8_crop.py

Korrekt zugeschnittene Figur 8 (Bodenoberflächentemperatur) aus Anhang C
der SIA 384-6 PDF. Seite 56 (Index 55).
"""
import fitz, sys, io
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

PDF_PATH = Path(r"C:/Users/schin/Downloads/SN 546384-6 SIA 384-6_2021_d.pdf")
ASSETS   = Path(r"C:/Users/schin/OneDrive/Desktop/Wissens_db/data/assets/SIA_384-6_2021")

doc = fitz.open(str(PDF_PATH))
mat = fitz.Matrix(3, 3)

page = doc[55]  # Seite 56, Index 55
w = page.rect.width

# Chart-Bereich: ohne Caption-Text (y=297), nur die Grafik
clip = fitz.Rect(22, 342, w - 22, 530)
pix  = page.get_pixmap(matrix=mat, clip=clip, colorspace=fitz.csRGB)
out  = ASSETS / "figur_8_bodenoberflaeche.png"
pix.save(str(out))
print(f"Seite 56: figur_8_bodenoberflaeche.png  ({pix.width}x{pix.height} px)")

doc.close()
print("Fertig.")
