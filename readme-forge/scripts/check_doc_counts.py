#!/usr/bin/env python3
"""Verify that hard-coded style, palette and profile counts in docs match the code.

Intended to run from the repository root. Exits non-zero on any mismatch,
printing the file and line.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]  # scripts -> readme-forge -> root


def get_counts():
    scripts_dir = ROOT / "readme-forge" / "scripts"
    sys.path.insert(0, str(scripts_dir))
    import make_banner  # noqa: E402

    styles = len(make_banner.STYLES)
    palettes = len(make_banner.PALETTES)
    profile_dir = ROOT / "readme-forge" / "templates" / "profile"
    profiles = len(list(profile_dir.glob("*.md")))
    return styles, palettes, profiles


def main() -> None:
    styles, palettes, profiles = get_counts()
    print(f"Code counts: {styles} styles, {palettes} palettes, {profiles} profile templates")

    # Capture a number immediately preceding the keyword.
    patterns = [
        (re.compile(r"(\d+)\s+(?:animated\s+)?(?:SVG\s+)?(?:banner\s+)?styles", re.I), styles, "styles"),
        (re.compile(r"(\d+)\s+palettes", re.I), palettes, "palettes"),
        (re.compile(r"(\d+)\s+(?:profile\s+)?archetypes", re.I), profiles, "archetypes"),
    ]

    # Files mentioned in the issue plus common places.
    files = [
        ROOT / "README.md",
        ROOT / "readme-forge" / "README.md",
        ROOT / "readme-forge" / "SKILL.md",
        ROOT / "readme-forge" / "references" / "widgets.md",
    ]

    mismatches = []
    for f in files:
        if not f.is_file():
            continue
        text = f.read_text(encoding="utf-8")
        for lineno, line in enumerate(text.splitlines(), 1):
            for pat, expected, kind in patterns:
                m = pat.search(line)
                if m:
                    found = int(m.group(1))
                    if found != expected:
                        snippet = line.strip()[:140]
                        mismatches.append(
                            f"{f.relative_to(ROOT)}:{lineno}: expected {expected} {kind}, found {found} — {snippet}"
                        )

    if mismatches:
        print("Count mismatches:")
        for m in mismatches:
            print(f"  {m}")
        sys.exit(1)

    print("All documented counts match the code.")
    sys.exit(0)


if __name__ == "__main__":
    main()
