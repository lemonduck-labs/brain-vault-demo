---
title: Fernmoor Hub build log
aliases: [Hub build log, Hub PR log]
type: log
parent: "[[Fernmoor Hub]]"
owner: the operator
updated: 2026-10-22
tags:
  - project/fernmoor
  - domain/reporting
---

# Fernmoor Hub build log

Every pull request on the Hub, what was asked and what came back, newest first. Claude builds and opens the PR; the operator reviews and merges. The front door is [[Fernmoor Hub]].

### 21 Oct 2026, PR 42 Warmstead survey outcome on the weekly view (Claude Code, Opus)

**Asked:** "show me Warmstead surveys and what came of them next to the leads."
**Delivered:** a card on the weekly view: surveys booked, held and sold for Warmstead, from 5 Oct only. Tests pass.
**Status:** open. Waiting on the operator's review.

### 21 Oct 2026, PR 41 call note on the lead (Claude Code, Opus)

**Asked:** write the call summary onto the lead in the CRM as a logged call plus a next-step task, metadata only.
**Delivered:** after each call the Hub writes a logged call (time, length, direction, outcome code) and one next-step task with a due date onto the lead. No call content is read or stored until the GDPR sign-off. Tested on ten calls from the call-team lead's queue.
**Snag:** PR 39 merged first and touched the same export module, so 41 was rebased on 21 Oct before it could merge. Tests re-run clean.
**Status:** merged 21 Oct.

### 20 Oct 2026, PR 40 CRM stage 1 field mapping (Claude Code, Opus)

**Asked:** read the new fields the contractor added in stage 1.
**Delivered:** the brand field and the routing outcome read into the Hub, with the old fields kept until stage 2 lands.
**Reviewed 21 Oct:** two small fixes asked for. Two field names in the contractor's handover note differ from the names in the CRM, so the mapping reads the CRM's names and logs the mismatch.
**Status:** open, with the two fixes to make.

### 20 Oct 2026, PR 39 weekly director report export (Claude Code, Opus)

**Asked:** the report's table straight from the Hub, all three brands.
**Delivered:** a weekly export with a row per brand and a group total, and Warmstead shown from 5 Oct.
**Status:** merged 20 Oct.

### 20 Oct 2026, PR 38 Ridgeby Search naming (Claude Code, Sonnet)

**Asked:** read the new repairs and replacement campaign names ahead of the restructure.
**Delivered:** the parser reads both, and the old name until it has no spend.
**Status:** merged 20 Oct.

### 16 Oct 2026, PR 37 calls per lead (Claude Code, Opus)

**Asked:** calls per lead and time to first call, per brand.
**Delivered:** the calls view, from call metadata only.
**Status:** merged 17 Oct.

### 14 Oct 2026, PR 36 stale flag on cached figures (Claude Code, Sonnet)

**Asked:** "tell me when a number is old."
**Delivered:** any source older than 26 hours shows a stale flag and its last pull time.
**Status:** merged 14 Oct.

### 9 Oct 2026, PR 35 Warmstead counts from zero (Claude Code, Opus)

**Asked:** no lead before 5 Oct is Warmstead.
**Delivered:** the brand filter matches "warmstead" exactly and drops anything dated before 5 Oct.
**Status:** merged 9 Oct.

### 5 Oct 2026, PR 34 Warmstead in the combined view (Claude Code, Opus)

**Asked:** the third brand on every view, on launch day.
**Delivered:** Warmstead as a brand across the combined and per-brand views.
**Status:** merged 5 Oct.

### 1 Oct 2026, PR 33 UTM parser to the spec (Claude Code, Sonnet)

**Asked:** read source, medium and campaign the way [[Attribution and UTM spec]] writes them.
**Delivered:** the parser and a list of leads with no source, per brand.
**Status:** merged 2 Oct.

### 28 Sep 2026, PR 32 GA4 sessions card (Claude Code, Sonnet)

**Asked:** sessions and form starts per brand landing page.
**Delivered:** a GA4 card per brand.
**Status:** merged 29 Sep.

### 24 Sep 2026, PR 31 anonymised export for Gaugewell (Claude Code, Opus)

**Asked:** an export the [[Gaugewell internal trial]] can read, with the managing director's agreement.
**Delivered:** a weekly CSV of spend, leads, surveys and sales per brand and channel, with no lead-level rows.
**Status:** merged 25 Sep.

### 22 Sep 2026, PR 30 Google Ads daily pull (Claude Code, Opus)

**Asked:** Google Ads spend and conversions daily, not weekly.
**Delivered:** a daily pull per brand, cached.
**Status:** merged 22 Sep.
