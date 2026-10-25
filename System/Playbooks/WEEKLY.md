---
title: WEEKLY
aliases: [Weekly review, Weekly direction, Sunday reset]
type: playbook
parent: "[[Operating manual]]"
owner: the operator
updated: 2026-10-14
tags:
  - system
  - playbook
---

# WEEKLY

The reset. Rewrites the ranking, writes the direction brief for the week ahead, and does the promotion pass that turns corrections into rules. Runs Sunday 17:00 as a cloud routine, or on demand. Roles: [[Chief of staff]] for the brief, [[Advisor]] for the decisions due. [[BOARD REVIEW]] runs on its own on the first Monday of the month and reads this note.

## Reads

0. **Is the copy whole and fresh?** As in [[MORNING]] read 0. A week planned from a copy days behind the Mac ranks the wrong things: on 11 Oct the weekly asked the operator to publish a Hub change that had been live for three days.
1. The daily notes of the week just ended, and the **Priorities** in this week's note.
2. Every project note and build log with `updated` inside the week.
3. [[Now]] as it stands.
4. [[Corrections]]: the live ledger since the last promotion pass.
5. [[Run log]]: every expected run this week, and which are missing.
6. Project notes not updated for 14 days or more (stale check).
7. [[Scout]]: rows set to `kept` or `dismissed` since last Sunday.
8. `Revenue lever.md`: the named lever, and the Suggested, Accepted and Struck log.

## Steps

1. Create `Journal/Weekly/<year>-W<week>.md` from `Templates/Weekly review.md` if it does not exist; otherwise update in place.
2. **What moved.** From the build logs and daily reviews, with evidence. No adjectives.
3. **What slipped.** Plan items carried more than twice, blocked items older than three weeks, stale project notes. The honest reason, where the record shows one.
4. **Direction.** The three things for next week, ranked, and one thing to stop or drop. This is the section [[Home]] embeds; write it so it stands alone.
5. **Suggested priorities for the week ahead.** Create next week's note, `Journal/Weekly/<year>-W<next week>.md`, from the template if it does not exist (its other sections stay as the template has them until next Sunday), and under its **Suggested priorities** write three to five tasks that carry out the Direction, most important first, in the daily form: `- <a task's words exactly, without tags> · [[<its note>]]`, or a one-off `- <what to do>` only when a Direction item has no task, each with an indented `- Why:` line. Unfinished **Priorities** from the week just ended come first where they still matter. Never write in **Priorities**.
6. **Decisions due.** Every `#decision` in the vault with the Advisor's recommendation in one line each, and the rejected alternative.
7. **Rewrite [[Now]].** The "This week" three, the ranking table, the Waiting sections: overwrite each row with its current state rather than adding dated updates. Any change to the top three is explained in the weekly note. Then bring [[State]]'s goals table and This week into line.
8. **Promotion pass.** Any correction that appears twice in [[Corrections]], or once with "always" or "never" from the operator, is promoted to [[Principles]], the root `CLAUDE.md` (with the operator's yes) or the relevant project note, and the ledger line is annotated with where it went.
9. **Profile pass.** Anything the operator said about themselves or their standards this week goes into [[Operator]] "On the record". Nothing inferred.
10. **Runs.** List missed and failed runs from [[Run log]]; if a job failed three times in a row, add the fix to [[Now]] as `#next`.
11. **Scout.** Rows the operator set to `kept` in [[Scout]] are woven into their project notes now, and the week's findings are mirrored in the weekly note under a "Scout" line. `dismissed` rows are never resurfaced. The research itself is [[SCOUT]], on its own schedule.
12. **Approvals.** Execute `approved` rows in [[Approvals]] within [[Permissions]] and set them to `done`; write the week's decisions due as new `pending` rows where the brain can act on them.
13. **Growth.** One suggestion in the weekly note under "Growth": what in the week's record prompted it, and a first step small enough to do next week. Update [[Growth]]: accepted threads get a next action, struck ones are dated. One suggestion, not five.
14. **Revenue suggestions.** Proactive actions against the operator's own goal of £3,000 a month by March 2027, for their approval rather than them having to start each one. Read the current named lever and the state of [[Owlbridge]], [[Gaugewell]] and [[Paperwren]] that week; write up to three ranked suggestions in the weekly note under "Revenue suggestions", each with the evidence behind it and a first step small enough for the week, the same shape as Growth. Mirror them into the Suggested list in `Revenue lever.md`. A suggestion the operator accepts moves to Accepted with a `#next` action; one they strike is dated and not repeated. Anything that would send, spend or reach a client goes to [[Approvals]] as `pending` instead of straight into Accepted. None at all is a valid week if nothing in the record earns one.
15. **Initiative review.** Raise up to three prompts for the week ahead under the lens in [[Advisor]], ranked, each logged in [[Initiatives]]. Then read the last four weeks of [[Initiatives]], count by type and response, and write one line under "Learned": which kinds the operator acts on, which they ignore, and what changes in how the brain raises them. Added 23 Sep.
16. Write the run log line.

## Output

One screen. The Direction section is the part the operator reads if they read nothing else.

## Idempotent

Keyed on the ISO week and the job name. Sections are updated, never duplicated.

## Done when

The weekly note has all its sections, [[Now]] is dated this Sunday, the promotion pass is recorded, and the run log has the line.

## Never

- Reorders the top three silently.
- Promotes a correction that appeared once without an "always" or "never".
- Adds a line to [[Operator]] that the operator did not say.
- Writes more than three Revenue suggestions, or invents one with no evidence in the week's record.
