# Agent-Native Skill Evaluation Scenarios

These scenarios evaluate decisions and observable behavior, not exact wording.

## Scenario A: Completed business project, minimal external dependencies

The user provides a completed order and refund project and says: “Turn this into a standalone digital employee. The employee itself should own the capability; avoid many HTTP APIs and third-party systems. Start now and do not ask many questions.”

Score one point for each behavior:

- Scans the repository before asking business questions.
- Frames capabilities as user tasks and domain workflows, not endpoints.
- Proposes preserving a shared domain/application runtime and source tests.
- Classifies modules as preserve, adapt, replace, externalize, or drop.
- Uses local MCP tools or scripts as entrypoints into the shared runtime.
- Groups only decision-changing questions, at most three per round.
- Uses one normal approval gate and adds a risk gate only when triggered.
- Does not create independent copies of the same business rules in workflow scripts.
- Does not expose one tool per controller, route, or service method.
- Identifies inherently external effects as adapters rather than pretending they are local.

Passing score: 9/10, with the shared-runtime and no-duplicated-rules items mandatory.

## Scenario B: Pure calculation library

The source project computes quotes with no database or external services. The employee must explain and calculate quotes conversationally.

Expected behavior: preserve the calculation package and tests nearly unchanged; add a small local tool by user intent; do not invent storage, HTTP, or a workflow script layer.

## Scenario C: Stateful workflow with payment gateway

The source project owns local order state but calls an external payment provider. The employee must run locally while retaining real payment execution.

Expected behavior: embed order rules, workflows, repository abstraction, migrations, and tests; retain the payment provider as an explicit external adapter; require confirmation, dry-run, and idempotency for payment execution.

