"""Fix Tabelle 6 in 06_1_berechnung_energiebedarf.md."""
from pathlib import Path

path = Path(__file__).parent.parent / 'data' / 'Skript_Energie' / '06_1_berechnung_energiebedarf.md'
lines = path.read_text(encoding='utf-8').splitlines(keepends=True)

TABLE6 = (
    '**Tabelle 6: Wirkungsgrade Wärmeerzeugung**\n'
    '\n'
    '| Art der Wärmeerzeugung | Jahreswirkungsgrad resp. Jahresarbeitszahl (typische Bereiche) | Defaultwerte SIA Merkblatt 2031 |\n'
    '|---|---|---|\n'
    '| Öl-/Gaskessel herkömmlich | 65 bis 85 % (auf den Brennwert bezogen) | 80 % |\n'
    '| Öl-/Gaskessel Brennwert | 85 bis 95 % (auf den Brennwert bezogen) | 85 % |\n'
    '| Stückholzkessel, Holzofen, Cheminée mit Heizeinsatz | 60 bis 75 % (auf den Brennwert bezogen) | 65 % |\n'
    '| Holzschnitzel- oder Pellets-Kessel | 65 bis 80 % (auf den Brennwert bezogen) | 70 % |\n'
    '| Wärmepumpe Luft/Wasser | 2,5 bis 4,5 (Jahresarbeitszahl) | 2,8 |\n'
    '| Wärmepumpe Sole oder Wasser/Wasser | 3,5 bis 5,5 (Jahresarbeitszahl) | 3,4 |\n'
    '| Blockheizkraftwerk | 85 bis 90 % (Gesamtwirkungsgrad, ca. 30–40 % Strom, Rest Wärme) | – |\n'
    '| Fernwärme | 93 bis 98 % (Wirkungsgrad beim Verbraucher, zus. Wärmeerzeugungs- und Verteilverluste) | 93 % |\n'
    '| Elektro Direktheizung (El. Widerstandsheizung) | 90 bis 100 % | 93 % |\n'
)

# Lines 37–56 (1-based) = indices 36–55 (0-based)
new_lines = lines[:36] + [TABLE6] + lines[56:]
path.write_text(''.join(new_lines), encoding='utf-8')
print(f'Done. {len(lines)} -> {len(new_lines)} lines.')
