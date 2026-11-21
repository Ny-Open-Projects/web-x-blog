---
title: [Q1273] dataclass 的 slots=True 与 kw_only:3.10 的进化
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1273 · dataclass 的 slots=True 与 kw_only:3.10 的进化

> 难度:★★★☆☆ | 标签:dataclass, __slots__

**问**:dataclass 一直被批评「每个实例带个 __dict__」,3.10 怎么解决的?kw_only 解决什么坑?

**答**:3.10 给 @dataclass 加了 `slots=True`:生成类时自动加 `__slots__` 并重新构建类,实例不再有 `__dict__`,内存与属性访问向手工 slots 类看齐(Q008/Q423),代价依旧是「不能随意加属性、多继承冲突」。`kw_only=True` 把字段全部变成仅关键字,根治「同类型连续字段传错位」的经典 bug——比如 Point(x, y) 传反;也可用 `field(kw_only=True)` 只标记个别字段。两者可以组合,3.10+ 的冻结配置类推荐 `@dataclass(frozen=True, slots=True, kw_only=True)`。3.9 的等价做法是手写 `__slots__` 并放弃 dataclass 自动生成(或用 attrs 库)。注意 slots=True 与「类体中给字段赋默认值时 slots 冲突」的老坑由 dataclass 内部处理,但与继承非 slots 基类仍会带出 __dict__。

```python
# file: code/01_语言核心与底层/q1273_dataclass_slots.py
from __future__ import annotations

import sys
from dataclasses import dataclass


@dataclass
class V1:
    x: int
    y: int = 0


if __name__ == "__main__":
    print("python:", sys.version.split()[0])
    v = V1(3)
    print("basic:", v, "| has __dict__:", hasattr(v, "__dict__"))
    if sys.version_info >= (3, 10):
        @dataclass(slots=True, kw_only=True)
        class V2:
            x: int
            y: int = 0

        w = V2(x=3)                     # 全部字段必须按关键字
        print("slots instance has __dict__:", hasattr(w, "__dict__"))
        try:
            V2(3)
        except TypeError as e:
            print("positional rejected:", e)
    else:
        print("slots=True 与 kw_only 是 3.10 引入的 dataclass 参数")
```

**追问**:1) slots=True 的类还能 pickle 吗?——能,但与「定义时动态生成类」的组合要小心 __getstate__;slots 类默认没有 __dict__,pickle 协议会用 (None, slots 元组) 形态,3.11 起行为更稳。2) slots=True 的收益与代价?——省 __dict__ 内存、属性访问略快;代价:动态属性禁用、与 cached_property/weakref 默认机制冲突、多继承布局约束(Q559)。3) kw_only 解决什么?——位置参数膨胀后新增字段会错位;kw_only 字段可任意顺序添加,构造只能按名传参——API 演进安全。4) 生产陷阱?——slots 类与现有 Mixin 布局冲突;加 kw_only 后旧调用方的位置实参直接报错,要版本化迁移;slots + 动态加属性 AttributeError。
