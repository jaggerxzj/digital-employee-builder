# Migration Analysis

Analyze a completed project as business capability source material, not as a list of interfaces to wrap.

## Discovery Order

1. Identify primary actors and each user task they complete.
2. Trace each task from delivery layer into application service, domain rules, persistence, and external effects.
3. Read source tests alongside the implementation; tests are evidence of intended behavior and migration inputs.
4. Identify state ownership, transactions, scheduled work, events, and failure recovery.
5. Classify every relevant module for the target employee.

Routes, controllers, CLI commands, and jobs are discovery entrypoints. They are not automatically employee capabilities or MCP tools.

## Migration Decisions

| Decision | Use when | Target action |
|---|---|---|
| `preserve` | Domain or application code already runs without unwanted infrastructure coupling | Copy with minimal changes; retain source tests |
| `adapt` | Valuable business code is coupled through imports, framework types, or configuration | Extract behind a stable interface; preserve behavior and tests |
| `replace` | Infrastructure is necessary but the current implementation does not fit standalone runtime | Implement a local adapter, migration, or repository with parity tests |
| `externalize` | The effect or authoritative state must remain outside the employee | Define a port and explicit external adapter; document credentials and failure semantics |
| `drop` | UI, delivery, deployment, admin, or unrelated capability is not needed by the employee | Exclude it and record the reason |

Do not use `replace` merely because rewriting looks easier. Do not use `externalize` merely because an HTTP endpoint already exists.

## Required Migration Table

For every relevant source module or cohesive component, record:

| Source symbol/module | User task | Business purpose | Decision | Runtime target | State/dependencies | Source tests | Risk/notes |
|---|---|---|---|---|---|---|---|

Also record the source repository revision or commit. Generated files include provenance comments for adapted code without depending on the original path at runtime.

## Task-Oriented Capability Inventory

Each capability represents a user outcome. Record:

- name and user task;
- input and output contract;
- business rules and state transitions;
- read/write and real-world side effects;
- approval, dry-run, idempotency, and audit requirements;
- runtime application service that owns the behavior;
- source evidence and migrated tests;
- chosen entrypoint: local MCP tool, workflow script, prompt skill, or no agent surface.

Several endpoints or service methods may support one user task. One source method may support several tasks. Neither relationship determines tool count.

## Data Ownership

Classify each dataset:

- **employee-owned** — packaged local store is authoritative;
- **imported snapshot** — read-only data with an explicit refresh process;
- **external-authoritative** — accessed through an adapter and never silently copied;
- **ephemeral** — temporary runtime state with retention rules.

When replacing persistence, migrate schema constraints, transactions, uniqueness, and recovery behavior—not only fields. Confirm ownership changes at the risk gate.

### Data Cutover

When authoritative data moves into the employee, the migration plan defines:

1. source snapshot/export format and schema version;
2. pre-import integrity checks, counts, checksums, and rejected-record handling;
3. write-freeze window or a delta capture mechanism for concurrent changes;
4. idempotent import and post-import domain invariant checks;
5. cutover criteria and the point at which the employee becomes authoritative;
6. rollback procedure, retained source backup, and reconciliation owner;
7. later runtime-schema migration and recovery testing.

For an imported snapshot, define the refresh cadence and delta semantics instead of calling the snapshot authoritative. For external-authoritative data, test adapter outages and stale-read behavior rather than inventing a local cutover.

## Test Migration

- Preserve source tests for every preserved module.
- Adapt test imports and infrastructure fixtures without weakening assertions.
- Add parity tests when replacing persistence or another adapter.
- Add task-level tests at application-service boundaries.
- Record intentionally unsupported source behavior as an explicit exclusion.

Coverage is complete only when every approved user task maps to runtime code and at least one meaningful migrated source test or new task-level test.
