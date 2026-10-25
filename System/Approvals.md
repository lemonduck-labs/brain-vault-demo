---
title: Approvals
aliases: [Approval queue, The queue]
type: log
owner: the operator
updated: 2026-10-22
tags:
  - system
---

# Approvals

The queue. Requests from the operator (platform, chat or a task sent for approval) land as `requested`; a session or the approvals watcher scopes each into a proposal and sets it to `pending`; nothing runs before the operator approves. `approved` means carried through to finished, not re-scoped. Statuses: `requested`, `pending`, `approved`, `in progress`, `done`, `declined`. Settled rows move to `System/Archive/Approvals YYYY-MM.md` at the start of each month.

## Queue

| id | status | title | detail | cost | reversible | source | requested | decided | note | priority | department |
|---|---|---|---|---|---|---|---|---|---|---|---|
| a-2026-10-22-routine-times | pending | Reset the five cloud routine schedules for the clocks going back | British Summer Time ends Sun 25 Oct. The routines are scheduled in UTC, so from Monday every one runs an hour early by the wall clock: MORNING at 06:00, EVENING at 17:30. The brain would list each routine's new UTC time in [[Scheduled jobs]]; changing a schedule is a standing configuration, so the change itself is the operator's click, about five minutes. | None | yes | MORNING | 2026-10-22 |  | Waiting on the operator's yes. Est: 5 minutes. Needs: the operator's decision | P1 | brain |
| a-2026-10-21-warmstead-cpl-read | pending | Warmstead budget step: move £300 a week from Meta to Search | Agreed in principle at the 19 Oct meeting, pending two weeks of CPL and a check of the 47 leads against the CRM, which the managing director asked for because the Hub counts calls as leads. Both are done: 5 to 18 Oct, Search £520, 18 leads, CPL £28.89; Meta £1,040, 29 leads, CPL £35.86; the CRM agreed on 22 Oct. If approved, Search goes from £260 to £560 a week and Meta from £520 to £220, from Mon 26 Oct. The change in the ad accounts is the operator's click. | None: £300 a week moves inside the existing budget | yes, the next week | Platform, the operator | 2026-10-21 |  | 21 Oct 14:10, DIRECTOR: Analyst briefed. 22 Oct 10:30: CRM check done and the split read from the Hub on the Mac; detail in [[Warmstead launch plan]]. Waiting on the operator's yes. Needs: the operator's decision | P1 | fernmoor |
| a-2026-10-20-crm-stage2-brief | done | Write the stage 2 brief for the CRM contractor | Stage 1 (lead routing and the brand field) handed over 20 Oct. Stage 2 is the call team's task types and the next-step rules. The brief lists what is decided, what the sales manager and the call-team lead still have to agree, and what done looks like, for the operator to send. | Claude time only | yes | chat | 2026-10-20 | 2026-10-20 | 20 Oct 16:40: brief written in [[CRM rebuild]] and sent by the operator the same afternoon. Task types due from colleagues by 23 Oct. | P2 | fernmoor |
| a-2026-10-19-hub-pr-review | approved | Review Hub pull requests 40 and 42 before anything new is built | Five pull requests in two days; 41 needed a rebase after 39 merged under it. The Reviewer reads each open PR against the live Hub, lists what it changes and what could regress, and the operator merges. | Claude time only | yes | WEEKLY | 2026-10-19 | 2026-10-20 | 20 Oct: approved in chat ("yes, do the review first"). 40 reviewed 21 Oct, two small fixes pushed to the branch. 42 next. Est: 30 minutes | P1 | fernmoor |
| a-2026-10-19-owlbridge-two-replies | pending | Draft replies to the two Owlbridge leads who answered this week | Brackenfold Joinery and Orrin Valley Physio both replied on 19 and 20 Oct asking what a first month looks like. The SDR drafts a reply to each with two call slots; sending is the operator's. | Claude time only | yes, drafts only | LEADGEN | 2026-10-20 |  | Drafts are in [[Owlbridge follow-up drafts]]. Waiting on the operator's yes to send. Needs: the operator's decision | P1 | owlbridge |
| a-2026-10-16-call-note-gdpr | in progress | Prepare the GDPR pack for call content in the call note pipeline | The pipeline writes call metadata (time, length, outcome, next step) today. Summarising what was said needs the managing director's sign-off: a data protection impact assessment, the retention period, and the line added to the call script. The brain drafts all three for the operator to take to the managing director. | Claude time only | yes | chat | 2026-10-16 | 2026-10-16 | 16 Oct: the three drafts are in [[Call note pipeline]]; the operator took them to the managing director the same day. Waiting on the sign-off. Needs: someone else's decision | P2 | fernmoor |
| a-2026-10-14-owlbridge-followups | done | Follow-up drafts for the eight leads with no reply after seven days | LEADGEN marked eight leads due. The SDR drafts a second touch for each in the tone of voice note; the operator sends what they like. | Claude time only | yes, drafts only | LEADGEN | 2026-10-14 | 2026-10-14 | [dept=owlbridge; agents=SDR,Editor] 14 Oct: eight drafts written; the operator sent six on 15 Oct and two replied by 20 Oct. | P2 | owlbridge |
| a-2026-10-12-gaugewell-trial-reports | in progress | Gaugewell: render the five trial reports from the Hub's exports | The internal trial reads last month's exports. Three of five reports render (spend by brand, CPL by channel, leads by day). The Builder adds the survey-rate and weekly director views. | Claude time only | yes | Platform, the operator | 2026-10-12 | 2026-10-12 | 18 Oct: three reports render. The last two need the exports-or-API decision in [[Gaugewell internal trial]]. Needs: the operator's decision | P3 | ventures |
| a-2026-10-08-director-report-draft | done | Draft the Monday director report from the Hub every week | All three brands, the Hub's figures, the week against the one before, three lines of commentary. The operator checks and sends it. | Claude time only | yes | chat | 2026-10-05 | 2026-10-05 | Running since 12 Oct. The 19 Oct draft was sent unchanged. | P2 | fernmoor |
| a-2026-10-05-warmstead-launch-checks | done | Warmstead launch checks before the ads go live | Tracking on both forms, the brand field in the CRM, the call routing, the campaign names in the UTM spec, and the Hub's new brand view | Claude time only | yes | chat | 2026-10-02 | 2026-10-02 | [dept=fernmoor; agents=Analyst,Reviewer] All five passed at 08:40 on 5 Oct, before the ads went live. | P1 | fernmoor |
| a-2026-10-02-quillmere-onboarding | done | Onboard Quillmere Dental as Owlbridge's first client | Access checklist, the first month's plan, the reporting page and the monthly review agenda | Claude time only | yes | chat | 2026-10-02 | 2026-10-02 | [dept=owlbridge; agents=Marketer,Editor] Plan and checklist sent by the operator on 3 Oct. | P2 | owlbridge |
| a-2026-09-27-owlbridge-sdr-standing | in progress | Standing: the SDR drafts Owlbridge follow-ups when LEADGEN marks them due | A standing approval for drafts only: when a lead's next date passes, the SDR drafts the next touch from the sequence in [[Owlbridge follow-up drafts]]. Sending stays the operator's, every time. | Claude time only | yes, drafts only | chat | 2026-09-27 | 2026-09-27 | Standing row, never closed. Last used 21 Oct: email 3 drafted for four leads. | P3 | owlbridge |
| a-2026-10-07-paperwren-second-collection | declined | Paperwren: plan a second collection of twelve prints | Proposed by WEEKLY to lift orders before December. | About £60 in samples | yes | WEEKLY | 2026-10-04 | 2026-10-07 | Declined 7 Oct: "Not until Owlbridge has a second client." Parked in [[Now]]. | P4 | ventures |
| a-2026-10-06-platform-domain | declined | Buy a custom domain for the brain platform | Raised when the platform went live. | About £12 a year | yes | Platform, the operator | 2026-09-17 | 2026-10-06 | Declined 6 Oct: "The netlify address is fine." | P4 | brain |

## Notes

Notes the operator writes on tasks from the platform. Already-approved work: the watcher or the evening review picks each one up.

| id | status | task | note | file | line | added | done | outcome |
|---|---|---|---|---|---|---|---|---|
| n-2026-10-21-warmstead-split | done | Read Warmstead's CPL for 12 to 18 Oct in the Hub | Split it by Meta and Search, I want to see which one is dragging | Now.md | 47 | 2026-10-21 | 2026-10-21 | Added to the read in a-2026-10-21-warmstead-cpl-read. |
| n-2026-10-20-ridgeby-negatives | done | Ridgeby Roofing Search restructure | Add "jobs" and "course" as negatives before it goes live | Wiki/Fernmoor/Ridgeby Roofing.md | 38 | 2026-10-20 | 2026-10-20 | Both added to the shared negative list before the 21 Oct launch. |
| n-2026-10-22-quillmere-review | asked | Quillmere Dental first monthly review | Ask about the two practice owners they mentioned | Wiki/Ventures/Owlbridge/Quillmere Dental.md | 30 | 2026-10-22 |  |  |

## Related

[[Permissions]] · [[MANAGE]] · [[Director]] · [[Needs from the operator]] · [[Run log]]
