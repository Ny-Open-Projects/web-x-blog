---
title: [Q098] FastAPI 请求体与 Pydantic 基础模型
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q098 · FastAPI 请求体与 Pydantic 基础模型

> 难度:★☆☆ | 标签:FastAPI, Pydantic

**问**:如何声明请求体?嵌套 Pydantic 模型如何自动校验与生成文档?

**答**:把 Pydantic `BaseModel` 子类作为参数标注,FastAPI 自动把请求体 JSON 反序列化成模型实例并校验:类型不符、缺少必填字段都会返回 422。模型支持嵌套(字段类型是另一个模型)、默认值、`Optional` 字段,并自动生成 JSON Schema 写入 `/docs`。返回时直接 return 模型或 dict,FastAPI 用 `response_model` 再做一次序列化过滤。

```python
# file: code/03_Web后端开发/q098_request_body.py
try:
    from fastapi import FastAPI
    from pydantic import BaseModel, EmailStr
except ImportError:
    print("该题演示需要第三方库 fastapi:pip install fastapi[all],原理见正文")
    raise SystemExit(0)

app = FastAPI()

class Address(BaseModel):
    city: str
    street: str

class UserIn(BaseModel):
    name: str
    email: EmailStr
    age: int | None = None
    address: Address          # 嵌套模型

class UserOut(BaseModel):     # 响应模型:过滤敏感字段
    name: str
    city: str

@app.post('/users', response_model=UserOut)
def create_user(user: UserIn):
    return {'name': user.name, 'city': user.address.city, 'email': user.email}
```

**追问**:
- response_model 起什么作用?——出口过滤与文档:只序列化声明的字段、隐藏敏感字段(密码哈希)、为 /docs 生成响应 Schema;不声明则按返回类型推断。
- 嵌套模型的级联校验失败怎么定位?——422 的 detail.loc 是路径数组如 `['body','items',2,'price']`,精确定位到第几个元素哪个字段。
- 请求体模型能和路径/查询参数混用吗?——可以,FastAPI 按类型自动归类:标量是查询参数、BaseModel 是请求体,互不干扰。
