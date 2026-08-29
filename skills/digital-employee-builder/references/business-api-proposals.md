# External Contract Proposals

The source business project is read-only. Use `docs/business-api-proposals.md` only when an approved employee task requires an unavoidable external capability and no adequate contract exists.

Do not propose an API for code or data that the approved migration plan embeds locally. Do not create remote boundaries merely to mirror the source project's controllers.

## Proposal Triggers

Create a proposal when:

- an inherently external effect lacks a stable interface;
- external-authoritative data lacks a supported query or synchronization contract;
- an external write lacks idempotency, status, or reconciliation support;
- policy requires a subsystem to remain separately operated.

Never work around a missing contract with source-path imports, direct access to an external database, screen scraping, or silent production stubs.

## Required Contract

Each proposal records:

| Field | Required content |
|---|---|
| ID and status | stable ID; `proposed`, `approved`, `implemented`, `deployed`, `verified`, `rejected`, or `dropped` |
| User task / runtime port | the approved task and local port this unblocks |
| Current limitation | evidence showing why the retained external dependency is inadequate |
| Interface shape | HTTP, MCP, SDK, event, or synchronization contract |
| Request and response | field names, types, constraints, pagination, and examples |
| Errors | stable codes, retryability, and transport mapping |
| Effects | state changes, downstream effects, and consistency model |
| Auth | credential variable names and authorization scope |
| Idempotency | deduplication key and safe-retry/reconciliation semantics |
| Non-goals | excluded behavior and boundaries |
| Employee impact | runtime adapter, tool/task, test fake, and rollout plan |
| Approval | risk-gate approver and date |

## Employee-Side Rules

- The runtime owns the port; the external contract is implemented by one adapter.
- Tools and scripts continue to call the runtime rather than the adapter directly.
- Pending contracts may use an explicit fake for tests and demos. Never present fake data as live.
- Record the switch from fake to live adapter in TOOLS.md and `docs/harness-setup.md`.
- After deployment, run contract, failure, idempotency, and reconciliation tests before marking the proposal verified.
