# Workflow1 Playbook

Ang `workflow1/` ay koleksyon ng mga protocol, template, at ebidensiya para sa pitong yugto ng AI Governor delivery lifecycle (bootstrap hanggang operations). Pinagmumulan ito ng dokumentasyon at automation scripts na tinutukoy sa `INDEX.md`.

## Nilalaman sa Itaas na Antas

| Item | Deskripsyon |
| --- | --- |
| [`INDEX.md`](INDEX.md) | Master na talaan ng phases 0–6 kasama ang pangunahing templates, automation scripts, at lokasyon ng evidence. |
| [`PROJECT_EXECUTION_TEMPLATE.md`](PROJECT_EXECUTION_TEMPLATE.md) | Checklist-style na gabay sa pagpapatupad ng buong workflow. |
| `codex-phaseN-*` | Phase-specific packages (protocol + templates + scripts). |
| [`evidence/`](evidence) | Pre-seeded na manifest at validation files para sa bawat phase (2–6). |

## Phase Capsules

### Phase 0–1: Bootstrap & PRD
- Mga protocol file (`0-bootstrap-your-project.md`, `1-create-prd.md`) na nakalista sa index.
- Nakasalalay sa macro commands mula sa protocol upang kolektahin ang charter, context kit, at PRD deliverables.

### Phase 2: Design & Planning (`codex-phase2-design/`)
- **Protocol**: [`protocol.md`](codex-phase2-design/protocol.md) na naglalahad ng architecture at planning checkpoints.
- **Templates**: Architecture briefs, C4 diagrams, ADR template, backlog CSV, sprint-zero plan, environment at repo policies.
- **Scripts**:
  - [`scripts/generate_architecture_pack.py`](codex-phase2-design/scripts/generate_architecture_pack.py) – kinokopya ang template bundle papunta sa `evidence/phase2/outputs/<project>/architecture` at inaa-update ang `manifest.json`.
  - [`scripts/generate_contract_assets.py`](codex-phase2-design/scripts/generate_contract_assets.py) – gumagawa ng kontrata at API artifacts (sumusunod sa parehong manifest/run-log pattern).

### Phase 3: Quality Rails (`codex-phase3-quality-rails/`)
- Templates para sa security checklist, accessibility test plan, analytics spec, feature flags, at test plan.
- Automation:
  - [`scripts/run_quality_gates.sh`](codex-phase3-quality-rails/scripts/run_quality_gates.sh) – tumatakbo bilang orchestrator para sa lint, test, at security tooling.
  - [`scripts/configure_feature_flags.py`](codex-phase3-quality-rails/scripts/configure_feature_flags.py) – nag-uupdate ng feature flag inventory at evidence manifest.

### Phase 4: Integration (`codex-phase4-integration/`)
- Templates para sa observability spec, SLO/SLI, changelog, at staging smoke playbook.
- Scripts:
  - [`scripts/generate_observability_pack.py`](codex-phase4-integration/scripts/generate_observability_pack.py) – gumagawa ng observability evidence artifacts.
  - [`scripts/run_staging_smoke.sh`](codex-phase4-integration/scripts/run_staging_smoke.sh) – shell harness para sa staging regression suite.

### Phase 5: Launch (`codex-phase5-launch/`)
- Mga runbook template (deployment, rollback, DR), prod observability checklist, SEO/Release notes, at iba pa.
- Scripts tulad ng [`scripts/rehearse_rollback.sh`](codex-phase5-launch/scripts/rehearse_rollback.sh) at [`scripts/verify_dr_restore.sh`](codex-phase5-launch/scripts/verify_dr_restore.sh) para i-log ang rehearsals sa evidence folder.

### Phase 6: Operations (`codex-phase6-operations/`)
- Templates para sa postmortem, dependency/security update logs, at retro facilitation.
- Python automation: [`scripts/monitor_slo.py`](codex-phase6-operations/scripts/monitor_slo.py) at [`scripts/schedule_retros.py`](codex-phase6-operations/scripts/schedule_retros.py) na nag-e-emit ng trace entries sa evidence manifests.

## Evidence Workflow

- Bawat phase directory sa `evidence/` ay may paunang `manifest.json` at `validation.md` na kailangang i-update ng mga script.
- Ang scripts ay inaasahang mag-append ng ISO8601 timestamps sa `run.log` (kapag available) at magrehistro ng SHA-256 checksum sa manifest.
- Sumusunod ang manifest sa schema na binanggit sa [`../workflow/templates/evidence_schema.json`](../workflow/templates/evidence_schema.json).

## Pagpapatakbo ng Scripts

1. Tiyakin na nasa Python 3.10+ ka at may execution bit ang anumang shell script (`chmod +x`).
2. Tumakbo mula sa ugat ng repository upang manatiling tama ang relative paths, halimbawa:
   ```bash
   python workflow1/codex-phase2-design/scripts/generate_architecture_pack.py --project demo
   bash workflow1/codex-phase5-launch/scripts/rehearse_rollback.sh --project demo --env staging
   ```
3. Para sa scripts na umaasa sa iba pang toolchains (hal. lint o smoke tests), i-configure muna ayon sa `docs/LOCAL_DEV_WORKFLOW.md`.

## Dependencies

- **Python**: ginagamit ng karamihan sa automation (hashlib, argparse, json, pathlib).
- **Bash + coreutils**: para sa quality at release rehearsals.
- **External CLIs**: depende sa iyong pipeline (hal. kubectl, aws cli) – tingnan ang bawat script para sa eksaktong requirements.

## Paano Mag-extend

- Magdagdag ng bagong phase sa pamamagitan ng pag-clone ng pattern (`protocol.md`, `scripts/`, `templates/`, `evidence/phaseX`).
- I-update ang [`INDEX.md`](INDEX.md) upang irehistro ang bagong assets at priority ordering.
- Kapag nagdagdag ng bagong automation, tiyaking sumusulat ito sa manifest (`manifest.json`) at validation log upang manatiling auditable ang evidence trail.

### Week 7 Ops Alignment
- Sundin ang [Migration Guide](../docs/operations/migration-guide.md) kapag ina-upgrade ang legacy Workflow1 assets papunta sa unified workflow.
- I-coordinate ang operator handoffs gamit ang [Operator Quickstart](../docs/operations/operator-quickstart.md) at [Support Playbook](../docs/operations/support-playbook.md).
- Gamitin ang [Troubleshooting Guide](../docs/operations/troubleshooting.md) kapag may hindi pagkakatugma sa evidence schema o automation scripts.
