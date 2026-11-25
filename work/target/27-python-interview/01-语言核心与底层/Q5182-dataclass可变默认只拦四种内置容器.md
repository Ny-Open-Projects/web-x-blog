---
title: "[Q5182] dataclass 只拦四种内置可变默认：自定义对象静默共享"
date: 2026-11-23
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5182 · dataclass 只拦四种内置可变默认：自定义对象静默共享

难度：P6 ｜ 标签：dataclass、default_factory、可变默认、共享状态、hash

**问**：`@dataclass class C: tags: list = []` 会被 dataclasses 当场拒绝，可换成自定义的 `bag: Bag = Bag()` 就一声不响地过了，两个实例共享同一个 `Bag`，一个请求往里塞的数据出现在另一个请求的响应里。这个检查到底查什么？为什么只查那几个类型？`default_factory` 和 `__post_init__` 该怎么选？

**答**：
结论：`dataclasses` 在生成 `__init__` 时对字段默认值做的是**白名单式**检查——只对 `list`、`dict`、`set`、`bytearray` 这四个内置可变容器抛 `ValueError: mutable default ... use default_factory`，其余对象一律放行。没被拦下的默认值在**类创建时求值一次**，存进 `Field.default`，之后每个实例的 `__init__` 都把同一个对象绑到 `self.xxx` 上，于是"默认值"变成了"全局单例"。这不是 CPython 偷懒，而是无法可靠判定任意对象是否可变（`__hash__`、自定义 `__eq__`、内部可变但对外只读的类都会让判定失效），所以只在最容易踩、且能确定的地方兜底。

取舍：`field(default_factory=...)` 是唯一正确的通用写法，每次 `__init__` 调用工厂、实例天然隔离；`__post_init__` 更适合"需要基于其他字段计算"或"要按条件初始化"的场景，而且它在 `frozen=True` 下必须用 `object.__setattr__` 才能赋值。选型口诀：静态可变容器用 factory，派生值用 `__post_init__` / `field(init=False)`，需要深拷贝外部传入的可变对象则显式 `copy.deepcopy`——别指望 dataclass 替你做隔离。

实战：事故形态是"某个 DTO 加了个 `metadata: dict = {}` 的兄弟字段 `filters: Filters = Filters()`，单测只断言字段值、没断言身份，线上出现跨请求污染"。排查只需一行 `Leaky.__dataclass_fields__["bag"].default is instance.bag`。下面同时展示：四种内置容器被拦、自定义对象被共享、factory 版本隔离、以及可变字段导致类不可哈希（`eq=True` 默认会把 `__hash__` 置 None）。

```python
from dataclasses import dataclass, field


class Bag:
    """自定义可变容器：dataclasses 的"可变默认值"检查看不见它。"""

    def __init__(self):
        self.items = []

    def add(self, x):
        self.items.append(x)


try:

    @dataclass
    class Bad:
        tags: list = []  # list/dict/set/bytearray 会被 dataclasses 当场拒绝

except ValueError as e:
    print("list 默认值被拦截:", e)


@dataclass
class Leaky:
    bag: Bag = Bag()  # 自定义可变对象：不报错，所有实例共享同一个 Bag


@dataclass
class Fixed:
    bag: Bag = field(default_factory=Bag)  # 每个实例各自一份


a, b = Leaky(), Leaky()
a.bag.add("x")
print("共享: a.bag is b.bag ->", a.bag is b.bag, "| b.bag.items =", b.bag.items)

c, d = Fixed(), Fixed()
c.bag.add("x")
print("工厂: c.bag is d.bag ->", c.bag is d.bag, "| d.bag.items =", d.bag.items)

print("字段对象上的默认值就是那个共享实例:",
      Leaky.__dataclass_fields__["bag"].default is a.bag)
try:
    hash(Leaky())
except TypeError as e:
    print("可变 dataclass 不可哈希:", e)
```

**追问一**：为什么 `default_factory=list` 能保证每实例独立，而 `default=[]` 不行？—— 前者存的是可调用对象，`__init__` 里执行 `self.f = factory()`；后者在类体执行时就把 `[]` 创建好了，存的是结果。顺带一个高频笔误：写成 `field(default_factory=list())` 会得到 `TypeError: 'list' object is not callable`，因为传的是空列表而不是 `list` 这个类型。

**追问二**：共享默认值在 `frozen=True` / 放进 set 的场景会怎么放大？—— `frozen=True` 且 `eq=True` 会生成基于字段的 `__hash__`；如果字段是可变对象（或含可变成员），对象进 `set`/`dict` 之后内容一变哈希就变，后续 `in`/`remove` 全部失效，表现为"元素凭空消失"。可变对象本身不可哈希时则是直接 `TypeError`。所以冻结 DTO 的字段应尽量只放不可变类型，容器字段用 tuple / frozenset / `MappingProxyType` 收口。

## 背诵要点
- dataclasses 只拦 `list/dict/set/bytearray` 四种内置可变默认，其它可变对象静默共享（默认值在类创建时求值一次）。
- 正解是 `field(default_factory=...)`；派生值用 `__post_init__`（frozen 下需 `object.__setattr__`）。
- 判定共享只需 `__dataclass_fields__[name].default is instance.attr`；可变字段还会让类不可哈希、破坏 set 语义。

## 复盘追问
- 为什么 `tags: list = []` 报错而 `bag: Bag = Bag()` 不报？dataclasses 的检查边界为什么只能这么划？（四容器白名单、任意对象不可判定）
- 一个 DTO 的默认容器被跨请求污染，如何定位并给出三种隔离方案？（身份断言、factory、显式深拷贝）
