# Conversation Protocol

Use this protocol to keep repository-to-employee work collaborative without turning analysis into a long interview.

## Interaction Contract

### Start

State the input being analyzed, the assumed harness, and the next artifact. If the user already supplied a repository and did not name a harness, proceed with OpenClaw as a reversible default.

Do not ask for employee name, personality, tool names, or architecture before reading the project. Infer and propose them in the blueprint.

### Analyze

Inspect the repository first. Maintain an uncertainty ledger while reading instead of interrupting at every ambiguity. Send concise progress updates with evidence such as modules found, workflows traced, and risks discovered.

Questions must satisfy all of these conditions:

- the answer cannot be obtained from code, tests, configuration, or docs;
- different answers materially change scope, data ownership, safety, or architecture;
- work cannot safely continue using a reversible assumption.

Batch at most three questions per round. Each question includes the evidence, why the decision matters, and a recommended default. Use a structured question tool when available; otherwise ask concise plain-text questions.

### Present the Migration Brief

Lead with conclusions and present five blocks:

1. Employee mandate and primary user tasks.
2. Modules to preserve, adapt, replace, externalize, and drop.
3. Embedded runtime, data ownership, and retained external adapters.
4. Task-oriented local tools, workflow scripts, and prompt skills.
5. Risks, exclusions, test migration, and open decisions.

Link or summarize the full migration table rather than dumping every route or method into the conversation.

## Approval Gates

### Normal Gate

Every build has one normal approval gate after the migration brief and employee blueprint. Approval covers scope, module decisions, data plan, tool/skill surface, and exclusions. Do not generate the final workspace before approval.

### Risk Gate

Add a risk gate only when at least one trigger exists:

- ownership or location of authoritative data changes;
- destructive, financial, outbound, or irreversible effects are enabled;
- a new external API, SDK, queue, database, or synchronization contract is required;
- regulated or sensitive data is copied into the employee workspace.

The risk gate states the exact change, affected data/effect, rollback or recovery path, approval owner, and verification evidence required.

Present the normal gate first so scope and architecture are stable before risk acceptance. When the risk appendix is complete and unambiguous, the user may approve the normal gate and risk gate in the same reply; record the two approvals separately. If either changes, re-present only that gate's delta.

### Revisions

After user feedback, present a delta: changed decision, reason, downstream impact, and newly required tests. Do not restate unchanged tables. Ask for approval only on the revised blueprint or risk item.

## Fast-Path Behavior

When the user says “start,” “use your judgment,” or “do not ask many questions,” continue with reversible assumptions after repository inspection. Record assumptions in the migration brief. Stop only for a missing decision that changes data ownership, production effects, credentials, or regulated-data handling.
