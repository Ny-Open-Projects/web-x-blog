try:
    from typing import Annotated
    from fastapi import Depends, FastAPI, Request
    from fastapi.testclient import TestClient
except ImportError:
    print("需要 Python 3.9+ 并 pip install fastapi httpx")
    raise SystemExit(0)

app = FastAPI()

class RequestCtx(dict):
    pass

def get_ctx(request: Request) -> RequestCtx:
    ctx = RequestCtx(path=request.url.path)
    request.state.ctx = ctx
    return ctx

Ctx = Annotated[RequestCtx, Depends(get_ctx)]

def add_user(ctx: Ctx) -> str:
    ctx["user"] = "alice"
    return ctx["user"]

@app.get("/me")
def me(ctx: Ctx, user: Annotated[str, Depends(add_user)]) -> dict:
    return {"path": ctx["path"], "user": user}

client = TestClient(app)
print(client.get("/me").json())
