---
title: [Q739] Refresh token 双令牌机制
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q739 · Refresh token 双令牌机制

> 难度:★★★★ | 标签:FastAPI, JWT, 认证

**问**:access token 过期太快体验差,太慢又不安全,refresh token 机制怎么设计?

**答**:双令牌分工:**access token 短命**(5-15 分钟)随每个请求携带、无状态校验;**refresh token 长命**(天级)只在刷新端点出现,服务端存储(哈希后入库/Redis)以便吊销。三个关键设计:refresh **轮换**(一次一用,旧 token 第二次使用判定泄露,吊销整个家族)、**绑定上下文**(设备指纹/IP 变化要求重新登录)、access 无法主动失效所以敏感操作仍要查会话。签名校验用 `hmac.compare_digest` 这类恒时比较。

```python
# file: code/03_Web后端开发/q739_refresh_token.py
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
```

**追问**:
- refresh token 被盗怎么办?——轮换机制下旧 token 再次使用即触发泄露判定,可吊销整个令牌家族并要求重新登录。
- 为什么 access 不落库?——无状态省一次存储查询,代价是无法即时吊销,靠短过期和黑名单兜底。
