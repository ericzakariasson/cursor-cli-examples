# Security Hardening Log

Date: 2025-10-20
Branch: audit

Summary of findings and recommendations:
- Pin reusable actions to immutable SHAs (checkout, setup-python, upload-artifact, setup-uv).
- Reduce workflow permissions to least privilege (prefer `contents: read`).
- Add fork-safety guard to PR-triggered jobs to avoid using secrets on forks.
- Add a scheduled audit workflow to ensure periodic review (in a follow-up change where workflows permission allows).

Findings:
- No high-signal secrets detected in working tree via regex scan. Consider running gitleaks for comprehensive coverage and add an allowlist if needed.
- No deprecated `::set-env` or `::add-path` usages found.

Next steps:
- Approve a PR that pins actions and reduces permissions. Compare link will be provided on the latest open PR.
