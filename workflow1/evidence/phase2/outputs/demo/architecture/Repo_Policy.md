# Repository & Branch Policy

## Purpose
Define branching, review, and merge standards that satisfy AGENTS Phase 2 exit checks.

## Branching Model
- `main`: protected, deployable. Requires PR review + green CI.
- `develop`: integration branch for staging.
- `release/*`: temporary release branches for staging → production promotion.
- `feature/*`: developer branches; delete after merge.

## Commit Standards
- Conventional Commits enforced via lint (`npm run lint:commits`).
- Max PR size (lines/files) before additional approval.
- Reference related ADR/backlog ID in commit body.

## Pull Request Requirements
- Minimum 2 approvals (Engineering + QA/PM).
- All CI checks (lint, tests, security, perf, a11y) must pass.
- Link to testing evidence and feature flags toggled.

## Automation Hooks
- GitHub Actions / GitLab CI pipeline definitions stored in `.github/workflows/`.
- Requires `quality_gate_simple.sh` or equivalent to be invoked pre-merge.

## Compliance Controls
- Secret scanning and dependency scanning enabled.
- Branch protection preventing force pushes.
- Require signed commits if regulated environment.

## Documentation
- Link to `Code_Review_Checklist.md` (Phase 3) for reviewer prompts.

## Sign-off
- Repository maintainer:
- Date:
