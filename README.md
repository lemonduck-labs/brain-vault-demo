# brain-vault-demo

A working copy of an Obsidian vault that runs as an AI operating system, filled with a fictional
business so it can be read in full. The vault is the single source of truth: Claude sessions,
scheduled cloud routines and a web platform all read and write the same Markdown files, under one
constitution (`CLAUDE.md`) and one set of permission tiers.

The business is invented: Fernmoor Home Group, a UK home improvement group with three brands
(Fernmoor Heating, Ridgeby Roofing, Warmstead), run day to day by "the operator", its head of growth,
who also runs a small consultancy (Owlbridge), a reporting platform (Gaugewell) and a print shop
(Paperwren). Every figure, lead and date is demo data and only has to agree with the rest of the vault.
The demo's "today" is Thursday 22 October 2026.

The platform that reads this vault is in `brain-platform-demo`.

## What is where

| Path | What it is |
|---|---|
| `CLAUDE.md` | The constitution: start and end of session, current text against history, what wins when notes or rules disagree, the rules never bent |
| `AGENTS.md` | A pointer to `CLAUDE.md` for agents that do not load it on their own |
| `Home.md`, `Now.md` | The front door and the ranked list with this week's three |
| `Growth.md`, `Revenue lever.md` | Goals and suggestions the operator accepts or strikes |
| `System/State.md` | One screen, overwritten, never appended: the current picture |
| `System/Permissions.md` | Four tiers: read, vault write, draft outside, act outside (a yes per action) |
| `System/Approvals.md` | The queue: requested, pending, approved, in progress, done, declined |
| `System/Corrections.md` | Every correction, and the rule or note it was promoted into |
| `System/Initiatives.md` | What the brain raised without being asked, with the evidence and the outcome |
| `System/Run log.md` | One line per job run, plus the expected schedule and known failures |
| `System/Agents/` | The team: a Director who triages and briefs, ten specialists who report back |
| `System/Playbooks/` | The jobs: MORNING, EVENING, WEEKLY, SESSION EXPORT, INGEST, TIDY, SCOUT, MANAGE and others |
| `System/Setup/` | How the parts fit: scheduled jobs, vault sync, the watcher lock, the leads area |
| `Journal/` | Daily notes (plan, priorities, log, review) and weekly reviews (direction, what moved, what slipped) |
| `Wiki/` | The project notes: hubs, build logs, decisions, lessons, the Owlbridge lead pipeline |
| `Templates/` | The note templates the jobs fill |
| `.claude/skills/` | Four Claude Code skills: load the brain, run a playbook, export a session, apply the strategy lens |

## How the loop runs

```
07:00  MORNING   reads State, Now, yesterday's review, the run log and the queue;
                 writes today's plan and suggested priorities; one initiative at most
 any   sessions  read CLAUDE.md, State, Corrections; work; SESSION EXPORT writes the trace
18:30  EVENING   reads the day's log and sessions; writes the review and carry-forward
 Sun   WEEKLY    rewrites Now, writes the week's direction, promotes corrections
```

Three ledgers make it learn: a correction that appears twice, or once with "always" or "never", is
promoted into a rule and the line says where; decisions are dated and name what they ruled out; the
operator's profile holds only what they said, quoted and dated, apart from Claude's own read.

Nothing is sent, published, spent or deleted without the operator's yes (`System/Permissions.md`).
The queue moves one way: only a decision, something only the operator can supply, or a blocker comes
back to them, always with a recommendation.

## Open it

Open the folder as a vault in Obsidian. With Claude Code, start a session in the folder: the skills in
`.claude/skills/` load the brain (`brain-start`), run a playbook (`brain-run MORNING`) and write the
session's trace (`brain-export`).

See `NOTICE.md` for terms and `PUBLIC.md` for how this copy was made and checked.
