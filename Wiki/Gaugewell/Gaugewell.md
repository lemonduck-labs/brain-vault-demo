---
title: Gaugewell
aliases: [Gaugewell platform, Reporting platform]
type: project
status: build
stage: Internal trial, three of five reports render
owner: the operator
started: 2026-08-10
updated: 2026-10-22
repo: private GitHub repo
tags:
  - project/gaugewell
  - venture/gaugewell
  - domain/reporting
  - status/active
---

# Gaugewell

> [!abstract] In one line
> A marketing reporting platform for owner-run service businesses: spend, leads and what came of them, in five plain reports, without a dashboard to learn.

Built in the evenings. The idea settled on 10 Aug: most small firms do not need a dashboard, they need five answers every Monday, and they need them to agree with what the ad platforms say.

## State at a glance

| | |
|---|---|
| **Stage** | Internal trial on Fernmoor's anonymised Hub exports. Three of five reports render |
| **Goal** | Internal trial live on Fernmoor's data by 15 Nov |
| **Blocked on** | The decision between exports and the Hub's API |
| **Next** | Reports 4 and 5: survey rate by brand, and the Monday summary |
| **Money** | Commercial model drafted, not priced. See [[Gaugewell commercial model]] |

## Why it exists

"I spend money on ads every month and I cannot tell you what came back." The operator hears this from every owner-run business Owlbridge talks to, and solved it once already for Fernmoor with the [[Fernmoor Hub]]. Gaugewell is the same answer made general.

> [!important] The bet, 10 Aug
> Five fixed reports that are right beat fifty that need setting up. If the internal trial shows the five answer a director's Monday questions, the product is the five. [Guessing]

## The five reports

| # | Report | State |
|---|---|---|
| 1 | Spend by brand | Renders |
| 2 | CPL by channel | Renders |
| 3 | Leads by day | Renders |
| 4 | Survey (or booking) rate by brand | Not built |
| 5 | The Monday summary, in words | Not built |

> [!warning] Counts differ from the Hub on purpose
> Gaugewell counts form fills only; the Hub also counts answered inbound calls. Gaugewell's lead totals run lower, and both are right. Every report says which count it uses. See [[Gaugewell internal trial]].

## Decisions

- **24 Sep** Read Fernmoor through an anonymised weekly export, agreed with the managing director. Ruled out lead-level data, which Gaugewell does not need.
- **12 Oct** Form fills only as the lead count. Ruled out matching call logs, which most small clients would not have.

## Open threads

- [ ] Decide exports or API for the trial: the API needs a read-only key on the Hub, which is a Fernmoor change and needs the managing director's agreement #decision
- [ ] Build report 4, survey rate by brand, from the export's survey column #next
- [ ] Build report 5, the Monday summary in words, with Haiku writing from the four tables #next

## Where things live

- **Repo**: a private GitHub repo
- **Hosting**: Netlify
- **Detail**: [[Gaugewell backend]]

## Related

[[Gaugewell build log]] · [[Gaugewell commercial model]] · [[Gaugewell internal trial]] · [[Gaugewell backend]] · [[Twelve month plan]] · [[Index]]
