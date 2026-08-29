# Digital Employee Builder

Turn a completed business project into a **self-contained Agent digital employee**. The generated employee embeds reusable domain and application code, exposes task-oriented local tools, and retains external adapters only for effects or authoritative systems that cannot live locally.

## What It Produces

```text
<employee-name>/
├── AGENTS.md / SOUL.md / IDENTITY.md / USER.md
├── runtime/             # preserved/adapted business kernel and migrated tests
├── mcp-server/          # local task-oriented MCP entrypoints
├── skills/              # judgment guidance and optional workflow entrypoints
├── memory/
└── docs/
    ├── migration-plan.md
    ├── business-capabilities.md
    ├── employee-plan.md
    └── harness-setup.md
```

## Core Design

- **Agent-native capability.** Existing domain models, rules, workflows, migrations, and tests become a shared embedded runtime instead of being reimplemented as prompts or many remote APIs.
- **Preserve before rewriting.** Modules are classified as `preserve`, `adapt`, `replace`, `externalize`, or `drop`; source tests migrate with preserved behavior.
- **One business implementation.** Local MCP tools and workflow scripts call the same runtime and never maintain independent copies of business rules.
- **User-task tools.** Tool boundaries follow business outcomes, not controllers, routes, tables, or service methods.
- **Explicit external adapters.** Payments, email, carriers, identity providers, and external-authoritative data remain behind runtime-owned ports when necessary.
- **Standalone verification.** The employee is installed and tested without the source repository, with traceability from approved user tasks to runtime code and tests.

## Install

```bash
# Interactive
npx skills add jaggerxzj/digital-employee-builder

# Direct, global install
npx skills add jaggerxzj/digital-employee-builder --skill digital-employee-builder -g
```

## Usage

> “Turn the completed order-management project in `./service` into a standalone operations employee. Preserve its business capabilities locally and keep only unavoidable payment and notification integrations external.”

The builder scans the project before asking questions, presents a concise migration blueprint, gets one normal approval, then generates and verifies the employee. A separate risk gate appears only for data-ownership changes, destructive/real-world writes, new external contracts, or sensitive-data movement.

## Repository Structure

```text
skills/digital-employee-builder/
├── SKILL.md
├── references/
│   ├── conversation-protocol.md
│   ├── migration-analysis.md
│   ├── embedded-runtime.md
│   ├── script-encapsulation.md
│   ├── mcp-integration.md
│   └── harness adapters and workspace specifications
└── assets/
    ├── embedded-runtime-python/
    ├── mcp-server-python/ and mcp-server-ts/
    ├── skill-template/
    └── workspace/
```

## Safety

- The source business project is read-only input.
- Generated workspaces contain no source-repository paths or secrets.
- Dangerous effects require confirmation, dry-run where meaningful, idempotency, and audit evidence.
- External adapters and data ownership remain visible in `docs/migration-plan.md`.

## License

MIT
