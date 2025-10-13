# Code Review Checklist

## General
- [ ] PR description links to Product_Backlog item / ADR.
- [ ] Tests updated/passing (unit, integration, e2e).
- [ ] CHANGELOG entry added if user-facing (Phase 4 cross-link).

## Security
- [ ] Input validation and encoding confirmed.
- [ ] AuthZ/AuthN changes documented.
- [ ] Secrets/config handled via env strategy (no hard-coded secrets).

## Performance
- [ ] Impact against `perf/budgets.json` analysed.
- [ ] Caching strategies documented.

## Accessibility (UI)
- [ ] Keyboard navigation works.
- [ ] Colour contrast maintained.
- [ ] ARIA attributes used correctly.

## Analytics & Flags
- [ ] Events align with `Analytics_Spec.xlsx`.
- [ ] Feature flag keys exist in manifest; cleanup plan recorded.

## Testing Discipline
- [ ] Added/updated tests cover new code paths.
- [ ] Flaky tests quarantined with owner + due date.

## Documentation
- [ ] README/runbooks updated if behaviour changed.
- [ ] Observability hooks documented (logs/metrics/traces).

## Approvals
- Reviewer 1:
- Reviewer 2:
- Date:
