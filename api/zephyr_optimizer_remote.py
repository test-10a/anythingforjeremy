#!/usr/bin/env python3
"""
Remote Zephyr Optimizer MCP server – FastAPI‑MCP 0.3.x
"""

from fastapi import FastAPI
from fastapi_mcp import FastApiMCP

app = FastAPI()

# ── Define one regular FastAPI route.
#    `operation_id` becomes the MCP method name.
@app.post("/optimize_accounts", operation_id="optimize_accounts")
async def optimize_accounts():
    return "Zephyr optimizer completed successfully."

# ── Turn every FastAPI route into an MCP tool.
mcp = FastApiMCP(app)   # zero‑configuration
mcp.mount()             # adds POST /mcp  (no trailing slash)
