#!/usr/bin/env python3
from fastapi import FastAPI
from fastapi_mcp import FastApiMCP

app = FastAPI()

mcp = FastApiMCP(app)    

@mcp.tool()
async def optimize_accounts() -> str:
    return "Zephyr optimizer completed successfully."

mcp.mount()                # don’t pass path/stateless here
