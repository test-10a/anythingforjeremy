#!/usr/bin/env python3
"""
Remote Zephyr Optimizer MCP tool – FastAPI‑MCP edition
"""

from fastapi import FastAPI
from fastapi_mcp import FastApiMCP      # provided by fastapi‑mcp 0.3.7+

app = FastAPI()

mcp = FastApiMCP(app)                  # create the MCP wrapper
mcp.mount(path="/mcp", stateless=True) # expose it for Vercel’s stateless runtime

@mcp.tool()
async def optimize_accounts() -> str:
    """Basic smoke test."""
    return "Zephyr optimizer completed successfully."
