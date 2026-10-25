#!/usr/bin/env python3
"""Lists notes whose frontmatter `updated` field lags their real last git edit.

Why this exists. MORNING and EVENING both filter "what changed today" by a note's
`updated` frontmatter field. Found 18 Sep 2026: [[Fernmoor Hub build log]] carried five
sections dated 18 Sep while its frontmatter still read 16 Sep, and [[Now]] carried a
note dated 18 Sep with its frontmatter still on 17 Sep. A stale field is read as if
nothing happened that day, which understates the review silently.

What it does. For every tracked markdown file, compares the `updated:` value in its
frontmatter against the date of its most recent git commit. A mismatch where the git
date is newer than the frontmatter is listed for a quick fix; a mismatch the other way
(frontmatter newer than any commit, for example a same-day edit not yet committed) is
not flagged, since it is not the failure mode this exists to catch.

Read only. It never edits a note; TIDY or EVENING lists what it finds.

Usage, from the vault root:
    python3 System/Setup/check-stale-updated.py
"""
from __future__ import annotations
import re
import subprocess
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parents[2]
SKIP_DIRS = {".git", "_review", ".obsidian", "_to_delete"}
UPDATED_RE = re.compile(r"^updated:\s*(\d{4}-\d{2}-\d{2})\s*$", re.MULTILINE)

# The vault's git history starts 14 Sep 2026, when the git bridge first pushed the
# whole vault (see CLAUDE.md, Where the work lives). Every note's git date from that
# import is the day it entered git, not the day a person last edited it in Obsidian, so
# a note untouched since only reads as "stale since the bridge" and is not a real find.
# Tested 18 Sep against the vault as it stood then: without this floor, 75 of about 125
# notes came back as stale, nearly all of them import noise. Only a git change after
# this date reflects a real edit this check can trust.
BASELINE_DATE = "2026-09-15"


def frontmatter_updated(text: str) -> str | None:
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    match = UPDATED_RE.search(text[:end])
    return match.group(1) if match else None


def last_git_date(path: Path) -> str | None:
    result = subprocess.run(
        ["git", "log", "-1", "--format=%cs", "--", str(path.relative_to(VAULT_ROOT))],
        cwd=VAULT_ROOT, capture_output=True, text=True,
    )
    date = result.stdout.strip()
    return date or None


def find_notes() -> list[Path]:
    notes = []
    for path in VAULT_ROOT.rglob("*.md"):
        if any(part in SKIP_DIRS for part in path.relative_to(VAULT_ROOT).parts):
            continue
        notes.append(path)
    return notes


def main() -> int:
    mismatches = []
    for path in sorted(find_notes()):
        text = path.read_text(encoding="utf-8", errors="ignore")
        updated = frontmatter_updated(text)
        if updated is None:
            continue
        git_date = last_git_date(path)
        if git_date and git_date > updated and git_date > BASELINE_DATE:
            mismatches.append((str(path.relative_to(VAULT_ROOT)), updated, git_date))

    if not mismatches:
        print("No stale `updated` fields found.")
        return 0

    print(f"{len(mismatches)} note(s) with a stale `updated` field:\n")
    for rel_path, frontmatter_date, git_date in mismatches:
        print(f"- {rel_path}: frontmatter says {frontmatter_date}, last git change {git_date}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
