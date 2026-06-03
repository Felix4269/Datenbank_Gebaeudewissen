"""
extract_anhang_c_text.py

Extrahiert den Originaltext von Anhang C aus der SIA 384-6 PDF.
Gibt den Text seitenweise aus, bereinigt von Wasserzeichen und Seitenfuss.
"""
import fitz, sys, io
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

PDF_PATH = Path(r"C:/Users/schin/Downloads/SN 546384-6 SIA 384-6_2021_d.pdf")
doc = fitz.open(str(PDF_PATH))

SKIP_FRAGMENTS = [
    "SNV / licensed",
    "SIA 384/6, Copyright",
    "Hochschulbibliothek",
    "71462284",
    "ZHAW",
]

print(f"PDF hat {len(doc)} Seiten total\n")

# Anhang C: Suche ab Seite 55 (Index 54)
for page_idx in range(54, 80):
    if page_idx >= len(doc):
        break
    page = doc[page_idx]
    blocks = sorted(page.get_text("blocks"), key=lambda b: b[1])

    # Prüfen ob Anhang C auf dieser Seite beginnt oder ob Anhang D beginnt
    page_text = page.get_text()
    if "Anhang D" in page_text and "Anhang C" not in page_text:
        print(f"\n=== Anhang D beginnt auf Seite {page_idx+1} (Index {page_idx}) ===")
        break

    print(f"\n{'='*70}")
    print(f"=== SEITE {page_idx+1} (Index {page_idx}) ===")
    print(f"{'='*70}\n")

    for b in blocks:
        txt = b[4].strip()
        if not txt:
            continue
        if any(frag in txt for frag in SKIP_FRAGMENTS):
            continue
        if len(txt) < 5 and txt.isdigit():
            continue
        print(f"[y={b[1]:.0f}] {txt}")
        print()

doc.close()
