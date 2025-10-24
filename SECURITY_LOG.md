# Security Hardening Log

Date: 2025-10-24
Branch: audit

Summary of findings and recommendations (no workflow changes pushed due to missing `workflows` permission for this automation):

- Recommended pinning third-party actions to commit SHAs:
  - actions/checkout@08eba0b27e820071cde6df949e0beb9ba4906955
  - actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065
  - actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02
  - astral-sh/setup-uv@38f3f104447c67c051c4a08e39b64a148898af3a
- Recommended guardrails for PR workflows using secrets: `if: ${{ github.event.pull_request.head.repo.fork == false }}` to avoid exposing secrets to forks.
- Permissions appear scoped; continue aiming for least privilege per job.
- No plaintext secrets found in working tree; no `.gitleaks.toml` present. Consider adding gitleaks with an allowlist for test keys.

Next steps for maintainers:
1) Apply the above pins and guards in `.github/workflows/*.yml` (requires `workflows` permission).
2) Optionally add a scheduled gitleaks scan with allowlist.
