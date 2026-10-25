---
title: Approvals that stick
aliases: [Approve reverts on refresh, Undo window fix, Review settle fix]
type: spec
parent: "[[Console]]"
owner: the operator
updated: 2026-09-28
tags:
  - system
  - spec
---

# Approvals that stick

For a-2026-09-27-approvals-that-stick in [[Approvals]]. The operator, 27 Sep: approving a row on the platform did not seem to go through, and after a refresh the row was back among the approvals. Written by a Cowork session on 27 Sep from the live platform code; built on a `claude/` branch the next day and merged by the operator on 28 Sep.

## What was wrong

1. [Certain] **Approve, Decline and task ticks waited 8 seconds in the browser before anything was written** (the undo window in `public/app.js`). The held write lived only in page memory. A refresh, an app switch that ended the page, or the automatic reload after a new deploy inside those 8 seconds dropped it without a word, and the row came back on the next load. Nothing flushed it when the page closed.
2. [Certain] **A refresh of state during the window put the card back.** The loader replaced the whole state while an item was still pending, so an approved card reappeared until the write settled. The 5 minute timer, the refresh on returning to the tab and the Team poll all call the loader.
3. [Likely] **Done for review (Accept, Later) and Snooze could be lost or read stale.** Each was one shared map under one storage key, read and rewritten whole on every action, with eventual consistency. A refresh could show the old map, and two actions close together could overwrite each other.
4. [Certain] **The status write never retried.** It read `System/Approvals.md` and wrote it back against that version. If the watcher, Obsidian or a second approval moved the file in between, GitHub answered with a conflict and the approve failed.
5. [Likely] **No platform write had reached the vault for three days**, so the operator's recent approvals had never left the browser.

## The fix

Server, `netlify/functions/api.mts`:

1. Open the review and snooze stores with strong consistency.
2. Store one key per row (`row/<id>`) instead of the shared map, so two actions can never overwrite each other. Keep reading the old map as a fallback and fold it in, so nothing already settled comes back.
3. On a GitHub conflict, read the file again and reapply the change, up to three attempts.
4. The state route reads review and snooze state through the same strong stores, with no caching between requests.

Client, `public/app.js`:

5. When the page is hidden or closing, settle every pending undo item at once, sending its write with `keepalive` so it survives the page closing.
6. Keep the pending choices by row id and task id, and after every load apply them to the new state before rendering, so a refresh inside the window never shows the old status.
7. Never reload for a new deploy while anything is pending: settle first, then reload.
8. When a write fails, put the row back at its old status and keep the error on screen until the operator dismisses it.

## Acceptance

1. Approve a row and refresh within 2 seconds: the row stays approved and a `platform: queue <id> approved` commit lands.
2. Approve two rows 1 second apart: both commit and no conflict reaches the screen.
3. Accept three Done for review cards in a row, refresh at once and again after a minute: all three stay settled.
4. Snooze, then refresh: it stays snoozed.
5. Undo inside the window still cancels without any API call.
6. The test suite passes, with new tests for the retry and the per-row store.

## Related

[[Approvals]] · [[Console]] · [[The Brain build log]]
