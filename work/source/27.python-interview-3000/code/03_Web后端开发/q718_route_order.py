try:
    from fastapi import APIRouter, FastAPI
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

app = FastAPI()

@app.get("/users/me")          # 必须先注册字面量
def me():
    return {"who": "me"}

@app.get("/users/{user_id}")   # 再注册参数路由
def user(user_id: int):
    return {"user_id": user_id}

client = TestClient(app)
print(client.get("/users/me").json())
print(client.get("/users/42").json())
print(client.get("/users/abc").status_code)  # 参数路由 422, 不会回落到字面量
