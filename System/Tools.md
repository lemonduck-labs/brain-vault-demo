---
title: Tools
aliases: [Tools guide, Tools and agents, Which tool, Model routing]
type: system
parent: "[[Operating manual]]"
owner: the operator
updated: 2026-10-14
tags:
  - system
  - setup
---

# Tools

Which tool, agent and model the brain uses for which job, where scheduled work can run, and what needs the operator's yes. Set on 17 Sep 2026 and kept current since. Tools change, so every fact here carries the date it was checked; re-check before relying on one.

## How the brain picks

- **The vault first, then what the operator already has.** A tool already connected, or a setting already available, before anything new.
- **Reading and drafting are free; acting outside is the operator's call.** The tiers in [[Permissions]] apply to every tool below. Posting, publishing, deploying, sending and any change to a live campaign wait for their yes in chat, per action.
- **One source per figure.** Fernmoor's ad figures come from the [[Fernmoor Hub]]'s own API, which reads Meta Ads, Google Ads, GA4 and the CRM. No third-party connector is a reporting route.

## What each tool is for

| Tool | Use it for | Needs the operator's yes for |
|---|---|---|
| The [[Fernmoor Hub]] | Every Fernmoor ad and lead figure, all three brands; the director report's numbers | Any write to an ad account or the CRM |
| GitHub | The vault's sync, the platform, the Hub and Gaugewell repositories; `claude/` branches and pull requests | Merging to main |
| Netlify | Hosting the platform and the Hub; deploy previews | Deploys to production, settings, variables |
| GA4, Search Console | Site and search reporting for the brands and Owlbridge clients | Changing tracking, goals or properties |
| Notion, Google documents | Reading shared documents; drafts in a drafts folder | Sharing, or overwriting a file others use |
| Figma, Canva | Mockups, layouts and on-brand assets | Publishing or sharing externally |
| Mail and calendar (not connected) | See [[MAIL AND CALENDAR]] | Every send and every calendar change |

## Built into sessions

- Web search and page reading, with dated sources.
- The browser in the Claude app, and the operator's own signed-in browser, site by site. Never passwords, payments or account numbers.
- A shell on the Mac inside the vault and the code clones, and the cloud workspace for builds and tests.
- The brain's own skills in `.claude/skills/`: `brain-start`, `brain-run`, `brain-export`, `strategy-lens`.
- Sub-agents on a chosen model, below.

## Models and sub-agents

The operator's idea, 17 Sep: the main session manages the work and hands pieces to sub-agents on the right model, so the usage goes further.

- **The main session leads.** It plans, decides what to hand off, briefs each sub-agent, checks what comes back, and is the only one that writes to the vault or talks to the operator. In a cloud run, that is the [[Director]].
- **Briefs carry everything.** A sub-agent starts from nothing, so the brief holds the context, the sources to use, and the shape of the answer, with facts and judgement kept apart.
- **Parallel when independent, never for small jobs.** On a small task the brief costs more than the work.

Which model for what. Judgement, checked against real runs:

| Work | Model |
|---|---|
| Quick checks, pulling fields out of many notes, sorting and triage | Haiku |
| The daily loop (MORNING, EVENING, TIDY), web research with sources, first drafts, code changes with tests, bulk reading | Sonnet |
| Direction, decisions, the Director and its specialists, reviewing the operator's work, client-facing writing, final checks | Opus |

Evidence so far: on 17 Sep a tools research job ran as one Sonnet sub-agent in about eleven minutes, and the main session re-checked the highest-stakes claims before filing. On 25 Sep the operator moved every specialist to Opus after two Sonnet drafts of Owlbridge outreach needed a full rewrite.

Scheduled jobs run on one model each, set in each routine's own form ([[Scheduled jobs]]).

## Where scheduled work can run

Checked 17 Sep 2026 against Anthropic's documentation, and again on 14 Oct.

| Kind | Runs on | When the Mac sleeps | Notes |
|---|---|---|---|
| Local scheduled task (Claude app) | The Mac | Skipped, then one catch-up run on wake | Needs the app open and the Mac awake; model picked per task |
| Cloud routine | Anthropic's cloud, cloning the GitHub repositories it is given | Runs anyway | Minimum interval one hour; a daily cap on runs; pushes `claude/` branches; can be started by a web request with its own token; model picked per routine |
| Cowork task bound to the Mac | The Mac, through the Cowork link | Missed firings seen on 16 and 17 Sep | Not used for the brain's jobs |

Judgement, acted on 17 Sep: the jobs belong in cloud routines on the vault repository. They run with the Mac asleep, and the watcher can be started by the platform the moment the operator taps Approve.

## The routine cap

The Claude plan allows up to 15 routine runs a day (checked 14 Oct). A normal weekday uses nine on the schedule (seven watcher runs, morning and evening), ten on Scout days, leaving five or six for starts from the platform; taps within 90 seconds of a start usually share it. The "near the cap" rule in [[Departments]] warns when the days run close.

> [!warning] Two things to watch
> Routines are a preview feature, so limits can change without notice; re-check the cap monthly in [[TIDY]]. And a quiet watcher run still counts as a run, so the two-hourly schedule is the first thing to thin if the cap starts to bite. [Likely]

## Related

[[Permissions]] · [[Operating manual]] · [[Scheduled jobs]] · [[Team]] · [[Departments]]
