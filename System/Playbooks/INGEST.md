---
title: INGEST
aliases: [Inbox processing, Capture processing, File the inbox]
type: playbook
parent: "[[Operating manual]]"
owner: the operator
updated: 2026-09-16
tags:
  - system
  - playbook
---

# INGEST

Empties `Inbox/` into the right places. Runs inside [[MORNING]] and [[EVENING]], and on demand with "process the inbox". Any role.

## What arrives

Anything the operator drops in: a quick note typed on the phone, a voice memo transcript, a meeting note, a chat export, a brand file, a PDF, a link with a line of context. The only rule for the operator is that it goes in `Inbox/`; the naming does not matter.

## Steps, per item

1. Read it whole.
2. Classify: project update, decision, task, lesson, correction, reference, journal, or file to keep.
3. Route:
   - Project update: append a dated entry to the project's build log, and update the project note's "State at a glance" if the state changed.
   - Decision: the project note's Decisions section, dated, with the rejected alternative if the operator gave one; otherwise a `> [!question]` asking what it ruled out.
   - Task: [[Now]] if it is a priority, otherwise the project note's Open threads, tagged `#next`, `#blocked` or `#decision`.
   - Lesson: the Lessons Log in `Wiki/Fernmoor/` for day job lessons, or the venture's own note for the operator's own work.
   - Correction: [[Corrections]].
   - Reference: the existing reference note if one fits, otherwise a new one in the right folder, following `Wiki/CLAUDE.md`.
   - Journal: today's daily note, Log section, marked as captured from the inbox with the time.
   - File to keep (brand assets, statements of work, contracts): stays in the vault only if it is plain `.md`; otherwise it is left in `Inbox/` and the project note gets a link to where the operator keeps the original, because the vault holds `.md` only.
4. Mark the item processed: add `processed: <date>` and `routed_to:` naming the note it went to, in its frontmatter (create frontmatter if the file has none).
5. Once the operator has given the one-time yes recorded in [[Now]], processed items are moved to `Inbox/Processed/`. Until then they stay where they are with the frontmatter mark.

## Output

A one-line summary per item in the run's daily note entry: what it was, where it went.

## Idempotent

An item with `processed:` in its frontmatter is skipped.

## Never

- Deletes anything from the inbox.
- Summarises so hard that the operator's words are lost. Their phrasing is kept where it carries a decision or a preference.
- Files something it could not classify. It goes in the daily note under "Unfiled" with a question.
