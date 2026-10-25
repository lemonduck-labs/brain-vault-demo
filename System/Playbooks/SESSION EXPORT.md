---
title: SESSION EXPORT
aliases: [Session export, End of session, Export to the brain]
type: playbook
parent: "[[Operating manual]]"
owner: the operator
updated: 2026-10-14
tags:
  - system
  - playbook
---

# SESSION EXPORT

The last thing every session does, on every surface. The operator asked on 15 Sep for each chat's crucial actions and decisions to be exported into the vault so the brain learns from them. This is how.

## Trigger

The end of any Cowork, Claudian or Claude Code session that did work on any project, or when the operator says "export to the brain" or "/brain-export".

## Steps

1. **Build log entry.** Add a dated entry at the top of the project's build log, straight under its intro, so the newest entry is always first (create `<Project> build log.md` from the shape below if none exists):
   - Version or artefact, if any.
   - What was asked, in one line.
   - What was delivered, in plain terms.
   - What was ruled out, and why.
   - What is still open, as checkboxes tagged `#next`, `#blocked` or `#decision`.
   - Corrections the operator gave during the session, one line each (also copied to [[Corrections]]).
2. **Decisions.** Anything decided goes in the project note's Decisions section, dated, naming the rejected alternative. If it applies beyond the project, the Decisions Log in `Wiki/Fernmoor/` too.
3. **State.** If the project's state changed, overwrite the lines that changed in the project note's "State at a glance", in its row in [[Now]] and in [[State]]. Replace the old wording; never add "Update <date>:" after it. History belongs in the build log entry from step 1.
4. **Daily note.** Append one line to today's daily note under **Sessions**: time, project, what happened, a link to the build log entry.
5. **Profile.** If the operator said something about how they work or what they expect, one line in [[Operator]] "On the record", quoting them.
6. **Housekeeping.** Update every touched note's `updated` field. Check no wikilink points at a note that does not exist. Add any new note to `Wiki/Index.md`.
7. **Approvals.** Write any new proposals as `pending` rows in [[Approvals]], and execute `approved` rows within [[Permissions]], setting them to `done` with a note. The platform reads the vault, so nothing else needs syncing.
8. The [[Run log]] line, newest at the top of Latest, with the time read from the clock.
9. **Sync.** On the Mac, the vault reaches GitHub only while Obsidian is open. If it is not running, open it (`open -a Obsidian`) and say so; if `conflict-files-obsidian-git.md` has appeared, resolve it or tell the operator before ending.

## The entry shape

The same shape is kept in `Templates/Session entry.md`.

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

## Idempotent

If an entry for today and this session already exists in the build log, extend it rather than adding a second.

## Never

- Records a session's opinion as a decision. Decisions are the operator's.
- Skips the corrections. That is the part the brain learns from.
- Writes "done" for anything not verified in the session.
