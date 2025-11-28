# Security Hardening Log

Date: 2025-11-28
Branch: audit

Summary
- Pinned GitHub Actions to immutable commit SHAs.
- Added minimal default permissions where missing.
- Guarded PR workflows to avoid running with repository secrets on forked PRs.
- Replaced deprecated apt-key usage with signed-by keyring for Chrome install.
- Scanned repository and last 50 commits for common secret patterns; no findings.

Changes
- .github/workflows/code-review.yml
  - Pin: actions/checkout@34e114876b0b11c390a56381ad16ebd13914f8d5
  - Pin: astral-sh/setup-uv@38f3f104447c67c051c4a08e39b64a148898af3a
  - Guard forks: if: ${{ github.event.pull_request.draft == false && !github.event.pull_request.head.repo.fork }}
- .github/workflows/visual-testing.yml
  - Pin: actions/checkout@34e114876b0b11c390a56381ad16ebd13914f8d5
  - Pin: astral-sh/setup-uv@38f3f104447c67c051c4a08e39b64a148898af3a
  - Pin: actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02
  - Guard forks on job-level condition
  - Replace apt-key with signed-by keyring approach for Chrome repository
- .github/workflows/translate-keys.yml
  - Pin: actions/checkout@34e114876b0b11c390a56381ad16ebd13914f8d5
  - Guard forks on job-level condition
- .github/workflows/update-docs.yml
  - Pin: actions/checkout@34e114876b0b11c390a56381ad16ebd13914f8d5
  - Guard forks on job-level condition
- .github/workflows/test.yml
  - Pin: actions/checkout@34e114876b0b11c390a56381ad16ebd13914f8d5
  - Pin: actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065
  - Add: permissions: contents: read
- .github/workflows/fix-ci.yml
  - Pin: actions/checkout@34e114876b0b11c390a56381ad16ebd13914f8d5
- .github/workflows/fix-conflicts.yml
  - Pin: actions/checkout@34e114876b0b11c390a56381ad16ebd13914f8d5
- .github/workflows/improve-pr-description.yml
  - Pin: actions/checkout@34e114876b0b11c390a56381ad16ebd13914f8d5
- .github/workflows/secrets-audit.yml
  - Pin: actions/checkout@34e114876b0b11c390a56381ad16ebd13914f8d5

Secret Scans
- Working tree scan: no matches for AWS keys, GitHub tokens, Google API keys, Slack tokens, private keys, or common secret assignments.
- Recent history (last 50 commits) scan: no matches.
- No .gitleaks.toml allowlist found.

Guidance
- Prefer `permissions: contents: read` at workflow top; elevate narrowly per job when needed.
- Always pin actions by SHA; update SHAs during dependency refresh windows.
- Avoid running secret-reliant jobs on forked PRs; use job-level `if: !github.event.pull_request.head.repo.fork`.
- Replace any remaining `apt-key` usage with a keyring + signed-by configuration.
- Store secrets only in GitHub Actions secrets; avoid committing literals. If false positives arise, consider a `.gitleaks.toml` allowlist with precise rules.
