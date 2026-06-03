"""
extract_figur2_3.py

Findet und schneidet Figur 2 und Figur 3 aus der SIA 384-6 PDF aus.
Beide Figuren liegen in Kap. 3.5 (Nachbarsonden).
"""

import fitz
import sys, io
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

PDF_PATH = Path(r"C:/Users/schin/Downloads/SN 546384-6 SIA 384-6_2021_d.pdf")
ASSETS   = Path(r"C:/Users/schin/OneDrive/Desktop/Wissens_db/data/assets/SIA_384-6_2021")

doc  = fitz.open(str(PDF_PATH))
page = doc[24]   # Seite 25 (0-basiert: Index 24)
mat  = fitz.Matrix(3, 3)   # 3x Zoom fuer hohe Aufloesung

# --- Figur 2: Definition der anrechenbaren Grundstueckflaeche GSF_eff ---
clip2 = fitz.Rect(28, 65, page.rect.width - 25, 350)
pix2  = page.get_pixmap(matrix=mat, clip=clip2, colorspace=fitz.csRGB)
out2  = ASSETS / "figur_2_gsf_eff.png"
pix2.save(str(out2))
print(f"Figur 2 gespeichert: {out2}  ({pix2.width}x{pix2.height} px)")

# --- Figur 3: Temperaturabkuehlung durch kuenftige Nachbarsonden ---
clip3 = fitz.Rect(28, 398, page.rect.width - 25, 720)
pix3  = page.get_pixmap(matrix=mat, clip=clip3, colorspace=fitz.csRGB)
out3  = ASSETS / "figur_3_temperaturabkuehlung.png"
pix3.save(str(out3))
print(f"Figur 3 gespeichert: {out3}  ({pix3.width}x{pix3.height} px)")

doc.close()
print("Fertig.")
