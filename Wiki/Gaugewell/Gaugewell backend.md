---
title: Gaugewell backend
aliases: [Gaugewell stack, Gaugewell architecture]
type: spec
parent: "[[Gaugewell]]"
owner: the operator
updated: 2026-10-18
tags:
  - project/gaugewell
  - venture/gaugewell
  - domain/engineering
---

# Gaugewell backend

How Gaugewell is built. Small on purpose: one import, five reports, one store.

## Shape

```
weekly CSV export  ->  import function  ->  store (one table per client)
                                              |
                                              v
                                  report functions (1 to 5)  ->  static pages
```

- **Front end**: static pages, one per report, server-rendered from the store.
- **Functions**: on Netlify. One import function, one function per report.
- **Store**: a small hosted database, one table per client, weekly rows only.
- **Model**: report 5 (the Monday summary) will use Haiku to write a few sentences from the four tables. Every figure in the words is checked against the tables before it renders.

## Rules

- No lead-level data. The import refuses a file with a name, email or phone column.
- A client's figures never leave their table.
- Every report states its count ("form fills") and its week.

> [!warning] Gotchas
> - The export's week runs Monday to Sunday, London time. A file read on a Sunday evening holds a part week.
> - A brand with no spend in a week still gets a zero row, or the charts skip it.

## Related

[[Gaugewell]] · [[Gaugewell internal trial]] · [[Gaugewell build log]]
