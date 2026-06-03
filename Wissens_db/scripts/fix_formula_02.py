"""Fix garbled formula table rows in 02_Waermeverluste.md."""
from pathlib import Path

path = Path(__file__).parent.parent / 'data' / 'Skript_Energie' / '02_Waermeverluste.md'
lines = path.read_text(encoding='utf-8').splitlines(keepends=True)

# Fix line 105 (index 104): mangled $c_p$ row
# and remove duplicate Delta T row at index 107

new_105 = '| $c_p$ | spezifische Wärme der Luft (≈ 1 kJ/(kg·K)) | kJ/(kg·K) |\n'

result = []
for i, line in enumerate(lines):
    if i == 104:  # line 105 – replace mangled c_p row
        result.append(new_105)
    elif i == 107:  # line 108 – duplicate Delta T row
        pass  # skip
    else:
        result.append(line)

path.write_text(''.join(result), encoding='utf-8')
print(f'Done. {len(lines)} -> {len(result)} lines.')
