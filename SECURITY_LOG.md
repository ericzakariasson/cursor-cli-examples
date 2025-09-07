# Security Hardening Log

Date: 2025-09-07

Scope: GitHub Actions workflows and repo secret exposure audit for .

Summary of proposed changes
- Pin actions to immutable commit SHAs (checkout, setup-python, setup-uv, upload-artifact).
- Add fork PR guards to workflows that write or use elevated permissions.
- Replace deprecated apt-key usage with keyring method for Chrome repo.
- Add explicit minimal permissions to workflows lacking them.

Secret exposure audit
- Scanned tracked files and last 200 commits for common secret patterns; no findings.
- No  allowlist present.

Review
- See SECURITY_PATCH.diff for proposed edits; apply via  or open a compare link.
