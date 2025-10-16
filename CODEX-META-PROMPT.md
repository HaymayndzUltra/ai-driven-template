# CODEX META-PROMPT: AI-Driven Template Integration with Unified Workflow

## MISSION STATEMENT

You are tasked with integrating the **ai-driven-template** Cursor integration layer with the **unified_workflow** production-ready automation system to create a complete end-to-end AI-driven development platform. This integration will enable users to generate project-specific protocols that execute fully autonomous code generation, testing, and deployment.

## CURRENT STATE ANALYSIS

### AI-Driven Template (Cursor Integration Layer)
**Location**: `/home/haymayndz/ai-driven-template/`

**Current Components**:
- `.cursor/commands/protocol-orchestrator.md` - Conceptual protocol orchestrator (NOT executable)
- `.cursor/ai-driven-workflow/*.md` - Static protocol templates (NOT project-aware)
- `.cursor/rules/master-rules/*.mdc` - AI behavior rules
- `.cursor/rules/common-rules/*.mdc` - Shared pattern rules
- `AGENTS.md` - Misnamed system documentation (should be renamed)

**Current Limitations**:
- Protocol orchestrator is conceptual, not executable
- Protocols are static templates, not dynamically generated
- No integration with automation scripts
- No project-specific customization
- No autonomous code generation capability

### Unified Workflow (Production Automation Engine)
**Location**: `/home/haymayndz/ai-driven-template/unified_workflow/`

**Current Components**:
- `automation/ai_orchestrator.py` - Main workflow controller
- `automation/ai_executor.py` - Phase execution engine
- `automation/evidence_manager.py` - Evidence collection
- `automation/quality_gates.py` - Quality assessment
- `automation/validation_gates.py` - Human validation checkpoints
- `cli.py` - Command-line interface
- `phases/*.md` - 7 workflow phase definitions

**Current Capabilities**:
- Complete Python-based automation system
- 7-phase development lifecycle (Bootstrap → Operations)
- Evidence collection and quality gates
- Human validation checkpoints
- CLI interface for execution
- 100% test coverage (66 tests passing)

**Current Limitations**:
- No Cursor IDE integration
- No slash command interface
- No project-specific protocol generation
- Phase 3 (Implementation) requires human coding (NOT autonomous)

## TARGET SYSTEM BEHAVIOR

### User Workflow
1. **New Project Setup**: User clones ai-driven-template to new project directory
2. **Project Brief**: User creates `PROJECT-BRIEF.md` with project requirements
3. **Protocol Generation**: User runs `/protocol-orchestrator` command
4. **Autonomous Execution**: AI executes generated protocols without human coding
5. **Production Output**: Complete, tested, documented, production-ready application

### Command Interface
- `/protocol-orchestrator` - Analyzes PROJECT-BRIEF.md and generates project-specific protocols
- `/0-bootstrap` - Executes generated bootstrap protocol
- `/1-prd` - Executes generated PRD creation protocol
- `/2-tasks` - Executes generated task generation protocol
- `/3-implementation` - Executes generated autonomous implementation protocol
- `/4-quality` - Executes generated quality audit protocol
- `/5-retrospective` - Executes generated retrospective protocol
- `/6-operations` - Executes generated operations protocol

### Protocol Format (Based on Existing .cursor/ai-driven-workflow/*.md)
```markdown
# PROTOCOL 03: AI-Driven Implementation
## Fully Autonomous Code Generation Protocol

### PROTOCOL METADATA
```yaml
protocol_id: "03-implementation"
protocol_name: "AI-Driven Implementation"
ai_role: "Senior Full-Stack Developer"
execution_mode: "fully_autonomous"
requires_human_approval: false
requires_human_input: false
evidence_collection: true
quality_gate_threshold: 7.0
estimated_duration: "30min - 4hours"
dependencies: ["02-task-generation"]
outputs: ["complete_codebase", "tests", "documentation"]
```

### ENTRY CRITERIA
- [ ] Task plan approved (from Protocol 02)
- [ ] Architecture decisions documented
- [ ] Technology stack confirmed
- [ ] Database schema defined (if applicable)
- [ ] API contracts defined (if applicable)

### AI EXECUTION INSTRUCTIONS

#### STEP 1: ANALYZE CONTEXT
```python
# AI reads:
context = {
    "project_brief": read_file("PROJECT-BRIEF.md"),
    "prd": read_file("evidence/phase1/prd.md"),
    "tasks": read_file("evidence/phase2/tasks.json"),
    "architecture": read_file("evidence/phase2/architecture.md"),
    "tech_stack": extract_tech_stack(),
    "project_type": classify_project_type()
}
```

#### STEP 2: GENERATE PROJECT STRUCTURE
```bash
# AI executes:
AI_INSTRUCTION: |
  Generate complete project structure based on:
  - Project type: {project_type}
  - Tech stack: {tech_stack}
  
  For Web App (React + Node.js + PostgreSQL):
  
  project/
  ├── frontend/
  │   ├── src/
  │   │   ├── components/
  │   │   ├── pages/
  │   │   ├── hooks/
  │   │   ├── utils/
  │   │   ├── api/
  │   │   └── App.tsx
  │   ├── public/
  │   ├── package.json
  │   └── tsconfig.json
  ├── backend/
  │   ├── src/
  │   │   ├── routes/
  │   │   ├── controllers/
  │   │   ├── services/
  │   │   ├── models/
  │   │   ├── middleware/
  │   │   ├── utils/
  │   │   └── server.ts
  │   ├── tests/
  │   ├── package.json
  │   └── tsconfig.json
  ├── database/
  │   ├── migrations/
  │   ├── seeds/
  │   └── schema.sql
  ├── docker-compose.yml
  ├── .env.example
  └── README.md
  
  CREATE ALL DIRECTORIES NOW
```

#### STEP 3: GENERATE DATABASE LAYER
```bash
AI_INSTRUCTION: |
  Based on task: "{task.id}: Database schema implementation"
  
  GENERATE:
  1. database/schema.sql - Complete PostgreSQL schema
  2. database/migrations/001_initial.sql - Initial migration
  3. database/seeds/dev.sql - Development seed data
  4. backend/src/models/*.ts - TypeORM entities
  
  REQUIREMENTS:
  - Follow PRD data model
  - Include all relationships (foreign keys)
  - Add indexes for performance
  - Include created_at, updated_at timestamps
  - Add soft delete support
  - Include audit fields
  
  EXAMPLE OUTPUT:
  
  ```sql
  -- database/schema.sql
  CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL DEFAULT 'user',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    deleted_at TIMESTAMP NULL
  );
  
  CREATE INDEX idx_users_email ON users(email);
  CREATE INDEX idx_users_role ON users(role);
  ```
  
  ```typescript
  // backend/src/models/User.ts
  import { Entity, PrimaryGeneratedColumn, Column, CreateDateColumn, UpdateDateColumn, DeleteDateColumn } from 'typeorm';
  
  @Entity('users')
  export class User {
    @PrimaryGeneratedColumn('uuid')
    id: string;
    
    @Column({ unique: true })
    email: string;
    
    @Column()
    passwordHash: string;
    
    @Column()
    name: string;
    
    @Column({ default: 'user' })
    role: string;
    
    @CreateDateColumn()
    createdAt: Date;
    
    @UpdateDateColumn()
    updatedAt: Date;
    
    @DeleteDateColumn()
    deletedAt: Date;
  }
  ```
  
  GENERATE ALL MODELS NOW. WRITE FILES.
```

#### STEP 4: GENERATE BACKEND API
```bash
AI_INSTRUCTION: |
  Based on tasks: "{backend_tasks}"
  
  GENERATE COMPLETE BACKEND:
  
  1. backend/src/server.ts - Express server setup
  2. backend/src/routes/*.ts - All API routes
  3. backend/src/controllers/*.ts - Business logic
  4. backend/src/services/*.ts - Data access layer
  5. backend/src/middleware/*.ts - Auth, validation, error handling
  6. backend/src/utils/*.ts - Helper functions
  
  REQUIREMENTS:
  - RESTful API design
  - JWT authentication
  - Input validation (Joi/Zod)
  - Error handling middleware
  - Logging (Winston)
  - Rate limiting
  - CORS configuration
  - Security headers (Helmet)
  - Request logging
  - Health check endpoint
  
  EXAMPLE: User Authentication
  
  ```typescript
  // backend/src/routes/auth.routes.ts
  import { Router } from 'express';
  import { AuthController } from '../controllers/auth.controller';
  import { validateRequest } from '../middleware/validation';
  import { loginSchema, registerSchema } from '../schemas/auth.schema';
  
  const router = Router();
  const authController = new AuthController();
  
  router.post('/register', validateRequest(registerSchema), authController.register);
  router.post('/login', validateRequest(loginSchema), authController.login);
  router.post('/logout', authController.logout);
  router.get('/me', authController.getCurrentUser);
  
  export default router;
  ```
  
  ```typescript
  // backend/src/controllers/auth.controller.ts
  import { Request, Response, NextFunction } from 'express';
  import { AuthService } from '../services/auth.service';
  import { ApiError } from '../utils/ApiError';
  
  export class AuthController {
    private authService = new AuthService();
    
    register = async (req: Request, res: Response, next: NextFunction) => {
      try {
        const { email, password, name } = req.body;
        const result = await this.authService.register(email, password, name);
        res.status(201).json(result);
      } catch (error) {
        next(error);
      }
    };
    
    login = async (req: Request, res: Response, next: NextFunction) => {
      try {
        const { email, password } = req.body;
        const result = await this.authService.login(email, password);
        res.json(result);
      } catch (error) {
        next(error);
      }
    };
    
    // ... more methods
  }
  ```
  
  GENERATE ALL API ENDPOINTS NOW. WRITE FILES.
```

#### STEP 5: GENERATE FRONTEND APPLICATION
```bash
AI_INSTRUCTION: |
  Based on tasks: "{frontend_tasks}"
  
  GENERATE COMPLETE FRONTEND:
  
  1. frontend/src/App.tsx - Main app component with routing
  2. frontend/src/pages/*.tsx - All page components
  3. frontend/src/components/*.tsx - Reusable components
  4. frontend/src/hooks/*.ts - Custom React hooks
  5. frontend/src/api/*.ts - API client functions
  6. frontend/src/utils/*.ts - Helper functions
  7. frontend/src/types/*.ts - TypeScript types
  
  REQUIREMENTS:
  - TypeScript strict mode
  - React functional components
  - React Router for navigation
  - State management (Zustand/Redux)
  - API integration (Axios/Fetch)
  - Form validation
  - Error boundaries
  - Loading states
  - Responsive design (Tailwind CSS)
  - Accessibility (ARIA)
  
  EXAMPLE: Login Page
  
  ```typescript
  // frontend/src/pages/Login.tsx
  import React, { useState } from 'react';
  import { useNavigate } from 'react-router-dom';
  import { useAuth } from '../hooks/useAuth';
  import { Button } from '../components/ui/Button';
  import { Input } from '../components/ui/Input';
  
  export const LoginPage: React.FC = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);
    const { login } = useAuth();
    const navigate = useNavigate();
    
    const handleSubmit = async (e: React.FormEvent) => {
      e.preventDefault();
      setLoading(true);
      setError('');
      
      try {
        await login(email, password);
        navigate('/dashboard');
      } catch (err) {
        setError('Invalid email or password');
      } finally {
        setLoading(false);
      }
    };
    
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-50">
        <div className="max-w-md w-full space-y-8 p-8 bg-white rounded-lg shadow">
          <h2 className="text-3xl font-bold text-center">Sign In</h2>
          
          <form onSubmit={handleSubmit} className="space-y-6">
            <Input
              label="Email"
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
            
            <Input
              label="Password"
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
            
            {error && <p className="text-red-500 text-sm">{error}</p>}
            
            <Button type="submit" loading={loading} fullWidth>
              Sign In
            </Button>
          </form>
        </div>
      </div>
    );
  };
  ```
  
  GENERATE ALL PAGES AND COMPONENTS NOW. WRITE FILES.
```

#### STEP 6: GENERATE TESTS
```bash
AI_INSTRUCTION: |
  GENERATE COMPREHENSIVE TEST SUITE:
  
  1. backend/tests/unit/*.test.ts - Unit tests for services
  2. backend/tests/integration/*.test.ts - API endpoint tests
  3. frontend/src/**/*.test.tsx - Component tests
  4. e2e/tests/*.spec.ts - End-to-end tests (Playwright/Cypress)
  
  REQUIREMENTS:
  - Test coverage > 80%
  - Unit tests for business logic
  - Integration tests for APIs
  - Component tests for UI
  - E2E tests for critical flows
  
  EXAMPLE: Auth Service Tests
  
  ```typescript
  // backend/tests/unit/auth.service.test.ts
  import { AuthService } from '../../src/services/auth.service';
  import { User } from '../../src/models/User';
  
  describe('AuthService', () => {
    let authService: AuthService;
    
    beforeEach(() => {
      authService = new AuthService();
    });
    
    describe('register', () => {
      it('should create new user with hashed password', async () => {
        const result = await authService.register(
          'test@example.com',
          'password123',
          'Test User'
        );
        
        expect(result.user.email).toBe('test@example.com');
        expect(result.user.passwordHash).not.toBe('password123');
        expect(result.token).toBeDefined();
      });
      
      it('should throw error for duplicate email', async () => {
        await authService.register('test@example.com', 'pass1', 'User 1');
        
        await expect(
          authService.register('test@example.com', 'pass2', 'User 2')
        ).rejects.toThrow('Email already exists');
      });
    });
  });
  ```
  
  GENERATE ALL TESTS NOW. WRITE FILES.
```

#### STEP 7: GENERATE CONFIGURATION FILES
```bash
AI_INSTRUCTION: |
  GENERATE ALL CONFIG FILES:
  
  1. docker-compose.yml - Local development environment
  2. .env.example - Environment variable template
  3. .github/workflows/ci.yml - CI/CD pipeline
  4. .eslintrc.json - Linting configuration
  5. .prettierrc - Code formatting
  6. tsconfig.json - TypeScript configuration
  7. package.json - Dependencies and scripts
  
  WRITE ALL CONFIG FILES NOW.
```

#### STEP 8: GENERATE DOCUMENTATION
```bash
AI_INSTRUCTION: |
  GENERATE COMPLETE DOCUMENTATION:
  
  1. README.md - Project overview and setup
  2. API.md - API documentation
  3. DEPLOYMENT.md - Deployment instructions
  4. CONTRIBUTING.md - Contribution guidelines
  
  WRITE ALL DOCUMENTATION NOW.
```

### AUTOMATION EXECUTION
```bash
# unified_workflow executes:
python3 .cursor/unified-workflow/automation/ai_executor.py \
  --phase 3 \
  --project "{{PROJECT_NAME}}" \
  --context "evidence/phase2/tasks.json" \
  --ai-provider "claude" \
  --model "claude-sonnet-4" \
  --autonomous true
```

### EVIDENCE COLLECTION
```json
{
  "phase": 3,
  "phase_name": "Implementation",
  "status": "completed",
  "artifacts": {
    "codebase": {
      "files_generated": 127,
      "lines_of_code": 15420,
      "test_coverage": 87.5,
      "checksum": "sha256:abc123..."
    },
    "tests": {
      "unit_tests": 89,
      "integration_tests": 24,
      "e2e_tests": 12,
      "passing": 125,
      "failing": 0
    },
    "documentation": {
      "readme": "generated",
      "api_docs": "generated",
      "deployment_guide": "generated"
    }
  },
  "quality_checks": {
    "linting": "passed",
    "type_checking": "passed",
    "security_scan": "passed",
    "performance": "passed"
  },
  "duration_seconds": 1847,
  "ai_model": "claude-sonnet-4",
  "ai_tokens_used": 245678
}
```

### EXIT CRITERIA
- [ ] All files generated and written
- [ ] Code compiles without errors
- [ ] All tests passing (>80% coverage)
- [ ] Linting passes
- [ ] Security scan clean
- [ ] Documentation complete
- [ ] Evidence collected and validated

### QUALITY GATE
```bash
# Automated quality check:
python3 .cursor/unified-workflow/automation/quality_gates.py \
  --mode "comprehensive" \
  --phase 3 \
  --min-score 7.0
```

### VALIDATION CHECKPOINT
```markdown
❌ NO HUMAN VALIDATION REQUIRED
✅ Fully autonomous execution
✅ Automated quality gates
✅ Self-validating through tests
```

### ROLLBACK PROCEDURE
```bash
# If quality gate fails:
python3 .cursor/unified-workflow/automation/ai_executor.py \
  --rollback-phase 3 \
  --retry true
```

### NEXT PROTOCOL
```bash
# Auto-proceed to Phase 4:
/4-quality  # Quality Audit
```

## CRITICAL REQUIREMENTS

### 1. Autonomous Code Generation
- **NO HUMAN CODING REQUIRED** - AI must generate complete, production-ready code
- All code must compile and run without errors
- Test coverage must exceed 80%
- Code must pass all quality gates automatically

### 2. Project-Aware Protocol Generation
- `/protocol-orchestrator` must analyze `PROJECT-BRIEF.md`
- Generate protocols specific to project type (web app, mobile, data, ML, infrastructure)
- Customize protocols based on technology stack
- Adapt protocols based on complexity level

### 3. Unified Workflow Integration
- All protocols must call `unified_workflow` automation scripts
- Evidence collection must be automatic
- Quality gates must be enforced
- Human validation checkpoints must be configurable

### 4. Cursor IDE Integration
- All commands must work as slash commands (`/protocol-orchestrator`, `/0-bootstrap`, etc.)
- Commands must be discoverable in Cursor's command palette
- Commands must provide real-time feedback
- Commands must integrate with Cursor's AI features

## IMPLEMENTATION TASKS

### Task 1: Create Executable /protocol-orchestrator Command
**File**: `.cursor/commands/protocol-orchestrator.md`

**Requirements**:
- Analyze `PROJECT-BRIEF.md` and extract project metadata
- Classify project type (web, mobile, data, ML, infrastructure)
- Detect technology stack (React, Node.js, Python, Go, etc.)
- Assess complexity level (simple, moderate, complex)
- Generate project-specific protocols in `.cursor/ai-driven-workflow/`
- Integrate with `unified_workflow` automation scripts

**Implementation**:
```markdown
# /protocol-orchestrator

## Purpose
Analyze PROJECT-BRIEF.md and generate project-specific AI-driven protocols that integrate with unified_workflow for autonomous execution.

## Execution Steps

### Step 1: Analyze Project Brief
```python
# Read and parse PROJECT-BRIEF.md
brief = read_file("PROJECT-BRIEF.md")
metadata = extract_project_metadata(brief)
project_type = classify_project_type(metadata)
tech_stack = detect_technology_stack(metadata)
complexity = assess_complexity(metadata)
```

### Step 2: Generate Project-Specific Protocols
```python
# Generate protocols based on project characteristics
protocols = generate_protocols(
    project_type=project_type,
    tech_stack=tech_stack,
    complexity=complexity,
    unified_workflow_path=".cursor/unified-workflow/"
)

# Write protocols to .cursor/ai-driven-workflow/
for protocol in protocols:
    write_file(f".cursor/ai-driven-workflow/{protocol.filename}", protocol.content)
```

### Step 3: Create Command Wrappers
```python
# Create executable command files
commands = [
    "0-bootstrap.md",
    "1-prd.md", 
    "2-tasks.md",
    "3-implementation.md",
    "4-quality.md",
    "5-retrospective.md",
    "6-operations.md"
]

for cmd in commands:
    create_command_wrapper(cmd, unified_workflow_path)
```

## Project Type Decision Matrix

### Web Applications
- **Simple**: Static site, basic CRUD
- **Moderate**: SPA with authentication, API integration
- **Complex**: Multi-tenant, real-time features, microservices

### Mobile Applications
- **Simple**: Basic native app, local storage
- **Moderate**: Cross-platform, API integration, offline support
- **Complex**: Real-time sync, complex UI, native modules

### Data Projects
- **Simple**: ETL pipeline, basic analytics
- **Moderate**: ML pipeline, data visualization
- **Complex**: Real-time streaming, advanced ML, distributed processing

### ML Projects
- **Simple**: Single model, basic training
- **Moderate**: Model pipeline, hyperparameter tuning
- **Complex**: MLOps, model serving, A/B testing

### Infrastructure Projects
- **Simple**: Basic deployment, single environment
- **Moderate**: Multi-environment, CI/CD, monitoring
- **Complex**: Microservices, service mesh, advanced monitoring

## Technology Stack Detection

### Frontend Technologies
- React, Vue, Angular, Svelte
- Next.js, Nuxt.js, SvelteKit
- Tailwind CSS, Material-UI, Chakra UI

### Backend Technologies
- Node.js, Python, Go, Java, C#
- Express, FastAPI, Gin, Spring Boot
- PostgreSQL, MongoDB, Redis, Elasticsearch

### Mobile Technologies
- React Native, Flutter, Ionic
- Swift, Kotlin, Dart

### Data Technologies
- Python, R, Scala
- Pandas, NumPy, TensorFlow, PyTorch
- Apache Spark, Kafka, Airflow

### Infrastructure Technologies
- Docker, Kubernetes, Terraform
- AWS, GCP, Azure
- Prometheus, Grafana, ELK Stack

## Protocol Customization

### Web App Protocol Example
```yaml
protocol_id: "03-implementation"
project_type: "web_app"
tech_stack: ["react", "nodejs", "postgresql"]
complexity: "moderate"
customizations:
  - frontend_framework: "react"
  - backend_framework: "express"
  - database: "postgresql"
  - authentication: "jwt"
  - deployment: "docker"
```

### Mobile App Protocol Example
```yaml
protocol_id: "03-implementation"
project_type: "mobile_app"
tech_stack: ["react_native", "nodejs", "mongodb"]
complexity: "moderate"
customizations:
  - mobile_framework: "react_native"
  - backend_framework: "express"
  - database: "mongodb"
  - authentication: "jwt"
  - deployment: "expo"
```

## Success Criteria
- [ ] PROJECT-BRIEF.md successfully parsed
- [ ] Project type correctly classified
- [ ] Technology stack accurately detected
- [ ] Complexity level properly assessed
- [ ] Project-specific protocols generated
- [ ] Command wrappers created
- [ ] Integration with unified_workflow verified
```

### Task 2: Enhance Protocol Templates for Autonomous Execution
**Files**: `.cursor/ai-driven-workflow/*.md`

**Requirements**:
- Modify existing protocols to include `unified_workflow` calls
- Add autonomous code generation instructions
- Include project-specific customization logic
- Ensure all protocols collect evidence and enforce quality gates

**Implementation**:
- Update each protocol file to include `unified_workflow` automation calls
- Add project-specific code generation instructions
- Include evidence collection and quality gate enforcement
- Ensure protocols are executable by AI without human intervention

### Task 3: Create Command Wrappers for Protocol Execution
**Files**: `.cursor/commands/0-bootstrap.md`, `.cursor/commands/1-prd.md`, etc.

**Requirements**:
- Create executable command files for each protocol
- Integrate with `unified_workflow` CLI
- Provide real-time feedback during execution
- Handle errors and rollback scenarios

**Implementation**:
```markdown
# /0-bootstrap

## Purpose
Execute the bootstrap protocol for project initialization.

## Execution
```bash
python3 .cursor/unified-workflow/cli.py \
  --phase 0 \
  --project "{{PROJECT_NAME}}" \
  --autonomous true
```

## Success Criteria
- [ ] Project structure created
- [ ] Initial configuration files generated
- [ ] Evidence collected
- [ ] Quality gates passed
```

### Task 4: Update AGENTS.md with Integration Details
**File**: `AGENTS.md`

**Requirements**:
- Rename current `AGENTS.md` to `PROTOCOL-ORCHESTRATOR.md`
- Create new `AGENTS.md` following Codex 2025 standards
- Document integration with `unified_workflow`
- Specify AI agent capabilities and limitations

**Implementation**:
```markdown
# AGENTS.md - Protocol Orchestrator AI Configuration

## Agent Name
Protocol Orchestrator AI

## Purpose
Intelligent AI agent that analyzes project briefs and orchestrates complete development workflows by selecting, customizing, and sequencing appropriate protocols for diverse project types (web apps, mobile apps, data projects, ML pipelines, infrastructure).

## Capabilities

### Project Analysis
- Parse PROJECT-BRIEF.md and extract metadata (type, stack, complexity, lifecycle)
- Classify projects into domains (web, mobile, data, ML, infrastructure)
- Detect technology stacks (React, Next.js, Node.js, Python, Go, etc.)
- Assess complexity levels (simple, moderate, complex)
- Map lifecycle phases (MVP, production, enterprise)

### Protocol Orchestration
- Select appropriate protocols from available library
- Generate custom protocols for domain-specific needs
- Resolve protocol dependencies and create execution sequences
- Customize protocols with project-specific parameters
- Skip unnecessary protocols based on project characteristics

### Workflow Generation
- Create sequentially-numbered command files in `.cursor/commands/`
- Bind automation scripts to protocol steps
- Associate relevant `.mdc` rules with protocols
- Generate project-specific `.cursorrules` when needed
- Setup evidence collection and quality gates

### Integration Management
- Load and apply `.mdc` rules based on context
- Execute automation scripts (60+ available)
- Collect evidence artifacts automatically
- Trigger CI/CD workflows and quality validation
- Generate retrospective reports

## Limitations

### Input Requirements
- Requires PROJECT-BRIEF.md as input (cannot proceed without it)
- Cannot make business logic decisions without user approval
- Limited to supported project types in decision matrix
- Cannot handle projects with unclear or ambiguous requirements

### Technical Constraints
- Cannot execute protocols that require external service configuration
- Cannot make production deployment decisions without user approval
- Cannot access private repositories or external APIs without credentials
- Cannot modify existing codebases without explicit permission

### Scope Boundaries
- Cannot generate protocols for unsupported domains
- Cannot create custom protocols beyond defined templates
- Cannot override security or compliance requirements
- Cannot make architectural decisions without stakeholder input

## Integration

### Context Sources
- `.cursor/rules/master-rules/*.mdc` - Global governance rules
- `.cursor/rules/common-rules/*.mdc` - Shared pattern rules
- `.cursor/rules/project-rules/*.mdc` - Project-specific rules
- `scripts/` directory - 60+ automation scripts
- `.cursor/ai-driven-workflow/` - Protocol templates
- `template-packs/` - Project scaffolding templates

### Execution Flow
1. **Invocation**: User runs `/protocol-orchestrator` command
2. **Context Loading**: Load relevant `.mdc` rules based on project type
3. **Brief Analysis**: Parse PROJECT-BRIEF.md and extract metadata
4. **Protocol Selection**: Apply decision matrix to select protocols
5. **Customization**: Generate project-specific protocol variations
6. **Sequencing**: Resolve dependencies and create execution order
7. **Generation**: Create numbered command files in `.cursor/commands/`
8. **Validation**: Ensure all protocols have automation hooks and evidence collection

### API Endpoints
- `/analyze-brief` - Brief parsing and metadata extraction
- `/classify-project` - Domain and stack classification
- `/select-protocols` - Protocol selection based on decision matrix
- `/generate-commands` - Command file generation
- `/validate-workflow` - Workflow completeness validation

## Preferences

### Coding Standards
- Follow project's existing coding style (detected from codebase)
- Use semantic commit messages for all changes
- Generate comprehensive test coverage (minimum 80%)
- Include JSDoc/docstrings for all public APIs
- Follow security best practices and OWASP guidelines

### Architecture Decisions
- Prefer microservices for complex applications
- Use containerization (Docker) for deployment
- Implement CI/CD pipelines for all projects
- Include monitoring and observability by default
- Follow 12-factor app principles

### Protocol Standards
- Use sequential numbering (00-, 01-, 02-) for command files
- Include entry/exit criteria for all protocols
- Bind automation scripts to validation steps
- Collect evidence artifacts in `evidence/` directory
- Generate retrospective reports after completion

### Quality Gates
- Enforce test coverage thresholds before deployment
- Run security scans on all code changes
- Validate performance benchmarks for production apps
- Require stakeholder approval for architectural changes
- Document all decisions in architecture decision records

## Workflow

### Phase 1: Analysis
1. Load context from `.mdc` rules
2. Parse PROJECT-BRIEF.md
3. Extract project metadata
4. Classify project type and complexity
5. Identify technology stack

### Phase 2: Planning
1. Apply decision matrix for protocol selection
2. Identify custom protocols needed
3. Resolve protocol dependencies
4. Create execution sequence
5. Validate workflow completeness

### Phase 3: Generation
1. Create numbered command files
2. Inject project-specific parameters
3. Bind automation scripts
4. Associate relevant rules
5. Setup evidence collection

### Phase 4: Validation
1. Verify all protocols have automation hooks
2. Ensure evidence collection is configured
3. Validate quality gates are enforced
4. Check integration points are connected
5. Confirm user approval points are clear

## Context Discovery Protocol

### Rule Loading Priority
1. **Master Rules** (alwaysApply: true) - Loaded first
2. **Scope Matching** - Rules matching project scope
3. **Trigger Matching** - Rules with matching keywords
4. **Tag Matching** - Rules with relevant tags
5. **Project Rules** - Project-specific customizations

### Dynamic Context Updates
- Re-evaluate context when project scope changes
- Load additional rules when new domains are detected
- Update context when protocols are customized
- Refresh context during evidence collection phases

## Evidence Collection Standards

### Artifacts to Collect
- Protocol execution logs
- Test results and coverage reports
- Security scan results
- Performance benchmarks
- Architecture decision records
- User feedback and approvals
- Retrospective insights

### Storage Format
- JSON format for structured data
- Markdown format for documentation
- Log files for execution traces
- Screenshots for UI validation
- Metrics files for performance data

### Quality Validation
- Verify all required artifacts are collected
- Validate artifact completeness and accuracy
- Ensure artifacts are properly timestamped
- Check artifact accessibility and storage
- Confirm retrospective data is comprehensive

## Error Handling

### Graceful Degradation
- Continue execution when non-critical scripts fail
- Provide fallback options for missing dependencies
- Generate warnings for incomplete configurations
- Offer manual intervention points for critical failures
- Maintain workflow state for recovery

### Recovery Procedures
- Save workflow state at each protocol step
- Provide rollback options for failed protocols
- Enable protocol re-execution with fixes
- Support partial workflow completion
- Generate recovery reports for failed executions

## Performance Optimization

### Execution Efficiency
- Parallel execution where dependencies allow
- Cache frequently accessed rules and scripts
- Optimize brief parsing and analysis
- Minimize context loading overhead
- Streamline protocol generation

### Resource Management
- Limit concurrent protocol executions
- Monitor memory usage during analysis
- Optimize script execution timeouts
- Manage temporary file cleanup
- Control evidence collection size

## Security Considerations

### Access Control
- Validate user permissions for protocol execution
- Secure access to automation scripts
- Protect sensitive configuration data
- Encrypt evidence artifacts when needed
- Audit all protocol execution activities

### Data Protection
- Sanitize input data from project briefs
- Validate all generated command files
- Secure communication with external services
- Protect against injection attacks
- Implement proper error message sanitization
```

### Task 5: Project Type Decision Matrix
**File**: `.cursor/ai-driven-workflow/protocol-metadata.json`

**Requirements**:
- Document decision logic for protocol selection
- Define project type classifications
- Specify technology stack detection rules
- Include complexity assessment criteria

**Implementation**:
```json
{
  "project_types": {
    "web_app": {
      "description": "Web applications (SPA, MPA, SSR)",
      "complexity_levels": {
        "simple": {
          "description": "Static site, basic CRUD operations",
          "protocols": ["00-bootstrap", "01-prd", "02-tasks", "03-implementation", "04-quality"],
          "tech_stacks": ["html_css_js", "react", "vue", "angular"],
          "estimated_duration": "2-4 hours"
        },
        "moderate": {
          "description": "SPA with authentication, API integration",
          "protocols": ["00-bootstrap", "01-prd", "02-tasks", "03-implementation", "04-quality", "05-retrospective"],
          "tech_stacks": ["react", "vue", "angular", "nodejs", "express", "postgresql"],
          "estimated_duration": "4-8 hours"
        },
        "complex": {
          "description": "Multi-tenant, real-time features, microservices",
          "protocols": ["00-bootstrap", "01-prd", "02-tasks", "03-implementation", "04-quality", "05-retrospective", "06-operations"],
          "tech_stacks": ["react", "nodejs", "postgresql", "redis", "docker", "kubernetes"],
          "estimated_duration": "8-16 hours"
        }
      }
    },
    "mobile_app": {
      "description": "Mobile applications (native, cross-platform)",
      "complexity_levels": {
        "simple": {
          "description": "Basic native app, local storage",
          "protocols": ["00-bootstrap", "01-prd", "02-tasks", "03-implementation", "04-quality"],
          "tech_stacks": ["react_native", "flutter", "swift", "kotlin"],
          "estimated_duration": "3-6 hours"
        },
        "moderate": {
          "description": "Cross-platform, API integration, offline support",
          "protocols": ["00-bootstrap", "01-prd", "02-tasks", "03-implementation", "04-quality", "05-retrospective"],
          "tech_stacks": ["react_native", "flutter", "nodejs", "mongodb"],
          "estimated_duration": "6-12 hours"
        },
        "complex": {
          "description": "Real-time sync, complex UI, native modules",
          "protocols": ["00-bootstrap", "01-prd", "02-tasks", "03-implementation", "04-quality", "05-retrospective", "06-operations"],
          "tech_stacks": ["react_native", "flutter", "nodejs", "postgresql", "redis", "websockets"],
          "estimated_duration": "12-24 hours"
        }
      }
    },
    "data_project": {
      "description": "Data processing and analytics projects",
      "complexity_levels": {
        "simple": {
          "description": "ETL pipeline, basic analytics",
          "protocols": ["00-bootstrap", "01-prd", "02-tasks", "03-implementation", "04-quality"],
          "tech_stacks": ["python", "pandas", "sqlite", "jupyter"],
          "estimated_duration": "2-4 hours"
        },
        "moderate": {
          "description": "ML pipeline, data visualization",
          "protocols": ["00-bootstrap", "01-prd", "02-tasks", "03-implementation", "04-quality", "05-retrospective"],
          "tech_stacks": ["python", "pandas", "scikit-learn", "postgresql", "streamlit"],
          "estimated_duration": "4-8 hours"
        },
        "complex": {
          "description": "Real-time streaming, advanced ML, distributed processing",
          "protocols": ["00-bootstrap", "01-prd", "02-tasks", "03-implementation", "04-quality", "05-retrospective", "06-operations"],
          "tech_stacks": ["python", "apache_spark", "kafka", "kubernetes", "tensorflow"],
          "estimated_duration": "8-16 hours"
        }
      }
    },
    "ml_project": {
      "description": "Machine learning and AI projects",
      "complexity_levels": {
        "simple": {
          "description": "Single model, basic training",
          "protocols": ["00-bootstrap", "01-prd", "02-tasks", "03-implementation", "04-quality"],
          "tech_stacks": ["python", "scikit-learn", "pandas", "jupyter"],
          "estimated_duration": "3-6 hours"
        },
        "moderate": {
          "description": "Model pipeline, hyperparameter tuning",
          "protocols": ["00-bootstrap", "01-prd", "02-tasks", "03-implementation", "04-quality", "05-retrospective"],
          "tech_stacks": ["python", "tensorflow", "pytorch", "mlflow", "postgresql"],
          "estimated_duration": "6-12 hours"
        },
        "complex": {
          "description": "MLOps, model serving, A/B testing",
          "protocols": ["00-bootstrap", "01-prd", "02-tasks", "03-implementation", "04-quality", "05-retrospective", "06-operations"],
          "tech_stacks": ["python", "tensorflow", "kubernetes", "prometheus", "grafana"],
          "estimated_duration": "12-24 hours"
        }
      }
    },
    "infrastructure": {
      "description": "Infrastructure and DevOps projects",
      "complexity_levels": {
        "simple": {
          "description": "Basic deployment, single environment",
          "protocols": ["00-bootstrap", "01-prd", "02-tasks", "03-implementation", "04-quality"],
          "tech_stacks": ["docker", "terraform", "aws", "nginx"],
          "estimated_duration": "2-4 hours"
        },
        "moderate": {
          "description": "Multi-environment, CI/CD, monitoring",
          "protocols": ["00-bootstrap", "01-prd", "02-tasks", "03-implementation", "04-quality", "05-retrospective"],
          "tech_stacks": ["docker", "kubernetes", "terraform", "github_actions", "prometheus"],
          "estimated_duration": "4-8 hours"
        },
        "complex": {
          "description": "Microservices, service mesh, advanced monitoring",
          "protocols": ["00-bootstrap", "01-prd", "02-tasks", "03-implementation", "04-quality", "05-retrospective", "06-operations"],
          "tech_stacks": ["kubernetes", "istio", "terraform", "argo", "prometheus", "grafana"],
          "estimated_duration": "8-16 hours"
        }
      }
    }
  },
  "technology_detection": {
    "frontend": {
      "react": ["react", "jsx", "tsx", "next.js", "gatsby"],
      "vue": ["vue", "nuxt", "quasar"],
      "angular": ["angular", "ionic"],
      "svelte": ["svelte", "sveltekit"]
    },
    "backend": {
      "nodejs": ["node", "express", "koa", "fastify"],
      "python": ["python", "django", "flask", "fastapi"],
      "go": ["go", "gin", "echo", "fiber"],
      "java": ["java", "spring", "quarkus"],
      "csharp": ["c#", "asp.net", "dotnet"]
    },
    "database": {
      "postgresql": ["postgres", "postgresql", "pg"],
      "mongodb": ["mongo", "mongodb"],
      "mysql": ["mysql", "mariadb"],
      "redis": ["redis"],
      "sqlite": ["sqlite"]
    },
    "mobile": {
      "react_native": ["react-native", "expo"],
      "flutter": ["flutter", "dart"],
      "ionic": ["ionic"],
      "swift": ["swift", "ios"],
      "kotlin": ["kotlin", "android"]
    },
    "data": {
      "python": ["python", "pandas", "numpy"],
      "r": ["r", "rstudio"],
      "scala": ["scala", "spark"],
      "julia": ["julia"]
    },
    "ml": {
      "tensorflow": ["tensorflow", "tf"],
      "pytorch": ["pytorch", "torch"],
      "scikit": ["scikit-learn", "sklearn"],
      "keras": ["keras"]
    },
    "infrastructure": {
      "docker": ["docker", "container"],
      "kubernetes": ["kubernetes", "k8s"],
      "terraform": ["terraform"],
      "ansible": ["ansible"],
      "aws": ["aws", "amazon"],
      "gcp": ["gcp", "google"],
      "azure": ["azure", "microsoft"]
    }
  },
  "complexity_assessment": {
    "simple": {
      "criteria": [
        "Single technology stack",
        "Basic CRUD operations",
        "No authentication required",
        "No real-time features",
        "Single environment deployment"
      ],
      "max_files": 20,
      "max_endpoints": 10,
      "max_components": 15
    },
    "moderate": {
      "criteria": [
        "Multiple technology stacks",
        "Authentication and authorization",
        "API integration",
        "Basic real-time features",
        "Multi-environment deployment"
      ],
      "max_files": 50,
      "max_endpoints": 25,
      "max_components": 30
    },
    "complex": {
      "criteria": [
        "Microservices architecture",
        "Advanced authentication (OAuth, SSO)",
        "Multiple API integrations",
        "Real-time features (WebSockets, SSE)",
        "Multi-cloud deployment",
        "Advanced monitoring and logging"
      ],
      "max_files": 100,
      "max_endpoints": 50,
      "max_components": 60
    }
  }
}
```

### Task 6: Evidence and Quality Integration
**Files**: `.cursor/ai-driven-workflow/*.md`

**Requirements**:
- Ensure all protocols collect evidence automatically
- Integrate quality gates with `unified_workflow`
- Include validation checkpoints where needed
- Document evidence collection requirements

**Implementation**:
- Update each protocol to include evidence collection steps
- Integrate with `unified_workflow` quality gates
- Add validation checkpoints for critical decisions
- Ensure evidence is stored in standardized format

### Task 7: Testing and Validation
**Files**: Test scenarios and validation scripts

**Requirements**:
- Create test scenarios for different project types
- Validate protocol generation logic
- Test integration with `unified_workflow`
- Verify autonomous execution capability

**Implementation**:
- Create test PROJECT-BRIEF.md files for each project type
- Test protocol generation and customization
- Validate command execution and evidence collection
- Verify quality gates and error handling

## SUCCESS CRITERIA

### Functional Requirements
- [ ] `/protocol-orchestrator` command analyzes PROJECT-BRIEF.md and generates project-specific protocols
- [ ] Generated protocols integrate with `unified_workflow` automation scripts
- [ ] All protocols execute autonomously without human coding
- [ ] Evidence collection and quality gates work automatically
- [ ] Command wrappers provide real-time feedback

### Technical Requirements
- [ ] Protocol format matches existing `.cursor/ai-driven-workflow/*.md` structure
- [ ] Integration with `unified_workflow` is seamless and reliable
- [ ] Project type decision matrix covers all supported project types
- [ ] Technology stack detection is accurate and comprehensive
- [ ] Complexity assessment correctly categorizes projects

### Quality Requirements
- [ ] Generated code compiles and runs without errors
- [ ] Test coverage exceeds 80% for all generated code
- [ ] Security scans pass for all generated code
- [ ] Performance benchmarks meet requirements
- [ ] Documentation is complete and accurate

### User Experience Requirements
- [ ] Commands are discoverable in Cursor's command palette
- [ ] Execution provides clear progress feedback
- [ ] Error messages are helpful and actionable
- [ ] Rollback procedures work correctly
- [ ] Evidence collection is transparent and accessible

## DELIVERABLES

### 1. Executable Commands
- `.cursor/commands/protocol-orchestrator.md` - Project analysis and protocol generation
- `.cursor/commands/0-bootstrap.md` - Bootstrap protocol execution
- `.cursor/commands/1-prd.md` - PRD creation protocol execution
- `.cursor/commands/2-tasks.md` - Task generation protocol execution
- `.cursor/commands/3-implementation.md` - Autonomous implementation protocol execution
- `.cursor/commands/4-quality.md` - Quality audit protocol execution
- `.cursor/commands/5-retrospective.md` - Retrospective protocol execution
- `.cursor/commands/6-operations.md` - Operations protocol execution

### 2. Enhanced Protocol Templates
- `.cursor/ai-driven-workflow/0-bootstrap-your-project.md` - Enhanced with `unified_workflow` integration
- `.cursor/ai-driven-workflow/1-create-prd.md` - Enhanced with `unified_workflow` integration
- `.cursor/ai-driven-workflow/2-generate-tasks.md` - Enhanced with `unified_workflow` integration
- `.cursor/ai-driven-workflow/3-process-tasks.md` - Enhanced with autonomous code generation
- `.cursor/ai-driven-workflow/4-quality-audit.md` - Enhanced with `unified_workflow` integration
- `.cursor/ai-driven-workflow/5-implementation-retrospective.md` - Enhanced with `unified_workflow` integration

### 3. Configuration Files
- `.cursor/ai-driven-workflow/protocol-metadata.json` - Project type decision matrix
- `AGENTS.md` - Updated with integration details
- `PROTOCOL-ORCHESTRATOR.md` - Renamed from current `AGENTS.md`

### 4. Integration Scripts
- `scripts/protocol_orchestrator.py` - Protocol generation logic
- `scripts/project_classifier.py` - Project type classification
- `scripts/tech_stack_detector.py` - Technology stack detection
- `scripts/complexity_assessor.py` - Complexity assessment

### 5. Documentation
- `README.md` - Updated with integration instructions
- `INTEGRATION.md` - Detailed integration guide
- `TESTING.md` - Testing and validation procedures

## EXECUTION INSTRUCTIONS

**EXECUTE NOW. Analyze the current system, design the integration, implement all tasks, and validate with test scenarios. Deliver a complete, working system that achieves the target behavior.**

The integration must be seamless, reliable, and production-ready. All protocols must execute autonomously, generate production-quality code, and provide comprehensive evidence collection and quality validation.

**CRITICAL**: This system will be used as a template for generating diverse projects. It must be robust, scalable, and maintainable. The AI must be able to generate complete, working applications without human coding intervention.

**SUCCESS METRIC**: A user should be able to clone this template, create a PROJECT-BRIEF.md, run `/protocol-orchestrator`, and receive a complete, production-ready application that compiles, runs, passes tests, and meets all quality gates automatically.