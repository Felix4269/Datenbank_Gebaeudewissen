"""
Replace trailing footnote numbers with <sup>N</sup> in caption/label lines.
Only touches lines that contain 'Abbildung' or 'Tabelle' and do NOT contain
'![[' (image links) or '$' (LaTeX math).
"""
import re
from pathlib import Path

# Matches a letter immediately followed by one or more digits at a word boundary
PAT = re.compile(r'([A-Za-zäöüÄÖÜ])(\d+)(?=[\s\*\.,\)]|$)')

def fix_line(line):
    return PAT.sub(lambda m: f'{m.group(1)}<sup>{m.group(2)}</sup>', line)

target = Path(__file__).parent.parent / 'data' / 'Skript_Energie'
total = 0

for md in sorted(target.glob('*.md')):
    lines = md.read_text(encoding='utf-8').splitlines(keepends=True)
    changed = False
    for i, line in enumerate(lines):
        # Skip image links and LaTeX lines
        if '![[' in line or '$' in line:
            continue
        # Only process lines mentioning Abbildung or Tabelle
        if 'Abbildung' not in line and 'Tabelle' not in line:
            continue
        new = fix_line(line)
        if new != line:
            lines[i] = new
            print(f'  {md.name}:{i+1}  {new.rstrip()}')
            changed = True
            total += 1
    if changed:
        md.write_text(''.join(lines), encoding='utf-8')

print(f'\nDone. {total} lines updated.')
