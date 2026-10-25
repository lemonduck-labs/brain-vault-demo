---
title: Live run status patterns
aliases: [Run status UI, What is Run doing]
type: system
parent: "[[Console]]"
owner: the operator
updated: 2026-09-19
tags:
  - system
  - guide
---

# Live run status patterns

For a-2026-09-18-run-status in [[Approvals]]. The operator, 18 Sep: after pressing Run Claude now on the platform, nothing on screen said what the run was doing, and five minutes passed with no sign it had started. Research into how agent tools show work in progress, then a shortlist, then what was built.

> [!question] Not independently verified
> The patterns below come from a web search on 18 Sep, read from the results' own summaries rather than full pages. Treat them as a starting shortlist, and re-read the source of any pattern before building on it.

## Named patterns for this kind of interface

1. **Progress steps.** An agent's intermediate work (tool calls, searches, files touched) shown as a collapsible trace, collapsed by default to keep the screen calm, expanding on demand.
2. **Live step list.** What the agent is doing now and what it has finished, each step marked pending, active, done or failed, with a link to the result where there is one. Called a task list, an activity feed or a checklist depending on the product.
3. **Activity panel.** A dedicated panel for work in progress, apart from the chat or the log, so it does not get lost in a scrolling transcript.
4. **Live-updating single entry.** A long step does not sit frozen: one entry updates in place from "started" through to "complete" rather than adding a new line each time.
5. **Status chips.** A compact coloured label (queued, running, done, failed) next to each item in a list, for a glance across many runs rather than the detail of one.

## Shortlist for the Run button and the Runs area, ranked

Claude's read, for the operator's decision. [Guessing] on fit to this platform, since none of the sources was read in full.

1. **A status chip on the Run button while it runs**, plus a step list underneath once clicked. Smallest build, closest to the existing Runs area.
2. **A live step list in the Runs area**, one line per step the current run is on ("reading Approvals", "briefing the Analyst", "writing the review"), the current step highlighted, past steps ticked.
3. **A dedicated activity panel** for the full trace of a run. More building than the platform needs today; worth it only if runs grow more complex.

## What was built, 19 Sep

Pattern 4, the live-updating single entry: a bar under the header from the moment a run is started, showing the elapsed time while it runs, then the run's own log line once it lands, with the page refreshing itself underneath.

What it does not do is the step list (patterns 1 and 2), and that is a limit of where the work happens rather than a choice: a cloud run holds its own clone and pushes once at the end, so the platform has nothing to read between the start and the push. A step list would need each run to write its current step somewhere the platform can poll as it goes. The Team area's live claims from [[Watcher lock]], added 24 Sep, are the nearest thing so far: they show which rows a run holds while it runs, because each claim is pushed when it is made.

## Related

[[Console]] · [[Approvals]] · [[Run log]] · [[Watcher lock]]
