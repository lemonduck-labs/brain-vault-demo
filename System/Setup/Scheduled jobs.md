---
title: Scheduled jobs
aliases: [Job schedule, Automation schedule, The timetable]
type: system
parent: "[[Operating manual]]"
owner: the operator
updated: 2026-10-22
tags:
  - system
  - setup
---

# Scheduled jobs

The timetable, the state each job is in, and how a run is checked. Times are Europe/London. Since 17 Sep the jobs run as **cloud routines** on the GitHub copy of the vault, so the Mac, the app and folder access no longer matter; the set-up and the exact instructions are in [[Set up the cloud routines]].

## The timetable

| Job | Playbook | When (UK time) | Where it runs | Model | State on 22 Oct |
|---|---|---|---|---|---|
| Morning plan | [[MORNING]] | 07:00 Mon to Fri | Cloud routine | Sonnet | Running since 18 Sep |
| Evening review | [[EVENING]] | 18:30 Mon to Fri | Cloud routine | Sonnet | Running since 17 Sep |
| Weekly direction | [[WEEKLY]] | Sunday 17:00 | Cloud routine | Opus | Running since 20 Sep |
| Scout | [[SCOUT]] | Mon, Wed and Fri 12:00 | Cloud routine | Opus | Running since 21 Sep |
| Tidy | [[TIDY]] | First Sunday of the month, 07:30 | Cloud routine | Sonnet | First run 4 Oct |
| Approvals watcher and DIRECTOR | [[MANAGE]] | Every two hours 08:00 to 20:00 Mon to Fri, plus each start from the platform | Cloud routine | Opus | Running; quiet runs write one "Nothing waiting" line |
| Board review | [[BOARD REVIEW]] | First Monday of the month, 08:30 | Cloud routine | Opus | First run 5 Oct |
| Owlbridge pipeline | [[LEADGEN]] | Inside the DIRECTOR's runs, as a standing row | Inside the watcher | Opus | Standing row since 27 Sep |

> [!warning] The clocks go back on Sunday 25 Oct
> Every routine's schedule is saved as a cron expression in UTC, including the ones set with a preset in UK time (the saved morning routine reads `0 6 * * 1-5`). When British Summer Time ends on 25 Oct 2026, every routine runs an hour earlier by the wall clock (morning 06:00, evening 17:30, weekly 16:00, scout 11:00, tidy 06:30, watcher 07:00 to 19:00, board review 07:30) until each time is set again, one hour later in UTC. This is on the operator's list for this week in [[Needs from the operator]]. They move back when the clocks go forward in March.

The queue the jobs read and write is [[Approvals]] in the vault, shown on the platform ([[Console]]). Each routine sends a push notification to the operator's phone when it finishes: the plan in the morning, the review in the evening, the direction on Sunday.

## What each routine does

Each prompt is standalone: it names the vault repository, tells the session to read the root `CLAUDE.md` first, then the named playbook and agent brief, do exactly what they say, write the run log line, and send the operator the result as a short message. The prompts repeat the hard rules (British English, no em dashes, no invented numbers, never reorder the top three, never move, rename or delete, nothing sent or spent). The live instructions are in each routine and copied in [[Set up the cloud routines]]; to recreate one, the playbook is the spec and the instructions are a wrapper around it. A run clones the vault from GitHub and pushes a `claude/` branch, which a GitHub Action merges into main.

## How a run is checked

1. Every job writes a line to [[Run log]] when it finishes.
2. [[MORNING]] looks for yesterday's expected lines. Missing lines are reported at the top of the plan.
3. [[WEEKLY]] counts missed and failed runs for the week.
4. Three failures in a row put the fix into [[Now]] as `#next`.

Each routine's own history shows whether a run started and finished, and a green status there does not mean the job succeeded; the run log shows whether it did its job. Both are needed.

## Usage

A normal weekday uses nine routine runs on the schedule (seven watcher runs, morning and evening), ten on Scout days, plus one for each start from the platform. The cap is in [[Tools]]; the "near the cap" rule in [[Departments]] warns before it bites.

## Run lock

Built 24 Sep after two watcher runs started minutes apart on 23 Sep and worked the same rows twice. `System/Setup/watcher-lock.py` claims the queue for one run: it pushes a claim row to [[Watcher lock]] on a `claude/` branch, waits for the merge Action to carry it into main, then reads the ledger again; the earliest live claim wins and any other run stands down before it touches the queue. The run releases in its own last commit, and a claim that is never released goes stale after 90 minutes. Tested on 24 Sep with two runs started a second apart: the second stood down, and a third claimed cleanly after the release. `--key` lets the same ledger lock one row rather than the whole queue, which is how [[Agent delegation design]] keeps two agents off the same build.

## Related

[[Run log]] · [[Vault sync]] · [[Operating manual]] · [[Set up the cloud routines]]
