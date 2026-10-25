---
title: BOARD REVIEW
aliases: [Board review, Monthly review, Venture review]
type: playbook
parent: "[[Operating manual]]"
owner: the operator
updated: 2026-09-21
tags:
  - system
  - playbook
---

# BOARD REVIEW

The monthly look at each venture as a board would take it. Runs on the first Monday of the month as a cloud routine, reading the [[WEEKLY]] note written the day before, or on demand for one venture ("board review Owlbridge"). Role: [[Advisor]].

## Per venture: [[Owlbridge]], [[Gaugewell]], [[Paperwren]], and the [[Fernmoor]] role as a fourth

1. **State against plan.** What the project note said the next build was last month, and whether it happened. From the build log, not from memory.
2. **Numbers, sourced.** Whatever exists: spend, leads, revenue, clients, orders, margin. Blank where nothing exists, and a line saying what would need to be measured. Fernmoor figures come from the [[Fernmoor Hub]] only.
3. **The hard question.** The one in the [[Advisor]] brief for that venture, answered as far as the record allows.
4. **The biggest risk.** One, with its confidence tagged.
5. **What to stop.** One thing, or "nothing this month" with the reason.
6. **Next month's three.** Ranked.

## Across ventures

- Time: which ventures got sessions this month (counted from the build logs), which got none.
- The bridge question: which of these is funding or feeding another, and whether that still holds (Owlbridge's retainer income against the [[Twelve month plan]]; Gaugewell's trial running on Fernmoor's data).
- One decision to put to the operator, with the recommendation and the rejected alternative.

## Output

A dated "Board review, <Month YYYY>" section at the end of each venture's project note, one screen each, and a five-line summary in the latest weekly note. The project note's `updated` field changes.

## Idempotent

Keyed on the month and the venture. If a "Board review, <Month YYYY>" section already exists in the note, it is updated, not repeated.

## Done when

Each venture note has this month's section, the weekly note has the summary, and the run log has the line.

## Never

- Recommends a trade, an investment product or a legal position. It frames; professionals decide those.
- Grades the operator. It grades the plan against the record.
- Quotes a figure without its source.
