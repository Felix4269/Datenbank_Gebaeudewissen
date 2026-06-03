"""
format_headings.py

Converts numbered chapter/section titles (e.g. "2.1 Allgemeines") that appear
as plain text in Markdown files into proper Markdown headings (##, ###, ####, #####).

Also reverts already-formatted headings that are actually clauses (false positives
from a previous run).

Rules for a HEADING:
  - Does not end with a period or colon
  - Does not contain '. ' (embedded sentence break)
  - Does not end with common German continuation conjunctions (und, oder, sowie …)
  - Total line length <= 100 characters
  - Text portion does not start with a known German clause-starter word
  - The next non-empty line does not begin with a lowercase letter

Heading level from number depth:
  X        → ##
  X.Y      → ###
  X.Y.Z    → ####
  X.Y.Z.W  → #####

MOC / index files are skipped.
"""

import re
from pathlib import Path

CLAUSE_STARTERS = (
    "Die ", "Der ", "Das ", "Den ", "Dem ", "Des ",
    "Eine ", "Ein ", "Einem ", "Einen ", "Einer ",
    "Bei ", "Für ", "Mit ", "In ", "An ", "Auf ",
    "Zu ", "Nach ", "Über ", "Unter ", "Neben ",
    "Durch ", "Zwischen ", "Von ", "Vom ",
    "Wenn ", "Falls ", "Sofern ", "Soweit ",
    "Gibt ", "Wird ", "Werden ", "Wurden ", "Wurde ",
    "Ist ", "Sind ", "War ", "Waren ",
    "Hat ", "Haben ", "Hatte ", "Hatten ",
    "Alle ", "Als ", "Es ", "Je ", "Jede ", "Jeder ",
    "Zeigt ", "Um ", "Aus ", "Vor ", "Hierfür ",
    "Hierbei ", "Dabei ", "Hierzu ",
    "Zusätzlich ", "Neben ", "Bereits ",
    "Gemäss ", "Gemäß ",
    "Grundlage ", "Voraussetzung ", "Vorschrift ",
    "This ", "The ", "A ", "In order ",  # English
)

# Line endings that indicate the sentence continues on the next line
CONTINUATION_ENDINGS = (
    " oder", " und", " sowie", " beziehungsweise", " bzw.",
    " or", " and",  # English
)

NUMBER_RE = re.compile(r'^(\d+(?:\.\d+)*)\s+(.+)$')
HEADING_RE = re.compile(r'^(#{2,6})\s+(\d+(?:\.\d+)*)\s+(.+)$')

# Matches area/volume units followed by an exponent digit not part of a larger number
# e.g. m2 → m²,  cm3 → cm³,  mm2 → mm²
_UNIT_SUP_RE = re.compile(r'\b((?:k|c|d|m)?m)([23])(?!\d)')
_SUP_MAP = {"2": "²", "3": "³"}


def fix_unit_superscripts(line: str) -> str:
    return _UNIT_SUP_RE.sub(lambda m: m.group(1) + _SUP_MAP[m.group(2)], line)

HEADING_LEVELS = {1: "##", 2: "###", 3: "####", 4: "#####"}


def heading_prefix(number_str: str) -> str:
    depth = number_str.count(".") + 1
    return HEADING_LEVELS.get(depth, "#####")


def _text_looks_like_clause(text: str, raw_line: str, next_line: str) -> bool:
    """Return True if the text portion indicates a clause (not a heading)."""
    # Ends with period or colon
    if text.endswith(".") or text.endswith(":"):
        return True

    # Contains an embedded sentence break ('. ' inside the text)
    if ". " in text:
        return True

    # Line ends with a conjunction that continues on the next line
    for ending in CONTINUATION_ENDINGS:
        if raw_line.rstrip().endswith(ending):
            return True

    # Very long line (real headings are rarely > 80 chars)
    if len(raw_line.rstrip()) > 80:
        return True

    # Starts with a clause-starter word
    for starter in CLAUSE_STARTERS:
        if text.startswith(starter):
            return True

    # Next non-empty line continues the sentence
    if next_line:
        stripped = next_line.strip()
        if stripped and stripped[0].islower():
            return True
        # PDF hyphen wrap: current line ends with a hyphenated break
        if raw_line.rstrip().endswith("-") and stripped:
            return True

    return False


def process_lines(lines):
    """
    Process lines, converting headings and reverting false positives.
    Returns (result_lines, conversions, reversions).
    """
    in_frontmatter = False
    in_code_block = False
    result = []
    conversions = 0
    reversions = 0

    for i, raw_line in enumerate(lines):
        line = raw_line.rstrip("\n").rstrip("\r")
        ending = raw_line[len(raw_line.rstrip("\r\n")):]  # preserve \n or \r\n

        # ── Frontmatter ───────────────────────────────────────────────────
        if i == 0 and line.strip() == "---":
            in_frontmatter = True
            result.append(raw_line)
            continue
        if in_frontmatter:
            result.append(raw_line)
            if line.strip() == "---":
                in_frontmatter = False
            continue

        # ── Code blocks ───────────────────────────────────────────────────
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            result.append(raw_line)
            continue
        if in_code_block:
            result.append(raw_line)
            continue

        # Look ahead for next non-empty line
        next_line = ""
        for j in range(i + 1, len(lines)):
            candidate = lines[j].strip()
            if candidate:
                next_line = candidate
                break

        # ── Check existing headings for false positives (revert) ──────────
        hm = HEADING_RE.match(line)
        if hm:
            hashes, number, text = hm.group(1), hm.group(2), hm.group(3)
            # Reconstruct the original plain-text line to get its true length
            original_line = f"{number} {text}"
            if _text_looks_like_clause(text, original_line, next_line):
                # Revert to plain text
                result.append(f"{number} {text}{ending}")
                reversions += 1
            else:
                result.append(raw_line)
            continue

        # ── Convert plain numbered lines to headings ───────────────────────
        m = NUMBER_RE.match(line)
        if m:
            number, text = m.group(1), m.group(2).strip()
            if not _text_looks_like_clause(text, line, next_line):
                prefix = heading_prefix(number)
                result.append(f"{prefix} {line.strip()}{ending}")
                conversions += 1
                continue

        result.append(raw_line)

    return result, conversions, reversions


def apply_unit_superscripts(text: str):
    """Replace m2/m3 etc. with m²/m³ outside frontmatter and code blocks."""
    out_lines = []
    count = 0
    in_frontmatter = False
    in_code_block = False
    raw_lines = text.splitlines(keepends=True)
    for i, raw in enumerate(raw_lines):
        stripped = raw.strip()
        if i == 0 and stripped == "---":
            in_frontmatter = True
            out_lines.append(raw)
            continue
        if in_frontmatter:
            out_lines.append(raw)
            if stripped == "---":
                in_frontmatter = False
            continue
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            out_lines.append(raw)
            continue
        if in_code_block:
            out_lines.append(raw)
            continue
        fixed = fix_unit_superscripts(raw)
        if fixed != raw:
            count += len(_UNIT_SUP_RE.findall(raw))
            out_lines.append(fixed)
        else:
            out_lines.append(raw)
    return "".join(out_lines), count


def format_file(path: Path):
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    result, conversions, reversions = process_lines(lines)
    new_text, unit_fixes = apply_unit_superscripts("".join(result))
    if conversions or reversions or unit_fixes:
        path.write_text(new_text, encoding="utf-8")
    return conversions, reversions, unit_fixes


def should_skip(path: Path) -> bool:
    name = path.name
    return "_MOC" in name or name in ("CLAUDE.md", "00_Wissensbank_Index.md")


def main():
    root = Path(__file__).parent.parent / "data"
    md_files = sorted(root.rglob("*.md"))

    total_conv = total_rev = total_unit = total_files = 0

    for f in md_files:
        if should_skip(f):
            print(f"  SKIP  {f.relative_to(root.parent)}")
            continue
        conv, rev, unit = format_file(f)
        rel = f.relative_to(root.parent)
        if conv or rev or unit:
            print(f"  +{conv:3d} / -{rev:3d} / ~{unit:3d}unit  {rel}")
            total_files += 1
            total_conv += conv
            total_rev += rev
            total_unit += unit
        else:
            print(f"  --           {rel}")

    print(f"\nDone. {total_conv} headings converted, {total_rev} reverted, "
          f"{total_unit} unit superscripts fixed across {total_files} files.")


if __name__ == "__main__":
    main()
