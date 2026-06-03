"""
extract_anhang_a_forms.py (v2)

Extrahiert nur die Formular-Inhalte (ohne Seitentitel und Seitenfuss)
aus den Anhang-A-Seiten der SIA 384-6 PDF.
"""
import fitz, sys, io
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

PDF_PATH = Path(r"C:/Users/schin/Downloads/SN 546384-6 SIA 384-6_2021_d.pdf")
ASSETS   = Path(r"C:/Users/schin/OneDrive/Desktop/Wissens_db/data/assets/SIA_384-6_2021")

doc = fitz.open(str(PDF_PATH))
mat = fitz.Matrix(3, 3)   # 3x Zoom fuer scharfe Formulare

# (page_index, y_top, y_bottom, filename, label)
# y-Koordinaten beziehen sich auf die PDF-Punkte (A4 = 595 x 842 pt)
# Formular-Box beginnt nach dem Abschnittstitel, endet vor dem Seitenfuss
FORMS = [
    (38, 0,   785, "anhang_a1_bohrprotokoll.png",       "A.1 Bohrprotokoll"),
    (39, 128, 668, "anhang_a2_pruefprotokoll.png",       "A.2 Pruefprotokoll"),
    (40, 128, 582, "anhang_a3_anschluss_seite1.png",     "A.3.1 Anschluss"),
    (41, 106, 752, "anhang_a3_anschluss_seite2.png",     "A.3.2 Durchfluss/Fuellung"),
    (42, 162, 715, "anhang_a4_datenaustausch.png",       "A.4 EDV-Datenaustausch"),
    (43,  88, 622, "anhang_a5_abnahmeprotokoll.png",     "A.5 Abnahmeprotokoll"),
    (44,  88, 748, "anhang_a6_checkliste.png",           "A.6 Checkliste"),
]

for idx, y_top, y_bot, fname, label in FORMS:
    page = doc[idx]
    w = page.rect.width
    clip = fitz.Rect(20, y_top, w - 20, y_bot)
    pix  = page.get_pixmap(matrix=mat, clip=clip, colorspace=fitz.csRGB)
    out  = ASSETS / fname
    pix.save(str(out))
    print(f"  {label}: {pix.width}x{pix.height} px -> {fname}")

doc.close()
print("Fertig.")
