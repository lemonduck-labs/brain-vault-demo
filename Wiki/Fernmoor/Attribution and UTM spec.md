---
title: Attribution and UTM spec
aliases: [UTM spec, Tracking spec, UTM rules]
type: spec
parent: "[[Fernmoor]]"
owner: the operator
updated: 2026-10-05
tags:
  - project/fernmoor
  - domain/tracking
---

# Attribution and UTM spec

How every Fernmoor ad link is tagged, and how a lead keeps its source from the click to the CRM. The [[Fernmoor Hub]] parses these exactly as written here (PR 33), so a link that breaks the rules shows up in the Hub's "no source" list.

## The rules

| Parameter | Rule | Example |
|---|---|---|
| `utm_source` | The platform, lower case | `google`, `meta` |
| `utm_medium` | `cpc` for Search and Performance Max, `paid_social` for Meta | `cpc` |
| `utm_campaign` | `brand_channel_purpose`, lower case, underscores | `warmstead_search_heatpump` |
| `utm_content` | The ad or asset group, short | `explainer_v1` |
| `utm_term` | Search keyword, from the platform's own value | |

Brand prefixes: `fernmoorheating`, `ridgeby`, `warmstead`. Nothing else counts as a brand.

## How a lead keeps its source

1. The landing page stores the UTMs in a first-party cookie for 30 days.
2. The web form sends them as hidden fields.
3. The CRM stores them on the lead (stage 1 of the [[CRM rebuild]] made the brand field required).
4. The Hub reads source and brand from the lead.

> [!warning] Where it breaks
> - A lead that phones from the landing page has no form, so no UTMs. The Hub counts it as a lead, and gives it the brand of the number dialled and a source of "call".
> - Meta lead forms carry the campaign, not the UTMs. The Hub maps them by campaign name.

## Decisions

- **1 Oct** Campaign names carry the brand as the first word. Ruled out a separate brand parameter, which the platforms would not pass through to Meta lead forms.
- **5 Oct** Warmstead counts from zero: a lead before 5 Oct is never Warmstead, whatever its UTMs say.

## Related

[[Fernmoor Hub]] · [[Meta Ads]] · [[Google Ads]] · [[CRM rebuild]]
