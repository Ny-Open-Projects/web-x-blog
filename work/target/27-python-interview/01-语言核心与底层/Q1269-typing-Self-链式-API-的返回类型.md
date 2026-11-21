---
title: [Q1269] typing.Self:链式 API 的返回类型怎么标
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1269 · typing.Self:链式 API 的返回类型怎么标

> 难度:★★★☆☆ | 标签:typing, Self, API 设计

**问**:`Circle().move(3).scale(2)` 链式调用,返回类型怎么注解才不是每次退回基类?子类继承后还能拿到 Circle 吗?

**答**:老写法 `-> "Shape"` 会在链式调用时把类型丢回基类,后续子类专有方法在静态检查器眼里不存在。两条正路:3.11+ 直接 `from typing import Self`,方法注解 `def move(self, dx) -> Self`,含义是「返回与 self 同一个运行时类型」;更早版本用 F-bound 技巧 `T = TypeVar("T", bound="Shape")`,方法签名 `def move(self: T, dx) -> T`。两者对「返回 self 的方法、返回新实例但同类的方法」都成立,也是构建 Builder/流式 API 的标准答案。注意区分:返回 `type(self)(...)` 新实例的场景同样用 Self;而 `__new__`/classmethod 场景用 `-> Self` 也比 `-> "Cls"` 准确。

```python
# file: code/01_语言核心与底层/q1269_self_type.py
from __future__ import annotations

from typing import TypeVar

T = TypeVar("T", bound="Shape")       # 3.11+ 可直接 from typing import Self


class Shape:
    def move(self: T, dx: float) -> T:
        self.x = getattr(self, "x", 0.0) + dx
        return self

    def scale(self: T, k: float) -> T:
        self.k = getattr(self, "k", 1.0) * k
        return self


class Circle(Shape):
    pass


if __name__ == "__main__":
    c = Circle().move(3).scale(2)     # 静态检查器知道整条链都是 Circle
    print(type(c).__name__, c.x, c.k)
    s = Shape().move(1)
    print(type(s).__name__, s.x)
```

**追问**:1) Self 与 TypeVar bound 写法的差别?——语义等价,Self 更短且不会泄漏类型变量到类作用域;bound 写法在 3.10- 是唯一选择,迁移时直接替换注解即可。2) Self 的语义边界?——代表「当前类的实例类型」:实例方法返回 self 链、classmethod 返回 cls 实例;子类调用时自动收窄成子类类型——这是链式 builder 的正解。3) 底层机制?——PEP 673 在 3.11 落地 typing.Self;3.10- 用 TypeVar("TSelf", bound="...") 模拟;静态检查器把 Self 解析到「定义所在类的当前绑定」。4) 生产陷阱?——链式 API 注解成基类或 None,子类调用方类型崩;把 Self 用在模块级函数(语义是「这个函数的返回类型」没意义);3.10- 模拟写法在继承深了以后解不开。
