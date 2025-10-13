# Disaster Recovery Plan

## Objectives
- Restore critical services within defined RTO/RPO.

## RTO / RPO Targets
| Service | RTO | RPO | Notes |
| --- | --- | --- | --- |
| API Platform | 1 hour | 15 minutes | |
| Data Warehouse | 4 hours | 1 hour | |

## DR Runbook
1. Declare incident and form DR team.
2. Assess impact and determine recovery strategy.
3. Restore infrastructure (list scripts/commands).
4. Validate application functionality.
5. Communicate status to stakeholders.

## Testing Schedule
- Semi-annual full DR tests.
- Monthly table-top exercises.

## Dependencies
- Backup policy alignment.
- Third-party SLAs (list).

## Evidence
- Attach test results from `verify_dr_restore.sh`.

## Sign-off
- DR owner:
- Compliance:
- Date:
