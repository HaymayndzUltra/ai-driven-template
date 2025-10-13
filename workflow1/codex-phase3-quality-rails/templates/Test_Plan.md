# Test Plan

## Strategy
- Testing pyramid (unit, integration, end-to-end) with percentages.
- Automation vs manual testing boundaries.

## Coverage Targets
| Layer | Owner | Tooling | Target Coverage | Evidence |
| --- | --- | --- | --- | --- |
| Unit | | pytest/jest | 80% | |
| Integration | | Postman/Cypress | Critical paths | |
| E2E | | Playwright | Smoke suite | |

## Test Environments
- Local: developer machines (docker-compose).
- CI: ephemeral containers.
- Staging: nightly regression.

## Regression Schedule
- Daily smoke via `run_quality_gates.sh`.
- Weekly full regression.

## Non-Functional Testing
- Performance: see `perf/budgets.json`.
- Accessibility: see `A11y_Test_Plan.md`.
- Security: integrate with SAST/DAST.

## Toolchain
- Unit tests: `npm test` / `pytest`.
- Linting: `eslint`, `black`, `mypy`.
- Coverage reporting to CI dashboards.

## Exit Criteria
- All planned tests executed with pass rate ≥ 95%.
- Defects triaged and tracked.
- Sign-off captured below.

## Approvals
- QA lead:
- Engineering lead:
- Product owner:
