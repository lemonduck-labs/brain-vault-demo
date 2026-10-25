---
title: Initiatives
aliases: [Initiative ledger, Prompts raised]
type: log
owner: the operator
updated: 2026-10-22
tags:
  - system
---

# Initiatives

What the brain raised without being asked, under the strategy lens in [[Advisor]]: drift, slip, stale, contradiction, opportunity or risk. One line each, newest first, with the response and the outcome filled in when they come. Raised by MORNING (at most one a day), WEEKLY and BOARD REVIEW.

| date | type | prompt | evidence | recommended move | response | outcome |
|---|---|---|---|---|---|---|
| 2026-10-22 | Risk | The clocks go back on Sun 25 Oct and every cloud routine is scheduled in UTC | [[Scheduled jobs]]: five routines with UTC times; no reset listed | Reset the five schedules on Friday, about five minutes; row a-2026-10-22-routine-times | | |
| 2026-10-21 | Slip | Warmstead's budget step was due 19 Oct and waits on a channel split and a check of the leads against the CRM | [[Warmstead build log]] 19 Oct; no channel split in the vault | Read the split from the Hub on the next Mac session and settle the CRM check | Asked for the split by channel (note n-2026-10-21-warmstead-split) | Both done 22 Oct; the step is a pending row |
| 2026-10-20 | Contradiction | The Hub and Gaugewell define "lead" differently, so the same week shows two counts | Hub: form fills plus calls; Gaugewell: form fills only ([[Gaugewell internal trial]]) | One written definition, owned by the Hub, that Gaugewell reads | | |
| 2026-10-19 | Risk | Five Hub pull requests in two days; one already needed a rebase | [[Fernmoor Hub build log]] PRs 38 to 42 | Review and merge before building more | Accepted 20 Oct ("yes, do the review first") | Row a-2026-10-19-hub-pr-review |
| 2026-10-18 | Drift | Week 42 carried four lead gen station changes and no discovery call | [[Owlbridge build log]], [[Owlbridge activity log]] | Two calls booked before the next station feature | | Parked in [[Growth]] as suggestion 1 |
| 2026-10-14 | Risk | Four runs from 9 to 13 Oct planned from a copy five days behind the Mac | [[Run log]]: no `vault:` commit after 9 Oct 08:12 | Check the newest sync before planning; say so first when it is stale | Accepted 14 Oct | Promoted to the root `CLAUDE.md` and [[MORNING]] |
| 2026-10-07 | Opportunity | Quillmere Dental's first results could be the case study for the next three proposals | [[Quillmere Dental]]: first fortnight's bookings | Ask the client for permission to use anonymised figures at the first review | Accepted 8 Oct | Added to the review agenda |
| 2026-09-28 | Stale | [[Paperwren]] has had no listing change since July | [[Paperwren build log]] | Decide: park it on purpose, or one evening a month | "Park it on purpose" | Parked in [[Now]] |
| 2026-09-23 | Risk | Two watcher runs overlapped and wrote the same row twice | [[Run log]] 23 Sep 10:02 and 10:03 | A claim-and-release lock before a run touches the queue | Accepted | [[Watcher lock]] built 24 Sep |

## Related

[[Advisor]] · [[MORNING]] · [[WEEKLY]] · [[BOARD REVIEW]]
