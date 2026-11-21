from dataclasses import dataclass
try:
    from fastapi import Depends, FastAPI
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

@dataclass
class UserRepo:                     # 只管存取
    storage: dict

    def get(self, uid: int):
        return self.storage.get(uid)

@dataclass
class UserService:                  # 只管业务
    repo: UserRepo

    def profile(self, uid: int) -> dict:
        user = self.repo.get(uid)
        if not user:
            return {"id": uid, "name": "guest"}
        return {"id": uid, "name": user["name"]}

_storage = {1: {"name": "alice"}}

def get_service() -> UserService:   # 组合根
    return UserService(repo=UserRepo(storage=_storage))

app = FastAPI()

@app.get("/users/{uid}")
def get_user(uid: int, svc: UserService = Depends(get_service)):
    return svc.profile(uid)

client = TestClient(app)
print(client.get("/users/1").json())
print(client.get("/users/2").json())
