---
title: Vault sync
aliases: [Sync, git sync, merge conflicts]
type: system
parent: "[[Operating manual]]"
owner: the operator
updated: 2026-10-14
tags:
  - system
  - setup
---

# Vault sync

How the vault travels between the Mac, GitHub, the cloud routines and the platform, why it stopped on 18 Sep, and what to check when it stops again.

## The route

The Mac's copy is mirrored to a private GitHub repository by Obsidian Git, and only while Obsidian is open. The cloud routines clone that repository, work, and push `claude/` branches that a GitHub Action merges into main. The platform reads and writes main directly. Obsidian Git pulls main back to the Mac. Every commit Obsidian Git makes starts `vault:`, so the newest `vault:` commit is the Mac's last sync.

> [!warning] A stale copy plans the wrong day
> From 9 to 13 Oct Obsidian was closed on the Mac and nothing synced. Four cloud runs planned from a copy days behind the Mac and reported work as unmoved that had been done. Since 14 Oct every routine reads the newest `vault:` commit before planning and says so first if it is more than a day old.

## What was wrong, 18 September 2026

Four sync failures in a day. The diagnosis went through two wrong answers before the real one.

1. **Wrong: auto push was off.** The push interval read 0, but that field does nothing while split timers are off, and push on commit-and-sync was on the whole time. The Mac was pushing.
2. **Partly right: a bare pull on its own timer.** An auto pull interval was running alongside a commit-and-sync that already pulls. A bare pull that hits a conflict leaves the repository mid-merge with nothing to finish it. Set to 0 on 18 Sep and that helped.
3. **The actual cause: the fix for it had never worked.** `.gitattributes` carried `System/Run log.md merge=union`. Git splits every attributes line on the first whitespace, so that was read as the pattern `System/Run` with the attributes `log.md` and `merge=union`, and did nothing at all. No error, no warning. The union merge added to stop the run log conflicting had never once applied to it.

> [!warning] A .gitattributes pattern cannot contain a space
> Use a wildcard: `System/Run?log.md`, not `System/Run log.md`. Verify every change with `git check-attr merge -- "<the path>"` before believing it works.

## What is in place now

| File | Merge | Why |
|---|---|---|
| `System/Run log.md` | union | Append only. Both sides' rows are kept |
| `System/Corrections.md` | union | Append only |
| `System/Chat.md` | union | Append only |
| `System/Setup/Watcher lock.md` | union | Append only, written by the lock script |
| `*build log.md` | union | Append only |
| `System/Approvals.md` | **approvals** | Rows are edited in place, so union would duplicate them. A row-aware driver merges by id instead |
| Daily notes | none | Their sections are rewritten, not appended. A conflict here should be looked at by a person |

## The row-aware driver

`System/Setup/merge-approvals.py`, versioned in the vault. Git will not run a custom driver unless the machine is told where it is, and that setting lives in `.git/config`, which is not versioned, so it is set once per machine from the vault root:

```
git config merge.approvals.name "row-aware merge for Approvals.md"
git config merge.approvals.driver "python3 'System/Setup/merge-approvals.py' %O %A %B"
```

Applied on the Mac on 18 Sep. Each cloud routine sets the same line just before its rebase, in the SAVING clause of its prompt.

What it does. Both sides are parsed into rows keyed by id.

- A row only one side has is kept.
- A row both sides changed is settled by status, because work only moves forwards: `done` and `declined` beat `in progress`, which beats `approved`, `pending` and `requested`.
- A duplicate row on one side is deduped.
- Anything that is not a table row (the rules, the notes section, the markers) is three-way merged line by line; if the two sides changed the same lines, both versions are kept rather than either being lost.
- If it cannot place every row it exits non-zero, leaving an ordinary conflict for a person. A failure is never worse than no driver.

Tested before it was committed against five cases: both sides advancing the same row, a duplicate row on one side, one-sided edits, both sides adding several rows, and the Notes table.

## If it conflicts anyway

1. Obsidian Git leaves `conflict-files-obsidian-git.md` at the vault root while a conflict is open. **If that file exists, the vault is not syncing**, and the platform is showing stale data. It is the fastest thing to check.
2. Search the vault for lines starting `<<<<<<<` and resolve each by hand: keep both sides' real additions, and the newer dated fact wins.
3. In Obsidian, commit all changes, then commit-and-sync. A bare push is rejected when the branch is behind, which is the "non-fast-forward" error.

## Related

[[Approvals]] · [[Run log]] · [[Corrections]] · [[Set up the cloud routines]] · [[Scheduled jobs]]
