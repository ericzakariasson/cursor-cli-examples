# Security Audit Log

Date: 2025-10-31
Branch: audit-hardening
Scope: ericzakariasson/cursor-cli-examples

## Summary
- No potential secrets detected in tracked files or in the last 200 commits.
- No `.gitleaks.toml` allowlist found; none required based on current scan.
- Proposed GitHub Actions workflow hardening with minimal, safe changes. Applying workflow file edits may require repository-level `workflows` permission.

## Proposed Workflow Hardening
- Add explicit least-privilege permissions where missing; for test-only workflows, set:
  - `permissions: { contents: read }`
- Skip PR jobs that need secrets/write on forks:
  - Example job condition: `${{ github.event.pull_request.draft == false && github.event.pull_request.head.repo.fork == false }}`
- Pin third-party actions to immutable SHAs (examples as of this run; verify upstream before applying):
  - `actions/checkout@08eba0b27e820071cde6df949e0beb9ba4906955`
  - `actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065`
  - `actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02`
  - `astral-sh/setup-uv@38f3f104447c67c051c4a08e39b64a148898af3a`
- Replace deprecated `apt-key` usage with keyring-based installation when feasible.

## Secret Scan Details
Patterns scanned (non-exhaustive):
- AWS access keys, GitHub personal tokens, Slack tokens, Google API keys, private key headers
- Generic assignments: case-insensitive `(api|secret|token|password|passwd|pwd|key)\s*[:=]\s*"..."`

History window: last 200 commits (diffs). No hits found.

## Guidance
- Keep actions pinned to SHAs; update periodically by bumping to the latest release SHA.
- Prefer job-level `permissions` scoped to the minimum needed; ensure each workflow declares a `permissions` block.
- Avoid `pull_request_target` unless absolutely necessary and well-guarded.
- If future false positives arise in secret scans, add narrowly-scoped allowlist rules in a `.gitleaks.toml`.

## Compare and Create PR
- https://github.com/ericzakariasson/cursor-cli-examples/compare/main...audit-hardening

<!-- security-hardening-audit:2025-10-31 -->
