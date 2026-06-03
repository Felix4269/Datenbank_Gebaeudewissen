"""
extract_figur1_crop.py

Schneidet Figur 1 (Übersicht Erdwärmenutzung) sauber aus der SIA 384-6 PDF aus.
Figur 1 befindet sich auf Seite 6 (0-basiert: Index 5) der PDF.
"""

import fitz  # PyMuPDF
from pathlib import Path

PDF_PATH  = Path(r"C:/Users/schin/Downloads/SN 546384-6 SIA 384-6_2021_d.pdf")
OUT_PATH  = Path(r"C:/Users/schin/OneDrive/Desktop/Wissens_db/data/assets/SIA_384-6_2021/figur_1_uebersicht_erdwaermenutzung.png")

# Seite 6 (1-basiert) = Index 5 (0-basiert)
PAGE_INDEX = 5

doc  = fitz.open(str(PDF_PATH))
page = doc[PAGE_INDEX]

# Alle Bild-Objekte auf der Seite ausgeben
print(f"Seite {PAGE_INDEX+1}: {page.rect}")
print("\nBild-Objekte auf dieser Seite:")
for img in page.get_images(full=True):
    xref = img[0]
    bbox = page.get_image_bbox(img)
    print(f"  xref={xref}  bbox={bbox}")

# Zeichnungs-/Vektorgrafik-Blöcke
print("\nText/Bild-Blöcke (Typ 1 = Bild):")
blocks = page.get_text("dict")["blocks"]
for b in blocks:
    if b["type"] == 1:  # Bild-Block
        print(f"  Bild-Block: bbox={b['bbox']}")

# Seitenabmessungen
print(f"\nSeitenbreite: {page.rect.width:.1f} pt, Höhe: {page.rect.height:.1f} pt")

# Figur 1 liegt ungefähr im Bereich y=160..340 pt (von oben)
# Wir schneiden den Bereich mit etwas Rand aus
# Koordinaten in Punkten (pt): links, oben, rechts, unten
clip = fitz.Rect(30, 250, page.rect.width - 25, 540)

mat  = fitz.Matrix(3, 3)   # 3x Zoom → hohe Auflösung
pix  = page.get_pixmap(matrix=mat, clip=clip, colorspace=fitz.csRGB)

pix.save(str(OUT_PATH))
print(f"\n✓ Gespeichert: {OUT_PATH}")
print(f"  Grösse: {pix.width} × {pix.height} px")

doc.close()
