# Backup Policy

## Scope
- Systems covered (databases, object storage, configurations).

## Backup Schedule
| System | Frequency | Retention | Storage Location | Encryption |
| --- | --- | --- | --- | --- |
| PostgreSQL | Hourly incrementals, daily full | 30 days | S3 bucket | AES-256 |
| Object Storage | Daily differential | 14 days | S3 bucket | AES-256 |

## Responsibilities
- Backup owner:
- Verification owner:

## Verification & Testing
- Automated restore tests weekly.
- Quarterly full DR exercise.

## Compliance
- Aligns with policy/regulations (e.g., GDPR, SOC2).

## Evidence
- See `verify_dr_restore.sh` logs.

## Sign-off
- Infrastructure lead:
- Security/compliance:
- Date:
