---
title: Fernmoor Hub
aliases: [The Hub, Hub, Group dashboard]
type: project
status: live
stage: Live, weekly report source for all three brands
owner: the operator
started: 2026-06-08
updated: 2026-10-22
repo: private GitHub repo
tags:
  - project/fernmoor
  - domain/reporting
  - status/active
---

# Fernmoor Hub

> [!abstract] In one line
> The group's internal reporting dashboard: spend, leads, surveys and sales for all three brands in one place, read from Meta, Google Ads, GA4 and the CRM.

The operator built it so the director report stops being a Monday of copying numbers. It is a Netlify site with its own API, and since 18 Sep it is the only source of ad figures anywhere in the vault.

## State at a glance

| | |
|---|---|
| **Stage** | Live. Reads Meta, Google Ads, GA4 and the CRM daily |
| **Last merge** | PR 41, call note on the lead, 21 Oct |
| **Open** | PR 40 (CRM stage 1 field mapping, reviewed 21 Oct, two small fixes to make) and PR 42 (Warmstead survey outcome on the weekly view) |
| **Next** | The two fixes on 40, and a review of 42, before Mon 26 Oct's report run |
| **Route** | Claude builds on a branch and opens the PR; the operator reviews and merges. Netlify deploys on merge |

## What it shows

| View | What | Since |
|---|---|---|
| Combined | All three brands: spend, leads, CPL, surveys, sold, by week | PR 34, 5 Oct |
| Per brand | The same, per brand, with the channel split | PR 30 to 35 |
| Weekly | The director report's figures, exported as a table | PR 39, 20 Oct |
| Calls | Calls per lead and the call note status | PR 37 and 41 |
| Export | An anonymised CSV for the [[Gaugewell internal trial]], agreed with the managing director | PR 31, 24 Sep |

## How it is built

- **Front end**: a static dashboard, one design across every view.
- **Back end**: one function per source, cached daily, with a stale flag when a pull is older than 26 hours (PR 36).
- **Data**: Meta and Google Ads by API; GA4 for sessions; the CRM for leads, surveys and sales.
- **Brand match**: by campaign naming per [[Attribution and UTM spec]]; Warmstead on "warmstead" exactly, from 5 Oct.

> [!warning] Gotchas
> - A cached figure looks like a live one. Check the stale flag before quoting a number.
> - A Netlify environment key applies only on the next deploy. A new key with no deploy means the old one is still in use.
> - Check a PR is still open before pushing to its branch. A push to a merged branch goes nowhere useful.
> - Two PRs on the same module: whichever merges second needs a rebase (39 and 41, 21 Oct).
> - The Hub counts a form fill or an answered inbound call as a lead. [[Gaugewell]] counts form fills only, so its lead counts run lower. Say which count a figure uses.

## Decisions

- **18 Sep** The Hub is the only source of ad figures. Ruled out the third-party connector, which disagreed with the platforms three times.
- **24 Sep** The Gaugewell export is anonymised and agreed with the managing director before it runs. Ruled out a direct read from Gaugewell into the Hub's API.
- **20 Oct** The weekly report is built from the Hub's own export. Ruled out a separate report script reading the platforms again.

## Open threads

- [ ] Make the two fixes from the 21 Oct review on PR 40: read the CRM's field names, log the mismatch with the handover note #next
- [ ] Review PR 42, the Warmstead survey outcome card, before Mon 26 Oct #next
- [x] PR 41 merged 21 Oct: call note on the lead. See [[Call note pipeline]] #next

## Related

[[Fernmoor Hub build log]] · [[Fernmoor]] · [[Weekly director report]] · [[Gaugewell]]
