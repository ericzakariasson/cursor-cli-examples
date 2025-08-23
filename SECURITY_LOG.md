# Security Hardening Log

Date: 2025-08-23
Branch: `audit/hardening`

Summary of minimal changes proposed to improve workflow security and reduce supply-chain risk.

## Proposed changes
- Pin reusable actions to immutable commit SHAs in workflows:
  - `actions/checkout@08eba0b27e820071cde6df949e0beb9ba4906955` (v4)
  - `actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065` (v5)
- Add `permissions: contents: read` to `test` workflow to follow least-privilege.
- Add fork-guard conditions to PR-triggered workflows to avoid running with repo secrets on forked PRs:
  - `auto-update-docs.yml`, `auto-update-docs-split.yml`, `auto-improve-pr-description.yml`.

## Rationale
- Pinning actions prevents silent supply-chain drift and mitigates takeover risks of action tags.
- Least-privilege permissions reduce blast radius for default token.
- Fork guards ensure steps that access `secrets` or write to the repo don't execute for untrusted forks.

## Findings
- No hardcoded secrets found in tracked files or recent history scan (sampled regexes for common providers and tokens).
- No use of `pull_request_target` events detected.
- Existing workflows already set explicit `permissions` where writes are needed.

## Notes
- This branch avoids direct workflow edits due to missing `workflows` permission on the automation token. Apply the above edits in a follow-up PR or grant `workflows` permission and re-run.
