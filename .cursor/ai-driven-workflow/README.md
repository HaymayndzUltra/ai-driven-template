# The Governor Workflow: From Idea to Production

## 1. Why: A Structured Workflow for Predictable Results

Working with AI can sometimes feel unpredictable. The AI Governor Framework provides a development workflow designed to fix that, for both new and existing projects.

It provides a structured, sequential process that transforms your AI from a simple code generator into a reliable engineering partner. By following these five protocols, you ensure that both you and the AI are always aligned, moving from a high-level idea to a well-implemented feature with clarity, control, and consistency.

The goal is to make AI-powered development:
-   **Predictable:** Each step has a clear purpose and output.
-   **Controllable:** You are always in the loop for key decisions.
-   **Efficient:** The AI does the heavy lifting, you provide the strategic direction.

## 2. How it Works: The Optimized 5-Protocol Development Lifecycle

This workflow guides you through the entire development process, from initial setup to continuous improvement. Each protocol assigns a specific role to the AI, ensuring a structured and predictable collaboration with **intelligent session management**.

### Step 0: Bootstrap Your Project (One-Time Setup)
**Role:** The AI acts as a **Project Analyst**.

First, the AI analyzes your entire codebase to build a "Context Kit"—a set of foundational `READMEs` and project-specific rules. This is a one-time protocol that turns a generic AI into a project-specific expert.

```
Apply instructions from dev-workflow/0-bootstrap-your-project.md
```
*(For best results, Cursor users should use Max Mode for this step.)*

### Step 1: Create a Product Requirements Document (PRD)
**Role:** The AI acts as a **Product Manager**.

Next, you define the "what" and "why" of your feature. The AI interviews you to create a detailed Product Requirements Document (PRD), ensuring all requirements are captured before any code is written.

```
Apply instructions from dev-workflow/1-create-prd.md

Here's the feature I want to build: [Describe your feature in detail]
```
*(For best results, Cursor users should use Max Mode for this step.)*

### Step 2: Generate Your Task List
**Role:** The AI acts as a **Tech Lead**.

The AI then transforms the PRD into a granular, step-by-step technical execution plan. This ensures that both you and the AI are aligned on the implementation strategy.

```
Apply instructions from dev-workflow/2-generate-tasks.md to @prd-my-feature.md
```
*(Note: Replace `@prd-my-feature.md` with the actual filename of your PRD.)*

*(For best results, Cursor users should use Max Mode for this step.)*

### Step 3: Execute Tasks with Integrated Quality Gates
**Role:** The AI acts as a **Paired Developer** with built-in quality validation.

Here, the AI implements the plan one parent task at a time, within a dedicated chat session. Each session includes implementation + quality audit + retrospective for optimal context preservation.

**🔄 Per Parent Task (New Chat Session):**

1.  **Start a parent task in a fresh session:**
    ```
    Apply instructions from dev-workflow/3-process-tasks.md to @tasks-my-feature.md. Start on task 1.
    ```
    *(Note: Replace `@tasks-my-feature.md` with the actual filename of your task list.)*

2.  **Implementation with Quick Reviews:**
    - AI implements sub-tasks with **integrated quick validation**
    - Critical issues are caught and fixed immediately
    - You review and approve: **"yes"** or **"continue"**

3.  **Protocol 4: Unified Quality Review (Same Session)**
    Once the parent task is complete, use the unified review system by calling the central orchestrator:
    
    **🎯 Tool-Agnostic Command:**
    ```
    Apply instructions from dev-workflow/4-quality-audit.md
    ```
    
    **The orchestrator provides an interactive selection interface:**
    - ☐ **Code Review** - DDD compliance + Code quality (quick feedback)
    - ☐ **🚀 Run All** - Comprehensive 6-layer validation
    - ☐ **Security Check** - Focus on auth/data/multi-tenant validation
    - ☐ **Architecture Review** - Focus on performance + DDD architecture
    - ☐ **Design System** - Component usage + Visual consistency
    - ☐ **UI/UX & Accessibility** - WCAG compliance + Responsive design
    - ☐ **Pre-Production Security** - Complete security validation
    
    **Automatic Fallback:** Custom protocols → Generic protocols (tool-agnostic)

4.  **Protocol 5: Implementation Retrospective (Same Session)**
    Capture learnings while context is fresh:
    ```
    Apply instructions from dev-workflow/5-implementation-retrospective.md
    ```

5.  **Start the next parent task in a new chat:**
    ```
    Apply instructions from dev-workflow/3-process-tasks.md to @tasks-my-feature.md. Start on task 2.
    ```

---

### A Note on the Revolutionary Unified Workflow

This streamlined 5-protocol workflow with a **unified review system** eliminates tool-specific complexity while maintaining all quality benefits. **Key improvements:**

- **Simplified entry point** with a single, central orchestrator
- **Tool-agnostic design** works across Claude Code, Cursor, Aider
- **Context optimization** through intelligent session management  
- **Smart protocol selection** with automatic custom/generic fallback
- **Interactive selection** prevents tool-specific confusion
- **6-layer validation** including Design + UX coverage

**Tool-Specific Usage:**

**Claude Code:** Use the `/review` command for interactive selection.
**Cursor:** Use `@review` for interactive selection.
**Aider:** Use `/load .cursor/dev-workflow/4-quality-audit.md`
**Universal:** All tools use the same underlying protocol system.

The initial structured approach pays off exponentially as the AI learns your codebase patterns and becomes a true expert companion for your project with **predictable, high-quality output across any development tool**.

## 3. Automation Integration Architecture

The dev-workflow now includes comprehensive automation integration across all protocols, ensuring alignment, eliminating gaps, and creating a connected pipeline from client discovery to retrospective.

### Automation Flow Map

```
Protocol 00 (Discovery) → validate_brief.py, score_risks.py, classify_domain.py
                        ↓
Protocol 0 (Bootstrap)  → normalize_project_rules.py, rules_audit_quick.py
                        ↓
Protocol 1 (PRD)        → validate_prd_gate.py, generate_prd_assets.py
                        ↓
Protocol 2 (Tasks)     → validate_tasks.py, enrich_tasks.py
                        ↓
Protocol 3 (Execution) → update_task_state.py, evidence_report.py, run_workflow.py
                        ↓
Protocol 4 (Quality)   → run_workflow.py, aggregate_coverage.py
                        ↓
Protocol 5 (Retrospective) → rules_audit_quick.py, evidence_report.py (aggregate mode)
```

### Script Reference Table

| Protocol | Script | Purpose | Integration Point |
|----------|--------|---------|-------------------|
| 00 | `validate_brief.py` | Brief validation & quality scoring | Phase 5.5 |
| 00 | `score_risks.py` | Risk scoring by impact/likelihood | Phase 5.5 |
| 00 | `classify_domain.py` | Domain classification with ML | Phase 5.5 |
| 0 | `normalize_project_rules.py` | Rule metadata normalization | Steps 6.5, 7.5 |
| 0 | `rules_audit_quick.py` | Rule compliance validation | Steps 6.5, 7.5 |
| 1 | `validate_prd_gate.py` | PRD completeness validation | Phase 4.5 |
| 1 | `generate_prd_assets.py` | Generate user stories, schemas | Phase 4.5 |
| 2 | `validate_tasks.py` | Task file validation | Phase 4.5 |
| 2 | `enrich_tasks.py` | Task metadata enhancement | Phase 4.5 |
| 3 | `update_task_state.py` | Task state synchronization | Steps 3.5, 3.6 |
| 3 | `evidence_report.py` | Evidence capture & aggregation | Steps 3.5, 3.6 |
| 4 | `run_workflow.py` | CI workflow orchestration | Pre-Audit |
| 4 | `aggregate_coverage.py` | Coverage data aggregation | Pre-Audit |
| 5 | `rules_audit_quick.py` | Rule audit for retrospective | Pre-Retrospective |
| 5 | `evidence_report.py` | Evidence aggregation | Pre-Retrospective |

### Integration Checkpoints

Each protocol includes automation checkpoints that validate:
- **Script Execution**: All automation scripts run successfully
- **Quality Gates**: Validation scores meet thresholds
- **Evidence Capture**: Artifacts are properly stored
- **State Synchronization**: Task state is updated correctly

### Quality Gates per Protocol

| Protocol | Gate Criteria | Validation Threshold |
|----------|---------------|---------------------|
| 00 | Brief validation, risks scored, domain classified | Brief score ≥ 80 |
| 0 | Rules normalized, audit report generated | All rules validated |
| 1 | Assets generated, PRD validation complete | PRD score ≥ 85 |
| 2 | Tasks validated and enriched | All tasks enhanced |
| 3 | Task state synced, evidence captured | State synchronized |
| 4 | CI workflows executed, coverage aggregated | CI status checked |
| 5 | Rule audit complete, evidence aggregated | Audit complete |

## 4. Quick Start with Automation

### Step 0: Client Discovery (New)
**Role:** The AI acts as a **Client Discovery Specialist**.

Transform any job post into a structured project brief with automated validation:

```
Apply instructions from dev-workflow/00-client-discovery.md

--- JOB POST START ---
[Your job post content here]
--- JOB POST END ---
```

**Automation:** Brief validation, risk scoring, domain classification

### Step 1: Bootstrap with Automation
**Role:** The AI acts as a **Project Analyst** with automation.

```
Apply instructions from dev-workflow/0-bootstrap-your-project.md
```

**Automation:** Rule normalization, rule audit, template discovery

### Step 2: PRD Creation with Automation
**Role:** The AI acts as a **Product Manager** with asset generation.

```
Apply instructions from dev-workflow/1-create-prd.md
```

**Automation:** PRD asset generation, validation gate

### Step 3: Task Generation with Automation
**Role:** The AI acts as a **Tech Lead** with task enhancement.

```
Apply instructions from dev-workflow/2-generate-tasks.md to @prd-my-feature.md
```

**Automation:** Task validation, task enrichment

### Step 4: Execution with Automation
**Role:** The AI acts as a **Paired Developer** with evidence capture.

```
Apply instructions from dev-workflow/3-process-tasks.md to @tasks-my-feature.md. Start on task 1.
```

**Automation:** Task state sync, evidence capture

### Step 5: Quality Audit with Automation
**Role:** The AI acts as a **Quality Engineer** with CI integration.

```
Apply instructions from dev-workflow/4-quality-audit.md
```

**Automation:** CI workflow execution, coverage aggregation

### Step 6: Retrospective with Automation
**Role:** The AI acts as a **Process Improvement Lead** with evidence analysis.

```
Apply instructions from dev-workflow/5-implementation-retrospective.md
```

**Automation:** Rule audit, evidence aggregation

## 5. Troubleshooting Quick Reference

### Common Automation Issues

**Issue:** Script not found
```
Error: python scripts/script_name.py: No such file or directory
```
**Fix:** Check script exists and is executable: `chmod +x scripts/script_name.py`

**Issue:** Automation gate failure
```
[GATE FAILED] Automation Validation Complete
```
**Fix:** Check automation script output for specific errors and address underlying issues

**Issue:** Evidence pipeline broken
```
Missing evidence artifacts in retrospective
```
**Fix:** Verify evidence capture in Protocol 3 and aggregation in Protocol 5

**Issue:** CI workflow integration issues
```
CI workflows not executing or results not captured
```
**Fix:** Verify GitHub Actions workflow files exist and `run_workflow.py` configuration

### Validation Commands

```bash
# Validate entire workflow integration
python scripts/validate_workflow_integration.py

# Run integration tests
bash scripts/test_workflow_integration.sh

# Check specific protocol
python scripts/validate_brief.py brief.md --verbose
```

## 6. Documentation References

- **[INTEGRATION-GUIDE.md](INTEGRATION-GUIDE.md)** - Complete automation integration documentation
- **[VALIDATION-GUIDE.md](VALIDATION-GUIDE.md)** - Validation system documentation
- **[Protocol Files](.)** - Individual protocol documentation

## 7. Continuous Validation

The workflow includes continuous validation through:
- **GitHub Actions**: Automated validation on every commit
- **Integration Tests**: End-to-end workflow testing
- **Quality Gates**: Validation at each protocol checkpoint
- **Evidence Pipeline**: Traceable execution history

---

## 8. Folder Overview and Key Files

This directory contains the end-to-end dev-workflow protocols and the unified quality review system used throughout the repository.

### Directory structure (high level)

- `README.md` – Overview and usage of the 5‑protocol lifecycle with automation
- `INTEGRATION-GUIDE.md` – Detailed automation integration guide
- `VALIDATION-GUIDE.md` – Validation and quality gate details
- `0-bootstrap-your-project.md` – Protocol 0 bootstrap procedure
- `1-create-prd.md` – Protocol 1 PRD creation
- `2-generate-tasks.md` – Protocol 2 task generation
- `3-process-tasks.md` – Protocol 3 controlled execution
- `4-quality-audit.md` – Unified review orchestrator and entry point
- `5-implementation-retrospective.md` – Protocol 5 retrospective
- `review-protocols/` – Library of specialized review protocols and utilities

### Key interactions

- Orchestrated reviews are invoked via `4-quality-audit.md` and leverage utilities under `review-protocols/utils/`.
- Protocol 3 mandates running Protocol 4 (comprehensive audit) and then Protocol 5 (retrospective) per parent task.

### Quick links (protocol entry points)

- Bootstrap → `0-bootstrap-your-project.md`
- PRD → `1-create-prd.md`
- Tasks → `2-generate-tasks.md`
- Execute → `3-process-tasks.md`
- Review → `4-quality-audit.md`
- Retro → `5-implementation-retrospective.md`

### Notes on advanced features

- Interactive, tool‑agnostic review selection is centralized in `4-quality-audit.md` and routes through `_review-router.md` for automatic custom↔generic fallback.
- Automation checkpoints and evidence capture are integrated across protocols (see tables above) to maintain auditable execution.
