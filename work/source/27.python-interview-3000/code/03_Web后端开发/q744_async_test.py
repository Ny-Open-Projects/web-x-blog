import asyncio
try:
    import httpx
    from fastapi import FastAPI
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

app = FastAPI()

@app.get("/async-hi")
async def hi():
    return {"hi": True}

async def main():
    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as c:
        r = await c.get("/async-hi")
        print(r.status_code, r.json())

asyncio.run(main())
