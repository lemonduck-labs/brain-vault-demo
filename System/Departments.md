---
title: Departments
aliases: [Department registry, Lanes]
type: system
parent: "[[Team]]"
owner: the operator
updated: 2026-09-24
tags:
  - system
  - agent
---

# Departments

The lanes the [[Director]] sorts work into and the platform's Team area draws. A new department is a new row here; the platform reads this table. Set on a Queue row in [[Approvals]] as its 12th cell, by id.

| id | name | colour | covers | repositories |
|---|---|---|---|---|
| owlbridge | Owlbridge | #3DDC84 | The consultancy: the lead gen station, the pipeline, outreach and follow-up drafts, Quillmere Dental's monthly work | the vault |
| fernmoor | Fernmoor | #A3E635 | Fernmoor Heating, Ridgeby Roofing and Warmstead, the Fernmoor Hub, the CRM rebuild, the call note pipeline, the director report | the vault, the Hub repository |
| brain | The Brain | #A78BFA | The platform, the vault, the queue, the team itself | the vault, the platform repository |
| ventures | Ventures | #34D399 | Gaugewell and Paperwren | the vault, the Gaugewell repository (not yet granted) |

## Rules the platform reads

The What we need more of panel on the Team area uses these thresholds. Change a number here and the panel follows.

| rule | threshold |
|---|---|
| access-bound | access blocks are more than half of a department's open rows |
| short of runs | average open-row age above 3 days and runs used at the daily budget on 3 of the last 5 weekdays |
| brief quality | Redo rate above 1 in 4 over 14 days, per specialist |
| near the cap | routine runs above 13 a day on 3 of the last 5 weekdays |

## Related

[[Team]] · [[MANAGE]] · [[Tools]]
