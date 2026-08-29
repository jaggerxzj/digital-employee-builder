# Harness Adapters

Use only when the target harness is not OpenClaw. Install the embedded runtime before registering its local MCP server.

## Claude Code

Workspace mapping:

| Employee artifact | Claude Code equivalent |
|---|---|
| AGENTS.md + SOUL.md | project-root `CLAUDE.md` |
| IDENTITY.md / USER.md | corresponding CLAUDE.md sections |
| TOOLS.md | environment section |
| skills/ | `.claude/skills/<name>/SKILL.md` |
| HEARTBEAT.md | external scheduler calling `claude -p` |

Install and configure:

```bash
python -m pip install -e <absolute-workspace>/runtime
python -m pip install "mcp[cli]"
```

```json
{
  "mcpServers": {
    "<employee-name>-tools": {
      "command": "python",
      "args": ["<absolute-workspace>/mcp-server/server.py"],
      "env": { "EMPLOYEE_DATA_PATH": "<absolute-workspace>/data/employee.db" }
    }
  }
}
```

Add environment variables only for adapters retained in `docs/migration-plan.md`. Verify with `claude mcp list` and a representative local tool call.

## Cursor

- Merge AGENTS.md and SOUL.md into `.cursor/rules/<employee-name>.mdc` with `alwaysApply: true`.
- Convert each required workspace skill into a focused `.mdc` rule.
- Use the same local runtime installation and MCP configuration shape as Claude Code in `.cursor/mcp.json`.
- Use an external scheduler for heartbeat behavior.

## Generic Harness

1. Assemble the system context from SOUL.md, IDENTITY.md, USER.md, AGENTS.md, and TOOLS.md without duplicating sections.
2. Install the runtime from its dependency manifest.
3. Register the local stdio MCP server. If MCP is unavailable, expose the same application-service methods through the harness's typed function interface.
4. Schedule HEARTBEAT.md only when periodic work was approved.
5. Record exact setup commands, adapter variables, and verification results in `docs/harness-setup.md`.
