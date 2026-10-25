---
name: brain-run
description: Run one of the Brain's playbooks on demand (MORNING, EVENING, WEEKLY, SCOUT, INGEST, TIDY, BOARD REVIEW, NEW PROJECT, MANAGE, LEADGEN, CORRECTION) against this vault, writing the run log line when done.
---

# Brain run

Use when the operator says "run MORNING", "process the inbox", "do the weekly", "board review Owlbridge", "run SCOUT on Gaugewell", "new project X", or names any playbook. The scheduled cloud routines run the same playbooks; this is how one runs by hand, in Claude Code on the Mac.

The vault root is the working directory (the folder with `CLAUDE.md` and `.obsidian/`). Work in place; do not copy notes elsewhere to read them.

## Steps

1. Read `CLAUDE.md`, then `System/Playbooks/<NAME>.md` for the playbook asked for, then the agent brief it names in `System/Agents/`.
2. Do read 0 if the playbook has one: on the Mac the copy is current, but check for `conflict-files-obsidian-git.md` and `<<<<<<<` lines first.
3. Do exactly what the playbook's **Reads** and **Steps** say, in order. The playbooks are written to be executable; do not improvise a different shape.
4. Respect **Idempotent**: check for today's output before writing. Update in place; never duplicate a plan, a review, a ledger line or a build log entry.
5. Write one line to the Latest table in `System/Run log.md`: time from the clock (run `date` in the same command, Europe/London), job, surface (CLAUDE CODE), OK or FAILED, and a short note. If a step could not be completed, the line says FAILED and why.
6. Report back in five lines or fewer: what was written, where, and anything that needs the operator's yes.

## Playbook map

| Say | Playbook | Writes |
|---|---|---|
| run MORNING, morning plan | `MORNING.md` | Today's daily note: Plan and Suggested priorities |
| run EVENING, review the day | `EVENING.md` | Today's daily note: Review and Carry forward; ledgers; Now ticks; State |
| run WEEKLY, do the weekly | `WEEKLY.md` | `Journal/Weekly/<YYYY>-W<WW>.md` and next week's note; Now; promotions |
| run SCOUT, scout <area> | `SCOUT.md` | New rows in `System/Scout.md` |
| process the inbox | `INGEST.md` | Routes each `Inbox/` item, marks it processed |
| tidy the vault | `TIDY.md` | Fixes and proposals, never moves or deletes |
| board review <venture> | `BOARD REVIEW.md` | A dated section in the venture note |
| new project <name> | `NEW PROJECT.md` | Project note, build log, Index and Now rows |
| run the team, work the queue | `MANAGE.md` | Approvals rows, the tagged DIRECTOR run log line |
| work the pipeline | `LEADGEN.md` | Owlbridge pipeline rows and activity lines, through the Director |
| log a correction | `CORRECTION.md` | `System/Corrections.md`, and a promotion on always or never |

## Rules

- British English, no em dashes, no invented numbers or status. Gaps are marked with `> [!question]`.
- Never reorder the top three of `Now.md` silently, never add tasks the operator did not create except as labelled proposals, and never move, rename or delete notes.
- MANAGE and LEADGEN claim in `System/Setup/Watcher lock.md` first, as the playbooks say, so a cloud run and this session never work the same row.
- Anything outside the vault that sends, publishes, deploys, merges or spends waits for the operator's explicit yes (`System/Permissions.md`).
