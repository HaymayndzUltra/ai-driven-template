# Staging Smoke Test Playbook

## Purpose
Validate staging deployments before promoting to production.

## Preconditions
- Deployment completed and feature flags configured.
- Observability dashboards healthy.

## Smoke Suite
| Step | Description | Tool | Expected Result | Owner |
| --- | --- | --- | --- | --- |
| 1 | User login | Playwright | Success | QA |
| 2 | Critical API call | Postman | 200 OK | QA |
| 3 | Feature flag toggle | CLI/API | Response OK | Dev |
| 4 | Error monitoring | Observability dashboard | No new alerts | SRE |

## Rollback Triggers
- Smoke failure > 1 critical step.
- Error rate > 2% after deployment.

## Evidence Capture
- Attach screenshots/logs to `evidence/phase4/run.log` and `validation.md`.

## Sign-off
- QA lead:
- Engineering lead:
- Product manager:
