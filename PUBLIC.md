# This public copy

The working vault is private. This copy keeps its operating system whole and replaces every piece of
content with a fictional business, so the system can be read end to end:

- **Kept as built:** the constitution (`CLAUDE.md`), the permission tiers, the two kinds of text (current
  and history), the ledgers (Approvals, Corrections, Initiatives, Run log, Scout), the playbooks and
  their schedule, the team of agents and the Director pattern, the templates, the build-log and
  decision conventions, the Owlbridge lead pipeline's table format, the merge driver and lock scripts
  in `System/Setup/`, and the skills in `.claude/skills/`.
- **Replaced:** every project, person, brand, figure, lead, date of a real event and journal entry.
  Fernmoor Home Group, its brands, Owlbridge, Gaugewell, Paperwren and every lead named in the
  pipeline are invented. People appear only as roles ("the managing director", "the call-team lead").
  The owner is "the operator".
- **Left out:** the private vault's personal areas, its archives before September, its
  `_review/` folder, the Obsidian plugins' code and settings, and the GitHub workflow the private
  vault runs.

Where a note points at a repository, a site or an account (the Fernmoor Hub, the CRM, the ad
accounts), none exists: the note describes the fictional business.

## How this copy was checked

- A scan of every file and the commit for anything that identifies the publisher: names, initials,
  employers, brands, sites, repositories and account names from the private vault.
- fd-core's guardrails screen over every tracked file and the commit message, with the private deny
  list of the people, firms and places named in the private vault (the list itself is never
  published): no findings.
- Scans for email addresses, phone numbers, UK postcodes and em dashes: none.
- The platform in `brain-platform-demo` was run against this vault and every area checked in a
  browser.
