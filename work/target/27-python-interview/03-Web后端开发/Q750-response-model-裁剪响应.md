---
title: [Q750] response_model 裁剪响应
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q750 · response_model 裁剪响应

> 难度:★★★☆ | 标签:FastAPI, 响应模型

**问**:handler 返回的对象带了密码、内部字段,怎么保证不会漏出去?

**答**:`response_model` 是**出口白名单**:FastAPI 按声明模型重新序列化,未声明的字段直接丢弃,即使 handler 返回了它们;列表接口用 `response_model=list[ItemOut]` 同样生效。它是防敏感泄露的最后一道闸,也是 OpenAPI 文档的输出契约。原则是**设计专用输出模型**,而不是依赖 `response_model_exclude_*` 在调用点打补丁——后者每处都要记得写,漏一处就泄一次。

```python
# file: code/03_Web后端开发/q750_response_model.py
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
```

**追问**:
- response_model 会做类型转换吗?——会,按模型校验并转换,还可能触发 Pydantic 校验错误,输入输出模型要分开定义。
- 想少写一遍模型有捷径吗?——用 `response_model_exclude_unset` 等参数应急,长期还是维护独立的输入/输出模型对。
