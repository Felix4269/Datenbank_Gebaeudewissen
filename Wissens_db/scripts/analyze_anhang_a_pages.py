"""
analyze_anhang_a_pages.py - Zeigt Y-Koordinaten der Textblöcke auf den Anhang-A-Formularseiten
"""
import fitz, sys, io
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

PDF_PATH = Path(r"C:/Users/schin/Downloads/SN 546384-6 SIA 384-6_2021_d.pdf")
doc = fitz.open(str(PDF_PATH))

# Seiten: A.2=39, A.3.1=40, A.3.2=41, A.4=42, A.5=43, A.6=44 (0-basiert)
pages = {39: "A.2", 40: "A.3.1", 41: "A.3.2", 42: "A.4", 43: "A.5", 44: "A.6"}

for idx, label in pages.items():
    page = doc[idx]
    blocks = page.get_text("blocks")
    blocks_sorted = sorted(blocks, key=lambda b: b[1])  # nach Y sortieren
    print(f"\n=== Seite {idx+1} ({label}) ===  Seitengrösse: {page.rect.width:.0f} x {page.rect.height:.0f} pt")
    for b in blocks_sorted[:4]:   # erste 4 Blöcke
        print(f"  OBEN  y={b[1]:.1f}-{b[3]:.1f}: {b[4].strip()[:60]!r}")
    print("  ...")
    for b in blocks_sorted[-3:]:  # letzte 3 Blöcke
        print(f"  UNTEN y={b[1]:.1f}-{b[3]:.1f}: {b[4].strip()[:60]!r}")

doc.close()
