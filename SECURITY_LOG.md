# Security Hardening Log

Date: 2025-08-29
Branch: audit

Summary
- Performed scheduled secrets exposure and workflow hardening audit.
- No hard-coded secrets detected in tracked files or recent history (50 commits).
- Found unpinned actions and PR jobs that write using repo secrets without fork guards.

Recommended minimal fixes (apply via maintainer PR):
- Pin third-party actions to immutable SHAs:
  - actions/checkout@08eba0b27e820071cde6df949e0beb9ba4906955 (v4)
  - actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065 (v5)
  - astral-sh/setup-uv@38f3f104447c67c051c4a08e39b64a148898af3a (v4)
  - actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02 (v4)
- Add least-privilege permissions:
  - In `test.yml`, add top-level and job-level `permissions: { contents: read }`.
- Guard PR-triggered write jobs from forks:
  - Add `if: ${{ github.event.pull_request.head.repo.full_name == github.repository }}` on jobs in `auto-translate-keys.yml`, `auto-update-docs.yml`, `auto-update-docs-split.yml`, and `auto-improve-pr-description.yml`.
- Safer curl usage:
  - Use `curl -fsSL` for installer pipelines and quote `$GITHUB_PATH`.

Notes
- Workflow file edits require the `workflows` permission; recommend a maintainer PR applying the above.
- Consider adding `.gitleaks.toml` to maintain allowlists for future scans.
