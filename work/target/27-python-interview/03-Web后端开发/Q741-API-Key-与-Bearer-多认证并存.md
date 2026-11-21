---
title: [Q741] API Key 与 Bearer 多认证并存
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q741 · API Key 与 Bearer 多认证并存

> 难度:★★★☆ | 标签:FastAPI, 认证

**问**:同一套 API 既给人用(JWT)又给内部服务用(API Key),认证层怎么组织?

**答**:定义多个 Security scheme(APIKeyHeader、OAuth2PasswordBearer),都设 `auto_error=False` 让它们"尝试但不强拒",再用一个聚合依赖做**或逻辑**:命中任一方案就构造统一 principal(如 `user:alice`、`service:pay-service`),全未命中才 401。principal 统一成字符串或数据类后,下游权限逻辑不关心凭证来自哪种方案。多方案并存的审计点:在日志里记录认证方式,便于区分人为误用与服务间调用。

```python
# file: code/03_Web后端开发/q741_multi_auth.py
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
```

**追问**:
- 为什么 auto_error 要设 False?——默认 True 时缺 header 直接 403,轮不到聚合依赖做"尝试多种方案"的或逻辑。
- API Key 相比 JWT 的取舍?——Key 简单、可即时吊销但每次要查存储;JWT 无状态但难吊销,服务间低频调用 Key 更合适。
