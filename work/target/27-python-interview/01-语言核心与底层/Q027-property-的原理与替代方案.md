---
title: [Q027] property 的原理与替代方案
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q027 · property 的原理与替代方案

> 难度:★★☆ | 标签:property, 描述符

**问**:为什么 Python 社区建议先写公开属性、需要时再改 property?

**答**:property 让「属性访问」在 API 不变的前提下切换为计算或校验逻辑,因此起步时无需防御性地写 getter/setter。原理上 `property(fget, fset, fdel, doc)` 是 data descriptor;`@x.setter`、`@x.deleter` 是在已有 property 上链式注册钩子。计算成本高或可能失败的操作更适合方法而非 property,避免「看起来便宜实则昂贵」的误导。

```python
# file: code/01_语言核心与底层/q027_property.py
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("radius must be non-negative")
        self._radius = value

    @property
    def area(self):
        import math
        return math.pi * self._radius ** 2   # 只读派生属性

if __name__ == "__main__":
    c = Circle(1)
    print(round(c.area, 4))
    c.radius = 2
    print(round(c.area, 4))
    try:
        c.radius = -1
    except ValueError as e:
        print("rejected:", e)
```

**追问**:1) property 能被实例属性覆盖吗?——不能,data descriptor 优先于实例 `__dict__`,这正是它能实施不变量的原因。2) property 的 setter 里写 `self.x = value` 会怎样?——再次触发同一 property 的 setter,无限递归 RecursionError;setter 内必须写 `self._x` 这类真实存储名。3) 把昂贵计算写成 property 有什么工程问题?——调用方误以为是廉价访问而不缓存结果,profiling 时也难定位;昂贵或可能失败的计算用方法,纯派生且高频的用 `functools.cached_property`。
