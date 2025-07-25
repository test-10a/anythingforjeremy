#!/usr/bin/env python3
"""
Remote Zephyr Optimizer MCP server – FastAPI‑MCP 0.3.x
"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi_mcp import FastApiMCP

app = FastAPI()

# ── Your “tool” becomes a normal POST route ───────────────────────────────
@app.post(
    "/optimize_accounts",              # URL path (won’t be hit directly by users)
    operation_id="optimize_accounts",  # MCP tool name (must be globally unique)
    summary="Collect host telemetry and return success marker",
)
async def optimize_accounts() -> JSONResponse:
    """
    Minimal smoke‑test tool.
    """
    return JSONResponse(content="Zephyr optimizer completed successfully.")

# ── Expose every FastAPI route as an MCP tool at /mcp ─────────────────────
mcp = FastApiMCP(app, path="/")  # zero‑config
mcp.mount()            # mounts at /mcp; stateless by default
