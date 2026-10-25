#!/usr/bin/env python3
"""A row-aware merge driver for System/Approvals.md.

Why this exists. Approvals.md is the one file a Cowork session and the cloud watcher both
write, and it cannot use git's union merge, because its rows are edited in place and union
would leave two copies of the same row. So every overlap became a conflict, the sync
stopped silently, and the operator had to fix it by hand. Four times on 18 September alone.

What it does. Both sides are parsed into rows keyed by id. Rows only one side has are kept.
Rows both sides changed are settled by status: whichever side has moved the row further
along wins, because work only ever progresses. Everything that is not a table row (the rules,
the notes section, the markers) is three-way merged line by line with git merge-file, so a
paragraph one side added is kept; if that text conflicts, both versions are kept rather than
either being lost (found 18 Sep, when the first version took our side's text and dropped a
rule paragraph the watcher had added).

It exits 0 on a clean merge and 1 if it genuinely cannot settle something, which leaves a
normal conflict for a human, so a failure here is no worse than today.

    git config merge.approvals.name "row-aware merge for Approvals.md"
    git config merge.approvals.driver "python3 'System/Setup/merge-approvals.py' %O %A %B"
"""
from __future__ import annotations
import subprocess
import sys
import tempfile
from pathlib import Path

# a placeholder line standing in for a row while the surrounding text is merged. No NUL byte,
# because git merge-file refuses a file with one as binary.
MARK = "ROWMARK::"

# how far along a row is. A row never moves backwards, so the higher rank wins.
RANK = {"requested": 1, "pending": 2, "approved": 3, "in progress": 4, "declined": 5, "done": 6}

# cell positions on a Queue row: the note, and the department (the optional 12th cell)
NOTE = 9
DEPT = 11


def row_id(line: str) -> str | None:
    if not line.startswith(("| a-", "| n-", "| L-")):
        return None
    parts = line.split("|")
    return parts[1].strip() if len(parts) > 2 else None


def row_status(line: str) -> str:
    parts = line.split("|")
    # Owlbridge pipeline rows (L- ids) carry their status in the eighth column, not the second.
    col = 8 if line.startswith("| L-") else 2
    return parts[col].strip().lower() if len(parts) > col + 1 else ""


def split(text: str) -> tuple[list[str], dict[str, str], list[str]]:
    """Returns (non-row lines in order with placeholders, rows by id, id order)."""
    skeleton: list[str] = []
    rows: dict[str, str] = {}
    order: list[str] = []
    for line in text.split("\n"):
        rid = row_id(line)
        if rid is None:
            skeleton.append(line)
        else:
            if rid not in rows:
                order.append(rid)
                skeleton.append(f"{MARK}{rid}")
            rows[rid] = line          # a later duplicate on one side wins, which dedupes too
    return skeleton, rows, order


def _cells(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def _join(cells: list[str]) -> str:
    return "| " + " | ".join(cells) + " |"


def pick(base: str | None, ours: str | None, theirs: str | None) -> str | None:
    if ours is None:
        return theirs
    if theirs is None:
        return ours
    if ours == theirs:
        return ours
    if base is not None:
        if ours == base:
            return theirs
        if theirs == base:
            return ours
    # Both changed the row. The side that changed the STATUS made the real move, whatever
    # its rank: in progress to pending is a run handing work back for review, which a pure
    # rank order threw away on 22 Sep. Rank only decides when both sides changed the status.
    sb = row_status(base) if base is not None else ""
    so, st = row_status(ours), row_status(theirs)
    if so == sb and st != sb:
        winner, loser = theirs, ours
    elif st == sb and so != sb:
        winner, loser = ours, theirs
    else:
        ro, rt = RANK.get(so, 0), RANK.get(st, 0)
        if ro != rt:
            winner, loser = (ours, theirs) if ro > rt else (theirs, ours)
        else:
            winner, loser = (ours, theirs) if len(ours) >= len(theirs) else (theirs, ours)
    # Notes are append-only: keep whatever the other side added to the note, so neither
    # side's record is lost, only placed after the winner's.
    if winner.startswith("| L-"):
        return winner             # a lead's last cell is its source, not an append-only note
    # A Queue row has 10, 11 or 12 cells: the note is always the 10th (index 9), priority the
    # 11th and the department the 12th (added 26 Sep for the Team area). The two sides can hold
    # the same row at different widths (one side set a department the other has not seen), so
    # the note is read by position, never as the last cell, and a department only one side set
    # is kept: departments are assigned, never cleared.
    try:
        w, l = _cells(winner), _cells(loser)
        b = _cells(base) if base is not None else None
        if len(w) >= 10 and len(l) >= 10:
            changed = False
            base_note = b[NOTE] if b and len(b) > NOTE else ""
            extra = l[NOTE][len(base_note):].strip() if base_note and l[NOTE].startswith(base_note) else ""
            extra = extra.lstrip("; ").strip()
            if extra and extra not in w[NOTE]:
                w[NOTE] = (w[NOTE].rstrip("; ") + "; " + extra) if w[NOTE] else extra
                changed = True
            l_dept = l[DEPT] if len(l) > DEPT else ""
            if l_dept and not (w[DEPT] if len(w) > DEPT else ""):
                while len(w) <= DEPT:
                    w.append("")
                w[DEPT] = l_dept
                changed = True
            if changed:
                return _join(w)
    except Exception:
        pass
    return winner


def merge_skeleton(base: list[str], ours: list[str], theirs: list[str]) -> list[str]:
    """Three-way merge of the non-row text. Clean merge first; if it conflicts, keep both sides."""
    if ours == theirs or base == theirs:
        return ours
    if base == ours:
        return theirs
    with tempfile.TemporaryDirectory() as d:
        paths = []
        for name, lines in (("base", base), ("ours", ours), ("theirs", theirs)):
            fp = Path(d, name)
            fp.write_text("\n".join(lines) + "\n", encoding="utf-8")
            paths.append(str(fp))
        b, o, t = paths
        for extra in ([], ["--union"]):
            try:
                r = subprocess.run(["git", "merge-file", "-p", *extra, o, b, t],
                                   capture_output=True, text=True, encoding="utf-8")
            except OSError:
                break
            if r.returncode == 0 or extra:
                text = r.stdout
                if text.endswith("\n"):
                    text = text[:-1]
                return text.split("\n")
    # git unavailable: our text, plus any lines the other side added, so nothing is lost
    seen = set(ours) | set(base)
    return ours + [l for l in theirs if l not in seen and not l.startswith(MARK)]


def main() -> int:
    if len(sys.argv) < 4:
        print("usage: merge-approvals.py <base> <ours> <theirs>", file=sys.stderr)
        return 1
    base_p, ours_p, theirs_p = (Path(a) for a in sys.argv[1:4])
    base = base_p.read_text(encoding="utf-8") if base_p.exists() else ""
    ours = ours_p.read_text(encoding="utf-8")
    theirs = theirs_p.read_text(encoding="utf-8")

    b_skel, b_rows, _ = split(base)
    o_skel, o_rows, o_order = split(ours)
    t_skel, t_rows, t_order = split(theirs)
    o_skel = merge_skeleton(b_skel, o_skel, t_skel)

    merged: dict[str, str] = {}
    for rid in set(o_rows) | set(t_rows):
        line = pick(b_rows.get(rid), o_rows.get(rid), t_rows.get(rid))
        if line is not None:
            merged[rid] = line

    # our skeleton, with rows only the other side has appended after the last row we know
    out: list[str] = []
    placed: set[str] = set()
    extras = [rid for rid in t_order if rid not in o_order]
    last_row_index = max((i for i, l in enumerate(o_skel) if l.startswith(MARK)), default=-1)

    for i, line in enumerate(o_skel):
        if line.startswith(MARK):
            rid = line[len(MARK):]
            if rid in merged and rid not in placed:
                out.append(merged[rid])
                placed.add(rid)
        else:
            out.append(line)
        if i == last_row_index:
            for rid in extras:
                if rid in merged and rid not in placed:
                    out.append(merged[rid])
                    placed.add(rid)

    for rid in extras:                      # nothing is dropped, whatever the skeleton looked like
        if rid in merged and rid not in placed:
            out.append(merged[rid])
            placed.add(rid)

    if len(placed) != len(merged):
        print("merge-approvals: could not place every row, leaving it to a human", file=sys.stderr)
        return 1

    ours_p.write_text("\n".join(out), encoding="utf-8")
    print(f"merge-approvals: merged {len(merged)} rows cleanly", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
