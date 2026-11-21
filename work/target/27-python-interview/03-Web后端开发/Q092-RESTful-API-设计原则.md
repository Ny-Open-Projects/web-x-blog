---
title: [Q092] RESTful API 设计原则
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q092 · RESTful API 设计原则

> 难度:★★☆ | 标签:REST, API 设计

**问**:什么是 REST?设计 RESTful API 有哪些核心原则?

**答**:REST 是以"资源"为中心的架构风格,核心原则:1) URL 表示资源,用名词复数而非动词,如 `GET /users/42`;2) HTTP 方法表达操作语义,GET/POST/PUT/DELETE 对应查/增/改/删;3) 无状态,每个请求携带全部认证与上下文信息;4) 正确使用状态码表达结果;5) 过滤、分页、排序用查询参数表达,如 `?page=2&size=20&sort=-created_at`。反例:`GET /getUser?id=1`、`POST /deleteUser`。

```python
# file: code/03_Web后端开发/q092_rest_design.py
try:
    from fastapi import FastAPI, HTTPException
except ImportError:
    print("该题演示需要第三方库 fastapi:pip install fastapi[all],原理见正文")
    raise SystemExit(0)

app = FastAPI()
users: dict[int, dict] = {}

@app.get('/users')                       # 列表:GET /users?page=1&size=10
def list_users(page: int = 1, size: int = 10):
    ids = sorted(users)[(page - 1) * size: page * size]
    return {'total': len(users), 'items': [users[i] for i in ids]}

@app.get('/users/{user_id}')             # 详情:GET /users/1
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(404, 'user not found')
    return users[user_id]

@app.post('/users', status_code=201)     # 创建:POST /users
def create_user(user: dict):
    uid = max(users or {0: 0}) + 1
    users[uid] = {'id': uid, **user}
    return users[uid]

@app.delete('/users/{user_id}', status_code=204)  # 删除:DELETE /users/1
def delete_user(user_id: int):
    users.pop(user_id, None)
```

**追问**:
- 「无状态」对横向扩容意味着什么?——任一实例可处理任一请求,会话必须外置(Redis/JWT);把状态藏在本地内存的接口无法水平扩展。
- 动作类业务怎么 REST 化?——把动作建模为资源子集合,如 `POST /orders/42/cancellation`,而不是 `/cancelOrder?id=42`。
- 过滤排序参数如何防注入?——白名单校验字段名(映射到列),值走参数化查询;`?sort=` 直接拼 SQL 是注入高发点。
