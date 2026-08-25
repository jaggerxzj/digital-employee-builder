# MCP Wrapping Essentials

Protocol and engineering details for wrapping business capabilities as an MCP server.

## Contents

- [Choosing a Transport](#choosing-a-transport)
- [Tool Design Conventions](#tool-design-conventions)
- [Python FastMCP Quick Reference](#python-fastmcp-quick-reference)
- [Smoke Testing](#smoke-testing)

## Choosing a Transport

| Mode | Use when | Notes |
|---|---|---|
| stdio | Harness runs on the same machine (default recommendation) | Harness spawns the server as a subprocess; no port management |
| streamable HTTP | Long-running server, shared by multiple harnesses, remote deployment | Handle auth and ports yourself |

## Tool Design Conventions

1. Naming: `verb_noun` snake_case (`query_order`, `create_refund`), one-to-one with the capability inventory.
2. Description is the contract: state what it does, parameter meanings/formats, what it returns, and side effects. Prefix write tools with `[WRITE — confirm with the user before executing]`.
3. Strongly typed parameters with per-field descriptions; list valid values for enums in the description.
4. Thin wrapper: validate params → call the existing business interface (HTTP client / SDK / imported module) → return structured results. Never copy business logic — dual implementations drift.
5. Error handling: convert business exceptions to text with error codes (e.g., `ORDER_NOT_FOUND: order xxx does not exist`); never let raw tracebacks flood the context.
6. Credentials: inject via env vars (`BUSINESS_API_BASE`, `BUSINESS_API_TOKEN`, etc.); TOOLS.md records variable names only.
7. Response size: list tools take a `limit` parameter (default 20) so a single call can't blow up the context window.

## Python FastMCP Quick Reference

```bash
pip install "mcp[cli]"   # or: uv add mcp
```

Minimal server:

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("<employee-name>-tools")

@mcp.tool()
def query_order(order_id: str) -> str:
    """Query order details (read-only). order_id: order number, e.g. SO20260101001."""
    ...

if __name__ == "__main__":
    mcp.run()  # stdio
```

## Smoke Testing

Quick stdio verification (send initialize + tools/list):

```bash
python3 - <<'EOF'
import json, subprocess
p = subprocess.Popen(["python3", "server.py"], stdin=subprocess.PIPE,
                     stdout=subprocess.PIPE, text=True)
def send(msg):
    p.stdin.write(json.dumps(msg) + "\n"); p.stdin.flush()
send({"jsonrpc":"2.0","id":1,"method":"initialize","params":{
  "protocolVersion":"2024-11-05","capabilities":{},
  "clientInfo":{"name":"smoke","version":"0"}}})
send({"jsonrpc":"2.0","method":"notifications/initialized"})
send({"jsonrpc":"2.0","id":2,"method":"tools/list"})
for _ in range(2):
    print(p.stdout.readline())
p.kill()
EOF
```

Confirm the tool count in tools/list matches the capability inventory. For HTTP mode, curl the health endpoint, then connect with any MCP inspector to verify.
