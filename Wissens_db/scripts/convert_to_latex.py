"""
convert_to_latex.py

Converts Obsidian ~subscript~ notation to LaTeX $...$ inline math across all
markdown files.  Only single-letter variable tokens (optionally with Δ prefix
or prime suffix) are converted, avoiding false positives in regular prose.

Examples:
  Q~h~          →  $Q_h$
  Q~tot~        →  $Q_{tot}$
  ΔQ~h,li~      →  $\Delta Q_{h,li}$
  η~R~          →  $\eta_R$
  E'~W,aux~     →  $E'_{W,aux}$
  σ~Q,i~        →  $\sigma_{Q,i}$

Run:  py scripts/convert_to_latex.py
"""

import re
import sys
import io
from pathlib import Path

# ── Greek letter → LaTeX command ───────────────────────────────────────────────

GREEK = {
    'α': r'\alpha',   'β': r'\beta',      'γ': r'\gamma',  'δ': r'\delta',
    'ε': r'\varepsilon', 'ζ': r'\zeta',   'η': r'\eta',    'θ': r'\theta',
    'λ': r'\lambda',  'μ': r'\mu',        'ν': r'\nu',     'ξ': r'\xi',
    'π': r'\pi',      'ρ': r'\rho',       'σ': r'\sigma',  'τ': r'\tau',
    'υ': r'\upsilon', 'φ': r'\varphi',    'χ': r'\chi',    'ψ': r'\psi',
    'ω': r'\omega',
    'Φ': r'\Phi', 'Ψ': r'\Psi', 'Ω': r'\Omega',
    'Σ': r'\Sigma', 'Λ': r'\Lambda', 'Θ': r'\Theta', 'Ξ': r'\Xi',
}

# ── Pattern ─────────────────────────────────────────────────────────────────────

_VAR  = r'[A-ZΦΨΩΣΛΘΞa-zαβγδεζηθλμνξπρστυφχψω]'
_PRIM = r"[''′]"   # ASCII apos, right-single-quote U+2019, prime U+2032

# Negative lookbehind: not preceded by an ASCII letter or German umlaut,
# so we don't accidentally match the last letter of an ordinary word.
_PAT = re.compile(
    r"(?<![A-Za-zäöüÄÖÜ])"   # not preceded by a regular letter
    r"(Δ?)"                    # optional Δ prefix (capital delta)
    r"(" + _VAR + r")"        # single variable letter
    r"(" + _PRIM + r")?"      # optional prime / apostrophe
    r"~([^~\n]+)~"            # ~subscript content~
)


def _replace(m):
    delta  = m.group(1)   # '' or 'Δ'
    letter = m.group(2)   # single letter
    prime  = m.group(3)   # None or prime char
    sub    = m.group(4)   # subscript text

    latex_letter = GREEK.get(letter, letter)

    # Normalise any prime variant to ASCII apostrophe (LaTeX prime operator)
    latex_prime = "'" if prime else ""

    # Use braces when subscript has >1 char or contains non-alnum chars
    if len(sub) == 1 and sub.isalnum():
        latex_sub = sub
    else:
        latex_sub = f'{{{sub}}}'

    delta_part = r'\Delta ' if delta else ''
    return f'${delta_part}{latex_letter}{latex_prime}_{latex_sub}$'


# ── File processing ─────────────────────────────────────────────────────────────

def process_text(text):
    """Returns (new_text, changed_lines_count)."""
    lines = text.splitlines(keepends=True)
    result = []
    fixes = 0
    in_frontmatter = False
    in_code_block   = False

    for i, raw in enumerate(lines):
        s       = raw.rstrip('\r\n')
        stripped = s.strip()

        # ── frontmatter ──
        if i == 0 and stripped == '---':
            in_frontmatter = True
            result.append(raw)
            continue
        if in_frontmatter:
            result.append(raw)
            if stripped == '---':
                in_frontmatter = False
            continue

        # ── fenced code blocks ──
        if stripped.startswith('```'):
            in_code_block = not in_code_block
            result.append(raw)
            continue
        if in_code_block:
            result.append(raw)
            continue

        new_s = _PAT.sub(_replace, s)
        if new_s != s:
            fixes += 1
        ending = raw[len(raw.rstrip('\r\n')):]
        result.append(new_s + ending)

    return ''.join(result), fixes


def should_skip(path):
    n = path.name
    return '_MOC' in n or n in ('CLAUDE.md', '00_Wissensbank_Index.md')


# ── Main ────────────────────────────────────────────────────────────────────────

def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

    root  = Path(__file__).parent.parent / 'data'
    files = sorted(root.rglob('*.md'))
    total_fixes = total_files = 0

    for f in files:
        if should_skip(f):
            print(f'  SKIP  {f.relative_to(root.parent)}')
            continue
        text     = f.read_text(encoding='utf-8')
        new_text, fixes = process_text(text)
        rel = f.relative_to(root.parent)
        if fixes:
            f.write_text(new_text, encoding='utf-8')
            print(f'  ~{fixes:3d}  {rel}')
            total_fixes += fixes
            total_files  += 1
        else:
            print(f'  --   {rel}')

    print(f'\nDone. {total_fixes} lines converted in {total_files} files.')


if __name__ == '__main__':
    main()
