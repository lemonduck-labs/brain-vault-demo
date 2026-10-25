---
title: NEW PROJECT
aliases: [New project, Start a project, Project intake]
type: playbook
parent: "[[Operating manual]]"
owner: the operator
updated: 2026-09-16
tags:
  - system
  - playbook
---

# NEW PROJECT

How a new venture, product or piece of work gets a home. Any role.

## Steps

1. **Which side.** Fernmoor work goes in `Wiki/Fernmoor/`. The operator's own goes in `Wiki/Ventures/`, or its own folder once it passes about five notes, as [[Gaugewell]] has. Never both: if something serves both, it is two notes, one for each reader.
2. **The note.** Copy `Wiki/_Project template.md` to `<Name>.md`. Fill the frontmatter: `status` (`idea`, `build`, `pre-launch`, `live`, `paused`, `closed`), `started`, and `tags` with `project/<name>`.
3. **The five questions.** Ask the operator, in one message, with a guess at each answer for them to correct:
   - What is it, in one line a stranger would understand?
   - What is the bet, and when was it settled?
   - What is it blocked on right now?
   - What is the next thing to build or do?
   - What is the commercial model, even roughly?
4. **The build log.** Create `<Name> build log.md` with a first dated entry saying the project was opened and what came in with it.
5. **The map.** Add a row to `Wiki/Index.md` and to the ranking in [[Now]]. Link the note from the relevant hub ([[Fernmoor]], [[Owlbridge]] or [[Gaugewell]]).
6. **Intake list.** If material exists elsewhere (brand files, statements of work, documents, chats), list what is expected and where it should land, as `#blocked` items on the operator.

## Idempotent

If a note with the name already exists, the playbook stops and asks whether this is the same project.

## Done when

The project note, its build log, the Index row and the Now row all exist.

## Never

- Fills the template with plausible text. Empty sections with a question beat invented ones.
- Files a venture under Fernmoor or Fernmoor work under a venture.
