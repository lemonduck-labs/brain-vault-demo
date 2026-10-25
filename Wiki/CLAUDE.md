---
title: Wiki rules
aliases: [Wiki CLAUDE, Wiki writing rules]
type: reference
owner: the operator
updated: 2026-10-14
tags:
  - domain/process
---

# Wiki rules

The wiki side of the vault: projects, ventures and plans. Read this before writing a note anywhere under `Wiki/`. The rules that never bend, what wins when notes disagree, and the permission tiers are in the `CLAUDE.md` at the vault root; read that first. They are not repeated here, so there is one copy to keep right.

## The folder rule

Four folders, kept apart on purpose.

| Folder | What goes in it |
|---|---|
| `Fernmoor/` | The day job: Fernmoor Home Group and its three brands (Fernmoor Heating, Ridgeby Roofing, Warmstead), the Fernmoor Hub, the CRM rebuild, the call note pipeline, the weekly director report, the ad and tracking notes. |
| `Gaugewell/` | Gaugewell, the operator's own reporting platform. Its own folder because of its depth. |
| `Ventures/` | The operator's side ventures: Owlbridge (the consultancy, with `Owlbridge/` and its `Owlbridge growth/` lead gen folder) and Paperwren. A venture earns its own folder when it passes about five notes. |
| `Strategy/` | Plans that span everything: the twelve month plan. |

`Index.md`, `_Project template.md` and this file are the only notes above the four.

A note belongs to one folder. If something serves both the day job and the operator's own work, it is two notes, one written for each reader. Cross-links are fine; mixing the files is not. Fernmoor is employer work and everything else is the operator's own: nothing from Owlbridge, Gaugewell or Paperwren goes into a note a Fernmoor colleague might read, and no Fernmoor figure leaves Fernmoor except as an anonymised Gaugewell trial export the managing director has agreed to.

## Writing

The root rules (British English, no em dashes, no invented numbers, date what you check, the operator's view kept apart from Claude's) apply. On top of them:

- Direct and plain. Plain topic headers, never slogans.
- Roles, never names: the managing director, the sales manager, the call-team lead, the finance lead, the installs manager, the CRM contractor.
- Mark what you could not verify with `> [!question]` rather than filling the gap.
- Advice carries a confidence tag: [Certain], [Likely] or [Guessing].
- **Current text is overwritten, history is appended.** "State at a glance", frontmatter `stage` and `status`, and open-thread checkboxes say how things stand now: replace a line when its fact changes, never add "Update 9 Oct:" after it. Build logs, decisions and lessons are added to and never rewritten.
- Ad figures come from the [[Fernmoor Hub]] and nowhere else (the correction of 18 Sep, in [[Corrections]]).

## Note shape

Frontmatter on every note: `title`, `aliases`, `type`, `owner`, `updated`, `tags`. Add `parent` on any child note, pointing at its hub. `updated` changes whenever the note does. If a merge leaves two `updated:` lines, keep the later date and delete the other.

- `type`: `project`, `log`, `reference`, `index`, `spec`, `list`, `draft`, `meeting`, `report`, `template`
- `status` on project notes: `idea`, `build`, `pre-launch`, `live`, `paused`, `closed`
- Tags: `project/<name>`, `venture/<name>`, `domain/<field>`, `status/active`

Structure: H1 matching the title, then one or two sentences saying what the note is for, then the body. A project note is a hub, not a document dump: its "State at a glance" table is a handful of short current lines, and anything longer belongs in the build log.

**Build logs** put the newest entry at the top, straight under the intro, with a `###` heading that starts with the date: `### 21 Oct 2026, <what> (<surface>, <model>)`.

Callouts carry what prose loses: `> [!important]` the bet or the decision, `> [!warning]` what breaks, `> [!danger]` an unsolved problem, `> [!note]` context, `> [!question]` unverified.

Decisions are dated and name what they ruled out. A decision without a rejected alternative is not a decision.

Open threads are checkboxes tagged `#blocked`, `#next` or `#decision`, so the platform and a search pull them across projects. A due date goes in the words ("by Fri 23 Oct"). When a thread is done, tick it and say where the work went. The ranked, cross-project list is [[Now]].

Fernmoor work that is not yet a thread in a project note goes in [[Fernmoor tasks]], under its brand. The platform's Fernmoor tab adds lines there.

New project: copy `_Project template.md`. Every project gets a build log alongside it.

## If you change a note

Update its `updated` field, and update [[Index]] if you added or renamed one. Check that no wikilink points at a note that does not exist. At the end of the session, run [[SESSION EXPORT]].
