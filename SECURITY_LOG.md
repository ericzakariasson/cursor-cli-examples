# Security Hardening Log

Date: 2025-09-25
Branch: audit/security-hardening

Summary of proposed changes
- Pin GitHub Actions to immutable commit SHAs for reproducibility
  - actions/checkout@08eba0b27e820071cde6df949e0beb9ba4906955
  - actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065
  - astral-sh/setup-uv@38f3f104447c67c051c4a08e39b64a148898af3a
  - actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02
  - browser-actions/setup-chrome@c785b87e244131f27c9f19c1a33e2ead956ab7ce
- Add minimal permissions blocks where missing (e.g., `contents: read` for CI-only)
- Add fork guards to steps that use secrets or write to PRs
- Replace manual Chrome install with a pinned setup action
- Harden curl install steps with `set -euo pipefail`

Note: Workflow file edits are provided as a diff in `proposed-edits/workflow-hardening.diff` due to GitHub App workflow permissions on this runner. Apply via PR.

Secret scan results
- No obvious credentials found in tracked files or recent history (last 60 days).
- No `.gitleaks*` allowlist found. Consider adding `.gitleaks.toml` if needed.

Workflow hardening details
- Code Review, Translate Keys, Improve PR Description, Update Docs, Visual Testing:
  - Pin actions, add fork guards for secret-using steps.
  - Use setup-chrome action instead of apt-based install in Visual Testing.
- Test:
  - Pin actions and add minimal permissions: `contents: read`.
- Fix CI and Fix Conflicts:
  - Pin checkout and add fork/repo guards to avoid using secrets on forks.

Follow-ups
- Review if any job requires elevated permissions beyond current settings.
- Periodically refresh pinned SHAs to latest stable releases.
