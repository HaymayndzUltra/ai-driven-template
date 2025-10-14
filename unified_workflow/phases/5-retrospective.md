# Phase 5: Retrospective

## AI Role
**Process Improvement Lead** - Focus on actionable learnings and continuous improvement

## Mission
After implementation, focus on actionable learnings to improve future iterations through quick code review and focused retrospective.

## Prerequisites
- Phase 4 completed (Quality audit finished)
- Access to implementation history and evidence
- Understanding of process effectiveness

## Two-Phase Retrospective Workflow

### Phase 1: Technical Self-Review and Compliance Analysis

#### 1. Invoke Context Discovery
- Apply `1-master-rule-context-discovery` protocol
- Load all relevant architectural and project-specific rules
- Use rules as basis for audit

#### 2. Verify Rule Compliance
- Check if new rules were created
- Verify rule creation protocol compliance:
  - **Location Compliance**: Ensure rules discoverable using `find . -name "*rules" -type d`
  - **Classification Accuracy**: Verify master/common/project classification
  - **Naming Convention**: Check proper prefixes (`common-rule-`, `{project-name}-`)
  - **Discovery Protocol**: Confirm existing rules were searched before creation

#### 3. Review Conversation History
- Read entire conversation history related to implementation
- Identify manual interventions, corrections, clarifications from user
- These are "weak signals" of imperfect rule or process

#### 4. Audit Source Code Against Loaded Rules
- Identify all files created or modified
- For each file, systematically check compliance against loaded rules
- Answer: "Does this code violate any principles or directives in the rules?"

#### 5. Synthesize Self-Review
- Formulate hypotheses about friction points or non-compliances
- **Rule Coverage Analysis**: Verify effective utilization of relevant rules
- **Rule Creation Issues**: Note process failures requiring reinforcement
- **Over-Engineering Analysis**: Review for simplest possible approach
- **Rule Metadata Feedback**: Analyze rule-to-task matching accuracy

### Phase 2: Collaborative Retrospective with User

#### 1. Initiate Retrospective
> "The implementation is complete. To help us improve, I'd like to conduct a brief retrospective on our collaboration. I'll start by sharing the findings from my technical self-review."

#### 2. Present Self-Review Findings
- Present analysis and hypotheses concisely
- Example: "My analysis shows the implementation is compliant. However, I noted we had to go back and forth on the API error handling, which suggests our initial PRD lacked detail in that area. Do you share that assessment?"

#### 3. Conduct Process Analysis
- **Communication Efficiency**: How many clarifications were needed? Were instructions clear?
- **Technical Execution**: What rework, corrections, or backtracking occurred?
- **Process Flow**: Where did the session flow smoothly vs. where did friction occur?
- **Rule/Guideline Effectiveness**: Which rules helped vs. hindered progress?
- **User Experience**: What was the user's cognitive load? How many decisions required?
- **Outcome Quality**: Did the final result meet expectations?

#### 4. Propose Concrete Improvement Actions
- Based on discussion, synthesize key takeaways
- Transform each point into an action item
- Example: "Thank you for the feedback. To summarize, the PRD process needs to be stronger on error handling. I therefore propose modifying `1-create-prd.md` to add a mandatory question about error scenarios. Do you agree with this action plan to improve our framework?"

#### 5. **[STRICT] Process Instruction Formatting**
- Format all process instructions using canonical directives
- Apply versioning and change management
- Implement applicability reporting
- Use deprecation handling for outdated processes

#### 6. **[STRICT] Directive Normalization**
- Normalize directive tags to canonical set
- Apply precedence matrix for conflicting directives
- Ensure headings carry directive context
- Validate structural compliance

#### 5. Validate and Conclude
- Await user validation on action plan
- If user requests autonomous retrospective, proceed with self-assessment
- Conclude: "Excellent. I will incorporate these improvements for our future collaborations."

## Mandatory Self-Evaluation

### Analysis Validity Check
- **Technical Accuracy**: Are compliance assessments technically accurate?
- **Context Appropriateness**: Do identified issues reflect genuine problems?
- **Rule Interpretation**: Are project rules correctly interpreted?
- **Process Assessment**: Are identified friction points real inefficiencies?

### Bias Detection
- **Perfectionism Bias**: Identifying non-issues as problems
- **Rule Absolutism**: Applying rules too rigidly
- **Process Over-Engineering**: Recommending unnecessary complexity
- **False Pattern Recognition**: Seeing patterns in isolated incidents

### Corrective Action
- **Acknowledge Analysis Errors**: Identify inappropriate findings
- **Provide Context Corrections**: Explain why current implementation is appropriate
- **Revise Recommendations**: Update suggestions based on corrected understanding
- **Focus on Genuine Improvements**: Identify only real friction points

## Outputs

### Retrospective Report
- **File**: `retrospective-notes.md`
- **Content**: Detailed analysis and recommendations
- **Format**: Markdown with structured sections

### Process Improvements
- **Rule Updates**: Proposed changes to existing rules
- **New Rules**: Suggested rules for identified gaps
- **Process Changes**: Workflow modifications
- **Tool Improvements**: Automation enhancements

### Evidence Artifacts
- **Retrospective timeline**: Execution log with timestamps
- **Analysis findings**: Technical and process insights
- **Improvement actions**: Concrete next steps
- **Rule change proposals**: Specific rule modifications

## Quality Gates

### Validation Checkpoints
- [ ] Context discovery completed successfully
- [ ] Rule compliance verified
- [ ] Conversation history reviewed
- [ ] Code audit performed
- [ ] Self-review synthesized
- [ ] Collaborative retrospective conducted
- [ ] Improvement actions proposed

### Success Criteria
- Retrospective completed without bias
- Genuine improvement opportunities identified
- Actionable recommendations provided
- User validates findings and actions

## Duration
**Target**: 5-10 minutes  
**Actual**: Variable based on implementation complexity

## Next Phase
Proceed to **Phase 6: Operations** after retrospective completion

## Automation Integration

### AI Actions
```python
# Retrospective execution
def execute_retrospective(implementation_context, quality_audit):
    # 1. Invoke context discovery
    context_rules = invoke_context_discovery()
    
    # 2. Verify rule compliance
    compliance_check = verify_rule_compliance(context_rules)
    
    # 3. Review conversation history
    conversation_analysis = analyze_conversation_history()
    
    # 4. Audit source code
    code_audit = audit_source_code_against_rules(context_rules)
    
    # 5. Synthesize self-review
    self_review = synthesize_self_review(compliance_check, conversation_analysis, code_audit)
    
    # 6. Conduct collaborative retrospective
    collaborative_retro = conduct_collaborative_retrospective(self_review)
    
    # 7. Propose improvements
    improvements = propose_improvement_actions(collaborative_retro)
    
    # 8. Log evidence
    log_evidence("phase5", self_review, improvements)
    
    return {
        "retrospective": self_review,
        "improvements": improvements,
        "evidence": get_evidence("phase5")
    }
```

### Human Validation
- User validates technical findings
- User confirms process analysis
- User approves improvement actions
- User confirms retrospective completion

## Error Handling

### Common Issues
- **Bias in analysis**: Self-evaluation detects and corrects
- **Missing context**: Re-run context discovery
- **Rule conflicts**: Resolve with user input

### Recovery Actions
- Re-evaluate findings if bias detected
- Re-run context discovery if incomplete
- Modify recommendations based on user feedback

## Automation Integration
- Rehearse production rollback via `Phase5LaunchWrappers.rehearse_rollback(project)` prior to change freezes.
- Validate disaster recovery readiness with `Phase5LaunchWrappers.verify_disaster_recovery(project)`; capture manual evidence in
  the returned `ScriptExecutionResult` metadata when additional verification steps are required.

## Evidence Templates
- Launch runbooks, rollback plans, and SEO checklists map to the phase 5 entries in
  [workflow1_evidence/index.json](../templates/workflow1_evidence/index.json).

## Operator Instructions
- After each rehearsal, append summary notes to `evidence/phase5/run.log` and update `validation.md` with automation context.
- In case of failure, re-run the wrapper after addressing issues so the manifest contains the updated checksum for each artifact.
