---
title: [Q100] Pydantic 模型配置与 ORM 对象转换
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q100 · Pydantic 模型配置与 ORM 对象转换

> 难度:★★☆ | 标签:Pydantic v2, ORM

**问**:如何让 Pydantic 模型直接接收 ORM 对象?`model_config` 有哪些常用配置?

**答**:v2 中设置 `model_config = ConfigDict(from_attributes=True)`(v1 的 `orm_mode`)后,可用 `Model.model_validate(orm_obj)` 从任意带属性的对象(ORM 实例、dataclass)构造模型,`response_model` 也能直接序列化 ORM 查询结果。常用配置还有 `frozen=True` 不可变、`extra='forbid'` 拒绝未知字段、`strict=True` 严格类型、`json_schema_extra` 补充文档示例。

```python
# file: code/03_Web后端开发/q100_from_attributes.py
try:
    from pydantic import BaseModel, ConfigDict
except ImportError:
    print("该题演示需要第三方库 pydantic:pip install pydantic,原理见正文")
    raise SystemExit(0)

class UserORM:
    """模拟一个 ORM 对象"""
    def __init__(self):
        self.id = 1
        self.name = 'alice'
        self.password_hash = 'secret'
        self.created_at = '2026-01-01'

class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True, extra='forbid')
    id: int
    name: str
    created_at: str

user = UserORM()
print(UserOut.model_validate(user))   # password_hash 被过滤
```

**追问**:
- from_attributes 的原理?——v2 从对象属性(而非仅 dict)读取数据,兼容 ORM 实例;等价 v1 的 orm_mode,迁移时直接改配置名。
- extra='forbid' 什么时候开?——对外 API 入参要严格:多传字段直接 422,避免「拼错字段名静默被忽略」;内部模型可保持 ignore。
- strict=True 与默认 lax 模式的差异?——lax 允许 '1'→1 等隐式转换,strict 全部拒绝;对接不可控上游时 lax 省事,内部服务间用 strict 暴露问题。
