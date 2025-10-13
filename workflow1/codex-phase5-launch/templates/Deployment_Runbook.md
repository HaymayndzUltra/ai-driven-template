# Deployment Runbook

## Overview
- Service:
- Release version:
- Deployment window:

## Pre-Deployment Checklist
- [ ] Change approved (link to ticket)
- [ ] Release notes published
- [ ] On-call notified
- [ ] Backups verified within SLA

## Deployment Steps
| Step | Description | Command / Link | Owner | Status |
| --- | --- | --- | --- | --- |
| 1 | Tag release | `git tag vX.Y.Z` | | |
| 2 | Trigger pipeline | CI/CD URL | | |
| 3 | Run database migrations | `alembic upgrade head` | | |
| 4 | Verify smoke tests | `scripts/run_staging_smoke.sh` | | |

## Post-Deployment Verification
- Metrics dashboard: []
- Error tracking: []
- Feature flag toggles: []

## Rollback Reference
- Link to `Rollback_Plan.md`

## Contacts
- Primary on-call:
- Backup:
- Product:

## Sign-off
- Engineering lead:
- Product lead:
- SRE lead:
