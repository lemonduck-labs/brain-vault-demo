---
title: Owlbridge lead gen station
aliases: [Lead gen station, Owlbridge outreach pipeline]
type: spec
parent: "[[Owlbridge]]"
owner: the operator
updated: 2026-10-22
tags:
  - venture/owlbridge
  - domain/lead-gen
---

# Owlbridge lead gen station

How Owlbridge finds, researches and writes to owner-run local service businesses, and who does each step. Version 2, rebuilt 27 Sep. The rows live in [[Owlbridge pipeline]], every touch in [[Owlbridge activity log]], and the run that drives it is [[LEADGEN]].

> [!important] Nothing sends itself
> Claude researches, scores and drafts. The operator sends every message, through the business's own site form, from their own browser. A draft is never a send. See [[Permissions]].

## The stages

| # | Who | Does | Writes to | Gate |
|---|---|---|---|---|
| 1 | Researcher | Finds candidates in the target segments and towns, from public listings and the businesses' own sites | A lead list note, `Owlbridge lead list YYYY-MM-DD` | None, research only |
| 2 | Researcher | Scores each one (below) and names the buying signal | The lead list's tier tables | None |
| 3 | SDR | Drafts email 1 per company in [[Owlbridge outreach drafts]] wording, with one line about that business | The pipeline row, status drafted | None |
| 4 | The operator | Approves the list and sends | The activity log, an email line | Their yes, per batch, in [[Approvals]] |
| 5 | Director | Marks the next touch due on the right day (days 1, 4, 10) | The pipeline's next date | None |
| 6 | SDR | Drafts replies to anyone who answers | [[Owlbridge follow-up drafts]] | The operator sends |
| 7 | The operator | Calls, proposals, signing | The activity log | Theirs |

## Who Owlbridge is for

Owner-run local service businesses with one to five sites, where the owner or a manager answers enquiries and nobody can say what the marketing brings in: dental and physio practices, nurseries, joiners, lettings agents, cafes. Ruled out on 27 Sep: national chains and anything with its own marketing team.

## Scoring

| Factor | Points | Full marks when |
|---|---|---|
| Sites | 25 | Two to five sites, or a second opening |
| Enquiry value | 25 | A new customer is worth several hundred pounds a year or more |
| Buying signal | 20 | A new site, new owner, rebrand or new booking system in the last 12 months |
| Owner-run | 15 | The owner or a manager decides, no head office |
| Reachable | 15 | A site form or a published business inbox |

Tier A from 80, B from 60, C below.

## Candidates

Seeds found but not yet scored or added to the pipeline.

| Company | Segment | What the research holds | Gaps before scoring | Status |
|---|---|---|---|---|
| Bramblecote Vets | Vets | Two practices, a third advertised | Who decides | seed |
| Thornwick Letting Rooms | Lettings | Took over a second branch in the summer | Reachable? No form found | seed |
| Siskin Play Nursery | Nurseries | One setting, waiting list on the site | Single site, may score low | seed |

## Referrals

Leads that came from a person rather than a list, with what was known when they were added.

| Company | Segment | Came from | What the research holds | Status |
|---|---|---|---|---|
| Quillmere Dental | Dental | The practice's accountant, 25 Sep | Two sites, second opened in the spring; booking form on both | won, 2 Oct |

## Suppression list

Company and address only, never deleted. A company on this list is never contacted again. Added by the platform's Leads area when a lead is opted out.

| company | address |
|---|---|
| Kestrelgate Dental |  |

## Open

- [ ] Score the three seeds in Candidates in the next LEADGEN run #next

## Related

[[Owlbridge pipeline]] · [[Owlbridge activity log]] · [[Owlbridge outreach drafts]] · [[Owlbridge follow-up drafts]] · [[Owlbridge tone of voice]] · [[Owlbridge lead list 2026-10-07]] · [[Owlbridge]]
