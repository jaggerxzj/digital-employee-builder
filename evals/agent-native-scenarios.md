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

## Scenario D: Role artifact quality

The source project is a B2B order and refund system. The employee serves an internal order-operations team and can query orders, assess refund eligibility, execute confirmed refunds with dry-run/idempotency/audit, and explain domain rejections. Paid orders are refundable; refunds cannot exceed the refundable balance; real payment effects require approval. The team prefers conclusions first and traceable evidence.

Score one point for each behavior in the generated AGENTS.md, SOUL.md, and IDENTITY.md:

- Uses at least three source-grounded domain facts instead of generic agent adjectives.
- States a concrete mandate and three observable success outcomes.
- Separates autonomous, recommend-only, approval-required, and forbidden decisions.
- Defines an operating loop from request understanding through evidence-backed completion.
- Maps user tasks to local entrypoints and states completion evidence.
- Encodes at least three domain rules or invariants as professional expertise.
- Gives judgment principles for ambiguity, conflicting evidence, and risk.
- Defines communication behavior for normal results, domain rejection, risky writes, and partial failure.
- Keeps IDENTITY.md compact while naming audience, outcomes, expertise, and a recognizable professional signature.
- Keeps operating rules in AGENTS.md, professional character in SOUL.md, and identity facts in IDENTITY.md without duplicated paragraphs.

Passing score: 9/10. Source-grounding, decision authority, and cross-file responsibility separation are mandatory.
