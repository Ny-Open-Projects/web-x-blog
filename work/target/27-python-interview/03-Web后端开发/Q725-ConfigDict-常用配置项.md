---
title: [Q725] ConfigDict 常用配置项
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q725 · ConfigDict 常用配置项

> 难度:★★★☆ | 标签:Pydantic v2, 配置

**问**:Pydantic v2 的 model_config 你常用哪些配置?分别解决什么问题?

**答**:`extra="forbid"` 拒绝未知字段,对外 API 建议开启,防止拼写错误的字段被静默吞掉;`from_attributes=True` 替代 v1 的 orm_mode,让模型能从 ORM 对象属性构造;`frozen=True` 让实例不可变、可哈希,适合做缓存键;`str_strip_whitespace=True` 自动去字符串空白;`strict=True` 关闭隐式类型转换(str 不再转 int)。这些配置也可用 `@dataclass` 式基类下发到一组模型。

```python
# file: code/03_Web后端开发/q725_config_dict.py
try:
    from pydantic import BaseModel, ConfigDict
except ImportError:
    print("pip install pydantic v2 后再运行")
    raise SystemExit(0)

class Strict(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True, frozen=True)
    name: str

class FromAttr(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    uid: int

class Obj:
    uid = 9

s = Strict(name="  alice ")
print(repr(s.name))
try:
    Strict(name="x", extra_field=1)
except Exception as e:
    print("多余字段被拒:", type(e).__name__)
print(FromAttr.model_validate(Obj()).uid)
```

**追问**:
- extra 的三种取值?——ignore 静默丢弃、forbid 报错、allow 保留到 `__pydantic_extra__`,对外接口选 forbid 最安全。
- 什么时候用 strict?——解析内部可信数据时追求确定性;对接外部输入时保留 lax 转换对用户更友好。
