# Environment Strategy

## Purpose
Outline the provisioning, isolation, and secrets approach for all environments in alignment with AGENTS Phase 2.

## Environments
| Environment | Purpose | Hosting | Branch Trigger | Data Policy | Notes |
| --- | --- | --- | --- | --- | --- |
| Local | Developer workstation | Docker Compose | feature/* | Synthetic | |
| Dev | Shared integration | Kubernetes | develop | Scrubbed | |
| Staging | Pre-prod validation | Kubernetes | release/* | Sanitised | |
| Production | Customer traffic | Kubernetes | main | Live | |

## Access & Secrets
- Secrets managed via vault (manual rotation, never stored in repo).
- Access control roles with least privilege.

## Deployment Strategy
- Continuous deployment to dev.
- Staging promoted through release branches with smoke automation.
- Production uses canary + feature flags.

## Tooling & Automation
- Reference `docs/LOCAL_DEV_WORKFLOW.md` for bootstrap commands.
- CI pipelines enforce lint/test/build prior to deployment.
- Infrastructure templates stored in `/deploy/` (see repo policy).

## Compliance & Audit
- Logging requirements per policy.
- Change management approvals.

## Risks & Mitigation
- Secret leakage → adopt secret scanning & vault integration.
- Drift → scheduled infra validation.

## Sign-off
- DevOps/Platform lead:
- Security lead:
- Date:
