# _fix_quotes_tutorial.py
# Entfernt verwaiste typografische Anfuehrungszeichen (Gaensefuesschen)
# aus den Tutorial .md Dateien.
from pathlib import Path

MD_DIR = Path(r"C:\Users\schin\OneDrive\Desktop\Wissens_db\data\IDA_ICE_Tutorial")

# Typografische Anfuehrungszeichen als Unicode-Escape-Sequenzen
BAD_CHARS = frozenset([
    '"',         # U+0022  ASCII double quote
    '“',    # U+201C  left double quotation mark
    '”',    # U+201D  right double quotation mark
    '„',    # U+201E  double low-9 quotation mark
    '‟',    # U+201F  double high-reversed-9
    '‘',    # U+2018  left single quotation mark
    '’',    # U+2019  right single quotation mark
    '‚',    # U+201A  single low-9 quotation mark
    ' ',         # Leerzeichen (erlaubt, z.B. bei Kombination)
])


def is_only_quotes(line):
    s = line.strip()
    if not s:
        return False
    return all(c in BAD_CHARS for c in s)


def fix_file(md_path):
    text = md_path.read_text(encoding='utf-8')
    lines = text.splitlines(keepends=True)
    new_lines = []
    removed = 0
    for line in lines:
        if is_only_quotes(line):
            removed += 1
        else:
            new_lines.append(line)
    if removed:
        md_path.write_text(''.join(new_lines), encoding='utf-8')
    return removed


def main():
    total = 0
    for f in sorted(MD_DIR.glob('*.md')):
        n = fix_file(f)
        if n:
            print(f'  {f.name}: {n} Zeilen entfernt')
            total += n
    print(f'\nGesamt: {total} Zeilen entfernt.')


if __name__ == '__main__':
    main()
