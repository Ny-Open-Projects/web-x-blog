---
title: [Q723] computed_field 计算字段
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q723 · computed_field 计算字段

> 难度:★★☆☆ | 标签:Pydantic v2, 序列化

**问**:模型里想暴露一个"由其他字段算出来"的字段,比如面积、全名,不想存库也不想每次手动拼,怎么做?

**答**:用 `@computed_field` 装饰 property:它参与**序列化与 JSON Schema**,`model_dump`、`model_dump_json`、OpenAPI 文档都会带上;普通 `@property` 只在 Python 侧可访问,不进序列化结果。computed_field 还可以配 alias 控制输出名,并会被响应模型裁剪逻辑一并处理。注意计算逻辑要幂等、便宜,别在里面做 IO。

```python
# file: code/03_Web后端开发/q723_computed_field.py
try:
    from pydantic import BaseModel, computed_field
except ImportError:
    print("pip install pydantic v2 后再运行")
    raise SystemExit(0)

class Rect(BaseModel):
    w: float
    h: float

    @property
    def area(self) -> float:        # 普通 property 不进序列化
        return self.w * self.h

    @computed_field(alias="area2x")
    @property
    def area2x(self) -> float:      # 计算字段进序列化
        return self.area * 2

r = Rect(w=3, h=4)
print(r.area)
print(r.model_dump())
```

**追问**:
- computed_field 能被 include/exclude 控制吗?——能,和普通字段一样参与 exclude/include 字段选择。
- 计算成本高怎么办?——加缓存 property(functools.cached_property 需确认与模型可变性兼容),或把计算下推到查询层。
