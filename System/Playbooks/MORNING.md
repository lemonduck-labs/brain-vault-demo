---
title: MORNING
aliases: [Morning plan, Morning brief, Daily plan job]
type: playbook
parent: "[[Operating manual]]"
owner: the operator
updated: 2026-10-14
tags:
  - system
  - playbook
---

# MORNING

Writes today's plan before the operator sits down. Runs 07:00 Monday to Friday as a cloud routine, or on demand with "run MORNING". Role: [[Chief of staff]].

## Reads

0. **Is the copy whole and fresh?** Stop and report if `conflict-files-obsidian-git.md` exists or a note carries `<<<<<<<` lines. Then read the time of the Mac's last sync: the newest commit whose message starts `vault:` (`git log -1 --format=%ci --grep='^vault:'`, deepening a shallow clone first). If it is more than a day old on a weekday, the plan's first line says so, and nothing is reported as unmoved or missed on the vault's evidence alone, because the Mac may hold the work. Added 14 Oct, after four runs from 9 to 13 Oct planned from a copy days behind the Mac.
1. Root `CLAUDE.md`, [[State]], [[Now]], [[Operator]] (the standards section only; it does not change day to day).
2. Yesterday's daily note: the **Review**, **Carry forward** and **Priorities** sections.
3. [[Run log]]: were yesterday's expected runs logged? Also: for each day since the last MORNING line (Friday to Sunday on a Monday), did the run log carry a session line (COWORK, CLAUDIAN or CLAUDE CODE) while that day's daily note has nothing under **Sessions**? Added 27 Sep.
4. Every `#blocked`, `#next` and `#decision` item whose text carries a date inside the next seven days.
5. `Inbox/`: anything unprocessed (run [[INGEST]] first if there is).
6. The calendar and mail, when connected: run [[MAIL AND CALENDAR]] first. Until then, skip without comment.
7. [[Growth]]: the accepted threads and the suggested list, for the one suggestion line.

## Steps

1. If `Journal/Daily/<today>.md` does not exist, create it from `Templates/Daily note.md`.
2. If the **Plan** section already has content for today, update it in place. Never write a second plan.
3. Write the plan in the [[Chief of staff]] shape: the one thing today is for; two more if there is room; one risk or deadline inside seven days; one decision waiting on the operator; one line marked "Suggestion" (a day-to-day action relevant to the plan, or a nudge on an accepted [[Growth]] thread); missed runs, only if there are any; unexported sessions, only if there are any.
4. Pull "the one thing" from the top of [[Now]] unless yesterday's carry forward says otherwise, in which case say why it moved.
5. Add a **Due** line for any dated item inside seven days.
6. **Suggested priorities.** Under **Suggested priorities** in the daily note, write three to five tasks for today, most important first: a task that exists as `- <its words exactly, without tags> · [[<its note>]]`, or a one-off as `- <what to do>` only when a plan item has no task, each with an indented `- Why:` line. Yesterday's unfinished **Priorities** come first where they still matter, then the plan's one thing and two more. Replace the list if one is there. Never write in **Priorities**: that list is the operator's, and the platform's Suggested buttons copy lines into it.
7. **Unexported sessions.** If read 3 found sessions on a day whose daily note has no lines under **Sessions**, name them on their own line after Missed runs: "Unexported sessions: <time, job> ..., run [[SESSION EXPORT]] or tell the brain what was decided". Do not write the Sessions lines from the run log: that section records what a session exported, and a guess from a one-line log is not that.
8. **Approval decisions.** In [[Approvals]], execute rows with status `approved` (within [[Permissions]]; never a send, spend or delete), and set them to `done` with a note.
9. **Initiative.** Read [[State]] first. Under the strategy lens in [[Advisor]], raise at most one prompt the plan does not already cover (drift, slip, stale, contradiction, opportunity or risk), with its evidence, the recommended move and the cost of ignoring it, as the plan's last line marked "Initiative". Log it in [[Initiatives]]. Nothing worth raising is a fine answer; say nothing rather than filler. Added 23 Sep.
10. Write one line to [[Run log]] Latest: time, MORNING, surface, OK, and the number of items planned.

## Output

Six lines in the Plan section, the sixth being the suggestion. A seventh line for Missed runs and one more for Unexported sessions, each only when there is one. Three to five lines in Suggested priorities. Nothing else. The operator reads this on a phone before work, or at the desk at nine.

## Idempotent

Keyed on today's date and the job name. If [[Run log]] already has a MORNING line for today, the job has run: exit after re-checking that the plan exists.

## Done when

The daily note exists, the Plan section has content, and the run log has the line. If any of the three is missing, the job is not done and the run log line says FAILED with the reason.

## Never

- Puts anything from [[State]]'s "Asked, not answered" line into the plan or the suggested priorities, unless the operator has reopened it. A question seen three times is parked, not repeated.
- Invents a calendar. If the calendar is not connected, there is no calendar line.
- Adds tasks the operator did not create. Proposals are marked as proposals.
- Writes in **Priorities**. That list is the operator's; suggestions go in **Suggested priorities**.
- Writes more than the shape allows. Detail belongs in the notes it links to.
