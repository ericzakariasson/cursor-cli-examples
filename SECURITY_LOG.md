# Security Hardening Log

Date: 2025-09-03

Scope: Automated secrets exposure scan and GitHub Actions workflow hardening.

Findings:
- No high-confidence secrets detected (working tree and last 90 days).
- Floating action versions; one deprecated apt-key usage; some workflows missing explicit permissions.

Proposed in :
- Pin actions to SHAs (checkout v4, setup-python v5, upload-artifact v4, setup-uv v4).
- Add least-privilege  blocks.
- Replace apt-key with keyring-based approach.

Compare: https://github.com/ericzakariasson/cursor-cli-examples/compare/main...audit-workflow-hardening
