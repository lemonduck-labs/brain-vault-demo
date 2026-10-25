---
title: CRM rebuild
aliases: [CRM, CRM project, The CRM]
type: project
status: build
stage: Stage 1 handed over, stage 2 waiting on task types
owner: the operator
parent: "[[Fernmoor]]"
started: 2026-09-21
updated: 2026-10-22
tags:
  - project/fernmoor
  - domain/crm
  - status/active
---

# CRM rebuild

> [!abstract] In one line
> The group's hosted CRM, rebuilt by the CRM contractor in stages so that every lead carries its brand and source, routes to the call team, and leaves a record the Hub can read.

## State at a glance

| | |
|---|---|
| **Stage** | Stage 1 (lead routing and the brand field) handed over 20 Oct |
| **Blocked on** | Stage 2 needs the sales manager and the call-team lead to agree the call team's task types, by Fri 23 Oct |
| **Contract** | The CRM contractor, three months with a break clause |
| **Next** | Stage 2: task types for the call team |

## The stages

| Stage | What | State |
|---|---|---|
| 1 | Web form leads routed by brand; a brand field on every lead; duplicate check | Handed over 20 Oct |
| 2 | Task types for the call team, so the call note's next-step task lands in the right queue | Brief sent 20 Oct; waiting on task types |
| 3 | Survey and sale stages, so the Hub reads outcomes from the CRM rather than a spreadsheet | Not started |

> [!important] Build so the group can run it without the contractor
> The operator's line when the contract was signed: every change documented in plain words and settings kept as settings wherever possible, so the group can take the CRM in house at the break clause or the end of the contract. Ruled out custom code for anything a setting can do.

## Stage 2 brief, sent 20 Oct

The call team needs a small fixed set of task types, each with an owner and a default due time. The contractor builds them once the list is agreed. The list is not Claude's or the operator's to set: the sales manager and the call-team lead own how the team works.

Proposed to them as a starting point, for them to change:

| Task type | Owner | Default due |
|---|---|---|
| Call back | Call team | Same day |
| Book survey | Call team | Next working day |
| Send quote | Sales | Two working days |
| Chase quote | Sales | Five working days |

> [!question] Not confirmed
> Whether Ridgeby Roofing's repairs need their own "book repair visit" type, separate from a survey. The installs manager would know.

## Decisions

- **21 Sep** A contractor in stages with a break clause. Ruled out a fixed-price rebuild in one go, which would leave nothing usable until the end.
- **20 Oct** Stage 1 accepted with two gaps noted. Ruled out holding the handover until the duplicate check also matches on email, which can follow in stage 2.

## Open threads

- [ ] Agree the call team's task types with the sales manager and the call-team lead, by Fri 23 Oct #blocked
- [ ] Decide whether the duplicate check matches on email as well as phone, in stage 2 or later #decision
- [x] Stage 1 handed over and checked, 20 Oct. See [[CRM rebuild build log]] #next

## Related

[[CRM rebuild build log]] · [[Agencies and partners]] · [[Call note pipeline]] · [[Fernmoor Hub]] · [[Fernmoor]]
