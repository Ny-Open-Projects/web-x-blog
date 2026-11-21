try:
    from fastapi import APIRouter, FastAPI
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

app = FastAPI()
users = APIRouter(prefix="/users", tags=["用户"])
items = APIRouter(prefix="/items", tags=["商品"])

@users.get("/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

@items.get("")
def list_items():
    return {"items": []}

@items.get("/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}

app.include_router(users, prefix="/api/v1")
app.include_router(items, prefix="/api/v1")

client = TestClient(app)
print(client.get("/api/v1/users/7").json())
print(client.get("/api/v1/items").json())
