# Embedded Domain Runtime

The embedded runtime is the employee's local business kernel and the single source of deterministic business behavior.

## Target Shape

```text
runtime/
├── src/<runtime-package>/
│   ├── domain/          # entities, value objects, policies, state machines
│   ├── application/     # user-task services and workflow orchestration
│   ├── ports/           # repository and external-effect contracts
│   └── adapters/        # local storage and retained external integrations
├── tests/               # migrated source tests plus parity/task tests
└── dependency manifest
```

Keep the source project's language and cohesive module boundaries by default. Do not translate a working project to another language merely to match a template.

## Extraction Rules

1. Copy preserved modules and source tests before adapting imports.
2. Remove delivery-framework types from application and domain boundaries.
3. Move infrastructure access behind ports only when it blocks standalone packaging or testing.
4. Preserve business exceptions, validation branches, ordering, transactions, and idempotency behavior.
5. Replace infrastructure through behavior-parity tests.
6. Record source revision and symbol provenance in `docs/migration-plan.md`.

Reimplementation from prose is the last resort. If direct extraction is impossible, use source code and tests as the specification and document the reason for rewriting.

## Entrypoints

### Local MCP

A local MCP server is an in-process or same-machine interface to application services. It does not imply an HTTP or third-party dependency. Each local MCP tool represents a bounded user intent and returns structured data or a structured domain error.

### Workflow Scripts

Scripts serve batch, scheduled, or CLI-suitable workflows. They parse arguments, construct the runtime, call one application service, serialize the result, and map domain errors to exit codes. They do not duplicate rules from the runtime.

### Prompt Skills

Prompt skills handle interpretation, judgment, drafting, and explanation. They may call local MCP tools or scripts, but prompts never become the authoritative implementation of validation or state transitions.

## Persistence

Choose the smallest local store that preserves required semantics:

- SQLite for transactional single-node relational state;
- files only for simple immutable/configuration data with atomic-write handling;
- an embedded database already used by the project when it packages cleanly;
- an external-authoritative adapter when the employee must not own the data.

Package migrations and initialize storage explicitly. Do not replace transactional persistence with ad hoc JSON solely to remove a dependency.

For multi-entity or dangerous writes, preserve the source unit-of-work boundary. Business state, idempotency state, and audit/outbox records must commit in one transaction when they share a database. When an external effect prevents a single transaction, use the source project's outbox, saga, or reconciliation design and test every crash boundary. The generic SQLite assets are a single-node scaffold, not evidence of parity with the source persistence model.

## External Adapters

An external adapter is appropriate for inherently external effects—payments, email delivery, carrier booking, identity verification, live market data—or external-authoritative state.

Each external adapter defines:

- a local port owned by the runtime;
- credential variable names;
- timeouts and bounded retry semantics;
- idempotency and reconciliation behavior for writes;
- structured failures and audit evidence;
- a fake or local test implementation.

For irreversible or regulated writes, prompt confirmation alone is not a server-side control. When the harness or organization provides signed approvals, capability tokens, or an approval service, model it as a runtime port and verify the approval reference before committing. Otherwise document the remaining trust boundary explicitly and do not describe the employee as independently authorized for that effect.

If a required external contract does not exist, follow `business-api-proposals.md`. Do not turn internal local capabilities into APIs merely for architectural symmetry.

## Consistency Checks

- Local MCP tools and scripts import the runtime package.
- No copied business rule appears in an entrypoint.
- Every external adapter is replaceable behind a port and tested at the application boundary.
- Runtime installation succeeds from its dependency manifest without the source repository.
- Migrated tests and task-level tests pass in the clean workspace.
