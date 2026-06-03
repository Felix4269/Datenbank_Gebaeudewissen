"""
find_anhang_a_pages.py - Findet alle Seiten von Anhang A im SIA 384-6 PDF
"""
import fitz, sys, io
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

PDF_PATH = Path(r"C:/Users/schin/Downloads/SN 546384-6 SIA 384-6_2021_d.pdf")
doc = fitz.open(str(PDF_PATH))

keywords = ["Bohrprotokoll", "Pruefprotokoll", "Prüfprotokoll",
            "Anschluss", "EDV", "Datenaustausch", "Abnahmeprotokoll",
            "Checkliste", "A.1", "A.2", "A.3", "A.4", "A.5", "A.6",
            "Schichtenverzeichnis", "Hinterfuellung", "Hinterfüllung"]

print("Seiten mit Anhang-A-Inhalt:\n")
for i in range(len(doc)):
    page = doc[i]
    text = page.get_text()
    hits = [kw for kw in keywords if kw in text]
    if hits and i >= 35:   # Anhang A beginnt frühestens ab Seite 36
        first_line = text.strip().splitlines()[0][:60] if text.strip() else "(leer)"
        print(f"Seite {i+1:3d} (Index {i:2d}): {hits[:4]}  →  {first_line!r}")

doc.close()
