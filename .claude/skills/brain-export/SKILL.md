---
name: brain-export
description: Run the SESSION EXPORT playbook at the end of any session on the operator's work, writing decisions, delivered work, rejected alternatives, open items and corrections into this vault so the Brain learns from the session.
---

# Brain export

The last thing every session does. The operator asked for each session's crucial actions and decisions to be exported into the vault so the brain learns from them. Use it when they say "export to the brain", "/brain-export", or when a session that did work on any project is ending.

The vault root is the working directory. The full playbook is `System/Playbooks/SESSION EXPORT.md`; read it first, then do the following. Edit files in place with the Edit tool or careful appends, never by retyping a whole note from memory.

## Steps

1. **Build log entry.** Add to the project's build log (`<Project> build log.md` beside the project note; create it if missing) a dated entry at the top, straight under the intro, in the shape kept in `Templates/Session entry.md`:

   ```
   ### DD Mmm YYYY, <session title or surface>

   **Asked:** one line.
   **Delivered:** what exists now that did not this morning. Version if any.
   **Ruled out:** what and why.
   **Open:**
   - [ ] item #next
   - [ ] item #blocked
   **Corrections:** none, or one line each.
   ```

   If an entry for today and this session already exists, extend it; never add a second. Changes to the brain itself go in `System/The Brain build log.md`.
2. **Decisions.** Anything decided goes in the project note's Decisions section, dated, naming the rejected alternative. If the reasoning applies beyond the project, also `Wiki/Fernmoor/Decisions Log.md`.
3. **State.** If the project's state changed, overwrite "State at a glance" in the project note, the project's row in `Now.md` and the line in `System/State.md`. Replace the old wording; never add "Update <date>:".
4. **Daily note.** Append one line under `## Sessions` in `Journal/Daily/<YYYY-MM-DD>.md` (create it from `Templates/Daily note.md` if missing): time from the clock, project, what happened, a link to the build log.
5. **Corrections.** Every correction the operator gave in the session becomes one line in the live ledger of `System/Corrections.md`: date, where, what was done, what they want instead, promoted-to blank (or filled, if they said always or never and it was promoted now).
6. **Profile.** If the operator said something about how they work or what they expect, one quoted, dated line in `System/Operator.md` under "On the record".
7. **Approvals.** New proposals as `pending` rows in `System/Approvals.md`; approved rows carried out within `System/Permissions.md` and set to `done` with a note.
8. **Run log.** One line in `System/Run log.md` Latest: time from `date`, CLAUDE CODE, OK, what was exported.
9. **Housekeeping.** Update the `updated` field of every touched note; check no wikilink points at a missing note; add any new note to `Wiki/Index.md`.
10. **Sync.** The vault reaches GitHub only while Obsidian is open. If it is not running, open it (`open -a Obsidian`) and say so.

## Rules

- British English, no em dashes anywhere.
- Decisions are the operator's. A session's opinion is recorded as Claude's, labelled.
- Never write "done" for anything not verified in the session.
- Never move, rename or delete a note.
