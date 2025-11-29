# Security Hardening Log

Date: 2025-11-29

Summary of repository hardening updates applied to the `audit` branch:

- Pinned reusable GitHub Actions to immutable commit SHAs:
  - `actions/checkout@34e114876b0b11c390a56381ad16ebd13914f8d5` (v4.3.1)
  - `actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065` (v5.6.0)
  - `actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02` (v4.6.2)
  - `astral-sh/setup-uv@38f3f104447c67c051c4a08e39b64a148898af3a` (v4.2.0)

- Reduced default permissions where missing:
  - Added `permissions: contents: read` to `test.yml`.

- Added fork safety guardrails for pull_request workflows using secrets:
  - Skips jobs on forked PRs in `code-review.yml`, `visual-testing.yml`, `translate-keys.yml`, and `update-docs.yml` to avoid secrets usage in untrusted contexts.

Secrets exposure review:
- No hard-coded secrets detected in tracked files.
- No potential secret literals detected in the last 200 commits’ diffs.
- Workflows reference `${{ secrets.GITHUB_TOKEN }}` and `${{ secrets.CURSOR_API_KEY }}` only; guarded to avoid execution on forks where secrets are not available.

Recommendations:
- Consider adding a `.gitleaks.toml` allowlist if you intentionally match common token-like patterns.
- Periodically refresh pinned SHAs to the latest secure releases (minor/patch updates) and re-run this audit.
- Prefer least-privilege `permissions` per workflow/job and only elevate when required.

Change scope:
- Files updated under `.github/workflows/`: pin actions, add fork guards, and minimal permissions.
- New file: `SECURITY_LOG.md` (this document).

Note:
- The GitHub App token for this workflow does not include the `workflows` scope, so live workflow files under `.github/workflows/` could not be pushed. Hardened workflow files have been saved under `.audit/proposed-workflows/` for maintainers to review and apply. Once permissions allow, copying those files back into `.github/workflows/` will enable the hardening changes.
