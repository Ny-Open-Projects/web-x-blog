---
title: [Q726] TypeAdapter 与 RootModel 非模型校验
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q726 · TypeAdapter 与 RootModel 非模型校验

> 难度:★★★☆ | 标签:Pydantic v2

**问**:校验目标不是 BaseModel 而是裸类型,比如 dict[str, int]、list[str],Pydantic v2 怎么做?

**答**:`TypeAdapter(类型)` 可以校验/序列化**任意类型注解**,不需要包一层模型,适合校验配置片段、消息队列 payload、缓存 JSON。顶层就是 list 或 dict 时,业务上又想定义成"模型"获得文档能力,用 `RootModel[...]` 包住根类型,数据放在 `.root` 属性。两者都享受同一套 ValidationError 与性能优化。

```python
# file: code/03_Web后端开发/q726_type_adapter.py
try:
    from pydantic import RootModel, TypeAdapter, ValidationError
except ImportError:
    print("pip install pydantic v2 后再运行")
    raise SystemExit(0)

adapter = TypeAdapter(dict[str, int])
print(adapter.validate_python({"a": "1"}))
print(adapter.dump_python({"b": 2}))

class Tags(RootModel[list[str]]):
    pass

print(Tags.model_validate(["x", "y"]).root)
try:
    TypeAdapter(list[int]).validate_python(["1", "a"])
except ValidationError as e:
    print("错误条数:", e.error_count())
```

**追问**:
- TypeAdapter 应该每次创建吗?——不要,它是带编译开销的对象,模块级创建一次复用。
- RootModel 的场景举例?——顶层 JSON 数组接口、包装第三方返回值,同时想给它加校验器和文档描述。
