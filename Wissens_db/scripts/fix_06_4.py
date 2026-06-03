"""Fix all formatting issues in 06_4_vorschriften.md."""
from pathlib import Path
import re

path = Path(__file__).parent.parent / 'data' / 'Skript_Energie' / '06_4_vorschriften.md'
lines = path.read_text(encoding='utf-8').splitlines(keepends=True)

MODULE_LIST = (
    '**Module MuKEn 2025<sup>6</sup>**\n'
    '\n'
    '- 1 Basismodul (inkl. Gebäudeenergieausweis)\n'
    '\n'
    'Zusatzmodule:\n'
    '- 2 VHKA in bestehenden Bauten\n'
    '- 3 Heizungen im Freien und Freiluftbäder\n'
    '- 4 Ferienhäuser und Ferienwohnungen\n'
    '- 5 Sanierungspflicht dezentrale Elektroheizungen\n'
    '- 6 Ausführungsbestätigung\n'
    '- 7 Betriebsoptimierung\n'
    '- 8 GEAK-Anordnung für bestimmte Bauten\n'
    '- 9 Energieplanung\n'
    '- 10 Energiedaten\n'
    '- 11 Wärmedämmung / Ausnützung\n'
    '- 12 Elektromobilität\n'
    '- 13 Gebäudehülleneffizienz\n'
    '- 14 Intelligente Steuerungen und Regelungen\n'
)

result = []
i = 0
while i < len(lines):
    line = lines[i]

    # ── Module MuKEn block (lines 39–54, 0-based 38–53) ──────────────
    if i == 38:
        result.append(MODULE_LIST)
        i = 54
        continue

    # ── Bullet list items starting with a leading space ───────────────
    if re.match(r'^ [^\s]', line):
        result.append('- ' + line.lstrip())
        i += 1
        continue

    # ── Fix caption footnote "Neubauten 7" → "Neubauten<sup>7</sup>" ──
    if 'Neubauten 7' in line:
        result.append(line.replace('Neubauten 7', 'Neubauten<sup>7</sup>'))
        i += 1
        continue

    # ── Remove duplicate plain-text caption (line 126, 0-based 125) ──
    if 'Abbildung 24: Entwicklung' in line and not line.strip().startswith('!') and not line.strip().startswith('*'):
        i += 1
        continue

    # ── Fix footnote line "7 Bulletin.ch" → "<sup>7</sup> Bulletin.ch" ─
    if re.match(r'^7 Bulletin', line):
        result.append('<sup>7</sup> ' + line[2:])
        i += 1
        continue

    result.append(line)
    i += 1

path.write_text(''.join(result), encoding='utf-8')
print(f'Done. {len(lines)} -> {len(result)} lines.')
