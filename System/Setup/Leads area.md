---
title: Leads area
aliases: [Lead management, Pipeline board, Owlbridge CRM view]
type: spec
parent: "[[Console]]"
owner: the operator
updated: 2026-09-29
tags:
  - system
  - spec
---

# Leads area

For a-2026-09-27-leads-area in [[Approvals]]. The operator, 27 Sep: the platform had no way to see whether [[Owlbridge]] outreach had been actioned. Build a Leads area on the platform over the Owlbridge pipeline, so every lead, its status and its next step are visible and changeable in one place. Written by a Cowork session on 27 Sep; shipped on the platform on 29 Sep.

## The biggest risk first

[Certain] Two writers on one table: the platform (the operator's clicks) and the runs (the Director, through [[LEADGEN]]). Status changes must go through the same per-row merge the Approvals table uses, or a click and a run in the same hour will conflict and stall the sync ([[Vault sync]]). The pipeline note gets the row-by-id merge and a `.gitattributes` line of its own, and a simultaneous edit is tested before shipping.

## Data

The table in `Wiki/Ventures/Owlbridge/Owlbridge growth/Owlbridge pipeline.md`: id, business, segment, tier, score, contact role, contact route, status, last touch, next step, next date, source. Statuses in order: researched, drafted, sent, replied, call booked, proposal, won, lost, opted out, disqualified. Research detail stays in the lead list note; the Leads area links to it by business.

## What it shows

1. **Top strip:** leads in play (not lost, opted out or disqualified); sent this week; replies and reply rate (replies divided by sent, shown only once 10 or more are sent); calls booked; won, as a count only.
2. **Due today:** every row whose next date is today or past, oldest first, with its next step. This is the list the operator works from.
3. **Board:** one column per status, cards showing business, contact role, tier, score and next date. A status menu moves a card; each move writes the status and today's date to "last touch" and commits `platform: lead <id> <status>`.
4. **Detail panel:** every field, an editable next step and next date, and the lead list's research row for that business.
5. **Filters:** tier, segment, source, status; remembered per device.
6. **Add lead:** a short form that appends a row with status researched.
7. **Opted out** asks to confirm, then also adds the business to the suppression list in the station note.

The same theme, components and sidebar pattern as the rest of the platform; a Leads item with a count of due-today rows. On a phone, Due today first and the board as a status list.

## Tests before the pull request

- Parser: the full table, a row with an empty score, a row with an escaped pipe.
- A status change and a Director run editing different rows of the same table merge cleanly; on the same row, the later status wins.
- Screenshots on desktop and phone.
- No figure shows without its source rows; empty states say what is missing.

## Related

[[Owlbridge]] · [[LEADGEN]] · [[Console]] · [[Approvals]]
