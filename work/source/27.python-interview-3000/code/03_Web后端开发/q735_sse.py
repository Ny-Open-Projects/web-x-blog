import asyncio
try:
    from fastapi import FastAPI
    from fastapi.responses import StreamingResponse
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

app = FastAPI()

async def tick(n: int):
    for i in range(n):
        yield f"event: tick\ndata: {{\"i\": {i}}}\n\n"
        await asyncio.sleep(0.01)
    yield "event: done\ndata: bye\n\n"

@app.get("/events")
def events():
    return StreamingResponse(
        tick(3),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache"},
    )

client = TestClient(app)
with client.stream("GET", "/events") as r:
    body = "".join(r.iter_text())
print(body.strip().replace("\n", " | "))
