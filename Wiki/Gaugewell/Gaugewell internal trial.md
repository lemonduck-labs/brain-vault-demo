---
title: Gaugewell internal trial
aliases: [Gaugewell trial, Internal trial]
type: spec
parent: "[[Gaugewell]]"
owner: the operator
updated: 2026-10-22
tags:
  - project/gaugewell
  - venture/gaugewell
  - domain/reporting
---

# Gaugewell internal trial

The first real data Gaugewell reads: Fernmoor's anonymised weekly export from the [[Fernmoor Hub]]. Goal: live on Fernmoor's data by 15 Nov.

## What it reads

A weekly CSV per brand and channel: spend, form fills, surveys, sales. No lead-level rows, no names, no contact details. Agreed with the managing director on 24 Sep (Hub PR 31).

## Where it stands

| Report | State | Check against the Hub |
|---|---|---|
| Spend by brand | Renders | Matches |
| CPL by channel | Renders | Spend matches; CPL higher, form fills only |
| Leads by day | Renders | Lower, form fills only |
| Survey rate by brand | Not built | |
| Monday summary | Not built | |

> [!warning] Two counts, both right
> The Hub counts form fills and answered inbound calls as leads. Gaugewell counts form fills only. On Fernmoor's data Gaugewell's lead totals run lower, so its CPL runs higher. Every Gaugewell report says "form fills" on its lead column.

## Exports or API

| | Exports | API |
|---|---|---|
| How | The weekly CSV the Hub already writes | Gaugewell reads the Hub's API |
| Needs | Nothing new | A read-only key on the Hub, which is a Fernmoor change |
| Fresh | Weekly | Daily |
| Risk | A missed export means a missed week | A key into a work system held by a side project |

Claude's view: stay on exports for the trial. The weekly cadence is what the reports are for, and a key into the Hub needs the managing director's yes for little gain. [Likely] The operator has not decided.

## Open threads

- [ ] Ask the managing director, if the API route is chosen, for a read-only key, with what it reads written down #blocked

## Related

[[Gaugewell]] · [[Gaugewell backend]] · [[Fernmoor Hub]]
