# Security Hardening Log

## 2025-11-21

- Scope: Repository-wide secrets exposure scan and GitHub Actions workflow hardening.
- Tracked files scan: no high-confidence secrets found.
- Recent git history (last 180 days, ~500 commits): no high-confidence secrets detected.
- No usage of `pull_request_target` detected.
- Proposed workflow edits (recorded due to missing `workflows` permission on token):
  - Pin actions to immutable SHAs:
    - actions/checkout@34e114876b0b11c390a56381ad16ebd13914f8d5 (was @v4)
    - actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065 (was @v5)
    - actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02 (was @v4)
    - astral-sh/setup-uv@38f3f104447c67c051c4a08e39b64a148898af3a (was @v4)
  - Add explicit default token permission in CI tests: `permissions: contents: read` in `.github/workflows/test.yml`.
  - Guard secrets on forked PRs: add `if: ${{ github.event.pull_request.head.repo.fork == false }}` to steps that use secrets in PR-triggered workflows (code review, visual testing, docs, i18n updates).
- Follow-ups: replace curl|bash installers with checksum-verified flows; migrate from deprecated `apt-key` to keyrings with `signed-by`; prefer least-privilege `permissions` scoped at job-level.

## 2025-11-11

- No high-confidence secrets detected in tracked files using heuristic patterns (API tokens, private keys, AWS keys, Slack tokens). Review `.gitleaks.toml` allowlist if added in future.
- Pinned unpinned GitHub Actions to immutable commit SHAs across workflows.
- Added explicit minimal token permissions to `test.yml` (`permissions: contents: read`).
- No `pull_request_target`, `secrets: inherit`, or deprecated `::set-output`/`::set-env` usages found.

Pinned Actions
- actions/checkout@v4 → 08eba0b27e820071cde6df949e0beb9ba4906955
- actions/setup-python@v5 → a26af69be951a213d495a4c3e4e4022e16d87065
- actions/upload-artifact@v4 → ea165f8d65b6e75b540449e92b4886f43607fa02
- astral-sh/setup-uv@v4 → 38f3f104447c67c051c4a08e39b64a148898af3a

Workflows touched
- .github/workflows/visual-testing.yml
- .github/workflows/improve-pr-description.yml
- .github/workflows/update-docs.yml
- .github/workflows/test.yml
- .github/workflows/translate-keys.yml
- .github/workflows/secrets-audit.yml
- .github/workflows/fix-conflicts.yml
- .github/workflows/code-review.yml
- .github/workflows/fix-ci.yml

Guidance
- Keep actions pinned; periodically bump SHAs to latest tags after review.
- Prefer least-privilege `permissions` at workflow/job level; elevate only where required.
- Avoid `pull_request_target` unless absolutely necessary; if used, never run untrusted code with secrets.
- Consider integrating gitleaks for scheduled scans and maintain `.gitleaks.toml` allowlists to reduce noise.

## 2025-11-09

Scope: Repository-wide secrets exposure scan and GitHub Actions workflow hardening.

Summary of changes
- Pinned GitHub Actions to immutable commit SHAs:
  - actions/checkout@v4 → 08eba0b27e820071cde6df949e0beb9ba4906955
  - actions/setup-python@v5 → a26af69be951a213d495a4c3e4e4022e16d87065
  - actions/upload-artifact@v4 → ea165f8d65b6e75b540449e92b4886f43607fa02
  - astral-sh/setup-uv@v4 → 38f3f104447c67c051c4a08e39b64a148898af3a
- Added minimal permissions to `.github/workflows/test.yml` (`permissions: contents: read`).

Findings
- No potential secrets found in tracked files (basic patterns: AWS keys, private keys, GitHub tokens).
- No potential secrets found in recent git history (last 200 commits) for the same patterns.
- No usage of `pull_request_target` or deprecated `::set-output` detected.

Recommendations & guidance
- Keep actions pinned to SHAs; update pins only after verifying upstream changes.
- Ensure each workflow declares the least-privileged `permissions:` needed. Prefer `contents: read` unless writes or PR comments are required.
- If you use an allowlist for secret scanning, commit a `.gitleaks.toml` with approved patterns/paths. Scheduled audits can read and honor allowlists.
- Avoid using repository secrets in forked PR contexts. Prefer `pull_request` (not `pull_request_target`) for untrusted contributions, and gate sensitive steps with conditions.

Maintenance
- A scheduled audit workflow is present (`.github/workflows/secrets-audit.yml`) and will continue scanning on a schedule. Review logs and rotate any secrets if newly reported.
