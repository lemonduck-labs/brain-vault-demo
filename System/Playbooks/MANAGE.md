---
title: MANAGE
aliases: [Director playbook, Management run, Delegation run]
type: playbook
parent: "[[Operating manual]]"
owner: the operator
updated: 2026-09-27
tags:
  - system
  - playbook
---

# MANAGE

The Director's run: read the queue, give each piece of work to the right specialist, check what comes back, and write it up. The operator asked on 21 Sep for the brain to work as an internal business team, with designers, developers, marketers, strategists, organisers and researchers, and one manager who delegates. It is what the approvals watcher routine runs. The design it follows is [[Agent delegation design]]; the team is [[Team]].

## The rules that do not bend

1. **One writer.** Only the [[Director]] writes to [[Approvals]], [[Run log]], [[Needs from the operator]] and the task notes. Specialists return their work to the Director; they never edit those files.
2. **Claim before work.** Nothing is handed out until the run holds the queue lock and a key per row (`watcher-lock.py claim` and `claim --key <row id>`, ledger in [[Watcher lock]]). A row someone else has claimed is skipped, not shared.
3. **A report is not a result.** The Director checks every result against its source before writing it down: the file exists, the branch is on GitHub, the figure is in the source it names. What cannot be checked is written as unchecked.
4. **Specialists stay in scope.** A specialist does the row as briefed and nothing next to it. Anything extra it finds comes back as a suggestion for a new row.
5. **Nothing leaves the building.** No send, spend, publish, delete, live campaign change, merge to main or account setting, by anyone on the team. Those become pending rows for the operator.
6. **House rules.** British English, no em dashes, no invented numbers, confidence tags on judgements ([Certain], [Likely], [Guessing]).

## Steps

1. **Claim.** Claim the run lock. If another run holds it, write the run log line "Stood down: <run> holds the lock" and stop.
2. **Read the work.** The Queue and Notes sections of [[Approvals]], `System/Chat.md`, and the operator's ticks and replies in [[Needs from the operator]]. If nothing is approved, requested or in progress, and no note or chat is waiting, write "Nothing waiting" in the run log and stop. Most runs end here, so keep it cheap.
3. **Triage.** For each workable row, in priority order (P1 first, then oldest):
   - Set its department if blank (`owlbridge`, `fernmoor`, `brain`, `ventures`) from [[Departments]].
   - Decide whether it needs the operator first: a real choice, a cost, or an action only they can take goes to `pending` with the choice named. An access block stays `in progress` with "Needs: <what>". A request that needs neither is work now.
   - Break the work into the smallest set of specialist jobs and the order they run in. One job per specialist per row; a row may need several (for example Researcher, then Strategist, then Copywriter).
4. **Brief.** For each job, a brief with: the row id and title; what done looks like; the vault notes and repositories to read (paths, not summaries); the shape of the answer; what it must not do; the time box. Specialists start with nothing but the brief, so the brief carries everything.
5. **Dispatch.** Claim a key per row, then start each specialist as a sub-agent on Opus (inherit the run's model; never a smaller one). Its prompt opens: "You are the <Role> on the operator's internal team. Read CLAUDE.md and System/Agents/<agent file>.md, your standing brief, then do only this job", followed by the brief from step 4 and the house rules. Jobs that do not depend on each other run in parallel; a job that needs another's output waits for it. At most five specialists at once, so one run cannot use up the day's allowance. Specialists never commit to the vault or edit [[Approvals]], [[Run log]] or [[Needs from the operator]]; the Developer alone may push a `claude/` branch in the code repository named in its brief.
6. **Review.** The [[Reviewer]] checks every result before anything is written: sources, figures, house rules, scope, and whether it answers the row. A result that fails goes back to its specialist once with the Reviewer's note. If it fails again, the row stays `in progress` with what is wrong.
7. **Write up.** For each row: put the work where the brief said (the project note, a draft, a branch), then add a dated clause to the row note in the usual shape ("Est: ...; <date> <time>, DIRECTOR: <who did what, where it is, what is left>"), and set the status. Code goes to the operator as "Waiting on you: review and merge" with the pull request link.
8. **Log.** One run log line, job `DIRECTOR`, opening with the tag the platform reads: `[dept=<d,...>; agents=<Role,...>; rows=<id,...>; done=<n>; moved=<n>; blocked=<n>]`, then a plain sentence.
9. **Release and save.** Release every key and the run lock in the last commit, and save on a `claude/` branch as the routine's SAVING clause sets out ([[Scheduled jobs]]).
10. **Tell the operator.** One short message: what the team finished, what waits for their yes, anything that went wrong.

## Who gets what

| Work | First specialist | Often followed by |
|---|---|---|
| Plans, pricing, positioning, offers, go or no-go | Strategist ([[Advisor]]) | Researcher before, Copywriter after |
| Markets, competitors, prospects, facts with dates | [[Researcher]] | Analyst or Strategist |
| Numbers, campaign performance, Hub figures, forecasts | [[Analyst]] | Strategist |
| Campaign plans, channels, audiences, search and content plans, ad structures | [[Marketer]] | Copywriter, Designer |
| Copy, emails, scripts, reports, site words | Copywriter ([[Editor]]) | Reviewer |
| Brand, UI, layouts, visuals, mockups | [[Designer]] | Developer |
| Code in the platform, the Hub or Gaugewell | Developer ([[Builder]]) | Reviewer |
| Working the Owlbridge pipeline: follow-ups, call briefs, new researched leads ([[LEADGEN]]) | [[SDR]] | Copywriter for tone, Reviewer |
| The queue, the day, the week, what the operator owes | Organiser ([[Chief of staff]]) | |
| Checking any of the above before it is written | [[Reviewer]] | |

## Standing rows

A row whose note starts "Standing:" is never set to done or pending by the three-runs rule. The Director works it as its playbook says (for a-2026-09-27-owlbridge-sdr-standing, [[LEADGEN]]: the sweep at most once a day, the batch on Mondays) and rewrites its note only when something moved. When there is nothing for it to do today, the run only reads the Owlbridge pipeline and activity log to confirm that, changes nothing, and says "standing row: nothing due" in the run log line. Added 27 Sep.

## Idempotent

Keyed on the run id. A row already claimed by a live run is skipped, and a row whose note already carries today's DIRECTOR clause for this run is not written again.

## Done when

Every claimed row has a new dated clause and a status, the run log line carries the tag, and every key and the run lock are released.

## Never

- Does a specialist's work itself when a specialist exists for it.
- Writes a result the Reviewer did not pass, unless it is marked unchecked.
- Lets any role send, spend, publish, merge or delete.

## Related

[[Team]] · [[Agent delegation design]] · [[Watcher lock]] · [[Approvals]] · [[Departments]]
