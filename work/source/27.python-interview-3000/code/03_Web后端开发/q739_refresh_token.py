import hashlib, hmac, json, time
try:
    from fastapi import FastAPI, HTTPException
    from pydantic import BaseModel
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

SECRET = b"dev-secret"
app = FastAPI()

def sign(payload: dict) -> str:
    body = json.dumps(payload, separators=(",", ":"), sort_keys=True)
    mac = hmac.new(SECRET, body.encode(), hashlib.sha256).hexdigest()
    return f"{body}.{mac}"

def verify(token: str) -> dict:
    body, mac = token.rsplit(".", 1)
    good = hmac.new(SECRET, body.encode(), hashlib.sha256).hexdigest()
    if not hmac.compare_digest(mac, good):
        raise HTTPException(401, "签名无效")
    payload = json.loads(body)
    if payload["exp"] < time.time():
        raise HTTPException(401, "已过期")
    return payload

class Tokens(BaseModel):
    access: str
    refresh: str

@app.post("/login")
def login() -> Tokens:
    now = int(time.time())
    return Tokens(
        access=sign({"sub": "alice", "typ": "access", "exp": now + 60}),
        refresh=sign({"sub": "alice", "typ": "refresh", "exp": now + 86400}),
    )

@app.post("/refresh")
def refresh(refresh_token: str):
    payload = verify(refresh_token)
    if payload["typ"] != "refresh":
        raise HTTPException(401, "需要 refresh token")
    now = int(time.time())
    return {"access": sign({"sub": payload["sub"], "typ": "access", "exp": now + 60})}

client = TestClient(app)
t = client.post("/login").json()
print("access 长度:", len(t["access"]))
r = client.post("/refresh", params={"refresh_token": t["refresh"]}).json()
print("换发的 access 类型:", verify(r["access"])["typ"])
