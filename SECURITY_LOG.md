# Security Hardening Log

Date: 2025-11-03
Branch: audit-security-hardening

This repository was scanned; minimal hardening is proposed below.

## Findings
- No plaintext secrets found in tracked files or recent history (~200 commits sampled).
- No deprecated `::set-output`/`::add-path` usage detected.
- No `pull_request_target` workflows present.
- Several workflows use version tags (`@v4`, `@v5`) instead of immutable SHAs.
- Several workflows legitimately require `contents: write`/`pull-requests: write` to push branches or comment on PRs; those should be retained.

## Summary of Proposed Actions
- Pin reusable GitHub Actions to immutable commit SHAs:
  - actions/checkout@08eba0b27e820071cde6df949e0beb9ba4906955 (v4)
  - actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065 (v5)
  - actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02 (v4)
  - astral-sh/setup-uv@38f3f104447c67c051c4a08e39b64a148898af3a (v4)
- Add least-privilege permissions where missing; for example in `test.yml`:
  permissions:
    contents: read
- Replace deprecated `apt-key` usage in `visual-testing.yml` with a signed keyring for the Google Chrome apt repo.
- Guard steps that require `secrets.CURSOR_API_KEY` to avoid secret exposure on forks (workflows using `pull_request` do not receive secrets for forked PRs by default).

Note: Pushing workflow file changes requires the `workflows: write` permission for the token. If your automation lacks that scope, apply the above edits manually and re-run this audit.

## Recommended Follow-ups
- Add a `.gitleaks.toml` for allowlists and org-wide rules (if false positives arise).
- Review per-workflow `permissions:` and scope down further where possible (consider job-level `permissions`).
- Periodically re-pin action SHAs to the latest secure release.
