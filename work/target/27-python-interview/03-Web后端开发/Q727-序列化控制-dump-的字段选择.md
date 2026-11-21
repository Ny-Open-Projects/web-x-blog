---
title: [Q727] 序列化控制:dump 的字段选择
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q727 · 序列化控制:dump 的字段选择

> 难度:★★★☆ | 标签:Pydantic v2, 序列化

**问**:model_dump 的 include/exclude 怎么用?嵌套字段怎么精细控制?

**答**:`exclude={"password"}` 顶层排除,`include={"name", "addr"}` 白名单式输出;嵌套用 dict 指定层级,如 `exclude={"addr": {"zip_code"}}` 只排除子模型的一个字段。`exclude_none`、`exclude_unset`、`exclude_defaults` 是三类常用过滤器,PATCH 场景用 unset,输出瘦身用 none。原则:**敏感字段用专门的输出模型裁剪,而不是到处写 exclude**,否则新增字段容易漏。

```python
# file: code/03_Web后端开发/q727_dump_control.py
try:
    from pydantic import BaseModel
except ImportError:
    print("pip install pydantic v2 后再运行")
    raise SystemExit(0)

class Addr(BaseModel):
    city: str
    zip_code: str

class User(BaseModel):
    name: str
    password: str
    addr: Addr

u = User(name="a", password="secret", addr={"city": "BJ", "zip_code": "100000"})
print(u.model_dump(exclude={"password"}))
print(u.model_dump(include={"name", "addr"}, exclude={"addr": {"zip_code"}}))
print(u.model_dump_json())
```

**追问**:
- include 和 exclude 同时给会怎样?——include 优先圈定范围,exclude 在其基础上再排除,能组合出精细视图。
- 为什么推荐输出模型而不是 exclude?——响应模型在 OpenAPI 里能看到真实结构,exclude 是调用点行为,文档与实际不一致。
