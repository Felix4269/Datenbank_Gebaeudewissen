# _fix_merged_words_tutorial.py
# Behebt zusammengewachsene Wörter in den Tutorial .md Dateien.
# Ursache: pdfplumber hat bei manchen Absätzen die Leerzeichen zwischen
# Wörtern nicht erkannt (z.B. "gezeichnetsind" statt "gezeichnet sind").
# Heuristik: Leerzeichen vor jedem Grossbuchstaben einfügen, der direkt
# auf einen Kleinbuchstaben folgt. Danach bekannte Falsch-Trennungen
# reparieren (z.B. SI-Einheit "kW" → darf nicht gespalten werden).
import re
import sys
from pathlib import Path

# Windows-Konsole: UTF-8 erzwingen damit Sonderzeichen nicht crashen
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

MD_DIR = Path(r"C:\Users\schin\OneDrive\Desktop\Wissens_db\data\IDA_ICE_Tutorial")

# Zusammengesetzte Begriffe, die NICHT getrennt werden dürfen.
# Werden vor dem Trennen durch Platzhalter ersetzt, danach wiederhergestellt.
PROTECTED_TERMS = [
    "LuWa",       # Luft-Wasser (Wärmepumpe)
    "SoWa",       # Sole-Wasser (Wärmepumpe)
    "WoZi",       # Wohnzimmer (Zonenabkürzung)
    "MitDaemm",   # Bauteilname: mit Dämmung
    "OhneDaemm",  # Bauteilname: ohne Dämmung
    "EnFK",       # Energie-Fachstellen Konferenz (Abkürzung)
    "kWh",        # Kilowattstunde (Einheit, Reihenfolge wichtig: vor kW)
    "kW",         # Kilowatt (Einheit)
    "kJ",         # Kilojoule (Einheit)
    "kgK",        # kg·K (Einheit spez. Wärmekapazität)
    "kgL",        # kg/L (Einheit Dichte)
    "idealHeat",  # IDA ICE Variantenname
    "EmeterFans", # IDA ICE UI-Element
]

# Zeilen-Präfixe, die komplett übersprungen werden
SKIP_PREFIXES = ("![[", "*", "#", ">", "---", "tags:", "normnummer:",
                 "titel:", "kapitel:", "gueltig_ab:", "gueltig_bis:")


def fix_line(line: str) -> str:
    stripped = line.strip()
    if not stripped:
        return line
    for prefix in SKIP_PREFIXES:
        if stripped.startswith(prefix):
            return line

    # Schütze bekannte CamelCase-Abkürzungen
    placeholders: dict[str, str] = {}
    working = line
    for i, term in enumerate(PROTECTED_TERMS):
        if term in working:
            ph = f"\x00PROT{i}\x00"
            placeholders[ph] = term
            working = working.replace(term, ph)

    # Kernregel: Leerzeichen vor Grossbuchstaben, der auf Kleinbuchstaben folgt
    working = re.sub(r"([a-zäöüß])([A-ZÄÖÜ])", r"\1 \2", working)

    # Falsch-Trennung SI-Einheit kW reparieren (z.B. "25k W" → "25kW")
    working = re.sub(r"([0-9])k W\b", r"\1kW", working)

    # Platzhalter zurücksetzen
    for ph, term in placeholders.items():
        working = working.replace(ph, term)

    return working


def fix_file(md_path: Path) -> int:
    text = md_path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)

    # YAML-Frontmatter (zwischen den ersten beiden "---"-Zeilen) überspringen
    frontmatter_end = 0
    if lines and lines[0].strip() == "---":
        for i, ln in enumerate(lines[1:], 1):
            if ln.strip() == "---":
                frontmatter_end = i
                break

    new_lines = []
    changed = 0
    for i, line in enumerate(lines):
        if i <= frontmatter_end:
            new_lines.append(line)
        else:
            new_line = fix_line(line)
            if new_line != line:
                changed += 1
                # Debug-Ausgabe für manuelle Überprüfung
                print(f"  [{md_path.name}:{i+1}]")
                print(f"    ALT: {line.rstrip()}")
                print(f"    NEU: {new_line.rstrip()}")
            new_lines.append(new_line)

    if changed:
        md_path.write_text("".join(new_lines), encoding="utf-8")
    return changed


def main() -> None:
    total = 0
    for f in sorted(MD_DIR.glob("*.md")):
        n = fix_file(f)
        if n:
            print(f"\n  → {f.name}: {n} Zeile(n) korrigiert")
            total += n
    print(f"\nGesamt: {total} Zeile(n) korrigiert.")


if __name__ == "__main__":
    main()
