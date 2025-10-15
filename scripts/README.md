# AI-Orchestrated Development Workflow System

## Overview

This system provides comprehensive AI-assisted project orchestration with human oversight, compliance validation, and protocol governance. It transforms project briefs into production-ready applications through structured phases with evidence tracking, quality gates, and automated compliance checking. The system integrates reasoning, validation, generation, and compliance automation into a unified AI-to-human collaboration framework.

## Module Map

### **Core Orchestration** (High Importance)
- **`run_workflow.py`** - CLI entry point, configuration loading, main execution hub (orchestration)
- **`ai_orchestrator.py`** - Central AI coordination engine for 7-phase workflow execution (orchestration)
- **`workflow_automation.py`** - Adapter bridging orchestration and quality/validation gates (orchestration)
- **`ai_executor.py`** - Main orchestrator executing complete unified workflow from bootstrap to operations (orchestration)

### **Human Oversight & Validation** (High Importance)
- **`validation_gates.py`** - Human validation checkpoints, approval workflows, evidence tracking (validation)
- **`validate_prd_gate.py`** - Validates PRD sign-off metadata and supporting architecture notes (validation)
- **`validate_workflow_integration.py`** - Validates end-to-end workflow integration (validation)
- **`validate_ai_directives.py`** - Validates AI directive structure and compliance (validation)
- **`detect_instruction_conflicts.py`** - Detects ambiguous, conflicting, or contradictory instructions in protocols (validation)
- **`generate_consistency_report.py`** - Generates comprehensive consistency reports across all protocols (validation)
- **`validate_protocol_steps.py`** - Validates logical flow and sequence of steps within each protocol (validation)
- **`validate_protocol_handoffs.py`** - Validates protocol transitions and handoff logic between phases (validation)
- **`validate_script_bindings.py`** - Validates automation script bindings for unified protocols (validation)
- **`simulate_protocol_execution.py`** - Simulates AI execution of protocols to detect runtime issues (validation)
- **`test_policy_decisions.py`** - Policy router regression test runner with YAML-based fixtures (validation)
- **`check_hipaa.py`** - Lightweight HIPAA compliance checks for session timeout, RBAC, audit logging (validation)
- **`router_benchmark.py`** - Benchmarks router route_decision performance with and without cache (validation)

### **Brief & Generation** (High Importance)
- **`analyze_brief.py`** - Extracts structured metadata, maps protocols, classifies domains (core)
- **`brief_processor.py`** - Unified brief analysis and project generator integration (core)
- **`generate_from_brief.py`** - Generates separate frontend/backend projects with curated Cursor rules (core)
- **`generate_client_project.py`** - Main CLI script for industry-specific, compliance-ready projects (core)
- **`generate_prd_assets.py`** - Generates PRD and architecture summaries from planning artifacts (core)

### **Compliance & Evidence** (High Importance)
- **`compliance_validator.py`** - Performs HIPAA/GDPR/SOX/PCI compliance checks (validation)
- **`evidence_manager.py`** - Comprehensive evidence tracking with SHA-256 checksums and audit trails (evidence)
- **`evidence_schema_converter.py`** - Converts legacy evidence formats to unified schema (evidence)
- **`evidence_report.py`** - Generates comprehensive evidence reports (evidence)
- **`collect_coverage.py`** - Collects test coverage metrics (evidence)
- **`migrate_evidence_data.py`** - Migrates historical evidence data from legacy to unified format (evidence)

### **Workflow & Lifecycle** (Medium Importance)
- **`lifecycle_tasks.py`** - Builds comprehensive task plans from brief specifications (supporting)
- **`update_task_state.py`** - Manages task state transitions and progress tracking (supporting)
- **`enrich_tasks.py`** - Enhances task specifications with additional context (supporting)
- **`plan_from_brief.py`** - Renders structured planning documents from briefs (supporting)

### **Protocol & Instruction Systems** (Medium Importance)
- **`generate_protocol_sequence.py`** - Builds command sequences and integrates with script registry (supporting)
- **`system_instruction_formatter.py`** - Manages authoring, validation, and versioning of system instructions (supporting)
- **`review_protocol_loader.py`** - Loads and parses review playbooks (supporting)
- **`project_generator_orchestration.py`** - Unified project generator adapter for legacy integration (supporting)

### **External Integration** (Medium Importance)
- **`external_services.py`** - Integrates Git, AI Governor, Policy DSL services (supporting)
- **`trigger_plan.py`** - Emits guided trigger/command plan for project generation (supporting)
- **`run_generate_rules.py`** - Lightweight rules generator following generation phase protocols (supporting)

### **Quality Assurance** (Medium Importance)
- **`quality_gates.py`** - Multi-layer quality validation with specialized protocols (validation)
- **`validate_protocol_steps.py`** - Validates protocol step completeness and dependencies (validation)
- **`validate_script_bindings.py`** - Validates script-to-protocol binding integrity (validation)

## Execution Flow

### Step-by-Step Project Pipeline

1. **Project Initialization**
   - `run_workflow.py` → loads configuration and initializes workflow
   - `ai_executor.py` → creates project directory and loads project config
   - `external_services.py` → initializes Git repository and external integrations

2. **Brief Analysis & Protocol Generation**
   - `analyze_brief.py` → extracts structured metadata from project brief
   - `brief_processor.py` → processes brief and generates planning artifacts
   - `generate_protocol_sequence.py` → builds command sequences from brief analysis
   - `trigger_plan.py` → creates guided trigger plan for project generation

3. **AI Validation & Human Approval**
   - `ai_orchestrator.py` → executes AI-driven phases with external service integration
   - `validation_gates.py` → enforces human validation checkpoints at each phase
   - `validate_prd_gate.py` → validates PRD sign-off metadata and architecture
   - `validate_ai_directives.py` → validates AI directive structure and compliance

4. **Project Generation**
   - `generate_from_brief.py` → generates separate frontend/backend projects
   - `generate_client_project.py` → creates industry-specific, compliance-ready projects
   - `generate_prd_assets.py` → generates PRD and architecture summaries
   - `run_generate_rules.py` → generates project-specific Cursor rules

5. **Compliance & Evidence Reporting**
   - `compliance_validator.py` → performs HIPAA/GDPR/SOX/PCI compliance checks
   - `evidence_manager.py` → tracks all artifacts with SHA-256 checksums and timestamps
   - `evidence_report.py` → generates comprehensive evidence reports
   - `collect_coverage.py` → collects test coverage metrics

6. **Quality Gates & Final Validation**
   - `quality_gates.py` → executes multi-layer quality validation
   - `validate_workflow_integration.py` → validates end-to-end workflow integration
   - `evidence_schema_converter.py` → ensures evidence format consistency

## Key Subsystems

### **Human Oversight & Validation**
- **`validation_gates.py`** - Manages human validation checkpoints with approval workflows
- **`validate_prd_gate.py`** - Validates PRD sign-off metadata and architecture requirements
- **`validate_workflow_integration.py`** - Ensures end-to-end workflow integration integrity
- **`validate_ai_directives.py`** - Validates AI directive structure and compliance standards

### **Brief & Generation**
- **`analyze_brief.py`** - Extracts structured metadata and maps protocols from briefs
- **`brief_processor.py`** - Provides unified brief analysis and project generator integration
- **`generate_from_brief.py`** - Generates separate frontend/backend projects with curated rules
- **`generate_client_project.py`** - Main CLI for industry-specific, compliance-ready projects
- **`generate_prd_assets.py`** - Generates PRD and architecture summaries from planning artifacts

### **Compliance & Evidence**
- **`compliance_validator.py`** - Performs HIPAA/GDPR/SOX/PCI compliance validation
- **`evidence_schema_converter.py`** - Converts legacy evidence formats to unified schema
- **`evidence_report.py`** - Generates comprehensive evidence reports for audit trails
- **`collect_coverage.py`** - Collects test coverage metrics and performance data

### **Workflow & Lifecycle**
- **`run_workflow.py`** - CLI entry point and main execution hub
- **`lifecycle_tasks.py`** - Builds comprehensive task plans from brief specifications
- **`update_task_state.py`** - Manages task state transitions and progress tracking
- **`enrich_tasks.py`** - Enhances task specifications with additional context

### **Protocol & Instruction Systems**
- **`generate_protocol_sequence.py`** - Builds command sequences and integrates with script registry
- **`system_instruction_formatter.py`** - Manages authoring, validation, and versioning of system instructions
- **`review_protocol_loader.py`** - Loads and parses review playbooks for quality gates
- **`project_generator_orchestration.py`** - Unified project generator adapter for legacy integration

### **External Integration**
- **`external_services.py`** - Integrates Git, AI Governor, Policy DSL services
- **`trigger_plan.py`** - Emits guided trigger/command plan for project generation
- **`run_generate_rules.py`** - Lightweight rules generator following generation phase protocols
- **`ai_executor.py`** - Main orchestrator executing complete unified workflow

## Human Oversight Layer

### **Validation Gates System**
The `validation_gates.py` script enforces manual checkpoints at critical workflow phases:

- **Phase 0**: Bootstrap completion validation (technical lead, product owner approval)
- **Phase 1**: PRD approval (product owner, stakeholder approval) 
- **Phase 2**: Task generation confirmation (technical lead, developer approval)
- **Phase 3**: Implementation review (technical lead, code reviewer approval)
- **Phase 4**: Quality audit results review (quality engineer, technical lead approval)
- **Phase 5**: Retrospective validation (process owner, team lead approval)
- **Phase 6**: Operations readiness (operations lead, technical lead approval)

### **PRD Gate Validation**
The `validate_prd_gate.py` script ensures PRD artifacts meet quality standards:

- Validates YAML frontmatter with sign-off metadata
- Checks required sections: Overview, Functional Specifications, Technical Specifications, Out of Scope
- Verifies architecture summary completeness
- Ensures proper timestamp and approver information

### **Evidence Tracking & Audit Support**
The evidence system provides comprehensive audit visibility:

- **`evidence_manager.py`** - Tracks all artifacts with SHA-256 checksums and ISO8601 timestamps
- **`evidence_report.py`** - Generates comprehensive evidence reports for compliance audits
- **`evidence_schema_converter.py`** - Ensures evidence format consistency across workflow versions
- **`collect_coverage.py`** - Collects test coverage metrics and performance data

## Usage

### **Starting the System**
```bash
# Complete workflow execution from brief
python scripts/run_workflow.py --brief ./path/to/brief.json

# Initialize project and execute full workflow
python scripts/ai_executor.py init --project my-project
python scripts/ai_executor.py full-workflow --project my-project

# Execute single phase with validation
python scripts/ai_executor.py phase --project my-project --phase 1
```

### **What Happens Next**
1. **Auto-generation**: System analyzes brief and generates protocol sequence
2. **Compliance Check**: Automated HIPAA/GDPR/SOX/PCI validation runs
3. **Validation Gates**: Human approval checkpoints are enforced at each phase
4. **Project Generation**: Industry-specific, compliance-ready projects are created
5. **Evidence Collection**: All artifacts are tracked with checksums and timestamps
6. **Quality Gates**: Multi-layer validation ensures production readiness

### **Manual Validation Commands**
```bash
# Validate PRD gate
python scripts/validate_prd_gate.py --prd PRD.md --architecture ARCHITECTURE.md

# Execute validation gates
python scripts/validation_gates.py request-validation --phase 1
python scripts/validation_gates.py approve-validation --phase 1 --approver "John Doe"

# Generate evidence report
python scripts/evidence_report.py --project my-project --output evidence-report.json
```

## Extensibility

### **Adding New Compliance Validators**
1. Extend `compliance_validator.py` with new control sets and validation logic
2. Add new compliance standards to the validation matrix
3. Update `validate_prd_gate.py` to include new compliance requirements
4. Integrate with `evidence_manager.py` for audit trail tracking

### **Adding New Workflow Rules**
1. Create new protocol files in `unified_workflow/phases/`
2. Update `generate_protocol_sequence.py` with new phase definitions
3. Add automation hooks to `scripts/script-registry.json`
4. Extend `validation_gates.py` with new checkpoint types

### **Adding New Quality Gates**
1. Extend `quality_gates.py` with new audit modes
2. Create new review protocols in `.cursor/ai-driven-workflow/review-protocols/`
3. Integrate with `review_protocol_loader.py` for protocol management
4. Update `evidence_manager.py` to track new quality metrics

### **Integration Points**
- **Rule System**: Extend `system_instruction_formatter.py` for new instruction types
- **External Services**: Add new service integrations to `external_services.py`
- **Evidence Tracking**: Add new artifact categories to `evidence_manager.py`
- **Workflow Automation**: Add new gate types to `workflow_automation.py`

### **Breaking Change Prevention**
- Maintain backward compatibility in evidence schema conversions
- Preserve existing CLI interfaces while adding new options
- Use feature flags for experimental functionality
- Implement proper error handling and graceful degradation
- Maintain comprehensive test coverage for critical paths

This system provides a robust foundation for AI-driven development workflows while maintaining human oversight and ensuring production readiness through comprehensive validation and compliance checking.