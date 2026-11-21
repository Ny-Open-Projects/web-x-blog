---
title: [Q740] 权限依赖工厂 require_scope
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q740 · 权限依赖工厂 require_scope

> 难度:★★★☆ | 标签:FastAPI, 授权, RBAC

**问**:接口很多、权限点很多,怎么避免每个接口手写一遍权限判断?

**答**:写一个**权限依赖工厂**:接收 scope 参数返回依赖闭包,配合 Annotated 定义成语义别名(`ReadItem`、`AdminOnly`),handler 签名里一个类型就完成授权声明。工厂内部只依赖 `current_user`,形成"认证 → 权限"的复用链。权限点命名建议 `资源:动作` 三段式,与 scope/网关限流维度对齐,审计日志直接可用。

```python
# file: code/03_Web后端开发/q740_perm_factory.py
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
```

**追问**:
- 对象级权限(只能改自己的数据)放哪层?——放 `get_object` 类的取数依赖或 service 层,凭据是资源归属字段,不能只靠 scope。
- 权限点怎么跟文档对齐?——用 `Security` 与 SecurityScopes 声明到 OpenAPI,文档里能看到每个接口要求的 scope。
