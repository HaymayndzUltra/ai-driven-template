# Complete System Logic: AI-Driven Development Workflow

## System Overview

Your system is a **comprehensive AI-driven development workflow automation platform** that transforms job posts into production-ready applications through a structured 7-protocol pipeline. It's essentially a "development factory" that uses AI agents to orchestrate the entire software development lifecycle.

---

## Core Architecture

### 1. The 7-Protocol Pipeline (The Heart of the System)

```
Protocol 00: Client Discovery → Protocol 0: Bootstrap → Protocol 1: PRD Creation → 
Protocol 2: Task Generation → Protocol 3: Task Execution → Protocol 4: Quality Audit → 
Protocol 5: Retrospective
```

**Each protocol has:**
- **AI Persona**: Specific role (Client Discovery Specialist, Code Architect, etc.)
- **Input/Output**: Clear data flow between protocols
- **Automation Scripts**: Quality gates and validation
- **Evidence Collection**: Artifacts for traceability

### 2. The AI Orchestration Engine

**How it works:**
1. **User Input**: Job post or project brief
2. **Protocol Orchestrator**: Analyzes input and selects appropriate protocols
3. **AI Agent Execution**: Each protocol runs with specific AI personas
4. **Automation Integration**: Scripts validate and enhance each step
5. **Evidence Pipeline**: Collects artifacts throughout the process
6. **Quality Gates**: Ensures standards are met before progression

---

## Detailed System Logic

### Protocol 00: Client Discovery & Project Briefing
**Purpose**: Transform raw job posts into structured project briefs

**Logic Flow:**
```
Job Post → Normalization → Signal Extraction → Clarification → 
Risk Analysis → Brief Generation → Validation
```

**Key Components:**
- **Domain Classification**: ML-based detection (web/mobile/data/ML/infra)
- **Risk Scoring**: Impact/likelihood analysis
- **Brief Validation**: Quality scoring (target: ≥80%)
- **Evidence Mapping**: Source quotes and assumptions tracking

**Automation Scripts:**
- `validate_brief.py`: Brief quality scoring
- `score_risks.py`: Risk impact/likelihood analysis  
- `classify_domain.py`: ML-based domain classification

### Protocol 0: Bootstrap & Context Engineering
**Purpose**: Initialize project context and governance

**Logic Flow:**
```
Codebase Scan → Stack Detection → Thematic Analysis → 
Principle Synthesis → README Generation → Rule Creation → Template Discovery
```

**Key Components:**
- **Dynamic Rule Discovery**: Finds and activates relevant rules
- **Semantic Code Analysis**: Extracts patterns from existing code
- **Template Pack Integration**: Discovers available scaffolding
- **Context Kit Initialization**: Creates project-specific documentation

**Automation Scripts:**
- `normalize_project_rules.py`: Rule metadata standardization
- `rules_audit_quick.py`: Compliance validation
- `generate_from_brief.py`: Fast-path project scaffolding

### Protocol 1: PRD Creation
**Purpose**: Define product requirements and specifications

**Logic Flow:**
```
Feature Analysis → Layer Detection → Specification Gathering → 
Constraint Validation → PRD Generation → Asset Generation
```

**Key Components:**
- **Layer-Specific Interrogation**: Frontend vs Backend vs Central API
- **Communication Constraint Enforcement**: Prevents over-engineering
- **Automated Asset Generation**: User stories, schemas, API contracts
- **Architectural Decision Matrix**: Guides implementation choices

**Automation Scripts:**
- `validate_prd_gate.py`: Completeness validation (target: ≥85%)
- `generate_prd_assets.py`: User stories, data schemas, API contracts

### Protocol 2: Task Generation
**Purpose**: Break down PRD into executable tasks

**Logic Flow:**
```
Rule Indexing → PRD Analysis → Layer Identification → 
High-Level Tasks → Detailed Breakdown → Automation Annotation → Validation
```

**Key Components:**
- **Dynamic Rule Application**: Applies relevant rules to sub-tasks
- **Dependency Tracking**: Enables parallel execution
- **Complexity Assessment**: Simple/Complex classification
- **Automation Hook Binding**: Links scripts and CI workflows
- **Business Value Alignment**: WHY context for each task

**Automation Scripts:**
- `validate_tasks.py`: Task file quality checks
- `enrich_tasks.py`: Effort estimation, risk flags, coverage metadata

### Protocol 3: Task Execution
**Purpose**: Implement tasks with evidence collection

**Logic Flow (Per Parent Task):**
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

**Key Components:**
- **Hybrid Commit Strategy**: Granular sub-task + consolidated parent task
- **Quality Gates Integration**: Security, architecture, database validation
- **Evidence Artifacts**: Test results, coverage, deployment logs
- **Task State Synchronization**: Real-time progress tracking

**Automation Scripts:**
- `update_task_state.py`: Task status synchronization
- `evidence_report.py`: Artifact collection
- `run_workflow.py`: CI orchestration

### Protocol 4: Quality Audit Orchestrator
**Purpose**: Comprehensive quality validation

**Logic Flow:**
```
Pre-Audit CI Check → Protocol Selection → Specialized Audit Execution → 
Coverage Aggregation → Findings Report → Fix Recommendations
```

**Key Components:**
- **Review Modes**: Code Review, Run All, Security Check, Architecture Review
- **CI Integration**: Pre-audit workflow status checking
- **Quality Gate Criteria**: All CI workflows pass, ≥80% coverage, no critical issues
- **Coverage Aggregation**: Multi-source coverage consolidation

**Automation Scripts:**
- `run_workflow.py`: CI workflow execution
- `aggregate_coverage.py`: Multi-source coverage consolidation

### Protocol 5: Implementation Retrospective
**Purpose**: Learn and improve the system

**Logic Flow:**
```
Evidence Aggregation → Rule Audit → Code Compliance Review → 
Process Analysis → Improvement Proposals → Framework Updates
```

**Key Components:**
- **Evidence-Driven Analysis**: Uses collected artifacts for insights
- **Rule Governance Validation**: Checks rule effectiveness
- **Process Flow Analysis**: Identifies friction points
- **Improvement Loop**: Updates rules and protocols based on learnings

**Automation Scripts:**
- `rules_audit_quick.py`: Rule governance validation
- `evidence_report.py --aggregate`: Comprehensive artifact collection

---

## Automation Script Ecosystem (60+ Scripts)

### 1. Validation Scripts (Quality Gates)
- `validate_brief.py`: Brief completeness (≥80%)
- `validate_prd_gate.py`: PRD quality (≥85%)
- `validate_tasks.py`: Task file structure
- `validate_workflows.py`: CI/CD configuration
- `validate_protocol_steps.py`: Protocol consistency

### 2. Enhancement Scripts (Asset Generation)
- `generate_prd_assets.py`: User stories, schemas, contracts
- `enrich_tasks.py`: Effort estimation, risk flags
- `generate_architecture_pack.py`: C4 diagrams, ADRs
- `generate_contract_assets.py`: API contracts

### 3. Execution Scripts (Orchestration)
- `run_workflow.py`: CI workflow triggering
- `update_task_state.py`: Task synchronization
- `lane_executor.py`: Parallel task execution

### 4. Evidence Scripts (Artifact Management)
- `evidence_report.py`: Artifact aggregation
- `aggregate_coverage.py`: Coverage consolidation
- `collect_perf.py`: Performance metrics

### 5. Governance Scripts (Rule Management)
- `normalize_project_rules.py`: Metadata standardization
- `rules_audit_quick.py`: Compliance checking
- `analyze_project_rules.py`: Rule effectiveness analysis

### 6. Infrastructure Scripts (DevOps)
- `deploy_backend.sh`: Backend deployment
- `rollback_backend.sh`: Deployment rollback
- `run_quality_gates.sh`: Quality orchestration

---

## Template Pack System

### Structure
```
template-packs/
├── frontend/          # Next.js, Nuxt, Angular, Expo
├── backend/          # FastAPI, Django, NestJS, Go
├── database/         # PostgreSQL, MongoDB, Firebase
├── cicd/            # GitHub Actions workflows
├── devex/           # Dev containers, docker-compose
└── policy-dsl/      # Industry-specific policies
```

### Template Manifest Format
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

### Project Generator Architecture
- **Generator Core**: 3000+ lines of scaffolding engine
- **Multi-threaded Template Copying**: Parallel file operations
- **Placeholder Replacement**: Regex-based variable substitution
- **CI/CD Integration**: Automatic workflow setup
- **Industry Config**: Healthcare, fintech, compliance requirements

---

## Evidence Pipeline Architecture

### Capture Points
1. **Sub-task Completion**: Individual task evidence
2. **Parent Task Completion**: Aggregated evidence
3. **CI Workflow Execution**: Automated test results
4. **Retrospective Analysis**: Comprehensive artifact collection

### Evidence Manifest Schema
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

## CI/CD Integration Architecture

### GitHub Actions Workflows
1. **ci-lint.yml**: Code quality, security scans
2. **ci-test.yml**: Test suite execution with coverage
3. **ci-deploy.yml**: Staging/production deployment

### Quality Gate Alignment
- **Pre-Audit Integration**: Workflow status checking
- **Parent Task Blocking**: Fails on critical issues
- **Coverage Thresholds**: Minimum 80% test coverage
- **Security Scans**: Zero critical vulnerabilities

---

## Rule Governance System

### Rule Hierarchy
1. **Master Rules** (8 foundational): Context discovery, AI collaboration, code quality
2. **Common Rules** (10 cross-project): CI alignment, UI standards, evidence pipeline
3. **Project Rules** (project-specific): Component structure, API patterns

### Rule Metadata Format
```yaml
---
description: "TAGS: [tag1,tag2] | TRIGGERS: keyword1,keyword2 | SCOPE: scope | DESCRIPTION: Purpose"
alwaysApply: false
---
```

### Rule Discovery Protocol
1. **Find Rule Directories**: Scan for `*rules` folders
2. **Parse Metadata**: Read YAML frontmatter
3. **Build Index**: Create TAGS/TRIGGERS/SCOPE index
4. **Apply Relevant Rules**: Match against task context

---

## Data Flow Architecture

### Input Processing
```
Job Post → Brief Generation → PRD Creation → Task Planning → 
Code Implementation → Quality Validation → Evidence Collection → 
Retrospective Analysis
```

### Context Management
- **JIT Rule Loading**: Load rules when needed
- **Context Persistence**: Maintain state across protocols
- **Evidence Aggregation**: Collect artifacts throughout
- **Quality Gates**: Validate before progression

### Output Generation
- **Production-Ready Code**: Complete applications
- **Comprehensive Documentation**: READMEs, APIs, tests
- **Quality Metrics**: Coverage, performance, security
- **Retrospective Insights**: Process improvements

---

## Integration Points

### Protocol Integration Map
```
Protocol 00 → validate_brief.py, score_risks.py, classify_domain.py
Protocol 0  → normalize_project_rules.py, rules_audit_quick.py
Protocol 1  → validate_prd_gate.py, generate_prd_assets.py
Protocol 2  → validate_tasks.py, enrich_tasks.py
Protocol 3  → update_task_state.py, evidence_report.py, run_workflow.py
Protocol 4  → run_workflow.py, aggregate_coverage.py
Protocol 5  → rules_audit_quick.py, evidence_report.py --aggregate
```

### Quality Gate Thresholds
| Protocol | Gate Criteria | Threshold |
|----------|--------------|-----------|
| 00 | Brief validation score | ≥80 |
| 0 | Rules normalized | All validated |
| 1 | PRD validation score | ≥85 |
| 2 | Tasks enriched | All enhanced |
| 3 | Task state synced | Synchronized |
| 4 | CI status | All passed |
| 5 | Evidence aggregated | Complete |

---

## System Intelligence Features

### AI Persona System
- **Client Discovery Specialist**: Job post analysis
- **Code Architect**: System design and architecture
- **Product Manager**: Requirements and specifications
- **Tech Lead**: Task planning and coordination
- **Paired Developer**: Code implementation
- **Senior Quality Engineer**: Quality validation
- **Process Improvement Lead**: Retrospective analysis

### Context-Aware Processing
- **Domain Detection**: Web, mobile, data, ML, infrastructure
- **Stack Recognition**: Technology stack identification
- **Pattern Extraction**: Code pattern analysis
- **Rule Application**: Context-specific rule activation

### Quality Assurance
- **Automated Testing**: Unit, integration, E2E tests
- **Security Scanning**: Vulnerability detection
- **Performance Monitoring**: Metrics collection
- **Compliance Checking**: Industry standards validation

---

## Business Logic

### Project Classification
- **Industry Detection**: Healthcare, fintech, e-commerce
- **Compliance Requirements**: HIPAA, PCI, SOC2
- **Technology Preferences**: Framework recommendations
- **Scalability Needs**: Performance requirements

### Resource Management
- **Template Selection**: Appropriate scaffolding
- **Dependency Resolution**: Technology compatibility
- **Resource Optimization**: Efficient resource usage
- **Cost Management**: Budget-aware decisions

### Risk Management
- **Risk Assessment**: Impact/likelihood analysis
- **Mitigation Strategies**: Risk reduction plans
- **Quality Gates**: Failure prevention
- **Rollback Procedures**: Recovery mechanisms

---

## System Capabilities

### What the System Can Do
1. **Transform Job Posts**: Convert raw requirements into structured briefs
2. **Generate Complete Applications**: Full-stack development
3. **Ensure Quality**: Automated testing and validation
4. **Collect Evidence**: Comprehensive artifact tracking
5. **Learn and Improve**: Retrospective analysis and optimization
6. **Scale Projects**: Handle enterprise-level applications
7. **Maintain Compliance**: Industry-specific requirements
8. **Orchestrate Teams**: Multi-agent coordination

### What Makes It Unique
1. **End-to-End Automation**: Complete development lifecycle
2. **AI-Driven Orchestration**: Intelligent workflow management
3. **Evidence-Based Quality**: Measurable quality metrics
4. **Template-Driven Generation**: Consistent project scaffolding
5. **Rule-Based Governance**: Context-aware behavior control
6. **Retrospective Learning**: Continuous improvement
7. **Multi-Stack Support**: Technology-agnostic approach
8. **Production-Ready Output**: Enterprise-grade applications

---

## Success Metrics

### Technical Metrics
- **Code Coverage**: ≥80% test coverage
- **Security Score**: Zero critical vulnerabilities
- **Performance**: Sub-200ms API response times
- **Uptime**: 99.9% availability
- **Deployment Time**: <5 minutes

### Process Metrics
- **Brief Quality**: ≥80% validation score
- **PRD Completeness**: ≥85% validation score
- **Task Completion**: 100% task execution
- **Quality Gates**: All gates passed
- **Evidence Collection**: Complete artifact coverage

### Business Metrics
- **Development Speed**: 10x faster than traditional methods
- **Quality Consistency**: Standardized output quality
- **Cost Reduction**: Minimal human intervention
- **Scalability**: Enterprise-scale project handling
- **Compliance**: Industry-standard adherence

---

## Conclusion

Your system is a **comprehensive AI-driven development factory** that transforms job posts into production-ready applications through intelligent orchestration, automated quality gates, and evidence-based validation. It combines the power of AI agents, automation scripts, template systems, and governance rules to create a self-organizing development environment that produces consistent, high-quality software at scale.

The system's intelligence lies in its ability to:
- **Understand context** through rule-based governance
- **Orchestrate workflows** through protocol automation
- **Ensure quality** through evidence-based validation
- **Learn and improve** through retrospective analysis
- **Scale efficiently** through template-driven generation

This is not just a development tool—it's a complete development ecosystem that revolutionizes how software is built by combining human creativity with AI automation.
