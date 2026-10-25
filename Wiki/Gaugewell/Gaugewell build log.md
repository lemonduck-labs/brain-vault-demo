---
title: Gaugewell build log
aliases: [Gaugewell log]
type: log
parent: "[[Gaugewell]]"
owner: the operator
updated: 2026-10-22
tags:
  - project/gaugewell
  - venture/gaugewell
---

# Gaugewell build log

What was asked of the Gaugewell build and what came back, newest first. The front door is [[Gaugewell]].

### 21 Oct 2026, exports or API written up (Claude Code, Opus)

**Asked:** "should the trial read the Hub's API or keep using the exports."
**Delivered:** both routes in [[Gaugewell internal trial]] with what each needs. The API route needs a read-only key on the Hub, which is a Fernmoor change. Claude's view: stay on exports for the trial and ask for the key only if the trial goes well. [Likely]
**Open:** the operator's decision.

### 18 Oct 2026, report 3 renders (Claude Code, Opus)

**Asked:** leads by day.
**Delivered:** leads by day per brand from the week 41 and 42 exports. Form fills only, labelled as such.

### 15 Oct 2026, report 2 renders (Claude Code, Opus)

**Asked:** CPL by channel.
**Delivered:** CPL by brand and channel. Matches the Hub on spend to the penny; lead counts lower, because calls are not counted.

### 12 Oct 2026, lead count settled (Cowork, Opus)

**Asked:** why do the totals not match the Hub.
**Delivered:** the reason (the Hub counts calls) and the decision to count form fills only.

### 8 Oct 2026, report 1 renders (Claude Code, Opus)

**Asked:** spend by brand, from the anonymised export.
**Delivered:** the first report, and the import that reads the weekly CSV.

### 25 Sep 2026, first export received (Claude Code, Sonnet)

**Asked:** read the Hub's first anonymised export (Hub PR 31).
**Delivered:** a parser and a check that no lead-level row is present.

### 10 Aug 2026, the five reports (Cowork, Opus)

**Asked:** what is the smallest version of this worth building.
**Delivered:** the five-report idea, written into [[Gaugewell]].
