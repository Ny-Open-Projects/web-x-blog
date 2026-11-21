---
title: [Q101] Pydantic 嵌套模型与复杂校验场景
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q101 · Pydantic 嵌套模型与复杂校验场景

> 难度:★★★ | 标签:Pydantic v2, 复杂校验

**问**:如何校验"列表内至少一项"或"字段间互斥"这类复杂规则?如何对敏感字段做脱敏?

**答**:跨字段规则用 `@model_validator(mode='after')`,集合元素校验用 `Field(min_length=...)` 限定列表长度或 `field_validator` 逐项检查;脱敏用 `@field_serializer` 控制序列化输出,或定义单独的 In/Out 模型对。也可以用 `Annotated` + `Before/After` 模式控制校验时机:Before 在类型转换前处理原始输入。

```python
# file: code/03_Web后端开发/q101_complex_validate.py
try:
    from pydantic import BaseModel, field_validator, model_validator
except ImportError:
    print("该题演示需要第三方库 pydantic:pip install pydantic,原理见正文")
    raise SystemExit(0)

class BatchDeleteIn(BaseModel):
    ids: list[int]

    @field_validator('ids')
    @classmethod
    def no_empty(cls, v: list[int]) -> list[int]:
        if not v:
            raise ValueError('ids 不能为空')
        if len(v) != len(set(v)):
            raise ValueError('ids 存在重复')
        return v

class NotifyIn(BaseModel):
    email: str | None = None
    phone: str | None = None

    @model_validator(mode='after')
    def exclusive_channel(self):
        if bool(self.email) == bool(self.phone):
            raise ValueError('email 与 phone 必须二选一')
        return self

print(BatchDeleteIn(ids=[1, 2]).model_dump())
print(NotifyIn(phone='13800000000').model_dump())
```

**追问**:
- 跨字段校验抛什么异常?——`ValidationError` 由 model_validator 内 raise ValueError 即可,FastAPI 统一转 422,不要自己返回 Response。
- 同一字段多处校验的执行顺序?——Field 约束 → field_validator(before→after) → model_validator;理解顺序才能定位「为什么我的校验没生效」。
- 序列化脱敏怎么做?——`@field_serializer` 按需遮蔽(手机号打码),或按角色定义不同 Out 模型;在序列化层做,别污染存储层。
