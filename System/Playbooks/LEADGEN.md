---
title: LEADGEN
aliases: [SDR sweep, Lead gen run, Pipeline sweep]
type: playbook
parent: "[[MANAGE]]"
owner: the operator
updated: 2026-09-27
tags:
  - system
  - playbook
  - venture/owlbridge
---

# LEADGEN

The standing work of [[Owlbridge]]'s lead gen station, run by the [[Director]] through the [[SDR]] inside an ordinary watcher run. Started by the standing row a-2026-09-27-owlbridge-sdr-standing in [[Approvals]], which stays `in progress` for as long as the operator wants the pipeline worked. Added 27 Sep with lead gen station v2.

The station lives in `Wiki/Ventures/Owlbridge/Owlbridge growth/`: the pipeline table (`Owlbridge pipeline.md`), the activity log (`Owlbridge activity log.md`), the outreach drafts, the follow-up drafts, and the station note with the scoring rubric and the suppression list.

## Limits

- **Once a day.** Skip the sweep if the activity log already has a line by SDR dated today. Skip the batch unless today is Monday (London) and no LEADGEN batch line is dated this week.
- **Nothing leaves the building.** Drafts only. No send, schedule, contact, purchase or paid data.
- **No pile-up.** Skip the batch while 15 or more rows sit at researched or drafted: new leads are no use until the operator sends to the ones they have.
- **Cheap when idle.** If no row is due and it is not a batch day, write nothing and move on; the standing row's note is only rewritten when something moved.

## Part 1: sweep (daily)

1. Read the pipeline. Due rows: next date today or earlier, status drafted, sent, replied, call booked or proposal.
2. For each due row, by status:
   - **drafted:** the operator has not sent email 1 yet. Do not re-draft. If no open item exists, add one to [[Needs from the operator]] listing the drafted rows ("Send email 1 to these N leads from the drafts") and move each row's next date to the next weekday.
   - **sent:** if 4 or more days since the last touch and no email 2 is drafted, write email 2 for this lead into the follow-up drafts; at 10 days, email 3. Next step "The operator sends email N", next date today.
   - **replied, call booked, proposal:** write a one-page brief under the lead's heading in the follow-up drafts (who they are, what they said, what to ask, what to offer, the discovery call format) and set the next step to the call or the reply.
   - **researched with no contact route:** find a published work route (the business's own site, its contact page, the named owner's public business profile) and put it in the row's next step. Never guess an address.
3. Return per lead: the change to its row and one activity line (`type` draft, research or system, `by` SDR).

## Part 2: batch (Mondays)

1. Read the ideal client profile and the scoring rubric in the station note.
2. Find up to 10 UK owner-run local service businesses that fit (two to ten sites or a team of five to forty, the owner still making the marketing calls; dental, veterinary, physiotherapy, trades and home services; the East Midlands first), not already in the pipeline or on the suppression list, registered businesses only, never a sole trader's personal details.
3. Score each on the rubric with the evidence and its date; drop any under 60.
4. Write them as a dated section in a new note `Owlbridge lead list <YYYY-MM-DD>` beside the first list (why they fit, a buying signal with its source and date, the person who signs, a first line that is true on the day), and as rows in the pipeline with status researched, source `LEADGEN <date>`.
5. One activity line per new lead (`type` research, `by` SDR).

## Write-up

The Director applies the row changes, appends the activity lines, rewrites the standing row's note ("<date>: swept N due, drafted N follow-ups, added N leads; next: ..."), and tags the run log line with `dept=owlbridge` and `agents=SDR`.

## Idempotent

Keyed on the date for the sweep and the ISO week for the batch, both read from the activity log's SDR lines. A lead already in the pipeline or on the suppression list is never added again.

## Done when

Every due row has a new next step and date, the activity log has a line per lead touched, and the standing row's note says what moved, or the run log says "standing row: nothing due".

## Never

- Sends, schedules or queues any message, or contacts anyone.
- Changes the outreach words the operator approved; follow-ups are drafted beside them.
- Adds a business on the suppression list, or anyone's personal address.

## Related

[[SDR]] · [[MANAGE]] · [[Owlbridge]] · [[Director]]
