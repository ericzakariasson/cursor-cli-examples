## Security Hardening Log

Date: 2025-09-09

Summary of audit results and recommended changes.

Findings
- No high-confidence secrets found in tracked files or last 200 commits.
- Workflows: consider pinning actions to commit SHAs, adding fork-PR guards for steps that use secrets or write perms, adding least-privilege permissions, and replacing deprecated apt-key usage.

Minimal Proposed Edits (PR recommended)
- Pin actions: actions/checkout, actions/setup-python, actions/upload-artifact, astral-sh/setup-uv.
- Add permissions: contents: read to test.yml.
- Guard PR jobs with !github.event.pull_request.head.repo.fork when secrets/write are used.
- Replace apt-key with signed-by keyring for Chrome install.

Next Steps
- Review and approve a compare PR with the above changes.
- Add a .gitleaks.toml allowlist if needed to tune scanning.
