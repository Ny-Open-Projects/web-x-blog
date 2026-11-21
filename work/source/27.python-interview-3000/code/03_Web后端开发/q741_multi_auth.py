try:
    from fastapi import Depends, FastAPI, HTTPException, Security
    from fastapi.security import APIKeyHeader, OAuth2PasswordBearer
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

app = FastAPI()
api_key_scheme = APIKeyHeader(name="X-API-Key", auto_error=False)
bearer_scheme = OAuth2PasswordBearer(tokenUrl="/login", auto_error=False)
KEYS = {"svc-123": "service-a"}

def any_auth(api_key: str | None = Security(api_key_scheme),
             token: str | None = Security(bearer_scheme)) -> str:
    if api_key and api_key in KEYS:
        return f"service:{KEYS[api_key]}"
    if token == "user-token":
        return "user:alice"
    raise HTTPException(401, "缺少有效凭证")

@app.get("/who")
def who(principal: str = Depends(any_auth)):
    return {"principal": principal}

client = TestClient(app)
print(client.get("/who", headers={"X-API-Key": "svc-123"}).json())
print(client.get("/who", headers={"Authorization": "Bearer user-token"}).json())
print(client.get("/who").status_code)
