# Security Hardening Log

Date: 2025-11-24
Branch: audit-workflow-hardening

Summary of audit (proposed changes, see notes)
- Proposed pinning reusable GitHub Actions to immutable commit SHAs:
  - actions/checkout@v4 -> 34e114876b0b11c390a56381ad16ebd13914f8d5 (v4.3.1)
  - actions/setup-python@v5 -> a26af69be951a213d495a4c3e4e4022e16d87065 (v5.6.0)
  - actions/upload-artifact@v4 -> ea165f8d65b6e75b540449e92b4886f43607fa02 (v4.6.2)
  - astral-sh/setup-uv@v4 -> 38f3f104447c67c051c4a08e39b64a148898af3a (v4.2.0)
- Proposed adding safer installer flags to `curl` invocations: `-fsSL --proto '=https' --tlsv1.2`.

Notes
- This run’s token lacks `workflows` permission; workflow file changes cannot be pushed directly. Use the compare link in the PR comment to open a PR with the proposed edits.

Workflows targeted
- .github/workflows/test.yml
- .github/workflows/visual-testing.yml
- .github/workflows/code-review.yml
- .github/workflows/fix-ci.yml
- .github/workflows/translate-keys.yml
- .github/workflows/update-docs.yml
- .github/workflows/improve-pr-description.yml
- .github/workflows/fix-conflicts.yml
- .github/workflows/secrets-audit.yml

Secrets exposure scan
- Working tree scan: no matches for common high-risk token patterns (AWS keys, GitHub PATs, Slack tokens, private key headers).
- Recent history scan (last 200 commits, all refs): no matches found for the same patterns.
  - Note: detections in YAML prompts referencing these token names were documentation mentions, not secrets.

Recommendations
- Continue to avoid `pull_request_target` unless absolutely necessary; prefer `pull_request` with fork guards on secret-using steps.
- Keep action pins updated periodically by bumping SHAs to the desired release commit.
- If a legitimate secret ever appears in git history, rotate it immediately and remove/rotate any derived credentials.
