#!/usr/bin/env python3
"""A run lock for the cloud routines, so two runs never work the same queue at once.

Why this exists. Twice on 23 Sep two approvals watcher runs started minutes apart (Done
presses, a schedule and a manual start) and both built the same pull request, the most
expensive kind of duplicate. The platform already refuses a second start from its own
buttons; this covers every other overlap, from any surface.

How it works. The lock is a ledger, System/Setup/Watcher lock.md, one table row per claim or
release, merged with union so two runs adding rows never conflict. A run claims by pushing a
row to a claude/ branch, which the merge Action carries into main within a minute, then waits
until its row is on main and reads the ledger again. Of the live claims, the earliest wins (a
tie goes to the lower run id); every other run releases and stands down. A claim with no
release goes stale after --ttl minutes, so a run that dies never blocks the next one. Nothing
is ever deleted: releasing is one more row.

    python3 System/Setup/watcher-lock.py claim   --run <id>   exit 0 go ahead, 3 stand down,
                                                              5 not confirmed on main in time
    python3 System/Setup/watcher-lock.py release --run <id>   adds the release row to the
                                                              working copy, for the run's own
                                                              last commit (--push sends it now)
    python3 System/Setup/watcher-lock.py status               prints the live claims

--key names what is locked (default "watcher"), so one ledger can hold a lock per job or per
queue row. Built 24 Sep 2026 for a-2026-09-24-team-view.
"""
from __future__ import annotations
import argparse
import datetime as dt
import subprocess
import sys
import tempfile
import time
from pathlib import Path

LEDGER = "System/Setup/Watcher lock.md"
REMOTE = "origin"
MAIN = "main"


def git(*args: str, cwd: str | None = None, check: bool = True) -> str:
    out = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)
    if check and out.returncode != 0:
        raise SystemExit(f"git {' '.join(args)} failed: {out.stderr.strip()}")
    return out.stdout


def now() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0)


def stamp(t: dt.datetime) -> str:
    return t.strftime("%Y-%m-%dT%H:%M:%SZ")


def parse(text: str) -> list[tuple[dt.datetime, str, str, str]]:
    """Rows of the ledger as (time, key, run, action). Anything else in the file is ignored."""
    rows = []
    for line in text.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 4 or cells[3] not in ("claim", "release"):
            continue
        try:
            t = dt.datetime.strptime(cells[0], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=dt.timezone.utc)
        except ValueError:
            continue
        rows.append((t, cells[1], cells[2], cells[3]))
    return rows


def live(text: str, key: str, ttl: int, at: dt.datetime) -> list[tuple[dt.datetime, str]]:
    """Claims on this key with no release by the same run and younger than ttl, earliest first."""
    rows = parse(text)
    released = {r for _, k, r, a in rows if k == key and a == "release"}
    claims = {}
    for t, k, r, a in rows:
        if k == key and a == "claim" and r not in released and at - t < dt.timedelta(minutes=ttl):
            claims.setdefault(r, t)
    return sorted((t, r) for r, t in claims.items())


def main_ledger(fetch: bool = True) -> str:
    if fetch:
        git("fetch", "-q", REMOTE, MAIN)
    out = subprocess.run(["git", "show", f"{REMOTE}/{MAIN}:{LEDGER}"], capture_output=True, text=True)
    return out.stdout if out.returncode == 0 else ""


def row(key: str, run: str, action: str) -> str:
    return f"| {stamp(now())} | {key} | {run} | {action} |\n"


def push_row(line: str, branch: str) -> None:
    """Commit one ledger row on top of main in a scratch worktree, so the run's own working
    copy is left alone, and push it to a claude/ branch for the merge Action."""
    with tempfile.TemporaryDirectory() as tmp:
        wt = str(Path(tmp) / "wt")
        git("worktree", "add", "-q", "--detach", wt, f"{REMOTE}/{MAIN}")
        try:
            path = Path(wt) / LEDGER
            text = path.read_text() if path.exists() else ""
            if text and not text.endswith("\n"):
                text += "\n"
            path.write_text(text + line)
            git("add", LEDGER, cwd=wt)
            git("commit", "-q", "-m", f"watcher lock: {line.split('|')[4].strip()} {line.split('|')[3].strip()}", cwd=wt)
            for wait in (0, 2, 4, 8, 16):
                time.sleep(wait)
                if subprocess.run(["git", "push", "-q", REMOTE, f"HEAD:refs/heads/{branch}"], cwd=wt).returncode == 0:
                    return
            raise SystemExit(f"could not push {branch}")
        finally:
            git("worktree", "remove", "--force", wt, check=False)


def claim(a) -> int:
    ledger = main_ledger()
    others = [(t, r) for t, r in live(ledger, a.key, a.ttl, now()) if r != a.run]
    if others:
        print(f"stand down: run {others[0][1]} holds '{a.key}' since {stamp(others[0][0])}")
        return 3
    line = row(a.key, a.run, "claim")
    push_row(line, f"claude/lock-{a.key}-{a.run}")
    deadline = time.time() + a.wait
    while True:
        ledger = main_ledger()
        if line.strip() in ledger:
            break
        if time.time() > deadline:
            print(f"claim pushed but not on {MAIN} after {a.wait}s: carrying on unconfirmed")
            return 5
        time.sleep(a.poll)
    holders = live(ledger, a.key, a.ttl, now())
    if holders and holders[0][1] != a.run:
        push_row(row(a.key, a.run, "release"), f"claude/lock-{a.key}-{a.run}-release")
        print(f"stand down: run {holders[0][1]} claimed '{a.key}' first, at {stamp(holders[0][0])}")
        return 3
    print(f"claimed '{a.key}' for run {a.run}")
    return 0


def release(a) -> int:
    line = row(a.key, a.run, "release")
    if a.push:
        main_ledger()
        push_row(line, f"claude/lock-{a.key}-{a.run}-release")
    else:
        path = Path(LEDGER)
        text = path.read_text() if path.exists() else ""
        if text and not text.endswith("\n"):
            text += "\n"
        path.write_text(text + line)
    print(f"released '{a.key}' for run {a.run}")
    return 0


def status(a) -> int:
    holders = live(main_ledger(), a.key, a.ttl, now())
    print("\n".join(f"{stamp(t)} {r}" for t, r in holders) or f"'{a.key}' is free")
    return 0


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("command", choices=["claim", "release", "status"])
    p.add_argument("--run", default="")
    p.add_argument("--key", default="watcher")
    p.add_argument("--ttl", type=int, default=90, help="minutes before an unreleased claim goes stale")
    p.add_argument("--wait", type=int, default=180, help="seconds to wait for a claim to reach main")
    p.add_argument("--poll", type=int, default=10)
    p.add_argument("--push", action="store_true", help="release: push the row now")
    a = p.parse_args()
    if a.command != "status" and not a.run.replace("-", "").isalnum():
        sys.exit("--run needs a plain id, letters, digits and hyphens")
    sys.exit({"claim": claim, "release": release, "status": status}[a.command](a))
