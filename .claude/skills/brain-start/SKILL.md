---
name: brain-start
description: Load the Brain (this Obsidian vault) at the start of any Claude Code session on the operator's work, Fernmoor, Owlbridge, Gaugewell, Paperwren or the Brain itself, so the session continues the work instead of starting over.
---

# Brain start

Run this at the start of any session that touches the Brain, the Fernmoor day job (Fernmoor Heating, Ridgeby Roofing, Warmstead, the Fernmoor Hub, the CRM), Owlbridge, Gaugewell or Paperwren. The vault is the master record and the operating system; Claude's own memory holds only what stays true for months. A session that has not read the vault will repeat old mistakes and start from an old picture.

## Where the vault is

The vault root is the folder that holds `CLAUDE.md`, `AGENTS.md` and `.obsidian/`. In Claude Code it is the working directory, so paths below are relative to it. Read with the Read tool or plain shell reads (`cat`, `grep`); never copy notes elsewhere just to read them. Do not run git commands on the vault except `git log`, `git show`, `git rev-list` and `git check-attr`.

## Read, in this order, and no more than the task needs

0. Is the vault whole? If `conflict-files-obsidian-git.md` exists at the root, or a note carries `<<<<<<<` lines, report that before anything else.
1. `CLAUDE.md`: the constitution. Follow it for the whole session.
2. `System/State.md`: one screen with the four goals, this week's three, what is live, what waits on the operator, and the known gaps. Treat anything it marks stale as stale.
3. `System/Corrections.md`: the last twenty lines.
4. Only then what the task needs: `Now.md` for the ranked list, `System/Operator.md` for the profile and standards, the project note and the newest entries of its build log (`Wiki/Fernmoor/`, `Wiki/Gaugewell/`, `Wiki/Ventures/`), `System/Approvals.md` rows by id rather than the whole table, and `Wiki/CLAUDE.md` before writing any note.

Every file read costs the operator's usage. Read less, read the right thing.

## Then

- State in one line what the vault says the current state and next action are, before doing anything, so the operator can correct it.
- **Initiative.** If the reading shows something the operator has not asked about that matters now, raise it: at most one prompt at the start of a session. Types: drift (a top three item untouched for seven days), slip (carried over three times), stale (a plan, figure or status older than its use allows), contradiction (what is being done differs from what the operator said matters), opportunity (serves a stated aim), risk (bites inside fourteen days). Shape: what you noticed, the evidence, the recommended move, the cost of ignoring it. Log it as a row in `System/Initiatives.md` with the response left blank. Nothing worth raising is a fine answer; never raise filler.
- Apply the `strategy-lens` skill (method in `System/Agents/Advisor.md`) to any plan, decision or advice.
- Work within `System/Permissions.md`: free inside the vault, drafts outside, an explicit yes for anything that sends, publishes, spends, merges, moves, renames or deletes. The operator's own builds (the brain platform, the Fernmoor Hub, Gaugewell) are built on a `claude/` branch with a pull request on their ask; merging is theirs.
- Fernmoor ad figures come from the Fernmoor Hub only. Warmstead counts from 5 Oct 2026.
- Problems first, with [Certain], [Likely] or [Guessing]. British English, no em dashes anywhere, no invented numbers, the operator's view kept separate from Claude's.
- If the session changes a priority, a decision or a build, overwrite the matching line in `System/State.md`.
- Finish the session with the `brain-export` skill.
