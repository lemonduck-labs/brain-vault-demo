---
title: Watcher lock
aliases: [Run lock, Run-in-progress marker, Claim ledger]
type: log
parent: "[[Scheduled jobs]]"
owner: the operator
updated: 2026-10-22
tags:
  - system
  - log
---

# Watcher lock

The ledger behind `System/Setup/watcher-lock.py`, which stops two cloud runs working the same queue at once. Written by the script only; never edit a row by hand. A run claims at its start and releases in its last commit; a claim with no release goes stale after 90 minutes, so a run that dies never blocks the next. Of the live claims, the earliest wins and every other run stands down. A key of `watcher` is the whole queue; a key that is a row id locks that row alone. Times are UTC; the run id carries the London time it started. Append-only and union-merged, so nothing is ever removed: [[TIDY]] may move old rows into the monthly archive like the run log.

Built 24 Sep 2026, after two watcher runs on 23 Sep worked the same rows twice. How a routine uses it is in [[Scheduled jobs]]; how the platform reads it is in [[Team]].

| utc | key | run | action |
|---|---|---|---|
| 2026-09-24T15:02:11Z | watcher | director-20260924-1602 | claim |
| 2026-09-24T15:02:40Z | watcher | director-20260924-1602 | release |
| 2026-09-27T12:08:19Z | watcher | director-20260927-1308 | claim |
| 2026-09-27T12:08:51Z | a-2026-09-27-lead-gen-station-v2 | director-20260927-1308 | claim |
| 2026-09-27T12:31:05Z | a-2026-09-27-lead-gen-station-v2 | director-20260927-1308 | release |
| 2026-09-27T12:31:05Z | watcher | director-20260927-1308 | release |
| 2026-10-14T07:10:22Z | watcher | director-20261014-0810 | claim |
| 2026-10-14T07:10:48Z | watcher | director-20261014-0810 | release |
| 2026-10-20T11:09:33Z | watcher | director-20261020-1209 | claim |
| 2026-10-20T11:10:02Z | a-2026-10-20-crm-stage-2-brief | director-20261020-1209 | claim |
| 2026-10-20T11:26:40Z | a-2026-10-20-crm-stage-2-brief | director-20261020-1209 | release |
| 2026-10-20T11:26:40Z | watcher | director-20261020-1209 | release |
| 2026-10-21T13:10:05Z | watcher | director-20261021-1410 | claim |
| 2026-10-21T13:10:31Z | a-2026-09-27-owlbridge-sdr-standing | director-20261021-1410 | claim |
| 2026-10-21T13:19:58Z | a-2026-09-27-owlbridge-sdr-standing | director-20261021-1410 | release |
| 2026-10-21T13:19:58Z | watcher | director-20261021-1410 | release |
| 2026-10-22T07:00:12Z | watcher | director-20261022-0800 | claim |
| 2026-10-22T07:01:30Z | watcher | director-20261022-0801 | claim |
| 2026-10-22T07:04:02Z | watcher | director-20261022-0801 | release |
| 2026-10-22T07:06:45Z | watcher | director-20261022-0800 | release |
