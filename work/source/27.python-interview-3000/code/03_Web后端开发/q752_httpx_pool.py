from contextlib import asynccontextmanager
try:
    import httpx
    from fastapi import FastAPI, Request
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with httpx.AsyncClient(
        timeout=2.0, limits=httpx.Limits(max_connections=50)
    ) as client:
        app.state.http = client
        yield

app = FastAPI(lifespan=lifespan)

@app.get("/probe")
async def probe(request: Request):
    return {"has_client": hasattr(request.app.state, "http")}

with TestClient(app) as c:
    print(c.get("/probe").json())
