# Security Hardening Log

Date: 2025-11-23
Branch: audit/workflow-hardening

Summary of actions
- Pinned GitHub Actions to immutable commit SHAs:
  - actions/checkout@v4 → 34e114876b0b11c390a56381ad16ebd13914f8d5
  - actions/setup-python@v5 → a26af69be951a213d495a4c3e4e4022e16d87065
  - actions/upload-artifact@v4 → ea165f8d65b6e75b540449e92b4886f43607fa02
  - astral-sh/setup-uv@v4 → 38f3f104447c67c051c4a08e39b64a148898af3a
- Added default minimal token permissions to `.github/workflows/test.yml`:
  - permissions: contents: read
- Added guardrails to PR-triggered workflows that require secrets to avoid running on forked PRs without secrets:
  - `visual-testing.yml`, `code-review.yml`, `translate-keys.yml`, `update-docs.yml`
  - Condition: `${{ secrets.CURSOR_API_KEY != '' }}` included in job `if`

Findings
- Potential secrets in tracked files: none detected via heuristic scan.
- Risky workflow patterns:
  - Unpinned actions: fixed (now pinned to SHAs).
  - Missing permissions: fixed in `test.yml`.
  - pull_request_target usage: none found.
  - Deprecated commands (`::set-output`, `add-path`): none found.
  - Secrets in forked PR contexts: guarded via job-level `if` checks.

Notes
- Git history secret scan was not executed due to lack of ripgrep in the runner. Consider enabling a scheduled scanner such as `gitleaks` with a repository-managed allowlist (e.g., `.gitleaks.toml`).

Remediation guidance
- Keep actions pinned to SHAs; update pins periodically.
- Declare minimal top-level `permissions` in all workflows; elevate only per job when needed.
- Avoid `pull_request_target` unless absolutely necessary; if used, never run untrusted code or expose secrets.
- Prefer `$GITHUB_OUTPUT` over deprecated `::set-output` if output steps are added in the future.
