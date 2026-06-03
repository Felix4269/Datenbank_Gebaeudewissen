"""
fix_sia_384_image_positions.py

Korrigiert die Positionen der SIA 384-6 Figuren:
Bilder wurden fälschlicherweise NACH dem Navigations-Footer angehängt.
Dieses Skript verschiebt sie VOR den Footer (ans Ende des Body-Texts)
und platziert sie wo möglich in der richtigen Sektion.

Ausführung: py scripts/fix_sia_384_image_positions.py
"""

import re, sys, io
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

SIA_DIR = Path("C:/Users/schin/OneDrive/Desktop/Wissens_db/data/SIA_384-6_2021")


def split_at_footer(text: str):
    """
    Trennt Text in (body, footer_block, after_footer).
    Footer = letztes '\n---\n\n> ◀...\n\n---\n' im Dokument.
    Gibt None zurück wenn kein Footer gefunden.
    """
    # Finde letztes Vorkommen von \n---\n\n> ◀
    marker = "\n---\n\n> ◀"
    idx = text.rfind(marker)
    if idx == -1:
        return None, None, None

    body = text[:idx]
    rest = text[idx:]

    # Footer-Block: \n---\n\n> ◀...\n\n---\n?
    footer_pat = re.compile(r'\n---\n\n> ◀[^\n]*\n\n---\n?')
    m = footer_pat.match(rest)
    if not m:
        return None, None, None

    return body, m.group(0), rest[m.end():]


def extract_image_blocks(text: str):
    """
    Extrahiert alle ![[...]] Blöcke (mit optionaler Caption-Zeile).
    Gibt eine Liste von (block_text,) zurück.
    """
    # Matcht: ![[filename]]\n*caption...*\n  (Caption optional, kann mehrzeilig sein)
    # Vereinfacht: alles zwischen zwei Leerzeilen oder Dateiende
    # Ansatz: splitten nach doppelten Leerzeilen und Blöcke mit ![[ finden
    blocks = []
    # Splitte nach \n\n
    parts = re.split(r'\n{2,}', text.strip())
    for part in parts:
        part = part.strip()
        if part.startswith('![['):
            blocks.append(part)
    return blocks


def insert_after_line_containing(body: str, search: str, insertion: str) -> (str, bool):
    """
    Sucht die erste Zeile im Body, die 'search' enthält,
    und fügt 'insertion' danach ein. Gibt (neuer_text, True/False) zurück.
    """
    lines = body.split('\n')
    for i, line in enumerate(lines):
        if search in line:
            lines.insert(i + 1, '\n' + insertion)
            return '\n'.join(lines), True
    return body, False


def fix_geltungsbereich(path: Path):
    """00_Geltungsbereich.md: Figur 1 nach Abschnitt 0.1.3 einfügen."""
    text = path.read_text(encoding="utf-8")
    body, footer, after = split_at_footer(text)
    if body is None:
        print(f"  SKIP (kein Footer): {path.name}")
        return

    after_stripped = after.strip() if after else ""
    if not after_stripped:
        print(f"  OK (nichts nach Footer): {path.name}")
        return

    blocks = extract_image_blocks(after_stripped)
    if not blocks:
        print(f"  OK (keine Bildblöcke nach Footer): {path.name}")
        return

    images_section = "\n\n".join(blocks)

    # Figur 1 gehört nach 0.1.3 (nach "Nicht in dieser Norm behandelt werden")
    new_body, placed = insert_after_line_containing(
        body,
        "Nicht in dieser Norm behandelt werden Nutzungsarten",
        images_section
    )
    if not placed:
        # Fallback: ans Ende des Body
        new_body = body.rstrip() + "\n\n" + images_section

    path.write_text(new_body + footer, encoding="utf-8")
    print(f"  ✓ {len(blocks)} Bild(er) verschoben: {path.name}")


def fix_pruefungen(path: Path):
    """06_Pruefungen.md: Figuren 6,7 nach 6.1.2.3 Dichtheitsprüfung einfügen."""
    text = path.read_text(encoding="utf-8")
    body, footer, after = split_at_footer(text)
    if body is None:
        print(f"  SKIP (kein Footer): {path.name}")
        return

    after_stripped = after.strip() if after else ""
    if not after_stripped:
        print(f"  OK (nichts nach Footer): {path.name}")
        return

    blocks = extract_image_blocks(after_stripped)
    if not blocks:
        print(f"  OK (keine Bildblöcke nach Footer): {path.name}")
        return

    # Figur 6 nach 6.1.2.3 (Dichtheitsprüfung)
    # Figur 7 direkt danach
    images_section = "\n\n".join(blocks)

    new_body, placed = insert_after_line_containing(
        body,
        "B.3 ein Langzeit-Dichtheitstest",
        images_section
    )
    if not placed:
        # Fallback: Ende des Body
        new_body = body.rstrip() + "\n\n" + images_section

    path.write_text(new_body + footer, encoding="utf-8")
    print(f"  ✓ {len(blocks)} Bild(er) verschoben: {path.name}")


def fix_systemoptimierung(path: Path):
    """
    03_2_3_4_systemoptimierung_berechnung.md:
    - Figur 23 nach Abschnitt 3.3.2 (Belastungsprofil)
    - Figuren 9-21 nach Abschnitt 3.3.3.4 (einfache Anlagen, D.4/D.5)
    - Figuren 4,5 nach Abschnitt 3.4.4.3 (D.7 Diagramme Druckverlust)
    """
    text = path.read_text(encoding="utf-8")
    body, footer, after = split_at_footer(text)
    if body is None:
        print(f"  SKIP (kein Footer): {path.name}")
        return

    after_stripped = after.strip() if after else ""
    if not after_stripped:
        print(f"  OK (nichts nach Footer): {path.name}")
        return

    blocks = extract_image_blocks(after_stripped)
    if not blocks:
        print(f"  OK (keine Bildblöcke nach Footer): {path.name}")
        return

    # Ordne Blöcke nach Figur-Nummer
    def figur_nr(block):
        m = re.search(r'figur_(\d+)', block.lower())
        return int(m.group(1)) if m else 99

    blocks_sorted = sorted(blocks, key=figur_nr)

    # Kategorisieren
    fig_4_5 = [b for b in blocks_sorted if figur_nr(b) in (4, 5)]
    fig_9_21 = [b for b in blocks_sorted if 9 <= figur_nr(b) <= 21]
    fig_23 = [b for b in blocks_sorted if figur_nr(b) == 23]
    rest_blocks = [b for b in blocks_sorted if b not in fig_4_5 + fig_9_21 + fig_23]

    new_body = body

    # Figur 23 nach "### 3.3.2 Belastungsprofil" Abschnitt
    # (nach letztem Aufzählungspunkt der Belastungsprofile)
    if fig_23:
        new_body, placed = insert_after_line_containing(
            new_body,
            "Monatsmittelwerte mit mindestens 24 Stunden Spitzenlast",
            "\n".join(fig_23)
        )
        if not placed:
            new_body, placed = insert_after_line_containing(
                new_body, "3.3.2 Belastungsprofil", "\n".join(fig_23)
            )

    # Figuren 9-21 nach 3.3.3.4 (D.4 und D.5 beschrieben)
    if fig_9_21:
        new_body, placed = insert_after_line_containing(
            new_body,
            "maximal vier Erdwärmesonden bestimmt werden",
            "\n".join(fig_9_21)
        )
        if not placed:
            new_body, placed = insert_after_line_containing(
                new_body, "3.3.3.4", "\n".join(fig_9_21)
            )

    # Figuren 4,5 nach 3.4.4.3 (D.7 Diagramme)
    if fig_4_5:
        new_body, placed = insert_after_line_containing(
            new_body,
            "D.7 Diagramme für gebräuchliche Dimensionen",
            "\n".join(fig_4_5)
        )
        if not placed:
            new_body, placed = insert_after_line_containing(
                new_body, "3.4.4.3", "\n".join(fig_4_5)
            )

    # Restliche Blöcke ans Ende des Body
    if rest_blocks:
        new_body = new_body.rstrip() + "\n\n" + "\n\n".join(rest_blocks)

    path.write_text(new_body + footer, encoding="utf-8")
    print(f"  ✓ {len(blocks)} Bild(er) verschoben: {path.name}")


def fix_anhang_c(path: Path):
    """Anhang_C_Kennwerte.md: Figuren 24-29 nach Tabelle 14 (C.4 Wärmeträger) einfügen."""
    text = path.read_text(encoding="utf-8")
    body, footer, after = split_at_footer(text)
    if body is None:
        print(f"  SKIP (kein Footer): {path.name}")
        return

    after_stripped = after.strip() if after else ""
    if not after_stripped:
        print(f"  OK (nichts nach Footer): {path.name}")
        return

    blocks = extract_image_blocks(after_stripped)
    if not blocks:
        print(f"  OK (keine Bildblöcke nach Footer): {path.name}")
        return

    images_section = "\n\n".join(blocks)

    # Nach Tabelle 14 (Eigenschaften der Wärmeträger) einfügen
    new_body, placed = insert_after_line_containing(
        body,
        "Ethanol 30 %",   # letzte Zeile von Tabelle 14
        images_section
    )
    if not placed:
        new_body, placed = insert_after_line_containing(
            body, "C.4.4 Auslegung von Expansionsgefässen", images_section
        )
    if not placed:
        new_body = body.rstrip() + "\n\n" + images_section

    path.write_text(new_body + footer, encoding="utf-8")
    print(f"  ✓ {len(blocks)} Bild(er) verschoben: {path.name}")


def fix_nachbarsonden(path: Path):
    """03_5_nachbarsonden.md: Figur 22 nach 3.5.2.6 einfügen."""
    text = path.read_text(encoding="utf-8")
    body, footer, after = split_at_footer(text)
    if body is None:
        print(f"  SKIP (kein Footer): {path.name}")
        return

    after_stripped = after.strip() if after else ""
    if not after_stripped:
        print(f"  OK (nichts nach Footer): {path.name}")
        return

    blocks = extract_image_blocks(after_stripped)
    if not blocks:
        print(f"  OK (keine Bildblöcke nach Footer): {path.name}")
        return

    # Figur 22 bereinigen (truncated/malformed caption)
    clean_blocks = []
    for b in blocks:
        # Normalisiere mehrzeilige Captions
        lines = b.split('\n')
        img_line = lines[0]
        # Kombiniere alle Caption-Zeilen zu einer
        cap_lines = [l.strip() for l in lines[1:] if l.strip() and l.strip() not in ('', '*')]
        # Letzte vollständige Caption verwenden
        caption = cap_lines[-1] if cap_lines else ""
        # Stelle sicher dass Caption korrekt formatiert
        if caption and not caption.startswith('*'):
            caption = '*' + caption
        if caption and not caption.endswith('*'):
            caption = caption + '*'
        if caption:
            clean_blocks.append(img_line + '\n' + caption)
        else:
            clean_blocks.append(img_line)

    images_section = "\n\n".join(clean_blocks)

    # Nach 3.5.2.6 Text einfügen
    new_body, placed = insert_after_line_containing(
        body,
        "Ein Beispiel zur Berechnung ist unter D.4.8.4 enthalten",
        images_section
    )
    if not placed:
        new_body, placed = insert_after_line_containing(
            body, "gemäss Figur 3 gerechnet werden", images_section
        )
    if not placed:
        new_body = body.rstrip() + "\n\n" + images_section

    path.write_text(new_body + footer, encoding="utf-8")
    print(f"  ✓ {len(blocks)} Bild(er) verschoben: {path.name}")


def main():
    print(f"\n{'═'*60}")
    print(f"  SIA 384-6 – Bildpositionen korrigieren")
    print(f"{'═'*60}\n")

    fixes = [
        ("00_Geltungsbereich.md",                    fix_geltungsbereich),
        ("06_Pruefungen.md",                         fix_pruefungen),
        ("03_2_3_4_systemoptimierung_berechnung.md", fix_systemoptimierung),
        ("Anhang_C_Kennwerte.md",                    fix_anhang_c),
        ("03_5_nachbarsonden.md",                    fix_nachbarsonden),
    ]

    for fname, func in fixes:
        p = SIA_DIR / fname
        if p.exists():
            func(p)
        else:
            print(f"  FEHLT: {fname}")

    print(f"\n  Fertig.")


if __name__ == "__main__":
    main()
