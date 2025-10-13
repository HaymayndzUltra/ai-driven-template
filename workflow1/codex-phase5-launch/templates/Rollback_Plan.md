# Rollback Plan

## Trigger Conditions
- Smoke test failure
- Error budget burn > threshold
- Critical incident declared

## Rollback Options
| Option | Description | Estimated Time | Risks | Owner |
| --- | --- | --- | --- | --- |
| Blue/Green | Switch traffic to previous version | 5 min | Requires warm standby | SRE |
| Database rollback | Restore backup snapshot | 20 min | Possible data loss | DBA |

## Procedure
1. Announce rollback in communication channels.
2. Disable feature flags if applicable.
3. Execute rollback command (document exact steps).
4. Verify system health (metrics, logs, alerts).
5. Update incident ticket with status.

## Validation
- Rehearsed on: (date)
- Evidence: link to `rehearse_rollback.sh` output

## Communication Plan
- Stakeholders notified via email/Slack.
- Incident commander:
- External comms contact:

## Post-Rollback Actions
- Root cause analysis
- Follow-up tasks recorded in backlog

## Sign-off
- SRE lead:
- Engineering lead:
- Product lead:
