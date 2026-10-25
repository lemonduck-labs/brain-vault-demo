---
title: Agent delegation design
aliases: [Several watchers, Watcher that hands work to agents, Dispatcher design]
type: spec
parent: "[[Scheduled jobs]]"
owner: the operator
updated: 2026-09-24
tags:
  - system
  - spec
---

# Agent delegation design

For a-2026-09-21-agent-delegation in [[Approvals]]. The operator, 21 Sep: they want the brain working at the upper end of delivery, and asked for a design, not a build, choosing between separate watchers per lane and one watcher that hands each piece of work to a specialist agent. Written 21 Sep by the approvals watcher; the lock section was brought up to date on 24 Sep. Everything below the first section is Claude's view unless it says otherwise.

## The biggest risk first

[Certain] Either shape multiplies the problem that already cost the most: two runs picking up the same row and building it twice. Several watchers would make that more likely, not less, because every lane's watcher reads the same [[Approvals]] table. So no delegation is safe until every piece of work carries a claim. That part is now built: [[Watcher lock]] and `System/Setup/watcher-lock.py`, with a `--key` so one row can be locked rather than the whole queue, live since 24 Sep after two runs overlapped on 23 Sep.

## The two options

| | Separate watchers per lane | One watcher that dispatches |
|---|---|---|
| Shape | Owlbridge, Fernmoor, the brain and the ventures each get a routine reading only their rows | One routine triages the whole queue and starts one agent per piece of work, inside the same run |
| Duplicate builds | Four readers of one table; needs a row lock in every routine | One reader; the lock only has to stop two watcher runs overlapping |
| Routine runs | Each lane's run counts against the daily cap ([[Tools]]), so four lanes on a two-hourly weekday schedule would pass the cap before any start from the platform | One run per start |
| Parallel work | Yes, across lanes | Yes, agents run side by side inside one run |
| Failure | A stuck lane does not block the others | A run that hits the usage limit stops every lane at once |
| Change cost | Four prompts to keep in step, each pasted by hand | One prompt |

## Recommendation

[Likely] One watcher that dispatches, with lanes as departments rather than as routines. It keeps one reader of the queue, stays inside the run cap, and matches the rule the operator set on 17 Sep in [[Tools]]: the main session leads, briefs each sub-agent with everything it needs, checks what comes back, and is the only thing that writes to the vault. Separate watchers are worth revisiting only if one lane's work starts to crowd out the others inside a single run. The operator said go on 21 Sep; the run is [[MANAGE]] and the team is [[Team]].

How a run works:

1. **Triage** (the Director). Read the queue, claim the run, then sort the work into the lanes in [[Departments]] and the roles in `System/Agents/`: each agent file's `goals` and `tools` frontmatter say which rows it serves. The platform's Team view reads the same files, so a new agent file is a new role with no prompt change.
2. **Claim each row.** Before handing a row out, `watcher-lock.py claim --key <row id>`, so a Cowork session or a second run that reaches the same row stands down.
3. **Dispatch.** One agent per job, in parallel when the jobs are independent. The brief carries the row, the note paths to read and the shape of the answer; the agent never writes to [[Approvals]].
4. **Hand over through the vault.** An agent that needs another's output reads it where the first one wrote it. No agent-to-agent messages outside the vault, so nothing happens that the vault cannot show.
5. **Check and write.** The Director reads each result against its source (a reported push is not a push until GitHub shows it), writes the row note and the run log line, and releases every key and the run lock in its last commit.

## Usage cost per run

> [!question] No per-run usage figure is recorded in the vault, so none is given here. What is known: routines draw on plan usage, and the plan caps routine runs a day ([[Tools]]). Dispatching does not add routine runs, but each agent draws usage for its own reading, so a run with five agents costs more than one run doing the same work in sequence wherever the briefs repeat reading. Measure three ordinary runs and write the figures here.

## What is not decided

- Whether the Director itself could drop to a lighter model once specialists do the building. The operator's call.
- Where a role's standing instructions live. Settled 21 Sep: in each agent file, because it is read on every run, while a routine prompt only changes when pasted.

## Related

[[Watcher lock]] · [[Scheduled jobs]] · [[Tools]] · [[MANAGE]] · [[Team]]
