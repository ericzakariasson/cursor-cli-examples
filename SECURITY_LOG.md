# Security Audit Log

Date: 2025-09-19
Repository: ericzakariasson/cursor-cli-examples
Audit branch: audit-hardening

## Scope
- Scanned tracked files for potential secrets (with support for allowlists like `.gitleaks.toml` if present).
- Scanned the last 90 days of commit diffs for common secret patterns.
- Audited GitHub Actions workflows for risky patterns (unpinned actions, overbroad/missing permissions, `pull_request_target` misuse, secrets exposure on forked PRs, deprecated commands like `::set-output`, etc.).

## Findings
- Secrets in working tree: none detected by high-signal pattern checks.
- Secrets in recent history (90 days): none detected.
- Workflows: none found in this repository at the time of the audit.

## Recommendations (minimal, safe defaults)
- When adding workflows:
  - Pin actions to immutable commit SHAs (not moving tags). Example:
    ```yaml
    uses: actions/checkout@<commit-sha>
    ```
  - Add a top-level `permissions:` block; default to least privilege (often `contents: read`). Grant write on a per-job or per-step basis only when required.
  - Avoid `pull_request_target` for untrusted code paths. Prefer `pull_request`. If `pull_request_target` is necessary, do not run or check out forked code before trust checks, and never expose secrets to untrusted code.
  - Do not use `secrets.GITHUB_TOKEN` with `write` in forked PR contexts unless strictly required and constrained.
  - Replace deprecated commands (`::set-output`, `::add-path`) with supported alternatives.
  - Consider adding a first step to harden the runner (e.g., network egress restrictions) and validate checksums for downloaded tools.
- Optional: add a repo-level `.gitleaks.toml` with allowlists for known test fixtures to reduce false positives.

## Next steps
- No redactions or workflow edits were required in this run.
- This branch (`audit-hardening`) contains only this log for traceability. If you want to adopt guardrails, open a PR from this branch and extend it with pinned workflow updates as you add workflows.

## Quick link to open a PR
- Compare and create PR: https://github.com/ericzakariasson/cursor-cli-examples/compare/main...audit-hardening?expand=1
