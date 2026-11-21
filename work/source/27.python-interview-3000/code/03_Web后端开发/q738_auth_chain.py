try:
    from fastapi import Depends, FastAPI, HTTPException, status
    from fastapi.security import OAuth2PasswordBearer
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

app = FastAPI()
oauth2 = OAuth2PasswordBearer(tokenUrl="/login")
FAKE = {"token1": {"username": "alice", "role": "admin"},
        "token2": {"username": "bob", "role": "user"}}

async def get_current_user(token: str = Depends(oauth2)) -> dict:
    user = FAKE.get(token)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            headers={"WWW-Authenticate": "Bearer"})
    return user

async def require_admin(user: dict = Depends(get_current_user)) -> dict:
    if user["role"] != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    return user

@app.get("/me")
def me(user: dict = Depends(get_current_user)):
    return user

@app.delete("/items/{iid}")
def del_item(iid: int, user: dict = Depends(require_admin)):
    return {"deleted": iid, "by": user["username"]}

client = TestClient(app)
print(client.get("/me", headers={"Authorization": "Bearer token1"}).json())
print(client.get("/me").status_code)                                  # 401
print(client.delete("/items/1", headers={"Authorization": "Bearer token2"}).status_code)  # 403
