# Observability Specification

## Objectives
- Define logs, metrics, and traces required to monitor golden journeys.

## Architecture Links
- Reference Architecture.md sections: []
- Feature flags impacting telemetry: []

## Logging
| Component | Log Format | PII Handling | Retention | Notes |
| --- | --- | --- | --- | --- |
| API | JSON | Mask sensitive fields | 30 days | |

## Metrics
| Metric | Type | Source | Frequency | Threshold | Dashboard |
| --- | --- | --- | --- | --- | --- |
| api.request.latency | Histogram | OpenTelemetry | Real-time | p95 < 300ms | Grafana: API Latency |
| web.vitals.lcp | Gauge | Web RUM | Real-time | p75 < 2.5s | Grafana: Web Vitals |

## Traces
- Trace IDs propagate via W3C Trace Context.
- Critical spans: web request, service processing, external dependency.
- Sampling rate: 50% in staging, 10% in production (adjust as needed).

## Alerting
| Alert | Condition | Channel | Runbook |
| --- | --- | --- | --- |
| API latency breach | p95 latency > 300ms for 5m | PagerDuty | Link to Deployment_Runbook.md |
| Error rate spike | Error rate > 2% | Slack #alerts | Link to Postmortem_Template.md |

## Dashboards
- Link to Grafana dashboards, include screenshot references.

## Validation
- Observability smoke executed via `generate_observability_pack.py` logging.
- Ensure metrics exist before Phase 5 sign-off.

## Approval
- SRE lead:
- Engineering lead:
- Product:
