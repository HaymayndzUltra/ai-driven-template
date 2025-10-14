# Phase 3: Implementation

## AI Role
**Paired Developer** - Execute technical task plan sequentially and meticulously

## Mission
Execute a technical task plan from a Markdown file, sequentially and meticulously, following the protocol strictly until all tasks are complete or user issues a different command.

## Prerequisites
- Phase 2 completed (Task plan approved)
- Access to project rules and context
- Development environment ready

## Execution Mode: Focus Mode (Recommended)

### Focus Mode (Per-Parent-Task Validation)
- Execute ALL sub-tasks of a single parent task
- Wait for validation before proceeding
- Maintain coherent short-term memory for the feature

### Continuous Mode (Opt-in)
- Execute all sub-tasks sequentially without intermediate checkpoints
- Stop only upon completion or error
- Requires user signal: "continue and don't stop"

## Context Management: One Parent Task, One Chat Rule

### Session Lifecycle
1. **Execute full parent task** within current chat with integrated quick reviews
2. **Mandatory Quality Gate** - Execute comprehensive quality audit upon completion
3. **Address quality findings** - Fix CRITICAL/HIGH priority issues
4. **Protocol 5** - Implementation Retrospective in same session
5. **Start new chat session** for next parent task
6. **Relaunch protocol** for next parent task

## Pre-Execution Model Check

### Model Verification
1. **Identify Target Parent Task** based on user instruction
2. **Verify Recommended Model** from task file
3. **Announce and await confirmation** if model specified
4. **Halt and await** explicit user confirmation ("Go")

### Communication Flow
```
[PRE-FLIGHT CHECK] The recommended model for parent task {Number} ('{Task Name}') is '{Model Name}'. Please confirm that you are using this model, or switch now.
[AWAITING CONFIRMATION] Reply 'Go' to begin the execution.
```

## Pre-Execution Checks

### Environment Validation
- Check tool versions (supabase, pnpm, wrangler, node)
- Test database connectivity (`supabase status`)
- Announce detected infrastructure

### Production Readiness Validation
- Confirm implementation approach follows production standards
- No mock data, proper validation, configuration management
- Set quality bar for entire execution

## Execution Loop

### Step 1: Sub-Task Context Loading
1. **Identify Next Sub-Task** - First unchecked `[ ]` in plan file
2. **Load Just-in-Time Rule Context**
   - Read sub-task line and identify `[APPLIES RULES: ...]` directive
   - For each rule listed, read corresponding file into active context
   - Announce context loading: `[CONTEXT LOADED] Applying rules: {list of rule names}`
3. **Platform Documentation Check**
   - If sub-task involves specific platform, consult official documentation
   - Announce research
4. **Initial Communication**
   - Announce task: `[NEXT TASK] {Task number and name}`

### Step 2: Execution
1. **Execute Task** - Use available tools to perform ONLY what is asked
   - Apply consulted rules and context
   - Avoid over-engineering - implement most direct solution
2. **Continuous Rule Compliance**
   - Validate against loaded rules during execution
   - Rule 3: Code quality standards (error handling, naming, simplicity)
   - Rule 5: Documentation requirements (README updates, context preservation)
3. **Self-Verification** - Reread sub-task description and confirm criteria met
4. **Integrated Quick Review & Validation**
   - **Security/Architecture Changes**: Apply quick validation, fix critical issues
   - **Database Changes**: Verify migration standards, rollback procedures
   - **System Integration**: Check global state, authentication, system-wide changes
   - **UI Component Validation**: Test shadow DOM communication, external assets

### Step 3: Update and Synchronize
1. **Update Task File** - Change sub-task status from `[ ]` to `[x]`
   - Check parent task if all sub-tasks complete
   - Task file serves as authoritative source of truth
2. **Hybrid Commit Strategy**
   - **Granular Commits** after each functional sub-task
   - **Message Format**: `{type}({scope}): {brief description}`
   - **Examples**: `feat(iam): implement role inheritance logic`
3. **Parent Task Completion Checkpoint**
   - Perform compliance check and optional consolidation
   - **Mandatory Quality Gate Integration**
   - Execute unified `/review` command for comprehensive validation
   - Address CRITICAL/HIGH findings before proceeding
   - Report audit results: `[QUALITY REPORT] Score: X/10. Critical: Y, High: Z. Status: PASS/NEEDS_ATTENTION`

### Step 4: Enhanced Checkpoint
1. **Single Validation Point** - Task complete and working?
2. **Execution Mode Awareness**
   - **Focus Mode**: `Task {Number} complete. Quick review: ✅ PASSED. Commit: {commit_hash}. Continue?`
   - **Continuous Mode**: No communication after each sub-task
3. **Mandatory Quality Gate Execution**
   - For parent task completion, automatically execute comprehensive audit
   - Address CRITICAL/HIGH findings before final checkpoint
   - Report: `[QUALITY REPORT] Audit complete. Score: X/10. Ready for Protocol 5 (Retrospective).`
4. **Resume** - Wait for confirmation only when required by execution mode

## Outputs

### Implemented Features
- **Code Changes**: All sub-tasks implemented
- **Tests**: Unit and integration tests added
- **Documentation**: README updates and inline comments
- **Configuration**: Environment and deployment configs

### Evidence Artifacts
- **Task Progress**: Updated task file with checkboxes
- **Commit History**: Granular commits with descriptive messages
- **Quality Reports**: Audit results and remediation
- **Implementation Log**: Detailed execution timeline

### Quality Gate Results
- **Code Review**: DDD compliance and code quality
- **Security Check**: Security and multi-tenant validation
- **Architecture Review**: Performance and architecture patterns
- **Design System**: Component usage and visual consistency
- **UI/UX**: Accessibility and user experience
- **Pre-Production**: Complete security validation

## Quality Gates

### Validation Checkpoints
- [ ] All sub-tasks completed successfully
- [ ] Code quality standards met
- [ ] Tests written and passing
- [ ] Documentation updated
- [ ] Security requirements satisfied
- [ ] Performance targets met

### Success Criteria
- Parent task fully implemented
- Quality gates pass with acceptable scores
- Evidence trail complete and traceable
- Ready for next parent task or phase

## Duration
**Target**: Variable (per parent task)  
**Actual**: Depends on task complexity and sub-task count

## Next Phase
Proceed to **Phase 4: Quality Audit** after all parent tasks complete

## Automation Integration

### AI Actions
```python
# Implementation execution
def execute_implementation(parent_task, task_plan, context_kit):
    # 1. Pre-flight checks
    preflight_checks(parent_task)
    
    # 2. Execute sub-tasks
    for subtask in parent_task.subtasks:
        # Load context and rules
        context = load_subtask_context(subtask)
        
        # Execute subtask
        result = execute_subtask(subtask, context)
        
        # Quick validation
        validation = quick_validation(result)
        
        # Update task file
        update_task_file(subtask, result)
        
        # Create commit
        create_commit(result)
    
    # 3. Quality gate
    quality_report = run_quality_gates(parent_task)
    
    # 4. Address findings
    if quality_report.critical_issues:
        address_critical_issues(quality_report)
    
    # 5. Log evidence
    log_evidence("phase3", parent_task, quality_report)
    
    return {
        "implementation": parent_task,
        "quality_report": quality_report,
        "evidence": get_evidence("phase3")
    }
```

### Human Validation
- User confirms sub-task completion
- User approves code changes
- User validates quality gate results
- User confirms readiness for next phase

## Error Handling

### Common Issues
- **Sub-task failure**: Stop execution, report failure
- **Quality gate failure**: Address critical issues before proceeding
- **Rule violation**: Fix compliance issues immediately

### Recovery Actions
- Re-execute failed sub-task after fixes
- Re-run quality gates after addressing issues
- Rollback changes if critical problems found

## Automation Integration
- Configure feature flags via `Phase3QualityWrappers.configure_feature_flags(project, flags=[...])`. Pass each flag in the
  `key:type:owner[:description]` format.
- Execute the quality gates with `Phase3QualityWrappers.run_quality_gates(project, bootstrap=True)` to seed templates before running
  the simple quality gate shell script. The wrapper enriches run logs with `automation_reference` metadata.

## Evidence Templates
- Generated assets correspond to the phase 3 entries in
  [workflow1_evidence/index.json](../templates/workflow1_evidence/index.json) including security checklists, A11y plans, and
  performance budgets.

## Operator Instructions
- Validate feature flag manifests and capture manual approvals by appending to the run log with the new metadata fields.
- In the event of a gate failure, inspect the wrapper output (`stdout`/`stderr`) before re-running; this preserves traceability in
  the evidence manifest.
