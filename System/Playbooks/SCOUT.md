---
title: SCOUT
aliases: [Research loop, Innovation scan, Web scout]
type: playbook
parent: "[[Operating manual]]"
owner: the operator
updated: 2026-09-21
tags:
  - system
  - playbook
---

# SCOUT

The outward-looking loop. Researches the world around what the operator is actively working on and brings back what is genuinely useful: a competitor move, a platform change, a technique, a regulation, a tool, an approach nobody in their lane is using yet. Asked for on 16 Sep: the brain should scan the web to learn about the operator's work and find new approaches, with no ceiling on what that improves. Runs Monday, Wednesday and Friday at 12:00 as a cloud routine, and on demand with "run SCOUT" (optionally scoped: "run SCOUT on Gaugewell"). Roles: [[Researcher]] for the finding, [[Advisor]] for the "so what", [[Analyst]] sourcing rules for any figure.

## Where it looks

Driven by the top of [[Now]] and the active project notes, not by a fixed list. In October that means: retrofit and heat pump advertising and the rules around grant-funded work for [[Warmstead]]; paid search and Meta changes that affect home improvement lead costs for [[Fernmoor]]; how small growth consultancies find and keep owner-run clients for [[Owlbridge]]; the marketing reporting market around [[Gaugewell]]; and AI agent practice that improves the brain itself.

## Steps

1. Read [[Now]] and the project notes updated in the last fortnight; pick the areas where new information changes a live decision. A scoped run skips this and takes the named area.
2. Research each properly: the platform's own documentation and announcements, primary studies, regulator publications, credible trade press. Competitor sites are evidence of competitor behaviour only. Every finding carries its source and the date checked.
3. Keep only findings that pass the "so what" test: it changes a decision, opens an approach, or removes work. One to three per run, never a link dump.
4. For each finding, one row in the Findings table of [[Scout]]: `id | status | title | summary | url | source date | project | found`, id `s-YYYY-MM-DD-slug`, status `new`, a two-sentence summary saying why it matters to the operator specifically.
5. A finding that demands action becomes a proposed task or an approval request, clearly marked as a proposal; it never lands in [[Now]] uninvited.
6. Kept findings (the operator presses Keep on the platform) are woven into the relevant project note by the next [[WEEKLY]]; dismissed ones are never resurfaced.
7. Run log line as usual.

## Idempotent

Keyed on the date and the job name. A finding whose url is already in [[Scout]], in any status, is not written again.

## Done when

The run log has the line, and either new rows are in [[Scout]] or the line says "nothing that changes a decision".

## Never

- Pads. A run with nothing worth keeping reports "nothing that changes a decision", which is a finding.
- Repeats a dismissed finding or re-argues it.
- Presents speculation as a finding. [Certain], [Likely] and [Guessing] apply here too.
- Quotes a figure without its primary source and date.

## Related

[[WEEKLY]] · [[Advisor]] · [[Researcher]] · [[Analyst]] · [[Principles]]
