---
name: mcp-server-engineering
description: Design and implement Model Context Protocol servers with clear tools, schemas, authorization, transport, errors, and evaluation.
---

# Mcp Server Engineering

## Workflow

Clarify the server's resources, prompts, tools, clients, and trust boundaries. Read the current MCP specification and SDK documentation for the selected language and protocol version. Define narrow tools with typed input/output schemas, clear descriptions, bounded scope, and predictable errors. Enforce authorization and validation in server code, not model prompts. Handle cancellation, timeouts, rate limits, and untrusted tool inputs. Avoid arbitrary shell execution or broad file/network access. Test protocol negotiation, tool discovery, invalid arguments, permission denial, and client interoperability.

## Completion checks
- State what was inspected and what remains unknown.
- Keep the work within the user's scope and authorization.
- Preserve existing behavior and project conventions.
- Verify important changes with an observable check.
- Report evidence, caveats, and unverified areas separately.
