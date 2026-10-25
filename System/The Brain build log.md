---
title: The Brain build log
aliases: [Brain build log, System build log]
type: log
owner: the operator
updated: 2026-10-22
tags:
  - system
  - log
---

# The Brain build log

What was built into the operating system itself, and the platform that reads it. Newest entry at the top. Each entry names what was decided and what was ruled out.

### 22 Oct 2026, routine times before the clocks go back (Cloud, Opus)

MORNING found the five routines scheduled in UTC with no reset listed before Sun 25 Oct. Raised as an initiative and row a-2026-10-22-routine-times, with the new UTC times written into [[Scheduled jobs]]. Changing a schedule is a standing configuration, so it is the operator's click. Ruled out: a routine that resets its own schedule, which would be a job changing its own permissions.

### 14 Oct 2026, the constitution revised (Claude Code, Opus)

At the operator's ask, after a week of contradictions: two kinds of text (current is overwritten, history is appended), what wins when notes disagree, what wins when rules pull against each other, and read 0 for cloud routines (check the newest `vault:` commit before planning). Prompted by four runs from 9 to 13 Oct that planned from a copy five days behind the Mac. Ruled out: a daily forced sync from the cloud side, which would need write access to the Mac.

### 5 Oct 2026, director report drafted from the Hub (Claude Code, Opus)

The Monday director report is drafted by the brain from the Hub's figures, all three brands, and the operator checks and sends it. Ruled out: sending it automatically, which is tier 3 in [[Permissions]].

### 27 Sep 2026, system review and lead gen station v2 (Cowork, Opus)

Two weeks in: the loop runs, the queue moves, and two things were slow. One, the operator answered approvals in chat and the rows never learned it: the watcher now reads [[Chat]]. Two, Owlbridge's pipeline lived in a spreadsheet: it moved into the vault as a table the platform reads and writes, with an activity log, drafts and a suppression list ([[Leads area]]).

### 24 Sep 2026, Departments, the Team view and the watcher lock (Claude Code, Opus)

Four lanes (owlbridge, fernmoor, brain, ventures) in [[Departments]], so the platform shows each agent's work by area. Two watcher runs had overlapped the day before, at 10:02 and 10:03 on 23 Sep, and wrote the same row twice: [[Watcher lock]] added, a claim and a release in a table, with a 90 minute expiry. Ruled out: a lock file outside the vault, which a cloud routine cannot see.

### 21 Sep 2026, the team of agents (Claude Code, Opus)

The brain works as a team: a [[Director]] who triages the queue, briefs specialists and reviews their work, and ten specialists who return reports and never write to the queue themselves. Set out in [[Team]] and [[MANAGE]]. Ruled out: every agent writing to the vault directly, which is how two runs had written the same row.

### 17 Sep 2026, cloud routines (Cowork, Opus)

MORNING and EVENING moved from the Mac to scheduled cloud routines working on the GitHub copy, so they run when the Mac sleeps. WEEKLY and SCOUT followed on 20 Sep. Each writes one line to [[Run log]].

### 15 Sep 2026, the approvals queue and the platform (Claude Code, Opus)

[[Approvals]] as one table with statuses, and the first version of the platform: a static site and one function that reads the vault from GitHub, shows tasks, the queue and today's note, and writes back with the file's sha so a job's edit is never overwritten.

### 14 Sep 2026, the vault becomes the operating system (Cowork, Opus)

The constitution, [[State]], [[Now]], [[Permissions]] (free inside the vault, drafts outside, a yes for anything that sends, spends, publishes, deploys or destroys), [[Corrections]] and the first playbooks. Ruled out: a separate task app, which would be a second source of truth.
