---
title: Claude Code workflow
aliases: [Repo workflow, How the repos are worked on]
type: reference
parent: "[[Operating manual]]"
owner: the operator
updated: 2026-10-14
tags:
  - system
  - setup
---

# Claude Code workflow

How the code repositories are worked on: the [[Fernmoor Hub]], the brain platform and [[Gaugewell]].

## The route

Git and the GitHub command line tool are on the Mac. Code repositories are cloned outside the vault, in a `_code/` folder beside it, so the vault holds notes only. A session branches (`claude/<what>`), builds, runs the tests, pushes and opens a pull request; Netlify builds a deploy preview; the operator reviews the preview and merges. Merging is the step that publishes. The current route for each repository is the table under "Where the work lives" in the root `CLAUDE.md`, kept there only.

The cloud routines follow the same route for code: the Director's Developer pushes a `claude/` branch in the repository named in its brief and raises the pull request as "Waiting on you: review and merge" in [[Approvals]].

## Rules on any repository

- Read the repository's own `CLAUDE.md` before the first edit.
- Branch, never main. A prepared change waits for the operator's merge ([[Permissions]] tier 3).
- Check a pull request is still open before pushing more to it; a branch whose pull request was merged starts again from main.
- No em dashes in code, comments, commit messages or file names.
- Every change gets a build log entry in the vault through [[SESSION EXPORT]], with the version or pull request number.
- Read state back after a deploy. A green build is not evidence the feature works.

## Related

[[Builder]] · [[Fernmoor Hub]] · [[Gaugewell]] · [[Vault sync]]
