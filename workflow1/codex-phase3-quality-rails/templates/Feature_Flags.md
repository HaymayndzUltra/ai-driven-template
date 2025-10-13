# Feature Flags Framework

## Platform
- Provider (LaunchDarkly, ConfigCat, homegrown, etc.):
- SDKs: web | mobile | backend
- Flag naming convention: `<area>_<feature>_<variant>`

## Governance
- Flag types: release, ops, permission, experiment.
- Default TTL: 30 days (review at sprint retro).
- Change management: PR + approvals required for permanent flags.

## Flag Inventory
| Flag Key | Type | Owner | Created | Target Segments | Removal Criteria | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

## Automation
- Managed via `configure_feature_flags.py` (generates JSON manifest and audit log).
- CI ensures flags referenced in code exist in manifest.

## Monitoring
- Analytics event `feature_toggled` tied to each evaluation.
- Alert on stale flags > 60 days.

## Cleanup Process
1. Identify flags meeting removal criteria.
2. Schedule removal PR and coordinate rollout.
3. Update documentation/analytics to reflect removal.

## Sign-off
- Engineering lead:
- Product manager:
- Date:
