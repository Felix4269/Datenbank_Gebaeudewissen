"""
extract_anhang_b_text.py

Extrahiert den Originaltext von Anhang B (Seiten 46-54) aus der SIA 384-6 PDF.
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

# Anhang B: Seiten 46-54 (Indizes 45-53)
for page_idx in range(45, 54):
    page = doc[page_idx]
    print(f"\n{'='*70}")
    print(f"=== SEITE {page_idx+1} (Index {page_idx}) ===")
    print(f"{'='*70}\n")

    blocks = sorted(page.get_text("blocks"), key=lambda b: b[1])
    for b in blocks:
        txt = b[4].strip()
        if not txt:
            continue
        # Wasserzeichen/Lizenztext überspringen
        if any(frag in txt for frag in SKIP_FRAGMENTS):
            continue
        # Seitenzahl-Zeile überspringen (nur Zahl + Copyright)
        if len(txt) < 5 and txt.isdigit():
            continue
        # Y-Position anzeigen für Orientierung
        print(f"[y={b[1]:.0f}] {txt}")
        print()

doc.close()
