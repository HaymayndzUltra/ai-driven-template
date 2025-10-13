# Coding Standards

## Purpose
Provide language/framework conventions used to enforce consistency and CI linting baselines.

## General Guidelines
- Follow SOLID and clean code practices.
- Prefer automated formatting tools (Prettier, Black, gofmt, etc.).
- Document all public interfaces with docstrings/comments.

## Language-Specific Rules
### Python
- Use type hints and run `mypy` during CI.
- Use `black` + `isort` for formatting/import order.
- Avoid side effects on import.

### JavaScript/TypeScript
- Enforce ESLint with recommended + security plugins.
- Enable strict TypeScript config for new packages.
- Limit module complexity (cyclomatic complexity < 10).

### Infrastructure as Code
- Terraform: run `terraform fmt` and `terraform validate` pre-commit.
- YAML (CI/CD): verify with `yamllint` and schema validation.

## Testing Standards
- Minimum unit test coverage: 80% (adjust with risk justification).
- Snapshot/UI tests for components.
- Integration tests for service contracts.

## Security Requirements
- Apply secure defaults (OWASP ASVS alignment).
- Validate inputs, sanitise outputs.
- Document threat mitigations in `Security_Checklist.md` (Phase 3).

## Documentation
- Update README/CHANGELOG with user-facing changes.
- Link to ADRs for major decisions.

## Review Checklist
- See `Code_Review_Checklist.md` for enforcement items.
