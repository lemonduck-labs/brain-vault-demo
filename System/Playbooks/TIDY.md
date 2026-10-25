---
title: TIDY
aliases: [Housekeeping, Vault tidy, Monthly clean]
type: playbook
parent: "[[Operating manual]]"
owner: the operator
updated: 2026-09-18
tags:
  - system
  - playbook
---

# TIDY

Keeps the vault sound. Runs on the first Sunday of the month at 07:30 as a cloud routine, or on demand. Any role. It fixes what is safe to fix, proposes the rest, and never deletes.

## Checks

1. **Broken wikilinks.** Every wikilink resolves to a note or an alias. Fix obvious typos; list the rest.
2. **Frontmatter.** Every note has `title`, `type`, `owner`, `updated`, `tags`; project notes have `status`; child notes have `parent`. Add what is missing where the value is certain; ask where it is not. A stale `updated` field is caught daily by [[EVENING]]'s own check; run the same comparison here and fold anything new into this section.
3. **Empty notes.** List them. Do not fill them with guesses.
4. **Stale notes.** Project notes with `status/active` and no update for 30 days: list them for the weekly note.
5. **Oversized notes.** A section past a screen wants its own note. Propose the split; do not do it without a yes, because it is a move.
6. **Duplicates.** Two notes on one subject, or a subject filed in two folders. Propose which becomes the note and which becomes a link.
7. **Run log.** Cut lines older than 60 days from Latest into the archive.
8. **Inbox.** Anything processed and awaiting the one-time move permission; anything unprocessed older than seven days.
9. **`_review/`.** List what is in it, with the date it was set aside, for the operator to decide.
10. **The map.** `Wiki/Index.md` and [[Home]] mention every folder and every project note.
11. **Wikilinks that could exist.** Scan every note for another note's title or alias appearing as plain text and list where a link could be added, leaving out names too common to be worth flagging. Pure text matching, no model. Propose the list; add a link only where it is genuinely useful, never applied blind.

## Output

A dated section in this month's first weekly note, "Tidy", with fixes made and proposals awaiting a yes. Fixes made are listed, not described.

## Idempotent

Keyed on the month and the job name. If the month's first weekly note already has a Tidy section, update it in place.

## Done when

The Tidy section exists in the month's first weekly note and the run log has the line.

## Never

- Moves, renames or deletes. Proposals only, per the ground rules.
- Rewrites content. It fixes structure.
