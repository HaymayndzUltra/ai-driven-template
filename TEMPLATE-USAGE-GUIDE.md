# AI-Driven Template Usage Guide
## Complete End-to-End Development Workflow

### Quick Start Guide

This template provides a complete AI-driven development workflow. Follow these steps to get started:

1. **Clone the Template**
   ```bash
   git clone <ai-driven-template-repo>
   cd ai-driven-template
   ```

2. **Create Your Project Brief**
   ```bash
   cp PROJECT-BRIEF.md.example PROJECT-BRIEF.md
   # Edit PROJECT-BRIEF.md with your project details
   ```

3. **Invoke Protocol Orchestrator**
   ```bash
   # In Cursor IDE, type:
   @protocol-orchestrator.md
   ```

4. **Execute Generated Protocols**
   ```bash
   # AI will generate numbered commands like:
   cursor apply .cursor/commands/00-analyze-brief.md
   cursor apply .cursor/commands/01-bootstrap-context.md
   # ... continue with each generated protocol
   ```

5. **Review Evidence and Retrospective**
   ```bash
   # AI automatically collects evidence and generates retrospective
   cat evidence/retrospective-report.md
   ```

---

## Detailed Usage Instructions

### Step 1: Project Brief Creation

Create a `PROJECT-BRIEF.md` file with your project description. Include:

**Required Sections**:
- **Project Overview**: What you're building
- **Target Audience**: Who will use it
- **Technology Stack**: What technologies to use
- **Requirements**: Functional and non-functional requirements
- **Constraints**: Budget, timeline, technical limitations
- **Success Criteria**: How you'll measure success

**Example PROJECT-BRIEF.md**:
```markdown
# PROJECT-BRIEF.md

## Project Overview
Create a multi-tenant SaaS application for project management with real-time collaboration features.

## Target Audience
Small to medium businesses (10-500 employees) managing multiple projects.

## Technology Stack
- Frontend: React with TypeScript
- Backend: Node.js with Express
- Database: PostgreSQL
- Real-time: WebSocket connections
- Deployment: AWS with Docker

## Requirements
### Functional
- User authentication and authorization
- Project creation and management
- Task assignment and tracking
- Real-time notifications
- Team collaboration features

### Non-Functional
- Support 1000+ concurrent users
- 99.9% uptime requirement
- GDPR compliance
- Mobile-responsive design

## Constraints
- Budget: $50K development cost
- Timeline: 6 months to MVP
- Team: 3 developers + 1 designer

## Success Criteria
- 100+ active users within 3 months
- <2 second page load times
- 90%+ user satisfaction score
```

### Step 2: Protocol Orchestration

Invoke the protocol orchestrator to analyze your brief and generate appropriate protocols:

```bash
# In Cursor IDE
@protocol-orchestrator.md
```

**What Happens**:
1. AI reads your PROJECT-BRIEF.md
2. AI analyzes project type, complexity, and requirements
3. AI selects appropriate protocols from the library
4. AI generates custom protocols for specific needs
5. AI creates numbered command files in `.cursor/commands/`
6. AI presents the generated sequence for your approval

**Expected Output**:
```
[ORCHESTRATION COMPLETE] Generated 8 protocols for your SaaS project:
- 00-analyze-brief.md ✅ (validate requirements)
- 01-bootstrap-architecture.md ✅ (analyze patterns)
- 02-security-design.md ✅ (multi-tenancy, compliance)
- 03-database-schema.md ✅ (complex data model)
- 04-api-contracts.md ✅ (OpenAPI specification)
- 05-implementation-tasks.md ✅ (development plan)
- 06-security-validation.md ✅ (compliance testing)
- 07-deployment-checklist.md ✅ (production readiness)
- 08-retrospective.md ✅ (capture learnings)

SKIPPED: monitoring (covered in deployment), docs (self-explanatory)

👤 USER ACTION REQUIRED: Type "approve" to proceed or "modify" to adjust
```

### Step 3: Protocol Execution

Execute the generated protocols sequentially:

```bash
# Execute each protocol in order
cursor apply .cursor/commands/00-analyze-brief.md
# Complete the task, then proceed to next
cursor apply .cursor/commands/01-bootstrap-architecture.md
# Continue with remaining protocols...
```

**What Happens During Execution**:
1. AI loads the protocol instructions
2. AI applies relevant rules and context
3. AI executes protocol steps automatically
4. AI runs validation scripts
5. AI collects evidence artifacts
6. AI reports completion status

**Manual Steps Required**:
- Stakeholder approvals (for PRD sign-off)
- External service configuration (API keys, credentials)
- Production deployment approval
- Code review and PR merges

### Step 4: Quality Gates and Validation

The system automatically enforces quality gates:

**Automated Validation**:
- Test suite execution
- Code coverage analysis
- Security scanning
- Performance benchmarking
- Linting and formatting

**Manual Approvals Required**:
- Quality audit report review
- Deployment to production approval
- Acceptance criteria confirmation
- Protocol completion sign-off

### Step 5: Evidence Collection and Retrospective

The system automatically collects evidence throughout the process:

**Evidence Artifacts**:
- Protocol execution logs
- Test results and coverage reports
- Security scan results
- Performance benchmarks
- Architecture decision records
- User feedback and approvals

**Retrospective Generation**:
- AI analyzes all evidence
- AI identifies learnings and improvements
- AI generates retrospective report
- AI suggests system improvements

---

## Project Type Examples

### Web Application (Frontend-Only)

**Brief**: "Create a marketing landing page with contact form"

**Generated Protocols**:
- `00-analyze-brief.md` - Validate requirements
- `01-design-ui-components.md` - UI/UX design
- `02-implement-frontend.md` - Frontend implementation
- `03-validate-accessibility.md` - Accessibility testing
- `04-deployment-guide.md` - Static hosting deployment

**Skipped**: Backend protocols, complex architecture, pre-production security

### Full-Stack SaaS Application

**Brief**: "Multi-tenant SaaS with Stripe integration, user roles, audit logs"

**Generated Protocols**:
- `00-client-discovery.md` - Detailed requirements
- `01-bootstrap-architecture.md` - Architecture analysis
- `02-security-design.md` - Multi-tenancy security
- `03-database-schema.md` - Complex data model
- `04-api-contracts.md` - OpenAPI specification
- `05-implementation-tasks.md` - Development plan
- `06-security-validation.md` - Compliance testing
- `07-integration-testing.md` - E2E testing
- `08-deployment-checklist.md` - Production readiness
- `09-monitoring-setup.md` - Observability
- `10-retrospective.md` - Learnings capture

### Data Analytics Dashboard

**Brief**: "BI dashboard for real estate loan portfolio analysis"

**Generated Protocols**:
- `00-data-discovery.md` - Analyze data sources
- `01-data-quality-assessment.md` - Validate data integrity
- `02-dashboard-design.md` - KPI selection and mockups
- `03-etl-pipeline.md` - Data extraction and transformation
- `04-visualization-implementation.md` - Dashboard implementation
- `05-user-acceptance-testing.md` - Stakeholder validation
- `06-retrospective.md` - Data quality learnings

### Mobile Cross-Platform App

**Brief**: "React Native app for fitness tracking with offline sync"

**Generated Protocols**:
- `00-analyze-brief.md` - Mobile requirements analysis
- `01-mobile-architecture.md` - Offline-first architecture
- `02-native-features.md` - Device integration
- `03-implementation-tasks.md` - Development plan
- `04-offline-sync.md` - Data synchronization
- `05-app-store-deployment.md` - Store deployment
- `06-retrospective.md` - Mobile development learnings

### Machine Learning Pipeline

**Brief**: "ML model for customer churn prediction with automated retraining"

**Generated Protocols**:
- `00-data-discovery.md` - Analyze customer data
- `01-data-preparation.md` - Feature engineering
- `02-model-training.md` - ML model development
- `03-model-validation.md` - Model performance testing
- `04-ml-deployment.md` - Model serving infrastructure
- `05-automated-retraining.md` - Continuous learning setup
- `06-monitoring-ml.md` - Model performance monitoring
- `07-retrospective.md` - ML pipeline learnings

---

## Troubleshooting Guide

### Common Issues and Solutions

**Issue**: Orchestration fails to generate protocols
- **Cause**: PROJECT-BRIEF.md missing or invalid format
- **Solution**: Create/validate PROJECT-BRIEF.md, then retry

**Issue**: Protocol execution fails with script errors
- **Cause**: Missing Python dependencies or incorrect environment
- **Solution**: Run `pip install -r requirements.txt`, then retry

**Issue**: Quality audit fails with test errors
- **Cause**: Code implementation issues or missing test setup
- **Solution**: Review test output, decide to fix code or adjust expectations

**Issue**: Deployment fails with environment errors
- **Cause**: Missing environment variables or incorrect configuration
- **Solution**: Configure deployment environment, then retry

### Getting Help

1. **Check Evidence**: Review `evidence/` directory for execution logs
2. **Review Retrospective**: Check `evidence/retrospective-report.md`
3. **Validate Brief**: Ensure PROJECT-BRIEF.md is complete and clear
4. **Check Dependencies**: Verify all required tools are installed
5. **Review Rules**: Check `.cursor/rules/` for relevant guidance

---

## Advanced Usage

### Custom Protocol Creation

To add custom protocols for specific domains:

1. **Create Protocol File**: Add new protocol to `.cursor/ai-driven-workflow/`
2. **Update Decision Matrix**: Modify protocol selection logic
3. **Add Automation Scripts**: Create validation scripts in `scripts/`
4. **Update Rules**: Add domain-specific rules to `.cursor/rules/`

### Template Customization

To customize the template for your organization:

1. **Update AGENTS.md**: Modify agent capabilities and preferences
2. **Add Organization Rules**: Create custom rules in `.cursor/rules/`
3. **Extend Template Packs**: Add organization-specific templates
4. **Customize Commands**: Modify slash commands for your workflow

### Integration with Existing Systems

To integrate with existing development tools:

1. **CI/CD Integration**: Connect with GitHub Actions, Jenkins, etc.
2. **Monitoring Integration**: Connect with Datadog, New Relic, etc.
3. **Documentation Integration**: Connect with Confluence, Notion, etc.
4. **Project Management**: Connect with Jira, Asana, etc.

---

## Best Practices

### Project Brief Writing
- Be specific about requirements and constraints
- Include clear success criteria
- Specify technology preferences
- Define target audience clearly
- Include timeline and budget constraints

### Protocol Execution
- Execute protocols in sequence
- Complete each protocol before moving to next
- Review AI suggestions before approval
- Provide feedback for protocol improvements
- Document any manual steps required

### Quality Assurance
- Review quality audit reports carefully
- Address security vulnerabilities promptly
- Maintain test coverage above 80%
- Validate performance benchmarks
- Ensure compliance requirements are met

### Continuous Improvement
- Review retrospective reports regularly
- Implement suggested improvements
- Share learnings with team
- Update protocols based on experience
- Contribute improvements back to template

---

## Conclusion

This AI-driven template provides a complete, production-ready solution for diverse project development. By following this guide, you can leverage AI to orchestrate entire development lifecycles, from initial brief to production deployment and retrospective analysis.

The system is designed to be:
- **Universal**: Works for any project type
- **Intelligent**: AI makes appropriate decisions
- **Quality-Focused**: Automated quality gates
- **Learning**: Continuous improvement
- **Maintainable**: Easy to extend and customize

Start with a clear project brief, invoke the protocol orchestrator, and let AI guide you through a complete, high-quality development workflow.
