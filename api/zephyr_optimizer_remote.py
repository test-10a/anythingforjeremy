from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/mcp")
async def handle_rpc(request: Request) -> JSONResponse:
    body = await request.json()
    method = body.get("method")
    rpc_id = body.get("id", None)

    if method == "optimize_accounts":
        return JSONResponse(content={"jsonrpc": "2.0", "id": rpc_id, "result": "Zephyr optimizer completed successfully."})

    return JSONResponse(content={
        "jsonrpc": "2.0",
        "id": rpc_id,
        "error": {"code": -32601, "message": "Method not found"}
    }, status_code=404)
