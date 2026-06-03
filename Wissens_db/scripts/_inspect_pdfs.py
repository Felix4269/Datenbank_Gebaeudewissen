# -*- coding: utf-8 -*-
"""Quick inspection of the 3 lecture PDFs: page count + first pages for TOC detection."""
import pdfplumber, sys

PDFS = [
    r"C:\Users\schin\Downloads\Skript Energie im Gebäude 2026.pdf",
    r"C:\Users\schin\Downloads\Skript Lüftung.pdf",
    r"C:\Users\schin\Downloads\Skript Bauphysik 2026.pdf",
]

for path in PDFS:
    print("=" * 70)
    print(f"FILE: {path.split(chr(92))[-1]}")
    with pdfplumber.open(path) as pdf:
        print(f"Pages: {len(pdf.pages)}")
        # Print pages 1-6 to find TOC
        for i, pg in enumerate(pdf.pages[:8]):
            t = pg.extract_text() or ""
            lines = [l.strip() for l in t.splitlines() if l.strip()]
            print(f"\n--- Page {i+1} ---")
            for l in lines[:40]:
                print(l)
