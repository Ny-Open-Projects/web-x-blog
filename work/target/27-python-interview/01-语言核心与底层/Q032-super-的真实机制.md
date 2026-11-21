---
title: [Q032] super 的真实机制
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q032 · super 的真实机制

> 难度:★★★ | 标签:继承, MRO

**问**:super 是「调用父类」吗?为什么说这种理解是错的?

**答**:`super()` 返回一个代理对象,沿实例所属类的 MRO 找「当前类的下一个」类,与当前类在继承树里是否是父子无关。多继承协作式初始化必须用 super 链,直接写父类名会导致公共基类被初始化多次或跳过调用。无参 `super()` 是编译器提供的 `super(__class__, first_arg)` 语法糖。

```python
# file: code/01_语言核心与底层/q032_super.py
class Root:
    def ping(self):
        print("Root.ping")

class Left(Root):
    def ping(self):
        print("Left.ping")
        super().ping()     # MRO 上的下一个,可能是兄弟类

class Right(Root):
    def ping(self):
        print("Right.ping")
        super().ping()

class Child(Left, Right):
    def ping(self):
        print("Child.ping")
        super().ping()

if __name__ == "__main__":
    Child().ping()
    # Child -> Left -> Right -> Root,Left 的 super 调到了兄弟 Right
    print(Child.__mro__)

    # 故意演示「直接写父类名」的重复初始化问题
    class Counter:
        instances = 0
        def __init__(self):
            Counter.instances += 1
    class L(Counter):
        def __init__(self):
            Counter.__init__(self)
    class R(Counter):
        def __init__(self):
            Counter.__init__(self)
    class Bad(L, R):
        def __init__(self):
            L.__init__(self)
            R.__init__(self)
    _ = Bad()
    print("Counter initialized:", Counter.instances, "times,应为 1")
```

**追问**:1) super 能在类外调用吗?——可以但要显式传参 `super(Child, obj)`,常见于 Mixin 复用逻辑。2) `super(Child)` 只传一个参数是什么?——未绑定形式,返回类代理只能访问类属性;常规 `super()` 是编译器注入 `super(__class__, 第一个参数)` 的零开销语法糖。3) Mixin 的设计纪律?——无状态、不单独实例化、内部协作一律走 super(),否则多继承组合时初始化链断裂;需要状态时用组合而不是 Mixin。
