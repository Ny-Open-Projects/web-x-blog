---
title: "[Q5202] __slots__ 的继承陷阱：子类不加 slots 等于白省"
date: 2026-11-24
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5202 · __slots__ 的继承陷阱：子类不加 slots 等于白省

难度：P6 ｜ 标签：__slots__、继承、内存布局、`__dict__`、多继承冲突

**问**：基类写了 `__slots__ = ("x", "y")`，实例确实没有 `__dict__` 了；但业务子类只是 `class Order(Base): pass`，一压测内存又回到优化前。为什么子类会把 `__dict__`"带回来"？`__slots__` 在继承链上到底怎么布局？多继承时为什么直接 `TypeError`？

**答**：
结论：`__slots__` 是**按类**声明实例属性存储的，不自动继承"禁止 dict"这个效果。子类如果没有自己的 `__slots__`，`type.__new__` 会为它补上 `__dict__` 和 `__weakref__` 两个槽，于是实例既能走基类槽、又能动态挂属性，内存优势全部消失。子类要延续优化，必须显式写 `__slots__ = ()`（不加新字段）或 `__slots__ = ("z",)`（加字段）；新槽只加在子类布局尾部，基类槽的偏移不变。

取舍：a) 继承链每一层都要写 `__slots__`，漏一层就前功尽弃；b) 子类不要重复声明父类已有的槽名，重复声明不会报错但会浪费空间、并让属性解析出现两套 descriptor；c) 多继承时只要两个基类都有**非空** `__slots__`，布局冲突直接 `TypeError: multiple bases have instance lay-out conflict`，这不是 bug 而是 CPython 的对象布局限制，解决方式是抽一个"纯接口/空 slots"的 mixin；d) `__slots__` 换来的代价是没有 `__dict__`（不能动态加属性）、默认不可弱引用（要手动加 `__weakref__` 槽）、`pickle` 与某些 ORM 需要额外适配。

实战：事故形态是"为省内存把 200 万条的行情快照类改成 slots，单测通过、线上内存没降——因为真正的实例是子类 `TickSnapshot`，它没写 slots，每个实例仍带一个空 dict（约 64 字节起步）"。下面用 `tracemalloc` 实测三层继承的每实例摊销，并演示多继承冲突。

```python
import sys
import tracemalloc


class Base:
    __slots__ = ("x", "y")

    def __init__(self):
        self.x = 1
        self.y = 2


class WithDict(Base):          # 没写 __slots__：重新获得 __dict__
    pass


class Slotted(Base):
    __slots__ = ("z",)

    def __init__(self):
        super().__init__()
        self.z = 3


def per_instance(cls, n=10000):
    tracemalloc.start()
    objs = [cls() for _ in range(n)]
    current, _ = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return current / n


print("[1] 子类是否带 __dict__:",
      hasattr(WithDict(), "__dict__"), hasattr(Slotted(), "__dict__"))
print("[2] 单实例 sizeof:", sys.getsizeof(Base()),
      sys.getsizeof(WithDict()), sys.getsizeof(Slotted()))
print("[3] 每实例摊销字节:", round(per_instance(Base)),
      round(per_instance(WithDict)), round(per_instance(Slotted)))

try:
    class A:
        __slots__ = ("a", "b")

    class B:
        __slots__ = ("b", "c")

    class C(A, B):
        pass
except TypeError as e:
    print("[4] 多继承 slots 冲突:", e)

class EmptyMixin:
    __slots__ = ()

class D(A, EmptyMixin):        # 空 slots 的 mixin 不参与布局冲突
    __slots__ = ()

print("[5] 空 slots mixin 可组合:", D().a if hasattr(D(), "a") else "未赋值")
```

**追问一**：为什么加了 `__slots__` 反而更慢？—— 槽访问走的是类上的 member descriptor，理论上是偏移直取，应该更快；但一旦涉及 `getattr` 动态名、`hasattr` 探测、`vars()`、序列化框架反射，slots 类没有 `__dict__`，框架会退化成异常探测或 `getattr` 循环，整体反而慢。另外每个槽 descriptor 常驻类对象，类多、实例少时内存账要反着算。

**追问二**：`__slots__` 里的名字和类变量同名会怎样？—— 类体里同时写 `x = 1` 和 `__slots__ = ("x",)` 会直接 `ValueError: 'x' in __slots__ conflicts with class variable`，因为槽要在类上创建同名 descriptor。需要默认值时用 `__init__` 赋值，或把默认值放到父类方法/`__new__` 里；dataclass 的 `field(default=...)` 与 `slots=True` 会由 dataclass 机制处理，不要手写混用。

## 背诵要点
- `__slots__` 不继承"禁止 dict"；继承链每层都要显式声明，子类漏写就重新获得 `__dict__`。
- 两个非空 slots 基类多继承会 `TypeError`；用空 slots mixin 组合。
- 代价：不能动态加属性、默认不可弱引用、与反射/序列化框架需适配。

## 复盘追问
- 200 万实例改成 slots 后内存没降，最可能漏了哪一层？（子类没写 `__slots__`）
- slots 类为什么有时比普通类更慢？（动态属性探测、反射退化、descriptor 常驻）
