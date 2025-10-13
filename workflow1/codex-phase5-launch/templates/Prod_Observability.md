# Production Observability Plan

## Objectives
- Ensure proactive monitoring and alerting post-launch.

## Dashboards
| Dashboard | Link | Owner | Purpose |
| --- | --- | --- | --- |
| Prod API Health | | SRE | Monitor latency/errors |
| User Journeys | | Product Analytics | Track key flows |

## Alerts
| Alert | Condition | Channel | Runbook |
| --- | --- | --- | --- |
| API Latency | p95 > 300ms for 5m | PagerDuty | Deployment_Runbook.md |
| Error Rate | Error rate > 2% | Slack #alerts | Postmortem_Template.md |

## Logging & Tracing
- Log retention: 30 days (hot), 180 days (archive).
- Trace sampling: 10% production, 50% staging.

## On-Call Rotation
- Primary schedule: []
- Secondary schedule: []
- Escalation matrix: []

## Runbooks
- Link to `Deployment_Runbook.md`, `Rollback_Plan.md`, `DR_Plan.md`.

## Validation
- Dashboards reviewed on (date).
- Alerts tested via synthetic events (link evidence).

## Sign-off
- SRE lead:
- Engineering lead:
- Product lead:
