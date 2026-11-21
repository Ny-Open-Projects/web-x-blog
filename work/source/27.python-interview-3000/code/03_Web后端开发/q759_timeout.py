import asyncio
try:
    from fastapi import FastAPI, HTTPException
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

app = FastAPI()

async def slow_db_query():
    await asyncio.sleep(5)
    return "row"

@app.get("/report")
async def report():
    try:
        row = await asyncio.wait_for(slow_db_query(), timeout=0.1)
    except asyncio.TimeoutError:
        raise HTTPException(504, "上游查询超时")
    return {"row": row}

client = TestClient(app)
print(client.get("/report").status_code)
