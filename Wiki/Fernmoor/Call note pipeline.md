---
title: Call note pipeline
aliases: [Call notes, Call note on the lead, Call summary]
type: project
status: live
stage: Metadata only, call content gated on the GDPR sign-off
owner: the operator
parent: "[[Fernmoor]]"
started: 2026-10-16
updated: 2026-10-22
tags:
  - project/fernmoor
  - domain/crm
  - domain/ai
  - status/active
---

# Call note pipeline

> [!abstract] In one line
> After each sales call, a logged call and one next-step task are written onto the lead in the CRM, so the call team stops typing notes and no lead is left without a next step.

Proposed 16 Oct, shipped 21 Oct as Hub PR 41.

## State at a glance

| | |
|---|---|
| **Live** | Logged call plus next-step task on the lead, from call metadata (time, length, direction, outcome code) |
| **Gated** | Any summary of what was said. Waits on the managing director's GDPR sign-off, asked 16 Oct |
| **Next** | Measure how many leads have no next step, before and after, from Mon 26 Oct |

> [!important] Metadata is a stage, not the rule
> The aim is an AI summary of each call and a drafted next step. Metadata-only is where it starts because it needs no sign-off. Ruled out on 16 Oct: recording and summarising calls before the sign-off, and a third-party notetaker that would hold call audio outside the group.

## How it works

1. The phone system logs the call.
2. The Hub matches the call to the lead by number.
3. The Hub writes a logged call and one next-step task (from the outcome code, using the task types from [[CRM rebuild]] once stage 2 lands).
4. Nothing is sent to the customer. The call team still decides what happens next.

> [!warning] What breaks
> - A call from a withheld or new number matches no lead. Those are listed in the Hub's calls view for the call-team lead.
> - Until stage 2, next-step tasks use one generic type, so they all land in one queue.

## What the sign-off needs to cover

Written for the managing director, 16 Oct: what is recorded, where it is held, for how long, who can read it, how a customer is told, and how a customer's request to see or delete it is handled. Claude did not draft a legal position; that is the managing director's call with the group's adviser.

## Open threads

- [ ] Count leads with no next step for the week before and after PR 41, from Mon 26 Oct #next
- [x] Shipped as Hub PR 41, merged 21 Oct #next

## Related

[[Fernmoor Hub]] · [[Fernmoor Hub build log]] · [[CRM rebuild]] · [[Fernmoor]]
