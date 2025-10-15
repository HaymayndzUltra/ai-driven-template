# Retrospective Protocol Template

## Overview

This template provides the universal structure for creating "Retrospective Protocol" meta-instructions. These are post-completion analysis workflows that extract learnings and improve future iterations through evidence-based reflection.

Unlike the Cognitive Phase Architecture (CPA) which guides multi-step reasoning workflows, or Awareness Protocols which trigger reactive validation, Retrospective Protocols are **evidence-based learning workflows** that occur after completion to improve future performance.

---

## Universal Template Structure

```markdown
# PROTOCOL [N]: [DOMAIN] RETROSPECTIVE

## 1. AI ROLE AND MISSION

You are a **[Specific Role]**. After [completion event], focus on actionable learnings:
1.  **[Quick Review Type]:** Verify [specific standards] compliance
2.  **Focused Retrospective:** Extract key learnings to improve future iterations

This protocol MUST be executed after all [completion criteria] are complete.

**🚫 [CRITICAL] DO NOT BEGIN WITHOUT [PREREQUISITE CONDITION].** Retrospectives rely on [evidence requirement].

---

## 2. THE TWO-PHASE RETROSPECTIVE WORKFLOW

You must execute these phases in order. Phase 1 informs Phase 2.

### Pre-Retrospective: Automation Enhancement - Evidence Aggregation

1. **`[MUST]` Execute [Domain] Audit:**
   ```bash
   python scripts/[domain]_audit.py --output .artifacts/[domain]-audit-$(date +%Y-%m-%d).md
   ```
   *   **Action:** Audit [specific compliance] and [validation type].
   *   **Action:** Generate [domain] audit report for retrospective analysis.

2. **`[MUST]` Announce [Domain] Audit:**
   ```
   [AUTOMATION] [Domain] Audit Complete: {total_items} items audited, {issues_count} issues found
   ```
   *   **Action:** Display [domain] audit summary.

3. **`[MUST]` Execute Evidence Aggregation:**
   ```bash
   python scripts/[domain]_evidence_report.py --scope [scope-identifier] --aggregate --output .artifacts/retrospective-evidence.json
   ```
   *   **Action:** Aggregate all evidence artifacts from completed [scope].
   *   **Action:** Generate comprehensive evidence report for retrospective.

4. **`[MUST]` Announce Evidence Aggregation:**
   ```
   [AUTOMATION] Evidence Aggregated: {artifact_count} artifacts collected
   ```
   *   **Action:** Display evidence aggregation summary.

### Pre-Retrospective: Evidence Review

1.  **`[MUST]` Aggregate Evidence Artifacts:** Before starting the retrospective, collect and present relevant evidence for the completed [scope].
    *   **Action:** Reuse `.artifacts/retrospective-evidence.json` generated during the automation phase and, if needed, filter it for [scope].

2.  **`[MUST]` Load Evidence into Context:**
    *   **Action:** Reference specific artifacts in analysis ([evidence types])
    *   **Action:** Base recommendations on objective metrics rather than subjective observations
    *   **Action:** Cite evidence in retrospective output with direct links

3.  **`[MUST]` Include [Domain] Outcomes:**
    *   **Action:** Reference [domain-specific metrics] from completed [scope]
    *   **Action:** Include [outcome types] (success/failure, [performance metrics])
    *   **Action:** Use [domain] data to identify patterns ([pattern examples])
    *   **[STRICT]** Archive any additional [scope]-scoped evidence into `.artifacts/` with the `retrospective-` prefix.

### PHASE 1: Technical Self-Review and Compliance Analysis

*This phase is mostly silent. You are gathering facts before presenting them.*

1.  **`[MUST]` Invoke Context Discovery:** Before auditing, you **MUST** apply the [context-discovery-protocol]. This will load all relevant [domain-specific] rules into your context. You will use these rules as the basis for your audit.

2.  **`[MUST]` Verify [Domain] Compliance:** During the audit, check if any new [domain-specific items] were created and verify they follow the [domain] protocol:
    *   **[Compliance Type 1]:** Ensure [specific requirement 1]
    *   **[Compliance Type 2]:** Verify [specific requirement 2]
    *   **[Compliance Type 3]:** Check [specific requirement 3]
    *   **[Compliance Type 4]:** Confirm [specific requirement 4]

3.  **Review the Conversation:** Read the entire conversation history related to the [implementation/process]. Identify every manual intervention, correction, or clarification from the user. These are "weak signals" of an imperfect [process/rule].

4.  **Audit the [Domain] against Loaded Rules:**
    *   Identify all [domain-specific items] that were created or modified.
    *   For each item, systematically check its compliance against the specific rules loaded during context discovery. The goal is to answer the question: "Does this [item] violate any of the principles or directives outlined in the rules I have loaded?"

    **Example Review Process:**
    *   **Identify the scope:** Determine if the modified [item] belongs to the [scope type 1], [scope type 2], or another defined [domain] scope.
    *   **Filter relevant rules:** Select the rules that apply to that specific scope (e.g., all rules with `SCOPE: [scope-identifier]`).
    *   **Conduct the audit:** Go through each relevant rule and verify that the [item] respects its directives. For instance:
        *   If a [item type 1] was created, check it against the [item type 1] structure rule.
        *   If a [item type 2] was added, verify its structure, validation, and [domain-specific requirements] against the relevant [domain] rules.
        *   Verify that [documentation/evidence] was updated as per the project's [domain] guidelines.

5.  **Synthesize Self-Review:**
    *   Formulate one or more hypotheses about friction points or non-compliances.
    *   *Example Hypothesis: "The initial omission of the [required item] suggests its mandatory nature is not emphasized enough in the [specific rule]."*
    *   **[Domain] Coverage Analysis:** Verify that you have effectively utilized the relevant [domain-specific rules] for each [task/process] you implemented. Which rules that you were unaware of could have been beneficial?
    *   **[Domain] Creation Issues:** If [domain-specific items] were created in wrong locations or with incorrect naming, note this as a process failure requiring [domain] protocol reinforcement.
    *   (If applicable) Prepare a `diff` proposal to fix a rule and make it clearer or stricter.
    *   **[NEW] Over-Engineering Analysis:** Review the implemented solution. Was it the simplest possible approach? Did any project rules encourage unnecessary complexity or premature abstraction? Formulate a hypothesis if you suspect a rule is leading to over-engineered outcomes.
    *   **[Domain] Metadata Feedback Loop:** Analyze the rules that were applied during execution based on the `[APPLIES RULES: ...]` annotations in the [task plan/process].
        *   Identify which rules were genuinely relevant and helpful.
        *   Identify which rules were irrelevant ("false positives").
        *   For each irrelevant rule, pinpoint the specific text in its metadata (description, tags, triggers) that likely caused the incorrect association. This analysis is a critical input for continuously improving the rule-to-task matching algorithm.

### PHASE 2: Collaborative Retrospective with the User

*This is where you present your findings and facilitate a discussion to validate improvements.*

1.  **Initiate the Retrospective:**
    > "The [implementation/process] is complete. To help us improve, I'd like to conduct a brief retrospective on our collaboration. I'll start by sharing the findings from my technical self-review."

2.  **Present Self-Review Findings:**
    *   Present your analysis and hypotheses concisely.
    *   *Example: "My analysis shows the [implementation/process] is compliant. However, I noted we had to go back and forth on the [specific area], which suggests our initial [planning document] lacked detail in that area. Do you share that assessment?"*

3.  **Conduct Process Analysis:**
    *   **[STRICT]** Since the AI that executed the [implementation/process] has access to the complete execution data, you **MUST** first provide self-assessment answers based on observed patterns throughout the entire session.
    *   **[STRICT]** Analyze the complete collaboration using these dimensions:
        *   **Communication Efficiency:** How many clarifications were needed? Were instructions clear from the start?
        *   **Technical Execution:** What rework, corrections, or backtracking occurred? Which approaches worked smoothly?
        *   **Process Flow:** Where did the session flow smoothly vs. where did friction occur? What caused delays or confusion?
        *   **Rule/Guideline Effectiveness:** Which rules or patterns helped vs. hindered progress? What was missing or ambiguous?
        *   **User Experience:** What was the user's cognitive load? How many decisions or validations were required?
        *   **Outcome Quality:** Did the final result meet expectations? Were there unexpected issues or benefits?
    *   **[STRICT]** Present your analysis using evidence from the actual session:
        ```
        **PROCESS ANALYSIS BASED ON EXECUTION DATA:**
        - Communication: [Evidence-based assessment of clarity and efficiency]
        - Technical Execution: [Evidence-based assessment of implementation flow]
        - Process Flow: [Evidence-based assessment of workflow efficiency]
        - Guidelines/Rules: [Evidence-based assessment of framework effectiveness]
        - User Experience: [Evidence-based assessment of collaboration quality]
        - Outcomes: [Evidence-based assessment of results vs. expectations]
        ```
    *   **[GUIDELINE]** After presenting your analysis, invite user input: "Do you have anything to add or share regarding this [implementation/process] session that might improve our future collaborations?"

4.  **Propose Concrete Improvement Actions:**
    *   Based on the discussion, synthesize the key takeaways.
    *   Transform each point into an action item.
    *   *Example: "Thank you for the feedback. To summarize, the [process] needs to be stronger on [specific area]. I therefore propose modifying [specific protocol] to add a mandatory question about [specific requirement]. Do you agree with this action plan to improve our framework?"*
    *   If you prepared a `diff`, this is the time to present it.

5.  **Validate and Conclude:**
    *   **[GUIDELINE]** Await user validation on the action plan, unless user indicates autonomous completion is preferred
    *   **[ALTERNATIVE]** If user requests autonomous retrospective, proceed with self-assessment and apply improvements directly
    *   Conclude the interview: "Excellent. I will incorporate these improvements for our future collaborations."

---

## 3. MANDATORY SELF-EVALUATION OF RETROSPECTIVE ANALYSIS

**[STRICT]** After completing your technical self-review and before presenting findings to the user, you MUST perform an objective self-evaluation of your analysis:

### ANALYSIS VALIDITY CHECK
**[REQUIRED]** Critically examine your retrospective findings:
- **Technical Accuracy:** Are your compliance assessments technically accurate for the specific [domain] stack?
- **Context Appropriateness:** Do your identified issues reflect genuine problems or impose inappropriate constraints?
- **Rule Interpretation:** Are you correctly interpreting project rules within their intended context?
- **Process Assessment:** Are identified friction points real inefficiencies or natural parts of [domain] development?

### BIAS DETECTION IN RETROSPECTIVE
**[REQUIRED]** Identify potential biases in your process analysis:
- **Perfectionism Bias:** Are you identifying non-issues as problems due to over-adherence to theoretical standards?
- **Rule Absolutism:** Are you applying rules too rigidly without considering contextual exceptions?
- **Process Over-Engineering:** Are you recommending additional complexity where current simplicity works?
- **False Pattern Recognition:** Are you seeing patterns in isolated incidents?

### CORRECTIVE ACTION FOR RETROSPECTIVE
**[REQUIRED]** If invalid assessments are identified:
1. **Acknowledge Analysis Errors:** Explicitly identify which findings were inappropriate or inaccurate
2. **Provide Context Corrections:** Explain why the current implementation or process is actually appropriate
3. **Revise Recommendations:** Update improvement suggestions based on corrected understanding
4. **Focus on Genuine Improvements:** Identify only real friction points that merit attention

### INTEGRATION WITH USER DISCUSSION
**[REQUIRED]** Use your self-evaluation to:
- Present only validated findings to the user
- Ask targeted questions about genuine friction points
- Avoid leading questions based on invalid assumptions
- Focus discussion on areas where improvement would provide real value

**[COMMUNICATION]** If your self-evaluation reveals errors in your initial analysis, present corrected findings using the format: "OBJECTIVE ANALYSIS OF RETROSPECTIVE FINDINGS" followed by your revised assessment.
```

---

## Pattern Components

### 1. **AI Role and Mission**
Defines the AI's specialized role for conducting retrospectives in a specific domain.

**Customization:**
- Replace `[Specific Role]` with domain expert (Process Improvement Lead, Security Analyst, Performance Engineer)
- Replace `[completion event]` with what triggers the retrospective
- Replace `[Quick Review Type]` with domain-specific review (Code Review, Security Scan, Performance Analysis)
- Replace `[specific standards]` with domain compliance requirements

### 2. **Two-Phase Workflow Structure**

#### **Pre-Retrospective: Automation Enhancement**
Evidence collection and aggregation before analysis.

**Customization:**
- Replace `[Domain]` with specific domain (Security, Performance, Quality, Deployment)
- Replace `[domain]_audit.py` with domain-specific audit script
- Replace `[specific compliance]` with domain compliance type
- Replace `[scope-identifier]` with what defines the scope

#### **Phase 1: Technical Self-Review**
Silent analysis phase gathering facts and evidence.

**Customization:**
- Replace `[context-discovery-protocol]` with domain-specific context loading
- Replace `[domain-specific items]` with what gets audited
- Replace `[Compliance Type N]` with specific compliance checks
- Replace `[item type N]` with domain-specific item types

#### **Phase 2: Collaborative Retrospective**
Present findings and facilitate improvement discussion.

**Customization:**
- Replace `[implementation/process]` with what was completed
- Replace `[specific area]` with domain-specific friction points
- Replace `[planning document]` with domain-specific planning artifact

### 3. **Self-Evaluation Protocol**
Mandatory bias detection and validation before presenting findings.

**Customization:**
- Replace `[domain]` with specific domain throughout
- Replace `[domain] stack` with technology stack
- Replace `[domain] development` with development process

---

## Usage Instructions

### Step 1: Identify Your Retrospective Domain
Determine what type of retrospective you need:
- **Implementation** - Code and feature retrospectives
- **Security** - Security implementation retrospectives
- **Performance** - Performance optimization retrospectives
- **Deployment** - Release and deployment retrospectives
- **Quality** - Quality assurance retrospectives
- **Process** - Workflow and methodology retrospectives

### Step 2: Define Completion Criteria
Identify what constitutes "completion" for triggering the retrospective:
- All tasks in execution plan complete
- Security scan results available
- Performance benchmarks achieved
- Deployment successful
- Quality gates passed

### Step 3: Specify Evidence Types
Define what evidence gets collected and analyzed:
- Code coverage reports
- Security scan results
- Performance metrics
- Deployment logs
- Test results
- User feedback

### Step 4: Configure Compliance Checks
Define what gets audited for compliance:
- Code standards compliance
- Security policy compliance
- Performance requirements compliance
- Deployment checklist compliance
- Quality standards compliance

### Step 5: Set Up Automation Scripts
Create domain-specific automation:
- Audit scripts for compliance checking
- Evidence aggregation scripts
- Report generation scripts
- Metrics collection scripts

---

## Key Differences from Other Protocol Types

| Aspect | CPA (Workflow Protocol) | Awareness Protocol | Retrospective Protocol |
|--------|------------------------|-------------------|----------------------|
| **Purpose** | Guide multi-step reasoning | Monitor cross-cutting concerns | Extract learnings from completion |
| **Activation** | User initiates workflow | Triggered at checkpoints | Triggered after completion |
| **Structure** | Sequential phases | Reactive checks | Two-phase analysis |
| **Human Interaction** | Continuous validation | Report deviations only | Collaborative improvement |
| **Evidence** | Process artifacts | Quality artifacts | Comprehensive execution artifacts |
| **Outcome** | Deliverable creation | Quality maintenance | Process improvement |

---

## Quality Checklist

Before deploying a retrospective protocol, verify:

- [ ] **Clear Role** - AI role is well-defined for domain expertise
- [ ] **Explicit Triggers** - Completion criteria are specific
- [ ] **Evidence Collection** - Comprehensive evidence aggregation
- [ ] **Compliance Checks** - Domain-specific audit criteria
- [ ] **Bias Detection** - Self-evaluation protocol included
- [ ] **Actionable Outputs** - Concrete improvement recommendations
- [ ] **Automation Integration** - Scripts for evidence collection
- [ ] **User Collaboration** - Structured discussion format

---

*This template provides the universal structure for creating Retrospective Protocol meta-instructions that extract learnings and improve future iterations through evidence-based reflection and collaborative analysis.*
