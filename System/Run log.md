---
title: Run log
type: log
owner: the operator
updated: 2026-10-22
tags:
  - system
  - log
---

# Run log

One line per automated run, written when the run finishes, and one when it stops if it can. A job that was due and has no line is a missed run; MORNING names it at the top of the plan. Sessions write a SESSION line when they export.

Format: date and time (Europe/London), job, surface, result (OK, PARTIAL or FAILED), note. Newest first. DIRECTOR lines open with a tag naming the department, the agents, the [[Approvals]] rows touched and what happened to them. The Director runs inside the approvals watcher, so a slot with Director work is logged as DIRECTOR and quiet slots as APPROVALS WATCHER. Only the Director writes here.

## Latest

| When | Job | Surface | Result | Note |
|---|---|---|---|---|
| 2026-10-22 10:52 | SESSION | Claude Code | OK | [dept=fernmoor; agents=Claude] Warmstead: the 47 leads checked against the CRM, the channel split read from the Hub, the budget step set up as a pending row (a-2026-10-21-warmstead-cpl-read). [[Warmstead build log]] |
| 2026-10-22 08:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. No row at approved or requested; no note commits since the last run. |
| 2026-10-22 07:03 | MORNING | Cloud | OK | Mac's last `vault:` sync 21 Oct 21:30, fresh. No missed runs. Plan: the Warmstead step (three days overdue), task types by tomorrow, the two Owlbridge replies. Initiative: routine times before the clocks go back, raised as a-2026-10-22-routine-times. |
| 2026-10-21 20:30 | SESSION | Claude Code | OK | [dept=ventures; agents=Builder] Gaugewell: exports or the Hub's API written up for the operator's decision. [[Gaugewell build log]] |
| 2026-10-21 20:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Lock claimed and released; no row moved. |
| 2026-10-21 18:36 | EVENING | Cloud | OK | Review from the Log and three sessions. Done: PR 41 merged, Ridgeby restructure live, PR 40 reviewed, the step set up. Slipped: the Warmstead decision, task types. |
| 2026-10-21 18:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Queue unchanged; [[Chat]] has no new message. |
| 2026-10-21 16:02 | DIRECTOR | Cloud | OK | [dept=fernmoor; agents=Reviewer; rows=a-2026-10-19-hub-pr-review; done=0; moved=0; blocked=0] PR 40 read against the live Hub: two field names in the handover note differ from the CRM's, so two small fixes. PR 42 next. |
| 2026-10-21 15:00 | SESSION | Claude Code | OK | [dept=fernmoor; agents=Builder] Hub PR 42: Warmstead survey outcome on the weekly view, open. [[Fernmoor Hub build log]] |
| 2026-10-21 14:10 | DIRECTOR | Cloud | OK | [dept=fernmoor; agents=Analyst; rows=a-2026-10-21-warmstead-cpl-read; done=0; moved=1; blocked=0] Analyst briefed: confirm the 47 Warmstead leads in the CRM, as the managing director asked, and set out the channel split. The step set up as a pending row for the operator's yes. |
| 2026-10-21 12:30 | SESSION | Cowork | OK | [dept=fernmoor; agents=Marketer] Ridgeby Search restructure by job type launched by the operator. [[Fernmoor build log]] |
| 2026-10-21 12:05 | SCOUT | Cloud | OK | One finding as a new row in [[Scout]]: heat pump enquiries in the pilot area lean to Search over social. |
| 2026-10-21 12:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. No row at approved or requested; no note commits since the last run. |
| 2026-10-21 10:40 | SESSION | Claude Code | OK | [dept=fernmoor; agents=Builder] Hub PR 41: call note on the lead, rebased after PR 39, merged. [[Fernmoor Hub build log]] |
| 2026-10-21 10:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Lock claimed and released; no row moved. |
| 2026-10-21 08:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Queue unchanged; [[Chat]] has no new message. |
| 2026-10-21 07:02 | MORNING | Cloud | OK | Mac's last `vault:` sync 20 Oct 21:05, fresh. No missed runs. Plan: the call note on the lead, the Warmstead step set up, the Ridgeby restructure live. |
| 2026-10-20 20:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. No row at approved or requested; no note commits since the last run. |
| 2026-10-20 19:30 | SESSION | Claude Code | OK | [dept=owlbridge; agents=Researcher] Two leads scored in batch 2. [[Owlbridge build log]] |
| 2026-10-20 18:35 | EVENING | Cloud | OK | Review from the Log and four sessions. Done: handover checked, brief sent, PRs 38 and 39 merged, Hub review approved in chat. Slipped: the Warmstead CRM check. |
| 2026-10-20 18:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Lock claimed and released; no row moved. |
| 2026-10-20 16:50 | SESSION | Claude Code | OK | [dept=fernmoor; agents=Builder] Hub PR 40: CRM stage 1 field mapping, open. [[Fernmoor Hub build log]] |
| 2026-10-20 16:40 | DIRECTOR | Cloud | OK | [dept=fernmoor; agents=Editor,Analyst; rows=a-2026-10-20-crm-stage2-brief; done=1; moved=0; blocked=0] Stage 2 brief written in [[CRM rebuild]]: what is decided, the task types still to agree, what done looks like. The operator sent it the same afternoon. |
| 2026-10-20 14:30 | SESSION | Claude Code | OK | [dept=fernmoor; agents=Builder] Hub PR 39: weekly director report export, all three brands. [[Fernmoor Hub build log]] |
| 2026-10-20 14:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Queue unchanged; [[Chat]] has no new message. |
| 2026-10-20 12:10 | SESSION | Claude Code | OK | [dept=fernmoor; agents=Analyst] CRM stage 1 handover checked, two gaps noted for stage 2. [[CRM rebuild build log]] |
| 2026-10-20 12:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. No row at approved or requested; no note commits since the last run. |
| 2026-10-20 10:50 | SESSION | Claude Code | OK | [dept=fernmoor; agents=Builder] Hub PR 38: Ridgeby Search naming read ahead of the restructure. [[Fernmoor Hub build log]] |
| 2026-10-20 10:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Lock claimed and released; no row moved. |
| 2026-10-20 08:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Queue unchanged; [[Chat]] has no new message. |
| 2026-10-20 07:03 | MORNING | Cloud | OK | Mac's last `vault:` sync 19 Oct 19:48, fresh. No missed runs. Plan: CRM handover and the stage 2 brief (a-2026-10-20-crm-stage2-brief), Ridgeby naming, the report export. |
| 2026-10-19 20:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. No row at approved or requested; no note commits since the last run. |
| 2026-10-19 18:34 | EVENING | Cloud | OK | Review from the Log and one session. Done: report 09:00 unchanged, step agreed in principle, task types owner named, first Owlbridge reply. Slipped: the step itself, GDPR sign-off. |
| 2026-10-19 18:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Lock claimed and released; no row moved. |
| 2026-10-19 16:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Queue unchanged; [[Chat]] has no new message. |
| 2026-10-19 14:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. No row at approved or requested; no note commits since the last run. |
| 2026-10-19 12:30 | SESSION | Cowork | OK | [dept=fernmoor; agents=Claude] Week 42 report and the marketing meeting written up: Warmstead step agreed in principle. [[Marketing meeting 19 Oct 2026]] |
| 2026-10-19 12:05 | SCOUT | Cloud | OK | Two findings as new rows in [[Scout]]: roofing repair searches up after the weekend's wind; a retrofit competitor's survey offer ending this month. |
| 2026-10-19 12:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Lock claimed and released; no row moved. |
| 2026-10-19 10:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Queue unchanged; [[Chat]] has no new message. |
| 2026-10-19 08:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. No row at approved or requested; no note commits since the last run. |
| 2026-10-19 07:02 | MORNING | Cloud | OK | Mac's last `vault:` sync 18 Oct 20:15, fresh. No missed runs. Plan: marketing meeting 11:00 with the Warmstead step, report 09:00, the Hub review (a-2026-10-19-hub-pr-review). |
| 2026-10-18 17:05 | WEEKLY | Cloud | OK | Mac's last `vault:` sync 18 Oct 16:30, fresh. Week 42 reviewed; W43 created. Direction: the Warmstead step, CRM task types by 23 Oct, the call note on the lead. Stop: new Hub pull requests until the open ones are read. |
| 2026-10-18 15:00 | SESSION | Claude Code | OK | [dept=ventures; agents=Builder] Gaugewell report 3: leads by day, form fills only. [[Gaugewell build log]] |
| 2026-10-16 20:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Lock claimed and released; no row moved. |
| 2026-10-16 18:36 | EVENING | Cloud | OK | Review from the Log and three sessions. Done: proposal, GDPR pack with the managing director since 14:30, Quillmere check-in, PR 37. Slipped: nothing. |
| 2026-10-16 18:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Queue unchanged; [[Chat]] has no new message. |
| 2026-10-16 16:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. No row at approved or requested; no note commits since the last run. |
| 2026-10-16 15:20 | SESSION | Claude Code | OK | [dept=fernmoor; agents=Builder] Hub PR 37: calls per lead and time to first call, per brand. [[Fernmoor Hub build log]] |
| 2026-10-16 14:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Lock claimed and released; no row moved. |
| 2026-10-16 13:20 | SESSION | Cowork | OK | [dept=owlbridge; agents=Claude] Quillmere's first check-in; the owner offered two introductions. [[Quillmere Dental]] |
| 2026-10-16 12:06 | SCOUT | Cloud | PARTIAL | One finding as a new row in [[Scout]]. Two sources refused the fetch, so the retrofit pricing check was read through search only and tagged [Likely]. |
| 2026-10-16 12:02 | DIRECTOR | Cloud | OK | [dept=fernmoor; agents=Editor,Reviewer; rows=a-2026-10-16-call-note-gdpr; done=0; moved=0; blocked=1] GDPR pack drafted in [[Call note pipeline]]: an impact assessment, the retention period, the line for the call script. Blocked on the managing director's sign-off. |
| 2026-10-16 11:00 | SESSION | Claude Code | OK | [dept=fernmoor; agents=Builder] Call note pipeline proposed: metadata only until the GDPR sign-off. [[Call note pipeline]] |
| 2026-10-16 10:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Queue unchanged; [[Chat]] has no new message. |
| 2026-10-16 08:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. No row at approved or requested; no note commits since the last run. |
| 2026-10-16 07:03 | MORNING | Cloud | OK | Mac's last `vault:` sync 15 Oct 22:40, fresh. No missed runs. Plan: call note pipeline proposal, the GDPR pack, calls per lead. |
| 2026-10-15 20:15 | SESSION | Claude Code | OK | [dept=ventures; agents=Builder] Gaugewell report 2: CPL by brand and channel, spend matching the Hub. [[Gaugewell build log]] |
| 2026-10-15 20:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Lock claimed and released; no row moved. |
| 2026-10-15 18:34 | EVENING | Cloud | OK | Review from the Log and one session. Done: six second touches, the Ridgeby date set for 21 Oct. Slipped: nothing. |
| 2026-10-15 18:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Queue unchanged; [[Chat]] has no new message. |
| 2026-10-15 16:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. No row at approved or requested; no note commits since the last run. |
| 2026-10-15 14:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Lock claimed and released; no row moved. |
| 2026-10-15 12:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Queue unchanged; [[Chat]] has no new message. |
| 2026-10-15 11:00 | SESSION | Claude Code | OK | [dept=owlbridge; agents=SDR] Eight second touches checked: six sent, two held (one lost, one disqualified). [[Owlbridge build log]] |
| 2026-10-15 10:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. No row at approved or requested; no note commits since the last run. |
| 2026-10-15 08:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Lock claimed and released; no row moved. |
| 2026-10-15 07:02 | MORNING | Cloud | OK | Mac's last `vault:` sync 14 Oct 21:12, fresh. No missed runs. Plan: send the second touches, Gaugewell report 2, the Ridgeby restructure date. |
| 2026-10-14 20:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Queue unchanged; [[Chat]] has no new message. |
| 2026-10-14 18:35 | EVENING | Cloud | OK | Review from the Log and three sessions. Done: constitution revised, Obsidian at login, eight drafts, PR 36. Slipped: nothing. |
| 2026-10-14 18:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. No row at approved or requested; no note commits since the last run. |
| 2026-10-14 17:00 | SESSION | Cowork | OK | [dept=ventures; agents=Claude] Paperwren order count checked. [[Paperwren build log]] |
| 2026-10-14 16:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Lock claimed and released; no row moved. |
| 2026-10-14 15:30 | SESSION | Claude Code | OK | [dept=fernmoor; agents=Builder] Hub PR 36: stale flag on any source older than 26 hours. [[Fernmoor Hub build log]] |
| 2026-10-14 14:02 | DIRECTOR | Cloud | OK | [dept=owlbridge; agents=SDR,Editor; rows=a-2026-10-14-owlbridge-followups; done=1; moved=0; blocked=0] LEADGEN marked eight leads due; eight second touches drafted in the tone of voice note, held for the operator to send. Nothing sent. |
| 2026-10-14 12:04 | SCOUT | Cloud | OK | One finding as a new row in [[Scout]]: dental practices in the region adding online booking to their ads. |
| 2026-10-14 12:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Queue unchanged; [[Chat]] has no new message. |
| 2026-10-14 10:15 | SESSION | Claude Code | OK | [dept=brain; agents=Claude] Constitution revised: read 0 for cloud routines, current text against history, what wins when notes disagree. [[The Brain build log]] |
| 2026-10-14 10:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. No row at approved or requested; no note commits since the last run. |
| 2026-10-14 08:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Lock claimed and released; no row moved. |
| 2026-10-14 07:03 | MORNING | Cloud | OK | Mac's last `vault:` sync 13 Oct 22:40, fresh. Found: four runs since 11 Oct planned from a stale copy; each re-marked PARTIAL. Plan: the constitution revision, Owlbridge second touches (a-2026-10-14-owlbridge-followups), Obsidian at login. |
| 2026-10-13 20:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Queue unchanged; [[Chat]] has no new message. |
| 2026-10-13 18:36 | EVENING | Cloud | OK | The Mac's notes from 9 Oct onward arrived at 17:55; review covers 12 and 13 Oct from the synced notes. |
| 2026-10-13 18:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. No row at approved or requested; no note commits since the last run. |
| 2026-10-13 16:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Lock claimed and released; no row moved. |
| 2026-10-13 14:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Queue unchanged; [[Chat]] has no new message. |
| 2026-10-13 12:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. No row at approved or requested; no note commits since the last run. |
| 2026-10-13 10:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Lock claimed and released; no row moved. |
| 2026-10-13 08:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Queue unchanged; [[Chat]] has no new message. |
| 2026-10-13 07:04 | MORNING | Cloud | PARTIAL | Plan written from the same copy as 12 Oct. Re-marked PARTIAL on 14 Oct: stale copy, last `vault:` sync 9 Oct 18:05. |
| 2026-10-12 20:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. No row at approved or requested; no note commits since the last run. |
| 2026-10-12 19:10 | SESSION | Cowork | OK | [dept=ventures; agents=Claude] Gaugewell lead count settled: form fills only, since the Hub counts calls. [[Gaugewell build log]] |
| 2026-10-12 18:34 | EVENING | Cloud | PARTIAL | Review said no log today. Re-marked PARTIAL on 14 Oct: stale copy; the operator's Log and the day's sessions were on the Mac only. |
| 2026-10-12 18:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Lock claimed and released; no row moved. |
| 2026-10-12 16:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Queue unchanged; [[Chat]] has no new message. |
| 2026-10-12 14:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. No row at approved or requested; no note commits since the last run. |
| 2026-10-12 12:05 | SCOUT | Cloud | OK | No new findings worth a row. |
| 2026-10-12 12:02 | DIRECTOR | Cloud | OK | [dept=ventures; agents=Builder,Analyst; rows=a-2026-10-12-gaugewell-trial-reports; done=0; moved=1; blocked=0] Trial reports row taken: report 1 renders; the other four briefed to the Builder in order. The row came from the platform, so the stale Mac copy did not touch it. |
| 2026-10-12 11:30 | APPROVALS WATCHER | Cloud | OK | Started from the platform. The Gaugewell trial reports row approved; queued for the Director. |
| 2026-10-12 10:30 | SESSION | Claude Code | OK | [dept=fernmoor; agents=Analyst] Warmstead first week read: too early on CPL; two broad terms made negative. [[Warmstead build log]] |
| 2026-10-12 10:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Lock claimed and released; no row moved. |
| 2026-10-12 08:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Queue unchanged; [[Chat]] has no new message. |
| 2026-10-12 07:03 | MORNING | Cloud | PARTIAL | Plan written: report 09:00, Warmstead week one, the counting rule. Re-marked PARTIAL on 14 Oct: stale copy, last `vault:` sync 9 Oct 18:05. |
| 2026-10-11 17:04 | WEEKLY | Cloud | PARTIAL | Week 41 reviewed and W42 created. Re-marked PARTIAL on 14 Oct: planned from a stale copy; the Mac's last `vault:` sync was 9 Oct 18:05, so PR 35 was listed as slipped. |
| 2026-10-09 20:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. No row at approved or requested; no note commits since the last run. |
| 2026-10-09 19:20 | SESSION | Claude Code | OK | [dept=fernmoor; agents=Builder] Hub PR 35: Warmstead counts from zero, exact match, nothing before 5 Oct. [[Fernmoor Hub build log]] |
| 2026-10-09 18:33 | EVENING | Cloud | OK | Review from the Log. Done: nine Owlbridge first emails sent, Quillmere tracking live on both sites. Slipped: the counting rule in the Hub. |
| 2026-10-09 18:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Lock claimed and released; no row moved. |
| 2026-10-09 16:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Queue unchanged; [[Chat]] has no new message. |
| 2026-10-09 14:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. No row at approved or requested; no note commits since the last run. |
| 2026-10-09 12:05 | SCOUT | Cloud | OK | One finding as a new row in [[Scout]]: print shops moving botanical prints to bundles of three. |
| 2026-10-09 12:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Lock claimed and released; no row moved. |
| 2026-10-09 10:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Queue unchanged; [[Chat]] has no new message. |
| 2026-10-09 08:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. No row at approved or requested; no note commits since the last run. |
| 2026-10-09 07:03 | MORNING | Cloud | OK | No missed runs. Plan: the counting rule in the Hub, nine Owlbridge first emails, Warmstead week one. |
| 2026-10-08 20:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Lock claimed and released; no row moved. |
| 2026-10-08 19:30 | SESSION | Claude Code | OK | [dept=ventures; agents=Builder] Gaugewell report 1 renders: spend by brand, and the weekly CSV import. [[Gaugewell build log]] |
| 2026-10-08 18:35 | EVENING | Cloud | OK | Review from the Log and two sessions, plus 7 Oct in one line. Done: Owlbridge price and batch 2, the report draft, Gaugewell report 1. Slipped: the counting rule in the Hub. |
| 2026-10-08 18:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Queue unchanged; [[Chat]] has no new message. |
| 2026-10-08 16:02 | DIRECTOR | Cloud | OK | [dept=fernmoor; agents=Analyst,Editor; rows=a-2026-10-08-director-report-draft; done=1; moved=0; blocked=0] First weekly draft for Mon 12 Oct from the Hub: all three brands, the week against the one before, three lines of commentary; Warmstead as days live, leads and spend. |
| 2026-10-08 14:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. No row at approved or requested; no note commits since the last run. |
| 2026-10-08 12:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Lock claimed and released; no row moved. |
| 2026-10-08 11:20 | SESSION | Claude Code | OK | [dept=owlbridge; agents=Claude] Two prices by location; batch 2 approved, nine first emails drafted. [[Owlbridge build log]] |
| 2026-10-08 10:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Queue unchanged; [[Chat]] has no new message. |
| 2026-10-08 08:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. No row at approved or requested; no note commits since the last run. |
| 2026-10-08 07:04 | MORNING | Cloud | OK | Missed: EVENING 7 Oct and the 20:00 watcher (usage limit). Plan: Owlbridge price and batch 2, the first report draft (a-2026-10-08-director-report-draft), Gaugewell report 1. |
| 2026-10-07 20:00 | APPROVALS WATCHER | Cloud | FAILED | Usage limit still reached; the run stopped before its checks. Nothing was waiting at 18:00. |
| 2026-10-07 18:41 | EVENING | Cloud | FAILED | Stopped at the usage limit after reading the Log; no review written. MORNING on 8 Oct covers the day in one line. |
| 2026-10-07 18:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Lock claimed and released; no row moved. |
| 2026-10-07 16:20 | SESSION | Cowork | OK | [dept=owlbridge; agents=Claude] Quillmere tracking: both sites' forms tagged; the second site's phone line still open. [[Quillmere Dental]] |
| 2026-10-07 16:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Queue unchanged; [[Chat]] has no new message. |
| 2026-10-07 14:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. No row at approved or requested; no note commits since the last run. |
| 2026-10-07 13:40 | SESSION | Cowork | OK | [dept=ventures; agents=Claude] Paperwren's second collection declined by the operator. [[Paperwren build log]] |
| 2026-10-07 12:04 | SCOUT | Cloud | OK | No new findings worth a row. |
| 2026-10-07 12:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Lock claimed and released; no row moved. |
| 2026-10-07 10:30 | SESSION | Claude Code | OK | [dept=owlbridge; agents=Researcher] Owlbridge lead list batch 2 scored. [[Owlbridge pipeline]] |
| 2026-10-07 10:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Queue unchanged; [[Chat]] has no new message. |
| 2026-10-07 08:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. No row at approved or requested; no note commits since the last run. |
| 2026-10-07 07:02 | MORNING | Cloud | OK | No missed runs. Plan: Owlbridge batch 2 lead list, Quillmere's tracking, Paperwren's second collection proposal. |
| 2026-10-06 20:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Lock claimed and released; no row moved. |
| 2026-10-06 18:35 | EVENING | Cloud | OK | Review from the Log and one session. Done: CRM mid-point. Slipped: Gaugewell evening, lost to Warmstead; the counting rule. |
| 2026-10-06 18:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Queue unchanged; [[Chat]] has no new message. |
| 2026-10-06 16:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. No row at approved or requested; no note commits since the last run. |
| 2026-10-06 14:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Lock claimed and released; no row moved. |
| 2026-10-06 12:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Queue unchanged; [[Chat]] has no new message. |
| 2026-10-06 11:00 | SESSION | Claude Code | OK | [dept=fernmoor; agents=Analyst] CRM stage 1 mid-point read with the contractor. [[CRM rebuild build log]] |
| 2026-10-06 10:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. No row at approved or requested; no note commits since the last run. |
| 2026-10-06 08:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Lock claimed and released; no row moved. |
| 2026-10-06 07:03 | MORNING | Cloud | OK | No missed runs. Plan: the counting rule in the Hub, Quillmere's tracking, CRM stage 1 mid-point. |
| 2026-10-05 20:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Queue unchanged; [[Chat]] has no new message. |
| 2026-10-05 18:34 | EVENING | Cloud | OK | Review from the Log and two sessions. Done: Warmstead live, counts from zero (the operator's call), PR 34, report 09:00, BOARD REVIEW. Slipped: the counting rule in the Hub. |
| 2026-10-05 18:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. No row at approved or requested; no note commits since the last run. |
| 2026-10-05 16:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Lock claimed and released; no row moved. |
| 2026-10-05 14:10 | SESSION | Claude Code | OK | [dept=brain; agents=Claude] Director report drafted by the brain from the Hub each Monday from 12 Oct; the operator checks and sends. [[The Brain build log]] |
| 2026-10-05 14:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Queue unchanged; [[Chat]] has no new message. |
| 2026-10-05 12:05 | SCOUT | Cloud | OK | No new findings worth a row. |
| 2026-10-05 12:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. No row at approved or requested; no note commits since the last run. |
| 2026-10-05 10:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Lock claimed and released; no row moved. |
| 2026-10-05 09:40 | SESSION | Claude Code | OK | [dept=fernmoor; agents=Builder] Hub PR 34: Warmstead on the combined and per-brand views. [[Fernmoor Hub build log]] |
| 2026-10-05 08:30 | BOARD REVIEW | Cloud | OK | First BOARD REVIEW. Four goals read against [[State]]: Warmstead live today, target £25 by 30 Nov; Owlbridge one of three; Gaugewell's trial has an export and no report; planning time not yet measured. Recommendation: the first Gaugewell report this week. |
| 2026-10-05 08:02 | DIRECTOR | Cloud | OK | [dept=fernmoor; agents=Analyst,Reviewer; rows=a-2026-10-05-warmstead-launch-checks; done=1; moved=0; blocked=0] All five launch checks passed: tracking on both forms, the brand field in the CRM, call routing, campaign names to the UTM spec, the Hub's brand view. Ads live this morning. |
| 2026-10-05 07:02 | MORNING | Cloud | OK | No missed runs. Plan: Warmstead live this morning, report 09:00, Warmstead on every Hub view, the counting call. |
| 2026-10-04 17:05 | WEEKLY | Cloud | OK | Week 40 reviewed; W41 created. Direction: Warmstead live and counted right, Quillmere's first month, new Owlbridge names. Revenue now £900 a month. |
| 2026-10-04 07:32 | TIDY | Cloud | OK | First TIDY. Fixed: 9 stale `updated` dates, 4 broken links, 2 notes missing frontmatter. Proposed for a yes: archive September's run log lines, move three empty Inbox files to `_review/`. |
| 2026-10-02 20:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Queue unchanged; [[Chat]] has no new message. |
| 2026-10-02 18:36 | EVENING | Cloud | OK | Review from the Log and one session. Done: Quillmere signed, the first paying client; launch checks approved; PR 33 merged. Slipped: the pre-launch counting decision. |
| 2026-10-02 18:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. No row at approved or requested; no note commits since the last run. |
| 2026-10-02 16:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Lock claimed and released; no row moved. |
| 2026-10-02 14:02 | DIRECTOR | Cloud | OK | [dept=owlbridge; agents=Marketer,Editor; rows=a-2026-10-02-quillmere-onboarding; done=1; moved=0; blocked=0] Quillmere onboarding drafted: access checklist, the first month's plan, the reporting page and the monthly review agenda. The operator sends them tomorrow. |
| 2026-10-02 13:15 | APPROVALS WATCHER | Cloud | OK | Started from the platform. Two rows approved (Quillmere onboarding, Warmstead launch checks); queued for the Director's 14:00 slot. |
| 2026-10-02 12:04 | SCOUT | Cloud | OK | Two findings as new rows in [[Scout]]: heat pump grant wording used by retrofit installers; review counts as a trust signal for dental practices in local search. |
| 2026-10-02 12:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Queue unchanged; [[Chat]] has no new message. |
| 2026-10-02 11:40 | SESSION | Cowork | OK | [dept=owlbridge; agents=Claude] Quillmere Dental accepted: £900 a month from 2 Oct. [[Owlbridge build log]] |
| 2026-10-02 10:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. No row at approved or requested; no note commits since the last run. |
| 2026-10-02 08:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Lock claimed and released; no row moved. |
| 2026-10-02 07:03 | MORNING | Cloud | OK | No missed runs. Plan: Quillmere's answer, the Warmstead launch checks as one row, merge PR 33. |
| 2026-10-01 20:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Queue unchanged; [[Chat]] has no new message. |
| 2026-10-01 18:33 | EVENING | Cloud | OK | Review from the Log and two sessions. Done: test lead (second attempt), proposal sent 13:00, PR 33. Slipped: nothing. |
| 2026-10-01 18:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. No row at approved or requested; no note commits since the last run. |
| 2026-10-01 16:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Lock claimed and released; no row moved. |
| 2026-10-01 14:20 | SESSION | Claude Code | OK | [dept=fernmoor; agents=Builder] Hub PR 33: UTM parser to the spec, no-source list per brand. [[Fernmoor Hub build log]] |
| 2026-10-01 14:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Queue unchanged; [[Chat]] has no new message. |
| 2026-10-01 12:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. No row at approved or requested; no note commits since the last run. |
| 2026-10-01 10:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Lock claimed and released; no row moved. |
| 2026-10-01 09:55 | SESSION | Cowork | OK | [dept=fernmoor; agents=Claude] Warmstead form brand field fixed; second test lead routed as Warmstead in the CRM. [[Warmstead build log]] |
| 2026-10-01 08:00 | APPROVALS WATCHER | Cloud | OK | Nothing waiting. Queue unchanged; [[Chat]] has no new message. |
| 2026-10-01 07:02 | MORNING | Cloud | OK | No missed runs. Plan: Warmstead test lead end to end, the Quillmere proposal, the UTM parser. |

## Expected schedule

What MORNING checks against. Kept in step with [[Scheduled jobs]]. All times Europe/London.

| Job | Expected | Status |
|---|---|---|
| MORNING | 07:00 Mon to Fri, cloud routine | Cloud since 18 Sep; run by hand in Claude Code 15 to 17 Sep |
| EVENING | 18:30 Mon to Fri, cloud routine | Cloud since 17 Sep, first run 18:36 |
| WEEKLY | Sunday 17:00, cloud routine | First run 20 Sep |
| SCOUT | 12:00 Mon, Wed and Fri, cloud routine | First run 21 Sep |
| APPROVALS WATCHER | Every two hours 08:00 to 20:00 Mon to Fri, plus each start from the platform; a quiet run writes one "Nothing waiting" line | On the timer since 21 Sep; [[Watcher lock]] since 24 Sep |
| DIRECTOR | Inside the approvals watcher, whenever a row is approved or a note waits | First run 21 Sep |
| TIDY | First Sunday of the month, 07:30 | First run 4 Oct; next Sun 1 Nov |
| BOARD REVIEW | First Monday of the month, 08:30 | First run 5 Oct; next Mon 2 Nov |
| SESSION | When a session exports | Claude Code, Cowork and Claudian |

The clocks go back on Sun 25 Oct. The routines are scheduled in UTC, so unless their times are reset first every job above runs an hour early from Mon 26 Oct (a-2026-10-22-routine-times).

## Known failures on record

| When | Job | Result | Cause |
|---|---|---|---|
| 2026-09-23 10:03 | APPROVALS WATCHER | PARTIAL | Started from the platform a minute after the 10:02 timer run; both worked the same row. [[Watcher lock]] added 24 Sep |
| 2026-10-07 18:41 | EVENING | FAILED | Usage limit reached after three long sessions; MORNING on 8 Oct covered the day |
| 2026-10-07 20:00 | APPROVALS WATCHER | FAILED | Usage limit, same cause; nothing was waiting |
| 2026-10-11 17:04 | WEEKLY | PARTIAL | Stale copy: the Mac did not sync from 9 Oct 18:05 to 13 Oct 17:55 (Obsidian closed) |
| 2026-10-12 07:03 | MORNING | PARTIAL | Stale copy, same cause |
| 2026-10-12 18:34 | EVENING | PARTIAL | Stale copy, same cause |
| 2026-10-13 07:04 | MORNING | PARTIAL | Stale copy, same cause. Rule added 14 Oct: check the newest `vault:` commit before planning |
| 2026-10-16 12:06 | SCOUT | PARTIAL | Two sources refused the fetch; read through search only |

## Archive

September's lines are in [[Run log 2026-09]], moved on 5 Oct after TIDY proposed it and the operator said yes. Each month's lines move out once the month is over, never deleted.

## Related

[[Scheduled jobs]] · [[Operating manual]] · [[MORNING]] · [[Approvals]] · [[Watcher lock]]
