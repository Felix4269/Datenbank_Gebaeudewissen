"""Fix garbled formulas in 05_Warmwasser.md section 5.2."""
from pathlib import Path

path = Path(__file__).parent.parent / 'data' / 'Skript_Energie' / '05_Warmwasser.md'
lines = path.read_text(encoding='utf-8').splitlines(keepends=True)

FORMEL4 = (
    '**Formel 4: Energiebedarf für Warmwasser**\n'
    '\n'
    r'$Q = m \cdot c_p \cdot \Delta T$' + '\n'
    '\n'
    '| Symbol | Bedeutung | Einheit |\n'
    '|---|---|---|\n'
    '| $Q$ | Wärme(energie) | kJ |\n'
    '| $m$ | Masse des zu erwärmenden Wassers (1 l = 1 kg) | kg |\n'
    '| $c_p$ | spez. Wärme Wasser (≈ 4,2 kJ/(kg·K)) | kJ/(kg·K) |\n'
    r'| $\Delta T$ | Temperaturdifferenz Kalt- zu Warmwasser | K |' + '\n'
)

FORMEL5 = (
    '**Formel 5: Umrechnung in Leistungsbedarf des Wassererwärmers**\n'
    '\n'
    r'$P = \frac{Q}{t}$' + '\n'
    '\n'
    '| Symbol | Bedeutung | Einheit |\n'
    '|---|---|---|\n'
    '| $P$ | Wärmeleistung | kW |\n'
    '| $Q$ | Wärme(energie) | kJ oder kWh |\n'
    '| $t$ | Zeit(dauer) der Erwärmung (s, oder h wenn Q in kWh) | s oder h |\n'
)

BEISPIEL = (
    '**Beispiel:**\n'
    '\n'
    'Für ein 4-Familienhaus (je 3 Personen) werden pro Tag 500 l Warmwasser à 60 °C benötigt. Das\n'
    'Wasser soll täglich innerhalb der Nachtabsenkung der Gas-Heizung (6 Stunden) aufgeheizt\n'
    'werden. Es ist ein genügend grosser Speicher vorhanden. Wie gross wird der tägliche\n'
    'Wärmebedarf, wie gross ist die erforderliche Leistung des Wassererwärmers?\n'
    '\n'
    'Wärme-Energie pro Tag:\n'
    '\n'
    r'$Q = m \cdot c_p \cdot \Delta T = 500\,\text{kg} \times 4{,}2\,\text{kJ/(kg·K)} \times (60-10)\,\text{K} = 105\,000\,\text{kJ} = 29{,}17\,\text{kWh}$' + '\n'
    '\n'
    r'$P = Q/t = 29{,}17\,\text{kWh} \,/\, 6\,\text{h} = 4{,}86\,\text{kW}$' + '\n'
)

result = []
i = 0
while i < len(lines):
    # Formel 4 block: lines 32–37 (0-based 31–36)
    if i == 31:
        result.append(FORMEL4)
        i = 37
        continue
    # Formel 5 block: lines 51–55 (0-based 50–54)
    if i == 50:
        result.append(FORMEL5)
        i = 55
        continue
    # Beispiel block: lines 56–63 (0-based 55–62)
    if i == 55:
        result.append(BEISPIEL)
        i = 63
        continue
    result.append(lines[i])
    i += 1

path.write_text(''.join(result), encoding='utf-8')
print(f'Done. {len(lines)} -> {len(result)} lines.')
