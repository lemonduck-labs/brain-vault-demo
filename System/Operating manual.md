---
title: Operating manual
aliases: [How the brain works, The loop, Brain OS]
type: system
owner: the operator
updated: 2026-10-14
tags:
  - system
---

# Operating manual

How the Brain runs as an operating system rather than a filing cabinet. Read this when you are about to run a job, change a job, or wonder why something is where it is.

> [!abstract] In one line
> A loop that captures what the operator is doing, keeps one ranked list of what matters, does the routine work unattended, and turns every correction the operator gives into a rule the next session follows.

## What it means, and what it does not

It means: the brain reads the vault before acting, keeps the list, writes the morning plan, does the routine reading and drafting, runs the checks, prepares the decisions, and carries out the work the operator approves. It carries the context so the operator does not have to.

It does not mean: sending, spending, publishing or deploying on its own. Those wait for the operator's yes, every time. See [[Permissions]]. It also does not mean pretending to know. A gap is marked, not filled.

## The loop

Six moves, each with a home in the vault.

| Move | What happens | Where it lands | Who |
|---|---|---|---|
| **Capture** | Anything raw: a thought, a meeting, a voice memo transcript, a chat export, a file | `Inbox/` | The operator, any device |
| **Process** | [[INGEST]] reads the inbox, files each item into the right note as a dated entry, and marks it processed | Project notes, journals, ledgers | The brain |
| **Direct** | [[MORNING]] writes today's plan from [[Now]], yesterday's carry-over and anything due. [[WEEKLY]] rewrites the ranking and writes the direction | `Journal/Daily/`, `Journal/Weekly/`, [[Now]] | [[Chief of staff]] |
| **Execute** | Sessions and the Director's team do the work: build, analyse, draft, research. Every session ends with [[SESSION EXPORT]] | Project notes and build logs | All roles |
| **Review** | [[EVENING]] reads what the operator logged and what sessions exported, and writes the review: done, slipped, learned | `Journal/Daily/` | The brain |
| **Learn** | Corrections, decisions and lessons go into their ledgers. Twice is a pattern: promoted to [[Principles]] or the constitution | [[Corrections]], Decisions, Lessons, [[Operator]] | The brain, with the operator's yes on rule changes |

## The surfaces

The brain is one set of files read by several kinds of session. They share nothing but the vault, so anything a session learns has to be written into the vault, not only into one surface's own memory, before another surface can know it ([[Vault sync]]).

| Surface | What it is for | Reaches |
|---|---|---|
| **Claude Code on the Mac** | Builds: the [[Fernmoor Hub]], the brain platform, [[Gaugewell]]; anything that needs the Mac's files or the code clones | The vault on the Mac, the code clones, the browser |
| **Cowork** (the Claude desktop app with the vault folder connected) | Connector work: mail drafts once connected, documents, design tools, research | The vault on the Mac, the connectors, the web |
| **Claudian** (inside Obsidian) | In-vault editing and quick jobs on the note in front of the operator | The vault |
| **Cloud routines** | The loop while the Mac sleeps: MORNING, EVENING, WEEKLY, SCOUT, TIDY, BOARD REVIEW and the approvals watcher, which runs the Director. They work on the GitHub copy and push `claude/` branches that an Action merges into main | The GitHub copy, the platform and Hub repositories, the web, no connectors |

How each surface loads the brain: Claude Code and Claudian read the root `CLAUDE.md` because the vault is their working directory, and Claude Code has the four skills in `.claude/skills/` (`brain-start`, `brain-run`, `brain-export`, `strategy-lens`). Other agents read `AGENTS.md`, which sends them to `CLAUDE.md`. The routines' prompts tell them to read `CLAUDE.md` and their playbook first ([[Set up the cloud routines]]). The Mac's copy reaches GitHub only while Obsidian is open.

Fernmoor's ad figures, all three brands, come from the [[Fernmoor Hub]], never from a third-party connector, on every surface.

## The jobs

| Job | Playbook | When (UK time) | Surface | Writes to |
|---|---|---|---|---|
| Morning plan | [[MORNING]] | 07:00 Mon to Fri | Cloud | Today's daily note, [[Run log]] |
| Evening review | [[EVENING]] | 18:30 Mon to Fri | Cloud | Today's daily note, ledgers, [[Now]] ticks, [[State]] |
| Weekly direction | [[WEEKLY]] | Sunday 17:00 | Cloud | The weekly note, next week's suggested priorities, [[Now]], [[Operator]], promotions |
| Scout | [[SCOUT]] | Mon, Wed, Fri 12:00 | Cloud | [[Scout]] |
| Approvals watcher and DIRECTOR | [[MANAGE]] | Every two hours 08:00 to 20:00 Mon to Fri, and when the platform starts it | Cloud | [[Approvals]], [[Needs from the operator]], [[Run log]], branches in the code repositories |
| Owlbridge pipeline | [[LEADGEN]] | Inside the Director's runs, as a standing row | Cloud | The Owlbridge pipeline and activity log |
| Tidy | [[TIDY]] | First Sunday of the month, 07:30 | Cloud | Link and frontmatter fixes, proposals |
| Board review | [[BOARD REVIEW]] | First Monday of the month | Cloud | Each venture's project note, the weekly note |
| Inbox processing | [[INGEST]] | Inside MORNING and EVENING, and on demand | Any | Project notes, journals |
| Session export | [[SESSION EXPORT]] | End of every session | Any | Build log, daily note, decisions, [[Corrections]], [[Now]], [[State]] |
| Mail and calendar | [[MAIL AND CALENDAR]] | Inside MORNING and EVENING, once connected | Any | Plan and review lines, mail drafts |
| Correction | [[CORRECTION]] | The moment the operator corrects something | Any | [[Corrections]], and a promotion when it says always or never |
| New project | [[NEW PROJECT]] | When a new piece of work needs a home | Any | The project note, its build log, the Index, [[Now]] |

The routines are scheduled in UTC, so from Sunday 25 Oct, when the clocks go back, each runs an hour earlier by the wall clock until its time is reset. The timetable is in [[Scheduled jobs]]; the instructions pasted into each routine are in [[Set up the cloud routines]].

## The team

Since 21 Sep the approvals watcher runs a Director and a team of specialists rather than doing every job itself: [[Team]] for who does what, [[Departments]] for the lanes, [[MANAGE]] for how a run goes, [[Watcher lock]] for how two runs are kept off the same row.

## How learning actually works

Four ledgers and one promotion rule. Nothing else counts as learning.

1. **[[Corrections]].** One dated line per correction: what the brain did, what the operator wanted instead. [[WEEKLY]] reads the ledger. A correction that has appeared twice, or once with "always" or "never", is promoted: into [[Principles]] if it is a judgement rule, into the root `CLAUDE.md` if it is a hard rule (with the operator's yes), into the brand or project note if it is specific to one. The ledger line records where it went.
2. **Decisions.** Dated, in the project note, naming the rejected alternative. The ones whose reasoning travels go to the Decisions Log in `Wiki/Fernmoor/`.
3. **Lessons.** What went wrong, the cause, the rule, in the Lessons Log.
4. **[[Operator]].** The profile. Only things the operator has said, quoted and dated. Claude's read is kept in its own section, labelled, and never quietly merged into theirs.

What is deliberately not learning: inferring a preference from one instance, rewriting the profile from tone, or changing a rule because a session found it inconvenient.

## Source of truth

- **The current picture**: [[State]], one screen, overwritten rather than appended. Every session reads it second.
- **Tasks**: [[Now]] and the checkboxes in project notes. The CRM's task list and any other tracker are mirrors or feeds, never masters. If an item lives only elsewhere, [[Now]] carries a one-line pointer to it.
- **Project state**: the project note's "State at a glance", overwritten when a fact changes. Build logs hold the history, newest entry at the top. When the two disagree, the build log's newest entry wins.
- **Code**: the repository. The vault describes, it does not duplicate.
- **Figures**: the source named next to the figure. A figure with no source is a gap, not a fact.

## Reliability

Every job writes one line to [[Run log]] when it finishes, and one line when it fails if it can. [[MORNING]] checks that yesterday's expected lines exist. A missing line is reported at the top of the plan as a missed run, so a dead scheduler is visible within a day rather than discovered when a brief does not turn up. If a job fails three times in a row, the fix goes into [[Now]] as a `#next` item, not into a note nobody reads.

## Idempotency

Every job checks for its own output before writing. Today's plan already there: update it, do not append a second. A build log entry for this session already there: extend it. A run log line already there: leave it. The check is by date and job name, never by memory of what probably ran.

## Failure modes to watch

- **A stale copy.** A cloud run planning from a vault the Mac has not synced. The newest `vault:` commit is the tell (9 to 13 Oct).
- **Bloat.** New notes for things that belong as a section in an existing one. A section that outgrows a screen earns a note; nothing smaller does.
- **Stale [[Now]].** If the ranking has not changed in three weeks, either nothing happened or nobody updated it. [[WEEKLY]] says which.
- **Silent job death.** Covered above. The run log is the tell.
- **Invented certainty.** A "done" nobody verified. Read state back, never trust the confirmation.
- **Two masters.** A task edited in the CRM and in [[Now]] to different states. The vault wins, and the difference is logged.

## Related

[[Operator]] · [[Principles]] · [[Permissions]] · [[Corrections]] · [[Run log]] · [[Scheduled jobs]] · [[Vault sync]] · [[Home]] · [[Tools]] (which model for which job)
