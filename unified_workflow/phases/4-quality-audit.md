# Phase 4: Quality Audit

## AI Role
**Quality Engineer** - Execute comprehensive quality validation protocol

## Mission
Conduct a systematic quality audit by loading and executing the appropriate specialized protocol from the review-protocols directory based on the user-selected mode.

## Prerequisites
- Phase 3 completed (Implementation finished)
- Access to review protocols and quality gates
- Evidence trail from previous phases

## Execution Flow

### 1. Mode Determination
Activated with specific `--mode` flag (e.g., `quick`, `security`, `comprehensive`)

### 2. Context Analysis & Protocol Routing
- Use **Centralized Router** to determine correct protocol file
- Router handles intelligent fallback from custom to generic protocols
- **Router**: `.cursor/dev-workflow/review-protocols/utils/_review-router.md`

### 3. Protocol Execution
- Load instructions from determined protocol file
- Execute specialized validation logic, checklists, and report formats
- All detailed validation defined within specialized files

### 4. Unified Reporting
- Consolidate findings into standardized report format
- Ensure consistency across all audit modes

### 5. **[STRICT] Quality Gate Formatting**
- Format all quality gate instructions using canonical structure
- Apply structural validation to all quality protocols
- Implement enforcement rubric for quality gates
- Use security protocols for security-sensitive gates

### 6. **[STRICT] Validation Gates**
- Gate A (Determinism): All directives must be tagged `[STRICT]` or `[GUIDELINE]`
- Gate B (Measurability): At least one measurable acceptance criterion
- Gate C (Safety): Security controls + audit/logging required
- Gate D (Sanity): No brand/telemetry in YAML frontmatter
- Gate E (Length): Keep under 500 lines or emit `[PERF_WARN]`

## Execution Modes

### Mode: `quick` ("/review" → "Code Review")
- **Focus**: Design compliance + Code quality core
- **Protocol**: `@review-protocols/code-review.md`
- **Duration**: 5-10 minutes

### Mode: `security` ("/review" → "Security Check")
- **Focus**: Security + Module/Component boundaries
- **Protocol**: `@review-protocols/security-check.md`
- **Duration**: 10-15 minutes

### Mode: `architecture` ("/review" → "Architecture Review")
- **Focus**: High-level design + Performance architecture
- **Protocol**: `@review-protocols/architecture-review.md`
- **Duration**: 15-20 minutes

### Mode: `design` ("/review" → "Design System Compliance")
- **Focus**: Design system compliance + Component usage
- **Protocol**: `@review-protocols/design-system.md`
- **Duration**: 8-15 minutes

### Mode: `ui` ("/review" → "UI/UX & Accessibility")
- **Focus**: Accessibility + User experience validation
- **Protocol**: `@review-protocols/ui-accessibility.md`
- **Duration**: 10-20 minutes

### Mode: `deep-security` ("/review" → "Pre-Production Security")
- **Focus**: Complete security validation with testing
- **Protocol**: `@review-protocols/pre-production.md`
- **Duration**: 20-30 minutes

### Mode: `comprehensive` ("/review" → "🚀 Run All")
- **Focus**: Complete quality validation across all layers
- **Protocol**: Sequential execution of ALL above protocols
- **Duration**: 30-60 minutes

## Quality Audit Framework

### Layer 1: Software Design & Architecture Compliance
- **Module & Boundary Validation**: Clear responsibilities, physical separation
- **Inter-Module Communication**: Well-defined interfaces, avoid tight coupling
- **Common Anti-patterns**: Direct imports, "God" objects, chaotic communication

### Layer 2: Security & Multi-Tenant Assurance
- **Module/Boundary Security**: Authentication, secret isolation, input validation
- **Multi-Tenant Data Protection**: RLS policies, tenant_id validation, audit trails
- **Security Audit Points**: SQL injection, XSS, missing validation, auth bypass

### Layer 3: Code Quality & Craftsmanship
- **Master Rules Compliance**: I/O in try/catch, explicit naming, function length
- **Code Craftsmanship**: Readability, structure, complexity, documentation
- **Anti-patterns**: Magic numbers, long functions, inconsistent naming

### Layer 4: Architecture & Performance
- **Architecture Patterns**: SOLID principles, coupling & cohesion, abstraction
- **Application Performance**: Startup time, bundle size, caching, resilience
- **Performance Concerns**: N+1 queries, unnecessary API calls, memory leaks

### Layer 5: Design System Compliance
- **Component Usage**: Design system components only, defined variants
- **Visual Consistency**: Established hierarchy, UI patterns, responsive breakpoints
- **Brand Guidelines**: Visual identity, tone of voice, established standards

### Layer 6: UI/UX & Accessibility
- **WCAG AA+ Validation**: Color contrast, keyboard navigation, ARIA attributes
- **Responsive Design**: Multi-device functionality, touch targets, navigation
- **User Experience**: Interaction consistency, cognitive load, visual feedback

### Layer 7: Testing & Maintainability
- **Testing Coverage**: Unit, integration, E2E, security, performance tests
- **Code Organization**: Modular structure, dependencies, configuration
- **Operational Readiness**: Monitoring, logging, rollback strategies

## Outputs

### Audit Reports
- **File**: `audit-reports/{mode}-{timestamp}.md`
- **Content**: Detailed findings with severity classification
- **Format**: Markdown with structured sections

### Quality Metrics
- **Overall Score**: X/10 rating
- **Critical Issues**: Count and details
- **High Issues**: Count and details
- **Medium Issues**: Count and details
- **Low Issues**: Count and details

### Recommendations
- **Immediate Actions**: Critical issue fixes
- **Short-term**: High priority improvements
- **Long-term**: Medium priority enhancements
- **Optional**: Low priority suggestions

### Evidence Artifacts
- **Audit timeline**: Execution log with timestamps
- **Protocol used**: Which specialized protocol executed
- **Findings log**: All issues discovered and classified
- **Remediation status**: Issues fixed vs. outstanding

## Quality Gates

### Validation Checkpoints
- [ ] Appropriate protocol selected and executed
- [ ] All relevant layers audited
- [ ] Findings properly classified by severity
- [ ] Recommendations provided for each finding
- [ ] Evidence trail complete and traceable

### Success Criteria
- Audit completed without errors
- All critical issues identified and addressed
- Quality score meets minimum threshold
- Report provides actionable recommendations

## Duration
**Target**: 10-60 minutes (depending on mode)  
**Actual**: Variable based on codebase size and complexity

## Next Phase
Proceed to **Phase 5: Retrospective** after audit completion

## Automation Integration

### AI Actions
```python
# Quality audit execution
def execute_quality_audit(mode, implementation_context):
    # 1. Determine protocol
    protocol = determine_protocol(mode)
    
    # 2. Load specialized protocol
    audit_protocol = load_protocol(protocol)
    
    # 3. Execute audit
    findings = execute_audit(audit_protocol, implementation_context)
    
    # 4. Classify findings
    classified_findings = classify_findings(findings)
    
    # 5. Generate report
    report = generate_audit_report(classified_findings, mode)
    
    # 6. Log evidence
    log_evidence("phase4", report, classified_findings)
    
    return {
        "audit_report": report,
        "findings": classified_findings,
        "evidence": get_evidence("phase4")
    }
```

### Human Validation
- User selects audit mode
- User reviews audit findings
- User approves remediation actions
- User confirms audit completion

## Error Handling

### Common Issues
- **Protocol not found**: Fall back to generic protocol
- **Audit failure**: Retry with different mode
- **Critical issues**: Halt until resolved

### Recovery Actions
- Re-run audit with different mode if needed
- Address critical issues before proceeding
- Escalate to human if automation fails

## Automation Integration
- Generate observability packs via `Phase4IntegrationWrappers.generate_observability_pack(project)`. This wrapper ensures the
  manifest records the template lineage for observability artifacts.
- Run smoke tests with `Phase4IntegrationWrappers.run_staging_smoke(project, result="pass", report=Path(...))`. Provide a custom
  report path when integrating with CI pipelines; the wrapper normalizes the expected evidence path.

## Evidence Templates
- Observability specifications and the staging smoke playbook align with the phase 4 entries in
  [workflow1_evidence/index.json](../templates/workflow1_evidence/index.json).

## Operator Instructions
- Attach any additional staging diagnostics to the manifest by setting `automation.parameters` with contextual metadata (e.g.,
  build number, environment).
- When smoke testing fails, capture the generated report path from the wrapper result and annotate the validation log before
  triggering a rerun.
