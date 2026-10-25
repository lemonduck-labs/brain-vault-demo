---
title: EVENING
aliases: [Evening review, Daily review job]
type: playbook
parent: "[[Operating manual]]"
owner: the operator
updated: 2026-10-14
tags:
  - system
  - playbook
---

# EVENING

Closes the day. Reads what the operator logged and what sessions exported, writes the review, and moves anything learned into its ledger. Runs 18:30 Monday to Friday as a cloud routine, or on demand. Role: [[Chief of staff]].

## Reads

0. **Is the copy whole and fresh?** As in [[MORNING]] read 0: stop and report on a conflict, and if the Mac's last `vault:` commit is more than a day old, the review says so and does not record a day as empty on the vault's evidence alone.
0b. **Duplicate frontmatter.** A union merge can leave a note with two `updated:` lines; keep the later date and delete the other.
0c. **Stale `updated` fields.** Compare each note's frontmatter `updated` date with the date of its last real change in git (`git log -1 --format=%cs -- <note>`), so a note edited without bumping its own date is not read as unchanged. List anything found in the review for a quick fix; do not fix it blind, because the field may be right and the note simply untouched. Added 18 Sep after [[Now]] read as unchanged on a day it was not.
1. Today's daily note: **Plan**, **Priorities**, **Log** (the operator's words), **Sessions** (what SESSION EXPORT appended).
2. [[Now]]: which items were ticked today.
3. `Inbox/`: run [[INGEST]] first if anything is waiting.
4. Build logs updated today (by `updated` date).
5. Mail, when connected: the "Needs the operator" and "Draftable" passes in [[MAIL AND CALENDAR]]. Until then, skip without comment.
6. [[Approvals]]: rows whose status changed since the last run, and the Notes section (its intake and rules are written there).

## Steps

1. If the **Review** section already has today's content, update it in place.
2. Against the plan and today's **Priorities**: what was done, what slipped. Use only what the Log, the Sessions, the build logs and ticked checkboxes show (a priority is done when its task, or its own checkbox, is ticked). If the operator wrote nothing and no session exported, the review says "No log today" and stops. It does not guess at the day.
3. Extract, if present in the log or the sessions: a decision (to the project note's Decisions, dated, with the rejected alternative), a lesson (to the Lessons Log), a correction (to [[Corrections]]). One line each, quoting the operator's words where they gave them.
4. Write **Carry forward**: unfinished plan items and unfinished priorities, in the operator's order unless they reordered them.
5. Tick items in [[Now]] that the log or sessions show as done, and move them to the review as "done today".
6. **Memory sweep.** Compare what Claude's account memory recorded today against the vault: any decision, correction, preference or project fact from today's conversations, on any surface, that the vault lacks is filed now through the routing in [[INGEST]], marked "from chat, <date>". Anything ambiguous goes in the review as a one-line question rather than being guessed into a note. If the run cannot read account memory at all, the review says "Memory sweep: no access" in one line, so a silent sweep is never mistaken for an empty day. Added 27 Sep.
7. **Notes.** Handle any note the watcher has not, exactly as the Notes section of [[Approvals]] sets out, and move the marker on.
8. **Approval decisions.** In [[Approvals]], execute rows with status `approved` (within [[Permissions]]: vault changes, drafts, prepared work; never a send, a spend or a delete, which are confirmed in chat only), set them to `done` with a one-line note, and leave `declined` rows alone for good.
9. **Propose, do not just report.** Anything the review surfaces that the brain can do itself (a note to update, a draft to prepare, a check to run) becomes a `pending` row in [[Approvals]] with what it costs and whether it is reversible, and is listed in the review under "Proposed".
10. **Nothing to sync.** The platform reads the vault directly; there is no separate store to update.
11. **State and initiatives.** Rewrite [[State]] from [[Now]], [[Approvals]], [[Needs from the operator]], today's review and the build logs, keeping its sections and staying under one screen. Overwrite lines; never add a dated paragraph. Keep its "Asked, not answered" line: a question seen in three plans without an answer goes on it, and comes off when the operator answers or reopens it. In [[Initiatives]], fill the response column for prompts raised in the last seven days from what the operator did (acted, answered, struck, or ignored once seven days pass), never guessed. Then keep the live files short: move `done` and `declined` rows in [[Approvals]] settled more than three days ago to `System/Archive/Approvals YYYY-MM.md`, and [[Run log]] lines older than three days (except each job's latest line) to `System/Archive/Run log YYYY-MM.md`, unchanged. Added 23 Sep.
12. Write one line to [[Run log]].

## Output

The Review section in three short parts, Done, Slipped, Learned. Then Carry forward. A plain list beats prose here.

## Idempotent

Keyed on date and job name. Ledger entries are checked for an existing line with the same date and gist before writing.

## Done when

Review and Carry forward exist, the ledgers have any new lines, and the run log has the line.

## Never

- Rewrites the operator's Log. Their words stay exactly as typed.
- Marks something done that only the plan mentioned.
- Adds a "reflection" the operator did not write. The brain reviews; the operator reflects if they want to.
