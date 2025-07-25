#!/usr/bin/env python3
"""
Minimal JSON-RPC handler for Zephyr optimizer — works on Vercel
"""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/mcp")  # <- endpoint Vercel will rewrite to
async def handle_rpc(request: Request) -> JSONResponse:
    try:
        body = await request.json()
        method = body.get("method")
        rpc_id = body.get("id", None)

        if method == "optimize_accounts":
            result = "Zephyr optimizer completed successfully."
            return JSONResponse(content={"jsonrpc": "2.0", "id": rpc_id, "result": result})

        return JSONResponse(
            content={"jsonrpc": "2.0", "id": rpc_id, "error": {"code": -32601, "message": "Method not found"}},
            status_code=400,
        )
    except Exception as e:
        return JSONResponse(
            content={"jsonrpc": "2.0", "id": None, "error": {"code": -32603, "message": str(e)}},
            status_code=500,
        )
