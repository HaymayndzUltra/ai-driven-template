# Accessibility Test Plan

## Objectives
- Achieve WCAG 2.2 AA compliance across core journeys.
- Integrate automated and manual accessibility testing into CI/CD.

## Scope
| Journey | Assistive Tech | Browser | Status |
| --- | --- | --- | --- |
| | Screen reader (NVDA/JAWS) | Chrome/Edge | |
| | Keyboard-only | Chrome/Firefox | |
| | High contrast mode | Windows/Edge | |

## Tooling
- Automated: `axe-core`, `lighthouse --accessibility`, Storybook a11y add-on.
- Manual: screen readers, keyboard walkthrough, colour contrast analyzers.

## Test Cadence
- Automated checks on every PR via `run_quality_gates.sh`.
- Manual regression before each release candidate.

## Defect Management
- Severity scale (Blocker/Major/Minor).
- SLA: Blockers fixed before release, Majors within 1 sprint, Minors within backlog triage.

## Evidence
- Store reports under `evidence/phase3/a11y`.
- Link to issues created for remediation.

## Approvals
- Accessibility champion:
- QA lead:
- Product representative:
