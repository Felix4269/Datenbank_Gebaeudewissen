"""
fix_subscripts.py

Merges orphan subscript lines (PDF extraction artefact) with the variable
symbols on the preceding line, using Obsidian ~subscript~ syntax.

Background: pdfplumber often places the subscript index of a variable on its
own line directly below the symbol line.  Examples from the source files:

    Q Wärmebedarf der Warmwasserversorgung kWh   +  W,gen,out
    → Q~W,gen,out~ Wärmebedarf der Warmwasserversorgung kWh

    E , E' Hilfsenergie kWh                      +  W,aux W,aux
    → E~W,aux~, E'~W,aux~ Hilfsenergie kWh

    A , A Geschossfläche m²                      +  GF NGF
    → A~GF~, A~NGF~ Geschossfläche m²

    f , f Faktoren …                             +  1 2
    → f~1~, f~2~ Faktoren …

Run:  py scripts/fix_subscripts.py
"""

import re
from pathlib import Path

# ── Orphan-subscript detection ─────────────────────────────────────────────────

# A subscript orphan line: only letters, digits, commas, apostrophes,
# optionally with spaces separating groups.  Max 35 chars.
_ORPHAN_RE = re.compile(r"^[A-Za-zÄÖÜäöüß0-9,']+(?: +[A-Za-zÄÖÜäöüß0-9,']+)*$")

_SKIP_WORDS = {
    "Symbol", "Begriff", "Einheit", "Index", "deutsch", "englisch",
    "kWh", "kW", "lx", "Hz", "Pa", "dB", "und", "oder", "die", "der",
    "das", "None", "français",
}


def _is_orphan(line: str, prev_stripped: str) -> bool:
    s = line.strip()
    if not s or len(s) > 35:
        return False
    if not _ORPHAN_RE.match(s):
        return False
    if s in _SKIP_WORDS:
        return False
    groups = s.split()
    if any(len(g) > 14 for g in groups):
        return False
    if any(g in _SKIP_WORDS for g in groups):
        return False
    # Reject if any group looks like a German noun (Title-case + 3+ lowercase chars)
    # e.g. "Balkontiefe", "Nutzungstage" → not a subscript
    if any(re.match(r'^[A-ZÄÖÜ][a-zäöü]{3,}', g) for g in groups):
        return False
    # Previous line must not be empty and must start with a variable character
    if not prev_stripped:
        return False
    if prev_stripped.startswith("#") or prev_stripped.startswith(">"):
        return False
    # Previous line starts with a single-letter variable (upper/lower/Greek)
    if not re.match(r"^[A-ZΦΨΩΔΣΛΘΞa-zαβγδεζηθλμνξπρστυφχψω]", prev_stripped):
        return False
    return True


# ── Variable extraction & subscript insertion ──────────────────────────────────

# A variable token: a single letter (possibly Greek) with optional trailing
# apostrophe/prime (ASCII ' U+0027, typographic ' U+2019, prime ′ U+2032)
_PRIME = "'’′"
_VAR_TOKEN_RE = re.compile(r"^[A-ZΦΨΩΔΣΛΘΞa-zαβγδεζηθλμνξπρστυφχψω]['’′]?$")

# Units that do NOT end the variable-prefix scan (they just get skipped)
_UNIT_WORDS = {
    "kWh", "kW", "lx", "Hz", "Pa", "dB", "W", "K", "l", "h", "d", "s",
    "Normliter", "J", "N", "–", "%", "°C",
}
_UNIT_RE = re.compile(
    r"^(?:m[²³]?|cm[²³]?|mm[²³]?|dm³?|km[²³]?|m³|[Ww]/m[²³]?)$"
)


def _apply_subscripts(line: str, sub_groups: list) -> str:
    """
    Insert ~subscript~ after each variable symbol in `line`.

    Variables are single-letter tokens (possibly with ') that appear BEFORE
    the first `|` or the first description word (3+ chars, not a unit).

    sub_groups: list of subscript strings, one per variable found, or one for all.
    """
    # Tokenize: list of (token_str, start_idx, end_idx)
    tokens = [(m.group(), m.start(), m.end()) for m in re.finditer(r"\S+", line)]
    if not tokens:
        return line

    # Collect variable positions (indices into tokens[])
    var_positions = []
    for i, (tok, start, end) in enumerate(tokens):
        # Stop at pipe — everything after is unit/description
        if "|" in tok:
            break
        core = tok.rstrip(",;")
        if _VAR_TOKEN_RE.match(core):
            var_positions.append(i)
        elif core in {"", ",", ";"}:
            continue
        elif core in _UNIT_WORDS or _UNIT_RE.match(core):
            continue
        else:
            # First real description word → stop
            if len(core) >= 3:
                break

    if not var_positions:
        return line

    # Build subscript list to apply
    if len(sub_groups) == 1:
        subs = [sub_groups[0]] * len(var_positions)
    elif len(sub_groups) == len(var_positions):
        subs = sub_groups
    else:
        # Mismatch: use first subscript for all (safe fallback)
        subs = [sub_groups[0]] * len(var_positions)

    # Insert subscripts from right to left so indices stay valid
    new_line = line
    for idx, sub in reversed(list(zip(var_positions, subs))):
        tok, start, end = tokens[idx]
        core = tok.rstrip(",;")
        insert_at = start + len(core)
        new_line = new_line[:insert_at] + f"~{sub}~" + new_line[insert_at:]

    return new_line


# ── File processing ────────────────────────────────────────────────────────────

def process_text(text: str) -> tuple:
    """Returns (new_text, fixes_count)."""
    raw_lines = text.splitlines(keepends=True)
    result = []
    fixes = 0
    in_frontmatter = False
    in_code_block = False

    i = 0
    while i < len(raw_lines):
        raw = raw_lines[i]
        line = raw.rstrip("\r\n")
        stripped = line.strip()

        # Frontmatter
        if i == 0 and stripped == "---":
            in_frontmatter = True
            result.append(raw)
            i += 1
            continue
        if in_frontmatter:
            result.append(raw)
            if stripped == "---":
                in_frontmatter = False
            i += 1
            continue

        # Code blocks
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            result.append(raw)
            i += 1
            continue
        if in_code_block:
            result.append(raw)
            i += 1
            continue

        # Check if the IMMEDIATELY next line is a subscript orphan
        # (no blank-line skipping — orphans are always directly below)
        if i + 1 < len(raw_lines):
            next_raw = raw_lines[i + 1]
            next_stripped = next_raw.strip()
            if next_stripped and _is_orphan(next_raw, stripped):
                sub_groups = next_stripped.split()
                # If all groups are identical, collapse to one
                if len(set(sub_groups)) == 1:
                    unique_groups = [sub_groups[0]]
                else:
                    unique_groups = sub_groups

                new_line = _apply_subscripts(line, unique_groups)
                ending = raw[len(raw.rstrip("\r\n")):]
                result.append(new_line + ending)
                # Skip the orphan line (i+1); advance past it
                i += 2
                fixes += 1
                continue

        result.append(raw)
        i += 1

    return "".join(result), fixes


def should_skip(path: Path) -> bool:
    name = path.name
    return "_MOC" in name or name in ("CLAUDE.md", "00_Wissensbank_Index.md")


def main():
    root = Path(__file__).parent.parent / "data"
    md_files = sorted(root.rglob("*.md"))

    total_fixes = total_files = 0

    for f in md_files:
        if should_skip(f):
            print(f"  SKIP  {f.relative_to(root.parent)}")
            continue
        text = f.read_text(encoding="utf-8")
        new_text, fixes = process_text(text)
        rel = f.relative_to(root.parent)
        if fixes:
            f.write_text(new_text, encoding="utf-8")
            print(f"  ~{fixes:3d}  {rel}")
            total_fixes += fixes
            total_files += 1
        else:
            print(f"  --   {rel}")

    print(f"\nDone. {total_fixes} subscript merges across {total_files} files.")


if __name__ == "__main__":
    main()
