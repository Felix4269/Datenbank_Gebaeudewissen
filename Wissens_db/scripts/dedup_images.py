"""
dedup_images.py

Removes duplicate image links in Skript_Energie markdown files.

Two kinds of duplicates are removed:
  1. Exact filename appearing more than once  → keep first occurrence.
  2. Non-numbered variant (e.g. abb8_x.jpg) when numbered variants
     already exist for the same figure (e.g. abb8_x_1.jpg, abb8_x_2.jpg)
     → numbered variants are the real sub-images; the plain one is a
     spurious extra extraction.

For each removed ![[file]] line the immediately-following *caption* line
(if any) and any trailing blank line are also removed.

Run:  py scripts/dedup_images.py
"""

import re
from pathlib import Path

IMG_RE       = re.compile(r'!\[\[([^\]]+)\]\]')
FIG_RE       = re.compile(r'^((?:abb|tab)\d+)', re.I)   # abb1, tab5, …
NUM_SUFFIX   = re.compile(r'_\d+\.[a-zA-Z]+$')          # ends with _1.jpg etc.
CAPTION_RE   = re.compile(r'^\*.*\*\s*$')


def fig_key(filename: str) -> str:
    """Return 'abb8', 'tab5', … from a filename; '' if unrecognised."""
    m = FIG_RE.match(filename)
    return m.group(1).lower() if m else ''


def has_num_suffix(filename: str) -> bool:
    return bool(NUM_SUFFIX.search(filename))


def decide_removals(filenames: list) -> set:
    """
    Given a list of filenames for one figure, return the set that should
    be removed.
    """
    if not filenames:
        return set()

    # Step 1 – exact duplicates: remove all but the first occurrence
    seen   = set()
    unique = []
    for f in filenames:
        if f not in seen:
            seen.add(f)
            unique.append(f)

    removed = set(filenames) - set(unique)   # extra occurrences

    # Step 2 – if numbered variants exist, drop non-numbered ones
    numbered   = [f for f in unique if has_num_suffix(f)]
    unnumbered = [f for f in unique if not has_num_suffix(f)]

    if numbered and unnumbered:
        removed |= set(unnumbered)

    # Step 3 – if multiple non-numbered variants, keep longest filename
    if not numbered and len(unnumbered) > 1:
        best = max(unnumbered, key=len)
        removed |= set(unnumbered) - {best}

    return removed


def clean_text(text: str) -> tuple:
    lines  = text.splitlines(keepends=True)
    fixes  = 0

    # ── Pass 1: collect all filenames per figure key ──────────────────
    fig_filenames: dict[str, list] = {}
    for line in lines:
        m = IMG_RE.search(line)
        if not m:
            continue
        fname = m.group(1)
        key   = fig_key(fname)
        if key:
            fig_filenames.setdefault(key, []).append(fname)

    # ── Determine which filenames to drop ─────────────────────────────
    to_remove: set[str] = set()
    for key, fnames in fig_filenames.items():
        to_remove |= decide_removals(fnames)

    if not to_remove:
        return text, 0

    # ── Pass 2: rebuild file, skipping removed image blocks ───────────
    result      = []
    skip_caption = False   # True after removing an image line

    for i, line in enumerate(lines):
        m = IMG_RE.search(line)

        if m and m.group(1) in to_remove:
            # Remove this image line (and signal caption removal)
            skip_caption = True
            fixes += 1
            continue

        if skip_caption:
            if CAPTION_RE.match(line.strip()):
                # Remove the paired caption
                skip_caption = False
                continue
            skip_caption = False   # no caption found – stop skipping

        result.append(line)

    # Collapse runs of 3+ blank lines down to 2
    cleaned = re.sub(r'\n{3,}', '\n\n', ''.join(result))
    return cleaned, fixes


# ── Main ──────────────────────────────────────────────────────────────

def main():
    target = Path(__file__).parent.parent / 'data' / 'Skript_Energie'
    files  = sorted(target.glob('*.md'))
    total_fixes = total_files = 0

    for f in files:
        if '_MOC' in f.name:
            continue
        text     = f.read_text(encoding='utf-8')
        new_text, fixes = clean_text(text)
        if fixes:
            f.write_text(new_text, encoding='utf-8')
            print(f'  -{fixes:2d} dupl.  {f.name}')
            total_fixes += fixes
            total_files  += 1
        else:
            print(f'  ok       {f.name}')

    print(f'\nDone. {total_fixes} duplicate image links removed in {total_files} files.')


if __name__ == '__main__':
    main()
