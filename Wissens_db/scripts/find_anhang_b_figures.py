"""
find_anhang_b_figures.py - Findet Seiten und Y-Koordinaten der Figuren 4-7 in Anhang B
"""
import fitz, sys, io
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

PDF_PATH = Path(r"C:/Users/schin/Downloads/SN 546384-6 SIA 384-6_2021_d.pdf")
doc = fitz.open(str(PDF_PATH))

# Anhang B: Seiten 46-54 (1-basiert) = Indizes 45-53
print("Anhang B Seiten (Index 45-53):\n")
for i in range(45, 54):
    page = doc[i]
    blocks = sorted(page.get_text("blocks"), key=lambda b: b[1])
    print(f"\n=== Seite {i+1} (Index {i}) ===")
    for b in blocks:
        txt = b[4].strip()[:80]
        if txt:
            print(f"  y={b[1]:.0f}-{b[3]:.0f}: {txt!r}")

doc.close()
