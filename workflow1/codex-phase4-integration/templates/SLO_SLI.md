# SLO / SLI Definition

## Service Overview
- Service name:
- Critical user journeys:

## Service Level Indicators
| ID | Indicator | Type | Measurement | Target | Source |
| --- | --- | --- | --- | --- | --- |
| SLI-001 | Availability | Ratio | Successful requests / total | ≥ 99.5% monthly | Observability stack |
| SLI-002 | Latency | Histogram | p95 response time | ≤ 300ms | OpenTelemetry |
| SLI-003 | Error Rate | Ratio | 5xx responses | ≤ 1% | API gateway |

## Service Level Objectives
| Objective | Indicator | Target | Window | Burn Rate Alert |
| --- | --- | --- | --- | --- |
| Keep availability ≥ 99.5% | SLI-001 | 99.5% | 30 days | 14x / 2h |
| Keep latency ≤ 300ms | SLI-002 | 300ms | 7 days | 6x / 1h |

## Error Budgets
- Monthly error budget (minutes):
- Policy for budget exhaustion:

## Review Cadence
- Weekly review in Ops meeting.
- Monthly exec summary.

## Links
- Observability dashboards
- Incident response playbooks

## Sign-off
- SRE lead:
- Product lead:
- Date:
