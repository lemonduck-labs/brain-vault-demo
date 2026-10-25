---
title: Team
aliases: [The team, Agent team, Org chart, Internal business team]
type: system
parent: "[[Operating manual]]"
owner: the operator
updated: 2026-09-27
tags:
  - system
  - agent
---

# Team

The brain works as an internal business team: a Director who manages, and specialists who do the work. The operator asked for it on 21 Sep: designers, developers, marketers, strategists, organisers and researchers, with one manager who delegates. How a run works is [[MANAGE]]; the design behind it is [[Agent delegation design]]; the platform's Team area draws this roster from the agent files.

## The team

| Role | Agent file | Does | Model | Writes to the vault |
|---|---|---|---|---|
| Director | [[Director]] | Triages the queue, briefs and dispatches specialists, reviews, writes up, reports to the operator | Opus | Yes, the only one during a run |
| Strategist | [[Advisor]] | Plans, pricing, positioning, offers, go or no-go, board review, the strategy lens | Opus | No, returns to the Director |
| Researcher | [[Researcher]] | Markets, competitors, prospects, dated facts with sources | Opus | No |
| Analyst | [[Analyst]] | Numbers, campaign performance, Hub figures, forecasts | Opus | No |
| Marketer | [[Marketer]] | Campaign plans, channels, audiences, search and content plans, ad structures | Opus | No |
| Copywriter | [[Editor]] | Copy, emails, scripts, reports, site words | Opus | No |
| Designer | [[Designer]] | Brand, UI, layouts, mockups as HTML, SVG or specs | Opus | No |
| Developer | [[Builder]] | Code in the platform, the Hub and Gaugewell, on `claude/` branches only | Opus | No; pushes branches in code repositories |
| Organiser | [[Chief of staff]] | Morning plan, evening review, the week, the monthly tidy | Opus | Only inside MORNING, EVENING, WEEKLY and TIDY |
| SDR | [[SDR]] | Works the Owlbridge pipeline daily: follow-up drafts, call briefs, contact routes; a weekly batch of new researched leads ([[LEADGEN]]) | Opus | No, returns to the Director |
| Reviewer | [[Reviewer]] | Checks every result against its source and the house rules before it is written | Opus | No |

Every specialist runs on Opus, at the operator's word on 25 Sep. Specialists are started by the Director as sub-agents inheriting its model, each reading its agent file as its standing brief ([[MANAGE]] step 5), so a role is changed by editing its file, with no code or routine change. The scheduled jobs that are not the Director's run on the model [[Scheduled jobs]] names.

## Standing work

Most rows are one-off. Work that repeats is carried by a standing row in [[Approvals]] that stays `in progress` so the Director picks it up on its normal runs, with the playbook setting how often it actually does anything. Today that is the Owlbridge pipeline (a-2026-09-27-owlbridge-sdr-standing: [[LEADGEN]], daily sweep, Monday batch, by the [[SDR]]). Added 27 Sep.

## How the team is run

- **Departments are lanes, roles are people.** Work is sorted into [[Departments]] (Owlbridge, Fernmoor, The Brain, Ventures) and done by role. The Designer works on an Owlbridge client report and a Warmstead landing page in the same week.
- **One manager, one routine.** The Director runs inside the approvals watcher routine, not one routine per department. One reader of the queue avoids double builds and spends one routine run per start, where four department routines would spend four.
- **Handovers go through the vault.** A specialist's work lands where its brief says; the next specialist reads it there. Nothing passes between agents that the vault cannot show.
- **Limits.** Routines run at most hourly, and the plan caps routine runs a day ([[Tools]]). The Director caps itself at five specialists at once.

## What the team cannot do from the cloud

No mail, calendar, Figma or Canva (the routines have no connectors), and no Mac. Work that needs them stays `in progress` with a "Needs:" label and is done in a Cowork or Claude Code session. Adding a repository to the routine's GitHub access widens what the Developer can reach.

## What the platform reads

The Team area reads four things and no other: the agent files' frontmatter (`role`, `colour`, `model`, `jobs`, `tools`, `goals`), [[Departments]] for the lanes and the thresholds, [[Watcher lock]] for live claims, and the tag on each DIRECTOR line in [[Run log]]. The routine cap comes from [[Tools]].

## Related

[[MANAGE]] · [[Departments]] · [[Agent delegation design]] · [[Watcher lock]]
