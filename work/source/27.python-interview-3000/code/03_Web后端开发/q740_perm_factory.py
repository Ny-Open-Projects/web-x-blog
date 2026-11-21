try:
    from typing import Annotated
    from fastapi import Depends, FastAPI, HTTPException
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

app = FastAPI()
CURRENT = {"username": "alice", "scopes": {"item:read"}}

def current_user() -> dict:
    return CURRENT

def require_scope(scope: str):
    def dep(user: Annotated[dict, Depends(current_user)]) -> dict:
        if scope not in user["scopes"]:
            raise HTTPException(403, f"缺少权限 {scope}")
        return user
    return dep

ReadItem = Annotated[dict, Depends(require_scope("item:read"))]
AdminOnly = Annotated[dict, Depends(require_scope("admin"))]

@app.get("/items")
def list_items(user: ReadItem):
    return {"by": user["username"]}

@app.post("/items")
def create_item(user: AdminOnly):
    return {"created_by": user["username"]}

client = TestClient(app)
print(client.get("/items").json())
print(client.post("/items").status_code)
