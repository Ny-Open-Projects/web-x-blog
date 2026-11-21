try:
    from fastapi import FastAPI
    from fastapi.testclient import TestClient
    from pydantic import BaseModel
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

class UserOut(BaseModel):
    id: int
    name: str

app = FastAPI()

@app.get("/users/{uid}", response_model=UserOut)
def get_user(uid: int):
    # 即使内部对象带敏感字段, 出口只保留声明字段
    return {"id": uid, "name": "alice", "password": "should-not-leak", "token": "x"}

client = TestClient(app)
print(client.get("/users/1").json())
