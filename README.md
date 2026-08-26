# Digital Employee Builder

Turn a business codebase into a **runnable Agent digital employee** — a self-contained workspace with identity, rules, tools, and workflows, ready to run on OpenClaw, Claude Code, Cursor, or any MCP-capable harness.

## What It Does

Point it at a business system or module (source code, API docs, or a functional spec) and it produces a complete digital-employee workspace:

```
<employee-name>/
├── AGENTS.md          # Operating rules: scope, approval gates, forbidden zone
├── SOUL.md            # Persona: identity, tone, expertise, boundaries
├── IDENTITY.md        # Name, emoji, one-line role
├── USER.md            # Audience profile
├── TOOLS.md           # Environment notes and credential variable names
├── HEARTBEAT.md       # Periodic tasks (optional)
├── skills/            # Script-driven workflow skills
├── mcp-server/        # MCP server wrapping atomic business capabilities
└── docs/              # Business capability inventory + harness setup guide
```

### Core Design Decisions

- **Deterministic logic lives in code, not prompts.** Atomic capabilities become MCP tools; multi-step business workflows (refunds, approvals, reconciliation) become executable `scripts/` ported from the business code — ordering, validation, and branching are enforced by code, so the model cannot skip steps.
- **Runtime self-containment.** The workspace deploys standalone into the harness runtime, where the business codebase does not exist. Scripts never reference business source via `sys.path` or file paths. Business logic is **fully ported into scripts by default** (zero network dependency, immune to API flakiness); calling a deployed API or a published SDK is an opt-in fallback.
- **Harness-native onboarding.** Ships with the OpenClaw workspace spec (character budgets, injection order, truncation pitfalls), plus adapters for Claude Code (`CLAUDE.md` / `.mcp.json`), Cursor (`.mdc` rules), and generic harnesses.
- **Safety gates by default.** Write operations require explicit human confirmation; every script supports `--dry-run`; secrets come from environment variables only; a clean-environment verification checklist runs before delivery.

## Install

```bash
# Interactive — pick the skill, agents, and scope
npx skills add jaggerxzj/digital-employee-builder

# Direct install, global scope
npx skills add jaggerxzj/digital-employee-builder --skill digital-employee-builder -g
```

Works with 40+ agents including Claude Code, Cursor, OpenCode, and Kimi Code CLI.

## Usage

Once installed, give your agent the business codebase and a role:

> "Turn the order-management module in ./aps-backend into a digital employee named ops-agent, running on OpenClaw."

The agent will walk through: business analysis → role modeling → workspace generation → MCP wrapping → script-driven skills → onboarding & verification.

## Repository Structure

```
skills/
└── digital-employee-builder/
    ├── SKILL.md                      # Main workflow (7 steps)
    ├── references/
    │   ├── script-encapsulation.md   # Script porting patterns & engineering standards
    │   ├── openclaw-workspace.md     # OpenClaw workspace spec
    │   ├── mcp-integration.md        # MCP wrapping essentials
    │   └── harness-adapters.md       # Claude Code / Cursor / generic harness adapters
    └── assets/
        ├── workspace/*.tmpl          # AGENTS.md, SOUL.md, IDENTITY.md, ... templates
        ├── skill-template/           # Thin-shell SKILL.md + workflow script templates
        ├── mcp-server-python/        # FastMCP server template
        └── mcp-server-ts/            # TypeScript MCP server template
```

## Safety Notes

- Generated scripts are thin, auditable wrappers — review them before connecting real credentials.
- Never commit secrets; all templates use environment variables.
- Dangerous operations ship with human-confirmation gates and `--dry-run` support.

## License

MIT
