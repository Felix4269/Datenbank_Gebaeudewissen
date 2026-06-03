"""Fix all formatting issues in 06_3_deckung_energiebedarf.md."""
from pathlib import Path
import re

path = Path(__file__).parent.parent / 'data' / 'Skript_Energie' / '06_3_deckung_energiebedarf.md'
lines = path.read_text(encoding='utf-8').splitlines(keepends=True)

result = []
i = 0
while i < len(lines):
    line = lines[i]

    # ── Duplicate plain-text captions ────────────────────────────────
    if line.strip() == 'Abbildung 19: Monovalente Wärmeerzeugung für ein Minergie-EFH':
        i += 1; continue
    if line.strip() == 'Abbildung 20: Bivalent-parallele Wärmeerzeugung EFH (herkömmliche Lösung)':
        i += 1; continue

    # ── Sub-section headings missing #### ────────────────────────────
    headings = {
        'Monovalente Wärmeproduktion',
        'Bivalent-parallele Wärmeproduktion',
        'Bivalent-alternative Wärmeproduktion',
        'Bivalent alternative Spitzenproduktion',
        'Bivalent-parallele Spitzenproduktion',
        'Erkenntnisse für die Auslegung:',
    }
    if line.strip() in headings:
        result.append(f'#### {line.strip()}\n')
        i += 1; continue

    # ── Abbildung 21 chart block (lines 57–71 in original, 0-based 56–70) ──
    # Detect start: line containing only a single digit (y-axis labels)
    # or the legend text "Heizung Holz (5000 kWh)"
    if line.strip() == '7' and i > 50:
        # Skip until we hit the Abbildung 21 caption
        while i < len(lines) and 'Abbildung 21' not in lines[i]:
            i += 1
        caption = lines[i].strip()
        result.append('\n')
        result.append('![[abb21_bivalent_alternativ_winter_sommer.jpg]]\n')
        result.append(f'*{caption}*\n')
        i += 1; continue

    # ── Abbildung 22 chart block ──────────────────────────────────────
    if 'Heizung Holz Spitze (1500 kWh)' in line:
        while i < len(lines) and 'Abbildung 22' not in lines[i]:
            i += 1
        caption = lines[i].strip()
        result.append('\n')
        result.append('![[abb22_bivalent_alternativ_spitze.jpg]]\n')
        result.append(f'*{caption}*\n')
        i += 1; continue

    # ── Abbildung 23 chart block ──────────────────────────────────────
    if '## 5 Spitzendeckung Holz' in line or 'Spitzendeckung Holz (330 kWh)' in line:
        while i < len(lines) and 'Abbildung 23' not in lines[i]:
            i += 1
        caption = lines[i].strip()
        result.append('\n')
        result.append('![[abb23_bivalent_parallel_spitze.jpg]]\n')
        result.append(f'*{caption}*\n')
        i += 1; continue

    # ── Strip stray ## prefixes from chart legend lines ──────────────
    if re.match(r'^## \d', line):
        result.append(line[3:])  # remove '## '
        i += 1; continue

    result.append(line)
    i += 1

path.write_text(''.join(result), encoding='utf-8')
print(f'Done. {len(lines)} -> {len(result)} lines.')
