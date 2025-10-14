# COMPREHENSIVE META-PROMPT FOR CODEX ANALYSIS
## AI-Driven Template System Evaluation & AGENTS.md Generation

### CONTEXT: Understanding the AI-Driven Template Ecosystem (2025)

You are analyzing an **ai-driven-template** system designed to provide complete end-to-end AI-driven development workflows. This system allows users to:

1. **Start with PROJECT-BRIEF.md** - User describes their project requirements
2. **Invoke @protocol-orchestrator.md** - AI analyzes brief and generates appropriate protocols
3. **Execute AI-driven protocols** - AI agents run complete development lifecycle
4. **Collect evidence automatically** - Quality gates, testing, documentation, retrospective

#### Key Components Explained:

**1. .cursorrules (DEPRECATED) → .mdc Rules (CURRENT)**
- **Old Way**: `.cursorrules` at project root (plain text, deprecated in 2025)
- **Modern Way**: `.cursor/rules/*.mdc` files with YAML frontmatter
- **Purpose**: Define AI coding behavior, context discovery, rule loading
- **Format**:
  ```yaml
  ---
  description: "TAGS: [...] | TRIGGERS: ... | SCOPE: ... | DESCRIPTION: ..."
  alwaysApply: true/false
  ---
  # Rule content in Markdown
  ```

**2. AGENTS.md (Codex Agent Configuration)**
- **Purpose**: Configure AI agent behavior per Codex 2025 standards
- **Content**: Agent capabilities, limitations, preferences, integration points
- **Function**: Compressed knowledge not visible in codebase
- **Usage**: Guides AI agent during protocol orchestration and execution

**3. .cursor/commands/ (Slash Commands)**
- **Purpose**: Predefined workflows invoked via `/command-name`
- **Format**: Markdown files with AI execution instructions
- **Examples**: `/protocol-orchestrator`, `/elaborate`, `/bootstrap`
- **Function**: Quick access to complex AI workflows

**4. Protocol Orchestrator System**
- **Purpose**: Intelligent protocol selection and sequencing
- **Input**: PROJECT-BRIEF.md
- **Output**: Sequentially-numbered command files (00-, 01-, 02-)
- **Function**: Analyzes project type, selects protocols, resolves dependencies

---

### TEMPLATE USAGE SCENARIO

```
User Workflow:
1. User creates PROJECT-BRIEF.md with project description
2. User invokes: @protocol-orchestrator.md
3. AI reads AGENTS.md (agent configuration)
4. AI loads .mdc rules (context discovery)
5. AI analyzes brief and classifies project
6. AI generates appropriate protocol sequence
7. AI creates project-specific .cursorrules (if needed)
8. AI sets up project rules and automation hooks
9. User executes generated protocols sequentially
10. AI collects evidence and runs retrospective
```

**Expected End-to-End Lifecycle:**
- **Initialization** → **Analysis** → **Planning** → **Generation** → **Execution** → **Validation** → **Deployment** → **Learning**

---

### ANALYSIS OBJECTIVE

You must conduct a comprehensive evaluation of this ai-driven-template system to determine:

1. **Template Readiness**: Can this be deployed as a permanent template for diverse projects?
2. **AGENTS.md Completeness**: What should be in AGENTS.md for optimal AI agent behavior?
3. **End-to-End Integration**: Do all components work together seamlessly?
4. **Gap Identification**: What's missing for production deployment?
5. **Universal Applicability**: Can it handle web/mobile/data/ML/infrastructure projects?

---

### ANALYSIS FRAMEWORK

#### SECTION 1: CURRENT STATE ASSESSMENT

**1.1 AGENTS.md Analysis**
- [ ] **Current Content**: What does the existing AGENTS.md contain?
- [ ] **Codex Compliance**: Does it follow Codex 2025 standards?
- [ ] **Completeness**: Are all required sections present?
- [ ] **Clarity**: Are agent capabilities clearly defined?
- [ ] **Integration**: Are integration points documented?

**1.2 Protocol Orchestrator Intelligence**
- [ ] **Brief Analysis**: Can AI extract project metadata accurately?
- [ ] **Classification**: Does project classification cover all major types?
- [ ] **Decision Matrix**: Are protocol selection rules comprehensive?
- [ ] **Dependency Resolution**: Can AI resolve protocol dependencies?
- [ ] **Custom Generation**: Can AI generate domain-specific protocols?

**1.3 .mdc Rule System Quality**
- [ ] **Metadata Completeness**: All .mdc files have valid YAML frontmatter?
- [ ] **Coverage**: Master-rules (8) and common-rules (10) cover all needs?
- [ ] **Discoverability**: TAGS, TRIGGERS, SCOPE enable semantic search?
- [ ] **Integration**: Rules properly integrated with protocol execution?

**1.4 .cursor/commands/ Usability**
- [ ] **Entry Points**: Are slash commands intuitive and discoverable?
- [ ] **AI Executability**: Do commands contain clear AI instructions?
- [ ] **Generated Commands**: How are dynamically generated protocols managed?
- [ ] **User Experience**: Is the command interface user-friendly?

#### SECTION 2: END-TO-END LIFECYCLE VALIDATION

**2.1 Complete Workflow Test**
Test the system against these scenarios:

**Scenario A: Simple Landing Page**
- Brief: "Create a marketing landing page with contact form"
- Expected: Minimal protocols (brief analysis, UI design, frontend implementation, deployment)
- Validate: Does AI skip unnecessary protocols (backend, complex architecture)?

**Scenario B: SaaS Billing System**
- Brief: "Multi-tenant SaaS with Stripe integration, user roles, audit logs"
- Expected: Comprehensive protocols (security, database, API, testing, monitoring, deployment)
- Validate: Does AI generate custom protocols for Stripe, multi-tenancy, compliance?

**Scenario C: Data Analytics Dashboard**
- Brief: "BI dashboard for real estate loan portfolio analysis"
- Expected: Data-centric protocols (data discovery, quality assessment, ETL, visualization)
- Validate: Does AI adapt to data-first (vs code-first) workflow?

**Scenario D: Mobile Cross-Platform App**
- Brief: "React Native app for fitness tracking with offline sync"
- Expected: Mobile-specific protocols (native features, offline-first, app store deployment)
- Validate: Does AI recognize mobile-specific requirements?

**Scenario E: Machine Learning Pipeline**
- Brief: "ML model for customer churn prediction with automated retraining"
- Expected: ML-specific protocols (data preparation, model training, deployment, monitoring)
- Validate: Does AI understand ML workflow differences?

**Scenario F: Microservices Architecture**
- Brief: "E-commerce platform with microservices, API gateway, event-driven architecture"
- Expected: Infrastructure protocols (service design, API contracts, event handling, deployment)
- Validate: Does AI handle complex distributed systems?

**Scenario G: DevOps/Infrastructure Project**
- Brief: "Infrastructure as Code for multi-cloud deployment with monitoring"
- Expected: Infrastructure protocols (IaC setup, multi-cloud config, monitoring, security)
- Validate: Does AI understand infrastructure automation needs?

**2.2 Integration Point Validation**
- [ ] **@protocol-orchestrator reads AGENTS.md**: Does orchestrator use agent config?
- [ ] **AI loads .mdc rules**: Are rules loaded during protocol execution?
- [ ] **Protocols reference scripts**: Are automation scripts properly bound?
- [ ] **Evidence collection**: Does evidence collection happen automatically?
- [ ] **Quality gates**: Are quality gates enforced at each step?
- [ ] **Retrospective**: Does retrospective capture learnings automatically?

#### SECTION 3: AGENTS.md CONTENT RECOMMENDATIONS

**3.1 Required Sections Analysis**
Based on Codex 2025 standards, AGENTS.md should contain:

- [ ] **Agent Name**: Clear identifier for the AI agent
- [ ] **Purpose**: What this AI agent does in the system
- [ ] **Capabilities**: Specific tasks the agent can perform
- [ ] **Limitations**: What the agent cannot do
- [ ] **Integration**: How it connects with other system components
- [ ] **Preferences**: Coding style, conventions, architectural decisions
- [ ] **Context Sources**: Where AI gets information (.mdc rules, scripts, etc.)
- [ ] **Workflow**: How AI executes tasks step-by-step
- [ ] **Error Handling**: How AI handles failures and edge cases
- [ ] **Security**: Security considerations and access controls

**3.2 Content Quality Assessment**
- [ ] **Compressed Knowledge**: Does it contain implicit knowledge not in codebase?
- [ ] **Coding Preferences**: Are coding style preferences clearly defined?
- [ ] **Architecture Guidelines**: Are architectural decision guidelines included?
- [ ] **Protocol Logic**: Is protocol selection logic documented?
- [ ] **Evidence Standards**: Are evidence collection standards defined?

#### SECTION 4: GAP ANALYSIS

**4.1 Missing Components**
Identify gaps in:
- [ ] **Protocol Coverage**: Missing protocols for specific project types?
- [ ] **Decision Framework**: Incomplete project classification logic?
- [ ] **Automation Scripts**: Missing automation for protocol steps?
- [ ] **Rule Coverage**: Incomplete .mdc rule coverage?
- [ ] **Documentation**: Missing user guides or technical documentation?
- [ ] **Integration**: Missing connections between components?

**4.2 Severity Assessment**
For each gap, assess:
- [ ] **Critical**: Blocks template deployment
- [ ] **High**: Significantly impacts usability
- [ ] **Medium**: Affects specific use cases
- [ ] **Low**: Minor improvement opportunity

#### SECTION 5: TEMPLATE READINESS EVALUATION

**5.1 Universal Applicability**
Can this template handle:
- [ ] **Web Applications**: Frontend-only, backend-only, fullstack?
- [ ] **Mobile Applications**: Native iOS/Android, cross-platform, PWA?
- [ ] **Data Projects**: Analytics dashboards, ML pipelines, ETL processes?
- [ ] **Infrastructure Projects**: DevOps automation, microservices, cloud migration?
- [ ] **Enterprise Features**: Multi-tenancy, compliance, audit logging?

**5.2 Production Readiness**
- [ ] **Stability**: Has system been tested with real project briefs?
- [ ] **Error Recovery**: Does it handle edge cases and failures gracefully?
- [ ] **Performance**: How long does protocol orchestration take?
- [ ] **Maintainability**: Can non-technical users update protocols?
- [ ] **Scalability**: Can it handle enterprise-scale projects?

---

### OUTPUT REQUIREMENTS

You must provide your analysis in this exact format:

```markdown
# AI-DRIVEN TEMPLATE SYSTEM: COMPREHENSIVE ANALYSIS REPORT

## EXECUTIVE SUMMARY
[2-3 paragraph overview of system readiness, key findings, and final verdict]

## DETAILED FINDINGS

### 1. CURRENT STATE ASSESSMENT
[Analysis of existing AGENTS.md, protocol orchestrator, .mdc rules, commands]

### 2. END-TO-END LIFECYCLE VALIDATION
[Results from testing 7 project scenarios and integration validation]

### 3. AGENTS.md CONTENT RECOMMENDATIONS
[Specific suggestions for AGENTS.md content following Codex 2025 standards]

### 4. GAP ANALYSIS
[Comprehensive list of identified gaps with severity ratings]

### 5. TEMPLATE READINESS EVALUATION
[Assessment of universal applicability and production readiness]

## READINESS SCORECARD

| Criteria | Score (0-10) | Justification |
|----------|--------------|---------------|
| AGENTS.md Completeness | __/10 | _____________ |
| Protocol Orchestrator Intelligence | __/10 | _____________ |
| .mdc Rule System Quality | __/10 | _____________ |
| .cursor/commands/ Usability | __/10 | _____________ |
| End-to-End Integration | __/10 | _____________ |
| Universal Applicability | __/10 | _____________ |
| Production Readiness | __/10 | _____________ |
| Documentation Quality | __/10 | _____________ |
| **OVERALL READINESS** | **__/10** | _____________ |

## RECOMMENDED AGENTS.md CONTENT

[Provide complete, production-ready AGENTS.md content following Codex 2025 standards]

## CRITICAL PATH RECOMMENDATIONS

**Must-Fix Before Template Deployment:**
1. ___________
2. ___________
3. ___________

**High-Priority Enhancements:**
1. ___________
2. ___________
3. ___________

**Documentation Requirements:**
1. ___________
2. ___________
3. ___________

## FINAL VERDICT

**STATUS**: [READY FOR DEPLOYMENT / NOT READY - REQUIRES WORK / REQUIRES MAJOR REVISION]

**OVERALL SCORE**: __/10

**KEY STRENGTHS**:
- ___________
- ___________
- ___________

**CRITICAL GAPS**:
- ___________
- ___________
- ___________

**CAN THIS BE A PERMANENT TEMPLATE?**: [YES/NO with detailed justification]

**ESTIMATED TIME TO PRODUCTION-READY**: [X weeks/months]

**RECOMMENDED NEXT STEPS**:
1. ___________
2. ___________
3. ___________
```

---

### ANALYSIS SUCCESS CRITERIA

Your analysis will be considered successful if it:
- [ ] Provides comprehensive coverage of all evaluation areas
- [ ] Tests system against 7+ diverse project scenarios
- [ ] Delivers complete AGENTS.md content following Codex standards
- [ ] Identifies specific, actionable gaps with severity ratings
- [ ] Offers clear, evidence-based conclusions
- [ ] Provides definitive readiness assessment with justification
- [ ] Answers: "Can this be deployed as a permanent template for diverse projects?"

**Execute this comprehensive analysis now and provide your detailed evaluation report.**
