---
name: digital-employee-builder
description: "Use when converting a completed business codebase, module, API specification, or functional description into a self-contained Agent digital employee, especially when domain logic should run inside the employee instead of being orchestrated through many external APIs."
---

# Digital Employee Builder

Convert business software into an agent-native employee with a reusable local business runtime, task-oriented tools, operating rules, and verifiable workflows.

## Default Architecture

For a completed project, the default is an **embedded domain runtime**:

- Preserve and adapt existing domain models, application services, state machines, validators, migrations, and tests.
- Remove or replace delivery layers the employee does not need, such as web controllers, UI, and deployment-specific shells.
- Put deterministic business behavior in one shared local runtime. Local MCP tools and workflow scripts are entrypoints into it, not separate implementations.
- Keep an external dependency only when the capability is inherently external or its authoritative state must remain outside the employee.

Read `references/embedded-runtime.md` before designing or generating the runtime.

## Non-Negotiable Invariants

1. **Source is read-only.** Analyze and copy from the business project; never modify it.
2. **Preserve before rewriting.** Prefer mechanical extraction and import adaptation over regenerating proven logic from prose.
3. **One business implementation.** Domain rules cannot be duplicated across tools, scripts, prompts, or adapters.
4. **Standalone delivery.** The generated workspace must run without the source repository or paths back into it.
5. **Tests migrate with behavior.** Port relevant source tests and add entrypoint tests before claiming parity.
6. **Writes are controlled.** Destructive, financial, outbound, or irreversible effects require confirmation, dry-run where meaningful, idempotency, and an audit result.
7. **Secrets stay external.** Record environment-variable names only.

## Workflow

### 1. Inspect Before Asking

Confirm only the business input and target harness when they cannot be inferred. Default to OpenClaw when no harness is named. When `.codegraph/` exists, use CodeGraph before text search.

Read the project, its tests, schemas, migrations, configuration, and documentation before asking business questions. Follow `references/conversation-protocol.md` for progress updates, grouped questions, and approval gates.

### 2. Model User Tasks and Migration Decisions

Analyze the project by user task and end-to-end business workflow, not by endpoint count. Follow `references/migration-analysis.md` and prepare:

- user tasks and expected outcomes;
- domain rules, state transitions, and side effects;
- module decisions: `preserve`, `adapt`, `replace`, `externalize`, or `drop`;
- data ownership and persistence plan;
- required external adapters;
- source-test migration and traceability plan;
- employee scope, approval boundaries, and forbidden operations.

Then read `references/role-modeling.md` and derive a source-grounded Employee Role Brief: identity facts, success outcomes, four-level decision authority, professional expertise, judgment posture, communication contract, and capability-to-outcome map.

Present a concise migration brief. Ask at most three decision-changing questions in one round, each with a recommended default.

### 3. Obtain the Required Approval

Use one normal gate for the employee blueprint: Employee Role Brief, user tasks, migration map, data plan, tools, skills, and exclusions.

Add a separate **risk gate** only when the plan changes data ownership, performs destructive or real-world writes, introduces a new external contract, or handles regulated/sensitive data. On revisions, present the delta and changed consequences; do not repeat the complete inventory.

After approval, write:

- `docs/migration-plan.md` — source-to-runtime module map, data ownership, adapters, provenance, and test migration;
- `docs/business-capabilities.md` — task-oriented capabilities, inputs/outputs, side effects, rules, and source evidence;
- `docs/employee-plan.md` — role, scope, tools, skills, approvals, and exclusions;
- `docs/business-api-proposals.md` only when an unavoidable external contract is missing.

### 4. Generate the Employee Workspace

Use the assets in this skill and generate:

```text
<employee-name>/
├── AGENTS.md
├── SOUL.md
├── IDENTITY.md
├── USER.md
├── TOOLS.md
├── HEARTBEAT.md                 # only when periodic work is justified
├── runtime/                     # embedded domain/application runtime
│   ├── src/
│   ├── tests/
│   └── dependency manifest
├── mcp-server/                  # local task-oriented entrypoints
├── skills/                      # judgment guidance and workflow entrypoints
├── memory/
└── docs/
    ├── migration-plan.md
    ├── business-capabilities.md
    ├── employee-plan.md
    └── harness-setup.md
```

Keep the source project's language and module boundaries when practical. For Python generation, start from `assets/embedded-runtime-python/`; for another language, reproduce the same ports-and-adapters contract in that language rather than translating automatically.

Generate `IDENTITY.md`, `SOUL.md`, and `AGENTS.md` from the approved Employee Role Brief and their workspace templates. Apply the file responsibility map and specificity test in `references/role-modeling.md`; do not leave template choices, alternatives, examples, or unresolved placeholders in the delivered files.

### 5. Expose Capabilities by User Intent

Read `references/mcp-integration.md` when generating MCP tools.

- Create the smallest tool set that covers approved user tasks.
- A tool represents a bounded business action or query, not a controller, endpoint, table, or service method.
- Local tools call the shared runtime directly.
- Workflow scripts are reserved for batch, scheduled, or CLI-suitable deterministic flows and call the same runtime; read `references/script-encapsulation.md` when scripts are needed.
- Judgment, interpretation, and content generation stay in prompt-oriented skills.

### 6. Verify Before Delivery

Read the harness-specific reference only for the selected target:

- OpenClaw: `references/openclaw-workspace.md`
- Claude Code, Cursor, or generic MCP harness: `references/harness-adapters.md`

Verification must include:

- clean-environment install and startup without the source project;
- migrated source tests plus new runtime, tool, and script tests;
- traceability from every approved user task to runtime code and tests;
- no source-repository paths, hardcoded secrets, placeholder implementations, or silent stubs;
- local MCP initialize, tools/list, and representative tools/call checks;
- dry-run, rejection, idempotency, and audit-result checks for dangerous writes;
- identity, read-only task, write confirmation, and failure-escalation dialogue smoke tests;
- role-artifact specificity: source-grounded success outcomes, all four authority levels, professional judgment, scenario behavior, and no cross-file paragraph duplication;
- exact match between approved plan and delivered tools/skills.

Record commands, results, retained external dependencies, and known limitations in `docs/harness-setup.md`.

## Conditional References

- `references/conversation-protocol.md` — interaction cadence, question batching, normal gate, and risk gate.
- `references/migration-analysis.md` — repository analysis, user-task discovery, module classification, data ownership, and test provenance.
- `references/embedded-runtime.md` — default agent-native architecture and packaging rules.
- `references/role-modeling.md` — required before proposing or generating employee identity, SOUL.md, and AGENTS.md.
- `references/script-encapsulation.md` — read only when the employee needs batch, scheduled, or CLI workflow scripts.
- `references/mcp-integration.md` — read when exposing local or external capabilities as MCP tools.
- `references/business-api-proposals.md` — read only when an unavoidable external interface is missing.
- `references/openclaw-workspace.md` or `references/harness-adapters.md` — read only for the selected harness.
