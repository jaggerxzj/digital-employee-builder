# Workflow Script Entrypoints

Use a workflow script only when a user task is naturally batch-oriented, scheduled, automation-facing, or safer as one deterministic CLI invocation.

## Boundary

The shared embedded runtime owns domain rules, validation, state transitions, ordering, and compensation. A script owns only:

- CLI argument parsing;
- dependency/runtime construction;
- dry-run selection;
- one application-service invocation;
- JSON serialization and exit-code mapping.

Do not copy business logic into `skills/<workflow>/scripts/`. Several scripts may call the same application service, but they must not fork its implementation.

## Runtime Independence

The script may import the packaged local runtime installed from `runtime/`. It may not import the source business repository through `sys.path`, absolute paths, or relative traversal.

External effects flow through runtime ports and adapters. The script does not create a second HTTP/SDK integration path.

## Dangerous Workflows

Dangerous workflows provide `--dry-run`. The dry run executes normal validation and reports the planned effect without committing it. Real execution still requires the approval rule in `AGENTS.md`.

Use stable output and exit contracts:

| Exit | Meaning | Agent behavior |
|---|---|---|
| `0` | success or successful dry-run | report structured result |
| `2` | invalid arguments | correct parameters once |
| `3` | domain rejection | report current state; do not bypass or retry |
| `4` | unavailable dependency | report adapter and recovery action |
| `5` | partial/uncertain effect | stop; report audit/correlation ID for reconciliation |

## Verification

Run each script in the clean generated workspace:

1. `--help` and invalid arguments;
2. happy path using the real local runtime;
3. dry-run for dangerous effects;
4. at least one domain rejection;
5. fake-adapter failure for external effects;
6. comparison with the corresponding application-service test.
