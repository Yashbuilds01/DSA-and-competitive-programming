#!/usr/bin/env python3
"""
Update the Questions Solved table in README.md.

Behavior:
- Counts files in /python, /javascript, /cpp by file extensions configured below.
- Updates the table found under the "## 📊 Progress Dashboard" section.
- If markers are present (<!-- progress-table:start --> ... <!-- progress-table:end -->),
  the content between markers will be replaced. Otherwise, it tries to replace the markdown
  table that starts with the header line "| Language | Questions Solved | Status |".
- Run locally with --dry-run to preview changes without writing.
"""

import argparse
import os
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]  # repo root
README = ROOT / "README.md"

# Configure mapping: key->(directory, extensions list, display name)
LANGS = {
    "Python": ("python", [".py"], "🐍"),
    "JavaScript": ("javascript", [".js", ".jsx", ".ts", ".tsx"], "🟨"),
    "C++": ("cpp", [".cpp", ".cc", ".c", ".cxx", ".h", ".hpp", ".hh", ".hxx"], "🟦"),
}

# Files/dirs to ignore while counting
IGNORED_DIRS = {"__pycache__", ".git", "node_modules", ".venv", "venv", ".github"}

START_MARKER = "<!-- progress-table:start -->"
END_MARKER = "<!-- progress-table:end -->"


def count_files(dirpath: Path, exts):
    if not dirpath.exists():
        return 0
    count = 0
    for root, dirs, files in os.walk(dirpath):
        # skip ignored dirs
        dirs[:] = [d for d in dirs if d not in IGNORED_DIRS]
        for f in files:
            if any(f.lower().endswith(ext) for ext in exts):
                count += 1
    return count


def make_table(counts):
    rows = []
    for name, (folder, exts, emoji) in LANGS.items():
        c = counts.get(name, 0)
        # Simple status heuristic: active if any solved, otherwise planned
        status = "🟢 Active" if c > 0 else "🟡 Planned"
        rows.append(f"| **{name}** {emoji} | {c} | {status} |")
    table = "\n".join([
        START_MARKER,
        "",
        "| Language | Questions Solved | Status |",
        "| :--- | :---: | :--- |",
        *rows,
        "",
        END_MARKER,
        ""
    ])
    return table


def replace_table_in_readme(readme_text, new_table):
    # 1) If markers exist, replace between them
    if START_MARKER in readme_text and END_MARKER in readme_text:
        pattern = re.compile(
            re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER),
            flags=re.DOTALL
        )
        new_text = pattern.sub(new_table.strip("\n") + "\n\n", readme_text)
        return new_text

    # 2) Fallback: find the first markdown table that starts with the header and ends before a blank line followed by a heading
    header_regex = r"^\| Language \| Questions Solved \| Status \|.*?(?=\n## |\Z)"
    match = re.search(header_regex, readme_text, flags=re.DOTALL | re.MULTILINE)
    if match:
        new_text = readme_text[:match.start()] + new_table + readme_text[match.end():]
        return new_text

    # 3) If neither found, append the table under the "## 📊 Progress Dashboard" heading if present
    heading_regex = r"(## 📊 Progress Dashboard\s*\n)"
    m = re.search(heading_regex, readme_text)
    if m:
        insert_at = m.end()
        new_text = readme_text[:insert_at] + "\n" + new_table + readme_text[insert_at:]
        return new_text

    # 4) As last resort, append to the end
    return readme_text.rstrip() + "\n\n" + new_table


def main(dry_run=False):
    counts = {}
    for name, (folder, exts, emoji) in LANGS.items():
        folder_path = ROOT / folder
        counts[name] = count_files(folder_path, exts)

    new_table = make_table(counts)

    if not README.exists():
        print("README.md not found at", README)
        sys.exit(1)

    text = README.read_text(encoding="utf-8")
    updated = replace_table_in_readme(text, new_table)

    if text == updated:
        print("No changes required. Counts:", counts)
        return 0

    if dry_run:
        print("=== DRY RUN: Generated table ===\n")
        print(new_table)
        print("\n=== End table ===")
        print("Counts:", counts)
        return 0

    README.write_text(updated, encoding="utf-8")
    print("README.md updated. Counts:", counts)
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Print results without writing README.md")
    args = parser.parse_args()
    sys.exit(main(dry_run=args.dry_run))
