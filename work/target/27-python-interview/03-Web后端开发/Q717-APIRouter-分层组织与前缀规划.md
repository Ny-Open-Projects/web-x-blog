---
title: [Q717] APIRouter 分层组织与前缀规划
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q717 · APIRouter 分层组织与前缀规划

> 难度:★★☆☆ | 标签:FastAPI, 路由组织

**问**:项目变大后路由怎么组织?prefix 和 tags 应该按什么维度切?

**答**:按**业务域**拆 router(用户、订单、商品),每个 router 自己带 `prefix` 与 `tags`,主应用只做 `include_router` 组装,版本号放在 include 时统一拼(`prefix="/api/v1"`)。prefix 必须以 `/` 开头、不能以 `/` 结尾;同一个业务域内"列表"和"详情"用 `""` 与 `"/{id}"` 区分,避免尾斜杠重定向。tags 对应 OpenAPI 分组,是文档可读性的关键。

```python
# file: code/03_Web后端开发/q717_router_org.py
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
```

**追问**:
- 请求 `/api/v1/items/` 多了尾斜杠会怎样?——Starlette 默认 `redirect_slashes` 会 307 重定向到无斜杠路径,规范上应统一路径并测试这条。
- prefix 拼接发生在什么时候?——include_router 时拼接,子 router 内部只关心自己的相对路径,便于复用与测试。
