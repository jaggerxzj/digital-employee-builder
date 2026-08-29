# MCP Integration

MCP is the employee's typed task interface. For the default embedded architecture, the server runs locally and calls the packaged runtime directly.

## Tool Design

Design tools from approved user tasks:

- one bounded query or business action per tool;
- names are user-intent verbs such as `calculate_quote`, `review_application`, or `process_refund`;
- inputs use business concepts and constraints, not controller payloads by default;
- outputs are structured, bounded, and useful to the conversation;
- domain rejections are distinguishable from dependency failures;
- side effects, confirmation requirements, idempotency, and dry-run behavior appear in the description and schema.

Do not generate one tool per endpoint, table, route, or service method. Do not expose low-level write building blocks that allow the model to bypass an approved business action.

## Local Runtime Pattern

The server constructs application services from the runtime package once, then each tool validates its transport schema and calls one application-service method. Domain rules remain in the runtime.

```python
from employee_runtime.application import EmployeeApplication

app = EmployeeApplication.from_environment()

@mcp.tool()
def calculate_quote(customer_id: str, items: list[dict]) -> dict:
    """Calculate a quote locally without side effects."""
    return app.calculate_quote(customer_id=customer_id, items=items)
```

Keep transport validation in the server and business validation in the runtime. Return structured objects; do not encode failures as ordinary success strings.

## External Capabilities

When an inherently external capability is retained, the MCP tool still calls the local application service. That service invokes an external adapter through a runtime port. The MCP server must not bypass the runtime with its own HTTP client.

If the external system itself must expose a direct tool, document why local orchestration is inappropriate and follow the approved external contract in `business-api-proposals.md`.

## Transport and Lifecycle

- Prefer stdio when the harness and employee run on the same machine.
- Use HTTP only when deployment topology requires a process/network boundary.
- Validate required configuration at startup.
- Reuse long-lived runtime resources safely and close them on shutdown.
- Bound list/search outputs with pagination or limits.
- Never log secrets or full sensitive payloads.

## Verification

Start the server and test:

1. initialize and `tools/list`;
2. one read-only local task;
3. one domain rejection with structured error data;
4. write dry-run and explicit execution path when applicable;
5. external-adapter failure through a fake;
6. tool inventory against `docs/employee-plan.md`;
7. runtime import/install without the source repository.
