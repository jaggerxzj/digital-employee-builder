# Role Modeling

Use this reference after migration analysis and before presenting the employee blueprint or generating AGENTS.md, SOUL.md, and IDENTITY.md.

The objective is a credible professional role grounded in the business source—not a generic assistant with a job-title label.

## Source Evidence

Build the role from evidence already found in:

- user tasks, actors, workflows, and operational screens or commands;
- domain entities, state machines, invariants, validation errors, and calculations;
- source tests, policies, schemas, audit records, scheduled work, and failure recovery;
- approval boundaries, external effects, sensitive data, and accountable owners;
- user/team preferences explicitly provided in the conversation.

Do not invent organization names, numeric KPIs, SLAs, regulatory duties, personality traits, or authority. When evidence is absent, use a qualitative observable outcome or mark the choice for approval.

## Employee Role Brief

Add an `Employee Role Brief` section to `docs/employee-plan.md` before the normal gate. It contains:

1. **Identity facts** — proposed name, job title, organization/team, primary audience, language, and one-sentence mandate.
2. **Success outcomes** — three to five observable business outcomes. Use source metrics only when the source or user defines them.
3. **Decision authority** — separate `autonomous`, `recommend-only`, `approval-required`, and `forbidden` responsibilities.
4. **Professional expertise** — domain vocabulary, at least three important invariants, key lifecycle/state knowledge, common failure patterns, and evidence hierarchy.
5. **Judgment posture** — how the employee handles ambiguity, conflicting evidence, stale state, exceptions, irreversible effects, and accountable human decisions.
6. **Communication contract** — language, conclusion/evidence order, numeric precision, desired level of detail, undesirable style, and behavior in five scenarios.
7. **Capability-to-outcome map** — each primary user task, entrypoint, authority level, and evidence that means the work is complete.

Present the role brief as part of the normal blueprint. Ask the user only about choices that materially change mandate, authority, audience, or communication; propose a source-grounded default for each.

## Synthesis Method

### Mandate

Use this shape:

> Serve **[audience]** by producing **[business outcomes]** in **[domain]**, while protecting **[critical constraint]**.

Avoid “help users manage X.” Name the outcome and constraint.

### Success Outcomes

Good outcomes are observable without inventing metrics:

- eligible work reaches a verified terminal or next-action state;
- rejected work includes the controlling rule and legitimate recovery path;
- real-world writes are confirmed, idempotent, and traceable;
- unresolved or partial effects reach the accountable reconciliation owner.

Adapt these to source evidence. Do not copy them unchanged into every employee.

### Decision Authority

Classify every primary task:

| Level | Meaning |
|---|---|
| Autonomous | read-only, reversible, or explicitly delegated action |
| Recommend-only | employee analyzes; a human owns the judgment or commitment |
| Approval-required | employee may execute only after approval of the exact effect |
| Forbidden | outside mandate, unsafe bypass, unsupported authority, or excluded scope |

If a responsibility does not fit one level, the role brief is incomplete.

### Professional Expertise

Translate code into how a professional thinks:

- state machine → “state before action” judgment;
- validation rule → invariant and rejection explanation;
- transaction/idempotency → duplicate and partial-effect awareness;
- audit/event model → evidence and traceability practice;
- source tests → examples of correct, rejected, and edge behavior;
- external adapter → dependency risk and reconciliation knowledge.

Do not paste implementation details or routes into SOUL.md. Express stable business concepts and reasoning patterns.

### Communication Contract

Define behavior for:

1. normal result;
2. domain rejection;
3. risky or approval-owned action;
4. partial failure or conflicting evidence;
5. unknown or out-of-scope request.

Each scenario states what leads, what evidence follows, and what next action is offered. Replace generic adjectives such as “helpful” or “professional” with observable communication behavior.

## File Responsibility Map

| File | Owns | Does not own |
|---|---|---|
| `IDENTITY.md` | canonical name, role, organization, mandate, audience, outcomes, expertise summary, signature | procedures, permissions, tool details |
| `SOUL.md` | professional purpose, domain mental model, judgment principles, communication behavior, professional boundaries | approval steps, retry limits, environment setup |
| `AGENTS.md` | mission outcomes, completion criteria, operating loop, authority, capability map, approval/failure/reporting protocols, memory/data rules | personality prose, environment paths, duplicated domain implementation |

Brief identity facts may appear once in IDENTITY.md and be referenced naturally elsewhere. Do not repeat the same bullet list or paragraph across files.

## Specificity Test

Before approval and again after generation, check:

- Could another industry replace only the nouns and keep the paragraph? If yes, rewrite it using source evidence.
- Does each file contain at least three domain-specific facts or behaviors?
- Are at least three success outcomes observable rather than aspirational?
- Are all four authority levels explicit?
- Does SOUL.md contain at least three real invariants and concrete behavior for all five scenarios?
- Does IDENTITY.md tell a colleague who this employee serves, what it owns, and how it works without reading the other files?
- Are unsupported KPIs, authority, policy, biography, emotion, and system access absent?
- Are detailed business rules still authoritative in the runtime/docs rather than duplicated as alternate implementations?

If any check fails, revise the role brief or generated file before delivery.
