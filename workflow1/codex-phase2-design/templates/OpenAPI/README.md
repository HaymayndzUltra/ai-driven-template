# OpenAPI Contract Guidance

## Purpose
Ensure services ship with validated OpenAPI specifications and mock servers as required by AGENTS Phase 2 exit criteria.

## Workflow
1. Define endpoints using contract-first approach.
2. Author YAML in `openapi/<service>.yaml` using Redocly or Stoplight style guides.
3. Validate locally: `npx @redocly/cli lint openapi/<service>.yaml`.
4. Generate mocks: `npx @redocly/cli mock openapi/<service>.yaml --watch`.
5. Commit contract updates with corresponding ADR references.

## Template Sections
- Info (title, version, contact)
- Servers (local, staging, production)
- Tags per capability
- Paths with request/response schemas
- Components (schemas, security, parameters)

## Integration Hooks
- CI step runs Redocly lint + spectral rules.
- Mock server used by integration tests.
- Contract diffs trigger QA review.

## Evidence
- Attach lint output to `evidence/phase2/validation.md`.
- Record mock server run info in `evidence/phase2/run.log`.
