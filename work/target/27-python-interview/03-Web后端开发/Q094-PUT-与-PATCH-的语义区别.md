---
title: [Q094] PUT 与 PATCH 的语义区别
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q094 · PUT 与 PATCH 的语义区别

> 难度:★☆☆ | 标签:HTTP, REST

**问**:更新资源用 PUT 还是 PATCH?各自的语义和幂等性如何?

**答**:PUT 是全量替换:客户端提交完整资源表示,未提供的字段视为清空/恢复默认,天然幂等;PATCH 是部分更新:只提交要修改的字段,重复提交结果一致时也可幂等(取决于实现),但语义上不保证。实践上 JSON API 常用 PATCH 做部分更新、PUT 做整体替换,FastAPI 里 PATCH 通常配合 `exclude_unset=True` 只更新显式传入的字段。

```python
# file: code/03_Web后端开发/q094_put_patch.py
try:
    from fastapi import FastAPI
    from pydantic import BaseModel
except ImportError:
    print("该题演示需要第三方库 fastapi:pip install fastapi[all],原理见正文")
    raise SystemExit(0)

app = FastAPI()
db = {1: {'name': 'alice', 'email': 'a@x.com', 'age': 20}}

class UserIn(BaseModel):
    name: str | None = None
    email: str | None = None
    age: int | None = None

@app.put('/users/{uid}')            # 全量替换:未传字段被置为 None
def replace_user(uid: int, body: UserIn):
    db[uid] = {'name': body.name, 'email': body.email, 'age': body.age}
    return db[uid]

@app.patch('/users/{uid}')          # 部分更新:只改传入的字段
def patch_user(uid: int, body: UserIn):
    patch = body.model_dump(exclude_unset=True)
    db[uid].update(patch)
    return db[uid]
```

**追问**:
- PATCH 什么情况下不幂等?——提交 `{"balance": balance+100}` 这类相对变更时重复执行会累加;绝对值更新才可幂等。
- JSON Merge Patch 与 JSON Patch 的区别?——RFC 7386 用 null 表示删除、只支持替换;RFC 6902 用 op 指令数组支持 add/remove/move,表达力强但复杂。
- FastAPI 里怎么只更新传入字段?——`Model(**request.model_dump(exclude_unset=True), exclude_unset=True)` 配合 PATCH,未传字段保持原值。
