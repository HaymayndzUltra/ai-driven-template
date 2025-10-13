# Complete End-to-End AI-Driven Pipeline Analysis

## Overview

This document provides a comprehensive technical architecture analysis and operational runbook for the AI Governor Framework - a complete AI-driven development workflow system spanning from client discovery to production operations.

---

## PART 1: TECHNICAL ARCHITECTURE

### 1.1 System Overview

**The AI Governor Framework** is an AI-driven development lifecycle automation system that transforms job posts into production-ready applications through a structured 7-protocol pipeline with automated quality gates, evidence capture, and template-based code generation.

**Core Components:**
- **7 Development Protocols** (00→5): Structured AI-guided workflows
- **60+ Automation Scripts**: Quality gates, validation, evidence capture
- **Template Pack System**: Multi-stack project scaffolding
- **Project Generator**: CLI-driven project creation engine
- **Evidence Pipeline**: Automated artifact collection and traceability
- **CI/CD Integration**: GitHub Actions workflow orchestration
- **Rule Governance System**: Context-aware AI behavior control

---

### 1.2 Protocol Architecture (The 7-Phase Pipeline)

#### Protocol 00: Client Discovery & Project Briefing
**AI Persona:** Client Discovery Specialist
**Input:** Raw job post, RFP, or project brief
**Output:** Structured, validated project brief with risks and acceptance criteria

**Flow:**
```
Job Post → Normalization → Signal Extraction → Clarification → Risk Analysis → 
Brief Generation → Validation
```

**Automation Scripts:**
- `validate_brief.py`: Brief quality scoring (target: ≥80%)
- `score_risks.py`: Risk impact/likelihood analysis
- `classify_domain.py`: ML-based domain classification

**Key Features:**
- Domain-specific extraction patterns (web/mobile/data/ML/infra)
- Assumption tracking with rationale
- Evidence mapping with source quotes
- Automated risk matrix generation

---

#### Protocol 0: Bootstrap & Context Engineering
**AI Persona:** Codebase Analyst & Context Architect
**Input:** Existing codebase or blank slate
**Output:** Context Kit (READMEs + project-specific rules)

**Flow:**
```
Codebase Scan → Stack Detection → Thematic Analysis → Principle Synthesis → 
README Generation → Rule Creation → Template Discovery
```

**Automation Scripts:**
- `normalize_project_rules.py`: Rule metadata standardization
- `rules_audit_quick.py`: Compliance validation
- `generate_from_brief.py`: Fast-path project scaffolding

**Key Features:**
- Dynamic rule discovery and activation
- Semantic code analysis for pattern extraction
- Template pack integration
- Context kit initialization

**Context Kit Structure:**
```
.cursor/
├── context-kit/
│   └── README.md              # Synthesized architectural principles
├── rules/
│   ├── master-rules/          # 8 foundational rules
│   ├── common-rules/          # 10 cross-project patterns
│   └── project-rules/         # Project-specific conventions
└── bootstrap/
    └── detected-stack.json    # Technology inventory
```

---

#### Protocol 1: PRD Creation
**AI Persona:** Product Manager
**Input:** Feature request or project brief
**Output:** Implementation-ready PRD with schemas, contracts, and workflows

**Flow:**
```
Feature Analysis → Layer Detection → Specification Gathering → 
Constraint Validation → PRD Generation → Asset Generation
```

**Automation Scripts:**
- `validate_prd_gate.py`: Completeness validation (target: ≥85%)
- `generate_prd_assets.py`: User stories, data schemas, API contracts

**Architectural Decision Matrix:**
| Need Type | Implementation Target | Communication Patterns |
|-----------|---------------------|----------------------|
| UI/Component | Frontend App | API calls (read-only REST) |
| Business Logic | Backend Microservices | Full CRUD to central API |
| Data CRUD | Central REST API | Direct DB queries |
| Static Assets | Object Storage (S3/R2) | Direct SDK access |

**Key Features:**
- Layer-specific interrogation (Frontend vs Backend vs Central API)
- Communication constraint enforcement
- Anti-over-engineering principles
- Automated asset generation for Protocol 2

---

#### Protocol 2: Task Generation
**AI Persona:** Tech Lead
**Input:** PRD + architectural context
**Output:** Granular task plan with automation hooks

**Flow:**
```
Rule Indexing → PRD Analysis → Layer Identification → High-Level Tasks → 
Detailed Breakdown → Automation Annotation → Validation
```

**Automation Scripts:**
- `validate_tasks.py`: Task file quality checks
- `enrich_tasks.py`: Effort estimation, risk flags, coverage metadata

**Task Structure:**
```markdown
- [ ] 1.0 **Develop User Profile Component** [COMPLEXITY: Complex] [DEPENDS ON: -]
> **WHY:** Enable users to manage personal information, improving retention by 15%
> **Recommended Model:** Claude Sonnet 4.5
> **Automation:** script:python scripts/run_tests.py --scope UserProfile, workflow:ci-test.yml

  - [ ] 1.1 File Scaffolding [APPLIES RULES: component-structure, file-naming]
  - [ ] 1.2 Base HTML Implementation [APPLIES RULES: html-standards, i18n]
  - [ ] 1.3 JavaScript Logic [APPLIES RULES: api-communication, error-handling]
```

**Key Features:**
- Dynamic rule application to sub-tasks
- Dependency tracking for parallel execution
- Complexity assessment (Simple/Complex)
- Automation hook binding (scripts + CI workflows)
- WHY context for business value alignment

---

#### Protocol 3: Task Execution
**AI Persona:** Paired Developer
**Input:** Task plan from Protocol 2
**Output:** Implemented code with evidence artifacts

**Flow (Per Parent Task):**
```
Model Verification → Environment Validation → Sub-task Loop → 
Quality Checks → Evidence Capture → Retrospective
```

**Execution Loop (Per Sub-task):**
```
1. Context Loading (JIT rule activation)
2. Platform Documentation Check
3. Code Implementation
4. Integrated Quick Reviews
5. Task File Update
6. Granular Git Commit
```

**Automation Scripts:**
- `update_task_state.py`: Task status synchronization
- `evidence_report.py`: Artifact collection
- `run_workflow.py`: CI orchestration

**Quality Gates (Integrated):**
- **Security/Architecture Changes:** Quick validation with 4-quality-audit.md
- **Database Changes:** Migration validation + rollback testing
- **UI Components:** Shadow DOM, asset loading, build tool checks

**Hybrid Commit Strategy:**
```bash
# Sub-task level (granular)
feat(iam): implement role inheritance logic

# Parent task level (consolidated - optional)
feat(iam): complete role-based access control module
- Implements role inheritance
- Adds permission validation
- Includes comprehensive tests
```

**Evidence Artifacts:**
```
.artifacts/
├── tests/
│   ├── test-results-task-1.1-20251006.json
│   └── coverage-task-1.1-20251006.html
├── quality/
│   └── quick-review-task-1.0-20251006.md
└── deployments/
    └── deployment-log-staging-20251006.txt
```

---

#### Protocol 4: Quality Audit Orchestrator
**AI Persona:** Senior Quality Engineer
**Input:** Completed parent task
**Output:** Comprehensive quality report with actionable findings

**Flow:**
```
Pre-Audit CI Check → Protocol Selection → Specialized Audit Execution → 
Coverage Aggregation → Findings Report → Fix Recommendations
```

**Automation Scripts:**
- `run_workflow.py`: CI workflow execution (ci-test.yml, ci-lint.yml)
- `aggregate_coverage.py`: Multi-source coverage consolidation

**Review Modes:**
- **Code Review:** DDD compliance + code quality
- **Run All:** 6-layer comprehensive validation
- **Security Check:** Auth/data/multi-tenant validation
- **Architecture Review:** Performance + DDD architecture
- **Design System:** Component usage + visual consistency
- **UI/UX & Accessibility:** WCAG compliance + responsive design
- **Pre-Production Security:** Complete security validation

**CI Integration:**
```bash
# Pre-audit workflow check
gh run list --workflow=ci-lint.yml --limit 5
gh run list --workflow=ci-test.yml --limit 5

# Status validation
[CI/CD ALIGNED] Pre-audit workflow status:
- ci-lint.yml (Run #1234): ✅ PASSED (0 critical issues)
- ci-test.yml (Run #1235): ✅ PASSED (87% coverage)
```

**Quality Gate Criteria:**
- All CI workflows pass
- Test coverage ≥80%
- No CRITICAL/HIGH severity issues
- Documentation updated
- Security scans clean

---

#### Protocol 5: Implementation Retrospective
**AI Persona:** Process Improvement Lead
**Input:** Completed parent task + evidence artifacts
**Output:** Learnings report with framework improvements

**Flow:**
```
Evidence Aggregation → Rule Audit → Code Compliance Review → 
Process Analysis → Improvement Proposals → Framework Updates
```

**Automation Scripts:**
- `rules_audit_quick.py`: Rule governance validation
- `evidence_report.py --aggregate`: Comprehensive artifact collection

**Analysis Dimensions:**
- Communication Efficiency
- Technical Execution Quality
- Process Flow Friction Points
- Rule/Guideline Effectiveness
- User Experience (cognitive load)
- Outcome Quality vs Expectations

**Evidence-Driven Analysis:**
```bash
# Aggregate all task evidence
python scripts/evidence_report.py \
  --scope parent-task-1.0 \
  --aggregate \
  --output .artifacts/retrospective-evidence.json

# Reference in retrospective
[EVIDENCE-BASED ANALYSIS]
- Test coverage: 87% (3 sub-tasks, 42 tests)
- CI workflows: 5/5 passed
- Deployment: Staging successful (2min deploy time)
- Issues found: 2 MEDIUM (both addressed)
```

**Improvement Loop:**
- Rule metadata feedback (false positives)
- Over-engineering detection
- Process bottleneck identification
- Rule/protocol diff proposals

---

### 1.3 Automation Script Ecosystem

#### Script Categories

**1. Validation Scripts** (Quality Gates)
- `validate_brief.py`: Brief completeness (≥80%)
- `validate_prd_gate.py`: PRD quality (≥85%)
- `validate_tasks.py`: Task file structure
- `validate_workflows.py`: CI/CD configuration
- `validate_protocol_steps.py`: Protocol consistency

**2. Enhancement Scripts** (Asset Generation)
- `generate_prd_assets.py`: User stories, schemas, contracts
- `enrich_tasks.py`: Effort estimation, risk flags
- `generate_architecture_pack.py`: C4 diagrams, ADRs
- `generate_contract_assets.py`: API contracts

**3. Execution Scripts** (Orchestration)
- `run_workflow.py`: CI workflow triggering
- `update_task_state.py`: Task synchronization
- `lane_executor.py`: Parallel task execution

**4. Evidence Scripts** (Artifact Management)
- `evidence_report.py`: Artifact aggregation
- `aggregate_coverage.py`: Coverage consolidation
- `collect_perf.py`: Performance metrics

**5. Governance Scripts** (Rule Management)
- `normalize_project_rules.py`: Metadata standardization
- `rules_audit_quick.py`: Compliance checking
- `analyze_project_rules.py`: Rule effectiveness analysis

**6. Infrastructure Scripts** (DevOps)
- `deploy_backend.sh`: Backend deployment
- `rollback_backend.sh`: Deployment rollback
- `run_quality_gates.sh`: Quality orchestration

---

### 1.4 Template Pack System

#### Structure
```
template-packs/
├── frontend/
│   ├── nextjs/        # Next.js SPA
│   ├── nuxt/          # Nuxt.js SSR
│   ├── angular/       # Angular SPA
│   └── expo/          # React Native mobile
├── backend/
│   ├── fastapi/       # Python FastAPI
│   ├── django/        # Django REST
│   ├── nestjs/        # NestJS TypeScript
│   └── go/            # Go Fiber
├── database/
│   ├── postgres/      # PostgreSQL + migrations
│   ├── mongodb/       # MongoDB + schemas
│   └── firebase/      # Firebase config
├── cicd/
│   ├── ci-test.yml    # Test workflow
│   ├── ci-lint.yml    # Linting workflow
│   ├── ci-deploy.yml  # Deployment workflow
│   └── gates_config.yaml
├── devex/
│   ├── devcontainer/  # VS Code containers
│   └── docker-compose/
└── policy-dsl/
    └── client-generator-policies.yaml
```

#### Template Manifest Format
```json
{
  "name": "FastAPI Starter",
  "variants": ["base", "async", "graphql"],
  "engines": ["jinja2"],
  "dependencies": {
    "python": ">=3.10",
    "postgresql": ">=14"
  }
}
```

---

### 1.5 Project Generator Architecture

#### Core Components

**1. Generator Core** (`project_generator/core/generator.py`)
- Project scaffolding engine (3000+ lines)
- Multi-threaded template copying
- Placeholder replacement (regex-based)
- CI/CD workflow integration

**2. Validator** (`project_generator/core/validator.py`)
- Stack compatibility matrix
- Compliance pack validation (HIPAA, SOC2, PCI)
- Project type requirements

**3. Industry Config** (`project_generator/core/industry_config.py`)
- Industry-specific playbooks (healthcare, fintech, etc.)
- Feature/regulation mapping

**4. Template Engine** (`project_generator/templates/template_engine.py`)
- Jinja2-based rendering
- Variable interpolation
- Asset copying with parallel execution

**5. Template Registry** (`project_generator/templates/registry.py`)
- Template discovery and indexing
- Manifest parsing
- Variant resolution

#### Generation Flow
```
Brief Parsing → Industry Config Merge → Validation → 
Template Discovery → File Generation → Post-Processing
```

**Example Usage:**
```python
from project_generator.core.generator import ProjectGenerator

args = Namespace(
    name="healthcare-portal",
    industry="healthcare",
    project_type="fullstack",
    frontend="nextjs",
    backend="fastapi",
    database="postgres",
    auth="auth0",
    compliance="hipaa",
    output_dir="./output"
)

generator = ProjectGenerator(args=args)
result = generator.generate()
# Output: Complete project in ./output/healthcare-portal/
```

---

### 1.6 Evidence Pipeline Architecture

#### Capture Points

**1. Sub-task Completion** (Protocol 3)
```bash
# After each sub-task
python scripts/collect_coverage.py \
  --scope task-1.1 \
  --output .artifacts/tests/coverage-task-1.1-$(date +%Y%m%d-%H%M).html
```

**2. Parent Task Completion** (Protocol 3)
```bash
# Aggregate sub-task evidence
python scripts/aggregate_coverage.py \
  --input ".artifacts/tests/coverage-*-task-1.*" \
  --output ".artifacts/tests/coverage-aggregated-task-1.0.html"
```

**3. CI Workflow Execution** (GitHub Actions)
```yaml
# In .github/workflows/ci-test.yml
- name: Upload Test Results
  uses: actions/upload-artifact@v3
  with:
    name: test-results-${{ github.run_id }}
    path: .artifacts/tests/
    retention-days: 30
```

**4. Retrospective Analysis** (Protocol 5)
```bash
# Aggregate all evidence for retrospective
python scripts/evidence_report.py \
  --scope parent-task-1.0 \
  --aggregate \
  --output .artifacts/retrospective-evidence.json
```

#### Evidence Manifest Schema
```json
{
  "task_id": "1.0",
  "timestamp": "2025-10-06T15:30:00Z",
  "artifacts": [
    {
      "type": "test_results",
      "path": ".artifacts/tests/test-results-task-1.0.json",
      "checksum": "sha256:abc123...",
      "metadata": {
        "tests_run": 42,
        "tests_passed": 40,
        "coverage": "87%"
      }
    }
  ]
}
```

---

### 1.7 CI/CD Integration Architecture

#### GitHub Actions Workflows

**Workflow 1: ci-lint.yml**
- **Triggers:** Push, PR, manual
- **Purpose:** Code quality, security scans
- **Tools:** Ruff, ESLint, Bandit, Shellcheck
- **Gate:** Fails on critical security issues

**Workflow 2: ci-test.yml**
- **Triggers:** PR, manual
- **Purpose:** Test suite execution
- **Coverage:** Frontend, backend, integration
- **Artifacts:** JUnit XML, coverage HTML/JSON

**Workflow 3: ci-deploy.yml**
- **Triggers:** Manual, release tags
- **Purpose:** Staging/production deployment
- **Environments:** Staging (auto), Production (gated)
- **Integrations:** Cloudflare Workers, Supabase

#### Quality Gate Alignment

**Pre-Audit Integration:**
```bash
# Query workflow statuses
gh run list --workflow=ci-lint.yml --limit 5
gh run list --workflow=ci-test.yml --limit 5

# Get specific run details
gh run view 1234 --log-failed
```

**Parent Task Blocking:**
```markdown
[QUALITY GATE] ❌ FAILED - Critical workflow failures

**ci-test.yml** (Run #1235)
- Status: ❌ FAILED
- Coverage: 72% (target: 80% - BELOW THRESHOLD)
- Failing tests: 3/42

**Action Required:** Fix failing tests before proceeding
```

---

### 1.8 Rule Governance System

#### Rule Hierarchy

**Master Rules** (8 foundational)
1. Context Discovery Protocol (BIOS)
2. AI Collaboration Guidelines
3. Code Quality Checklist
4. Code Modification Safety Protocol
5. Documentation & Context Guidelines
6. How to Create Effective Rules
7. Dev-Workflow Integration Guide
8. Protocol Integration Methodology

**Common Rules** (10 cross-project)
- CI Quality Gate Alignment
- UI Foundation Design System
- UI Interaction & A11y
- Evidence Pipeline Standard
- Task Automation Binding
- Template Bootstrap Integration
- Rule Automation Protocol

**Project Rules** (project-specific)
- Component structure conventions
- API communication patterns
- Database migration standards
- Authentication flows

#### Rule Metadata Format
```yaml
---
description: "TAGS: [tag1,tag2] | TRIGGERS: keyword1,keyword2 | SCOPE: scope | DESCRIPTION: Purpose"
alwaysApply: false
---
```

#### Rule Discovery Protocol
```bash
# Phase 1: Find all rule directories
find . -name "*rules" -type d

# Phase 2: Parse metadata
# Read YAML frontmatter from each .mdc file

# Phase 3: Build index
# Create in-memory index of TAGS, TRIGGERS, SCOPE

# Phase 4: Apply relevant rules
# Match against task context
```

---

## PART 2: OPERATIONAL RUNBOOK

### 2.1 Getting Started (New Projects)

#### Step 1: Clone Template
```bash
git clone <template-repo-url> my-new-project
cd my-new-project
rm -rf .git
git init
```

#### Step 2: Initialize Project
```bash
# Option A: From job post
Apply instructions from .cursor/ai-driven-workflow/00-client-discovery.md

--- JOB POST START ---
[Paste job post here]
--- JOB POST END ---

# Option B: From existing brief
python scripts/generate_from_brief.py \
  --brief docs/briefs/my-project/brief.md \
  --output-root ../generated-projects \
  --force --yes
```

#### Step 3: Bootstrap Context
```bash
Apply instructions from .cursor/ai-driven-workflow/0-bootstrap-your-project.md
```

---

### 2.2 Feature Development Workflow

#### Phase 1: Create PRD
```bash
Apply instructions from .cursor/ai-driven-workflow/1-create-prd.md

Here's the feature I want to build: [Describe feature]
```

**Output:** `prd-my-feature.md` in `.cursor/prds/`

#### Phase 2: Generate Tasks
```bash
Apply instructions from .cursor/ai-driven-workflow/2-generate-tasks.md to @prd-my-feature.md
```

**Output:** `tasks-my-feature.md` in `.cursor/tasks/`

#### Phase 3: Execute Tasks (Per Parent Task)
```bash
# Start new chat session for each parent task
Apply instructions from .cursor/ai-driven-workflow/3-process-tasks.md to @tasks-my-feature.md. Start on task 1.

# Review and approve: "yes" or "continue"

# Quality audit (automatic after parent task)
Apply instructions from .cursor/ai-driven-workflow/4-quality-audit.md

# Retrospective (same session)
Apply instructions from .cursor/ai-driven-workflow/5-implementation-retrospective.md

# Next parent task (NEW chat session)
Apply instructions from .cursor/ai-driven-workflow/3-process-tasks.md to @tasks-my-feature.md. Start on task 2.
```

---

### 2.3 Quality Validation Commands

#### Validate Protocols
```bash
python scripts/validate_protocol_steps.py
python scripts/validate_ai_directives.py
python scripts/generate_consistency_report.py
```

#### Test Workflow Integration
```bash
bash scripts/test_workflow_integration.sh
```

#### Check Specific Protocol
```bash
python scripts/validate_brief.py brief.md --verbose
python scripts/validate_prd_gate.py prd-feature.md
python scripts/validate_tasks.py tasks-feature.md
```

---

### 2.4 Project Generation Commands

#### Interactive Generation
```bash
python scripts/generate_client_project.py --interactive
```

#### Brief-Based Generation
```bash
python scripts/generate_from_brief.py \
  --brief docs/briefs/my-project/brief.md \
  --output-root ../generated-projects \
  --force --yes
```

#### Bootstrap Existing Project
```bash
python scripts/bootstrap_project.py \
  --name my-project \
  --project-type fullstack \
  --frontend nextjs \
  --backend fastapi
```

---

### 2.5 Evidence Management

#### Collect Evidence
```bash
# Per sub-task
python scripts/collect_coverage.py \
  --scope task-1.1 \
  --output .artifacts/tests/coverage-task-1.1.html

# Aggregate parent task
python scripts/aggregate_coverage.py \
  --input ".artifacts/tests/coverage-*-task-1.*" \
  --output ".artifacts/tests/coverage-task-1.0.html"

# Generate retrospective report
python scripts/evidence_report.py \
  --scope parent-task-1.0 \
  --aggregate \
  --output .artifacts/retrospective-evidence.json
```

---

### 2.6 CI/CD Operations

#### Trigger Workflows
```bash
# Manual workflow trigger
gh workflow run ci-test.yml --ref feature/my-feature

# Check workflow status
gh run list --workflow=ci-test.yml --limit 5

# View specific run
gh run view 1234 --log-failed
```

#### Deploy to Staging
```bash
gh workflow run ci-deploy.yml \
  --ref feature/my-feature \
  --field environment=staging
```

#### Rollback Deployment
```bash
bash scripts/rollback_backend.sh --env staging
bash scripts/rollback_frontend.sh --env staging
```

---

### 2.7 Rule Management

#### Normalize Rules
```bash
python scripts/normalize_project_rules.py --target .cursor/rules/
```

#### Audit Rules
```bash
python scripts/rules_audit_quick.py \
  --output .cursor/rules/audit-$(date +%Y-%m-%d).md
```

#### Analyze Rule Effectiveness
```bash
python scripts/analyze_project_rules.py --target .cursor/rules/
```

---

### 2.8 Troubleshooting Guide

#### Issue 1: Script Not Found
**Symptom:** `python scripts/script_name.py: No such file or directory`

**Resolution:**
```bash
# Check script exists
ls -la scripts/

# Make executable
chmod +x scripts/script_name.py

# Run from repo root
cd /path/to/repo
python scripts/script_name.py
```

#### Issue 2: Automation Gate Failure
**Symptom:** `[GATE FAILED] Automation Validation Complete`

**Resolution:**
```bash
# Check automation output
python scripts/validate_brief.py brief.md --verbose

# Review gate criteria
cat .artifacts/validation.json

# Address underlying issues
# Fix validation errors before proceeding
```

#### Issue 3: Evidence Pipeline Broken
**Symptom:** Missing artifacts in retrospective

**Resolution:**
```bash
# Check artifacts directory
ls -la .artifacts/

# Verify permissions
chmod 755 .artifacts/

# Re-run evidence capture
python scripts/evidence_report.py \
  --scope task-1.0 \
  --output .artifacts/evidence-task-1.0.md
```

#### Issue 4: CI Workflow Failures
**Symptom:** CI workflows not executing

**Resolution:**
```bash
# Check workflow files exist
ls -la .github/workflows/

# Validate workflow syntax
gh workflow view ci-test.yml

# Check GitHub Actions permissions
gh auth status

# View workflow logs
gh run view 1234 --log-failed
```

---

### 2.9 Performance Optimization

#### Parallel Task Execution
```bash
# Use lane executor for independent tasks
python scripts/lane_executor.py \
  --tasks tasks-feature.md \
  --parallel 3
```

#### Template Generation Optimization
```bash
# Use worker threads for large projects
python scripts/generate_client_project.py \
  --workers 8 \
  --brief brief.md
```

#### Evidence Aggregation Optimization
```bash
# Aggregate in batches
python scripts/aggregate_coverage.py \
  --input ".artifacts/tests/coverage-*.html" \
  --batch-size 10
```

---

### 2.10 Maintenance & Updates

#### Update Template Packs
```bash
# Pull latest templates
cd template-packs
git pull origin main
```

#### Migrate Evidence Data
```bash
python scripts/migrate_evidence_data.py \
  --from old-format \
  --to new-format
```

#### Backup Workflows
```bash
python scripts/backup_workflows.py --output ./backups
```

---

## PART 3: INTEGRATION REFERENCE

### 3.1 Protocol Integration Map
```
Protocol 00 → validate_brief.py, score_risks.py, classify_domain.py
Protocol 0  → normalize_project_rules.py, rules_audit_quick.py
Protocol 1  → validate_prd_gate.py, generate_prd_assets.py
Protocol 2  → validate_tasks.py, enrich_tasks.py
Protocol 3  → update_task_state.py, evidence_report.py, run_workflow.py
Protocol 4  → run_workflow.py, aggregate_coverage.py
Protocol 5  → rules_audit_quick.py, evidence_report.py --aggregate
```

### 3.2 Quality Gate Thresholds
| Protocol | Gate Criteria | Threshold |
|----------|--------------|-----------|
| 00 | Brief validation score | ≥80 |
| 0 | Rules normalized | All validated |
| 1 | PRD validation score | ≥85 |
| 2 | Tasks enriched | All enhanced |
| 3 | Task state synced | Synchronized |
| 4 | CI status | All passed |
| 5 | Evidence aggregated | Complete |

### 3.3 File Structure Reference
```
project-root/
├── .cursor/
│   ├── ai-driven-workflow/          # Protocol files
│   ├── rules/                 # Rule governance
│   ├── context-kit/           # Bootstrapped docs
│   ├── tasks/                 # Task plans
│   └── prds/                  # PRD documents
├── .artifacts/                # Evidence artifacts
│   ├── tests/                 # Test results, coverage
│   ├── quality/               # Audit reports
│   └── deployments/           # Deployment logs
├── .github/workflows/         # CI/CD workflows
├── scripts/                   # Automation scripts
├── template-packs/            # Template library
├── project_generator/         # Generator engine
└── workflow1/                 # Extended workflow phases
```

---

## PART 4: ADVANCED TOPICS

### 4.1 Custom Template Creation

#### Create Template Pack
```bash
# 1. Create directory structure
mkdir -p template-packs/backend/my-framework/base

# 2. Add manifest
cat > template-packs/backend/my-framework/template.manifest.json << EOF
{
  "name": "My Framework Starter",
  "variants": ["base"],
  "engines": ["jinja2"]
}
EOF

# 3. Add template files
cp -r my-framework-skeleton/* template-packs/backend/my-framework/base/

# 4. Test generation
python scripts/generate_client_project.py \
  --backend my-framework \
  --test-mode
```

### 4.2 Custom Automation Scripts

#### Create Validation Script
```python
#!/usr/bin/env python3
"""Custom validation script."""

def validate_custom(input_file):
    # Your validation logic
    return {"valid": True, "score": 95}

if __name__ == "__main__":
    import sys
    result = validate_custom(sys.argv[1])
    print(f"[AUTOMATION] Validation: {result['score']}/100")
```

#### Integrate into Protocol
```markdown
### PHASE X.5: CUSTOM VALIDATION

1. **`[MUST]` Execute Custom Validation:**
   ```bash
   python scripts/validate_custom.py --input my-file.md
   ```
```

### 4.3 Industry-Specific Customization

#### Add Industry Config
```python
# project_generator/core/industry_config.py

INDUSTRY_CONFIGS = {
    "fintech": {
        "compliance": ["pci", "soc2"],
        "required_stack": {
            "auth": ["auth0", "okta"],
            "database": ["postgres"]
        },
        "prohibited": {
            "storage": ["public-bucket"]
        }
    }
}
```

---

## Conclusion

This AI-driven pipeline provides a complete, production-ready development workflow from client discovery to operations. The system combines:

- **Structured AI Protocols**: 7-phase guided workflow
- **Automation Scripts**: 60+ quality gates and utilities
- **Template System**: Multi-stack scaffolding
- **Evidence Pipeline**: Complete traceability
- **CI/CD Integration**: Automated quality validation

**Key Success Factors:**
- Follow protocols sequentially (00→5)
- Use separate chat sessions per parent task
- Run automation scripts at each checkpoint
- Validate quality gates before progression
- Capture evidence at all stages
- Conduct retrospectives for continuous improvement

**Support Resources:**
- `.cursor/ai-driven-workflow/README.md` - Protocol guide
- `.cursor/ai-driven-workflow/INTEGRATION-GUIDE.md` - Automation reference
- `scripts/` - All automation utilities
- `template-packs/` - Template library
