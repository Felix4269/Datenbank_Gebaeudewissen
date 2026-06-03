"""Fix all formatting issues in 03_2_solare_waermegewinne.md."""
from pathlib import Path

path = Path(__file__).parent.parent / 'data' / 'Skript_Energie' / '03_2_solare_waermegewinne.md'
lines = path.read_text(encoding='utf-8').splitlines(keepends=True)

TABLE3 = (
    '**Tabelle 3: Richtwerte für U-, g- und τ-Werte von Verglasungen**\n'
    '\n'
    '| Art der Verglasung | U-Wert (W/m²K) | g-Wert (-) | τ-Wert (-) |\n'
    '|---|---|---|---|\n'
    '| Einfachverglasung (Klarglas, EV) | 5,8 | 0,87 | 0,90 |\n'
    '| Doppelverglasung (Klarglas, Doppelfenster DV) | 2,8 | 0,75 bis 0,8 | 0,80 bis 0,90 |\n'
    '| Isolierverglasung (Klarglas, 2 IV) | 3,0 | 0,75 bis 0,8 | 0,80 bis 0,90 |\n'
    '| Dreifachverglasung (Klarglas, 3 IV) | 2,2 | 0,65 bis 0,7 | 0,70 bis 0,80 |\n'
    '| Wärmeschutzglas (beschichtet, 2 WS) | 1,0 bis 1,4 | 0,50 bis 0,65 | 0,76 bis 0,80 |\n'
    '| Sonnenschutzglas (beschichtet, 2-fach) | 1,0 bis 1,4 | 0,25 bis 0,45 | 0,45 bis 0,70 |\n'
    '| Wärmeschutzglas (beschichtet, 3 WS) | 0,4 bis 0,7 | 0,35 bis 0,6 | 0,55 bis 0,74 |\n'
    '| Wärmeschutzglas (Weissglas, 3 WS) | 0,4 bis 0,7 | 0,66 | 0,74 |\n'
    '| Sonnenschutzglas (beschichtet, 3-fach) | 0,5 bis 0,7 | 0,15 bis 0,35 | 0,36 bis 0,60 |\n'
    '| 2 WS mit Lamellenstoren hell, aussen | – | 0,02 bis 0,06 | Je nach Winkel der Lamellen |\n'
    '| 2 WS mit Stoffstoren hell, aussen | – | 0,10 bis 0,15 | Je nach Stoff |\n'
    '| 2 WS mit Lamellen zw. den Scheiben | – | 0,10 bis 0,20 | Je nach Winkel der Lamellen |\n'
    '| 2 WS mit Lamellen spiegelnd innen | – | 0,25 | Je nach Winkel der Lamellen |\n'
    '| 2 WS mit Stoffstoren innen | – | 0,50 | Je nach Stoff |\n'
)

FORMULA2 = (
    '**Formel 2: Berechnung des externen Solarenergiegewinns**\n'
    '\n'
    r'$\dot{Q}_S = A_F \cdot (1 - f_R) \cdot g \cdot H_S$' + '\n'
    '\n'
    '| Symbol | Bedeutung | Einheit |\n'
    '|---|---|---|\n'
    r'| $\dot{Q}_S$ | Solargewinn | W |' + '\n'
    '| $A_F$ | Fläche des Fensters | m² |\n'
    '| $f_R$ | Rahmenanteil (einheitsloser Faktor) | – |\n'
    '| $g$ | g-Wert (Gesamtenergiedurchlassgrad) | – |\n'
    '| $H_S$ | Globalstrahlung rechtwinklig zum Fenster | W/m² |\n'
)

# Lines to remove (0-indexed): duplicate captions and misplaced labels
remove = {
    23,   # "Abbildung 7: Solare Gewinne in einem Raum2"
    52,   # "Abbildung 8: Passiv-Solarenergiehäuser in Trin3"
    64,   # "Abbildung 9: Strahlungsdurchgang..." (before images)
    163,  # "Abbildung 10: Strahlung auf unterschiedliche..." (duplicate)
}

# Table 3: lines 93-113 (0-indexed) → replace with TABLE3
# Formula 2: lines 152-159 (0-indexed) → replace with FORMULA2
# (indices after removal would shift, so process in reverse order)

result = []
i = 0
while i < len(lines):
    # Table 3 block (lines 94–114 in 1-based = indices 93–113)
    if i == 93:
        result.append(TABLE3)
        i = 114  # skip through end of old table
        continue
    # Formula 2 block (lines 153–160 in 1-based = indices 152–159)
    if i == 152:
        result.append(FORMULA2)
        i = 160
        continue
    # Section headings missing ###
    if i == 115:  # "Ausrichtung der Fenster"
        result.append('### Ausrichtung der Fenster\n')
        i += 1
        continue
    if i == 140:  # "Berechnung der externen Gewinne"
        result.append('### Berechnung der externen Gewinne\n')
        i += 1
        continue
    if i == 165:  # "Bauteile für Solarenergiegewinnung"
        result.append('### Bauteile für Solarenergiegewinnung\n')
        i += 1
        continue
    # Bullet list items (lines 143–146 = indices 142–145)
    if 142 <= i <= 145:
        result.append('- ' + lines[i].lstrip())
        i += 1
        continue
    # Remove duplicate captions
    if i in remove:
        i += 1
        continue
    result.append(lines[i])
    i += 1

path.write_text(''.join(result), encoding='utf-8')
print(f'Done. {len(lines)} -> {len(result)} lines (logical blocks, not raw lines).')
