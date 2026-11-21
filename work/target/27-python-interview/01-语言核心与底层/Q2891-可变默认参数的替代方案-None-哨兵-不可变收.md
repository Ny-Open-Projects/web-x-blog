---
title: [Q2891] 可变默认参数的替代方案:None 哨兵、不可变收编与有意共享
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2891 · 可变默认参数的替代方案:None 哨兵、不可变收编与有意共享

> 难度:★★☆☆☆ | 标签:默认参数, 可变对象, 惯用法

**问**:可变默认参数是经典陷阱,替代方案有哪几类?可变默认值有没有「正确用法」?

**答**:三条正路对应三种意图:**None 哨兵**是默认首选——`tags=None` 在体内 `tags = [] if tags is None else list(tags)`,顺带用 list() 复制防御外部传入的共享引用;**不可变默认值**适合确实要「预先带着点东西」的场景,元组、frozenset、字符串天然安全;**default_factory** 是 dataclass 世界的对应解法,`field(default_factory=list)` 保证每实例新建容器。「反例转正」的第三条路也存在:`_registry={}` 这种共享默认值是进程内登记与记忆化的最小实现,前提是命名带下划线、注释声明意图,让评审知道这是特性不是手滑。判别标准一句话:默认值是否跨调用累积状态?是且非故意,改;是且故意,写清楚。

```python
# file: code/01_语言核心与底层/q2891_mutable_default.py
"""可变默认参数的替代方案:None 哨兵、不可变收编与有意共享。"""
import dataclasses


def add_tag(item, tags=None):
    """方案一:None 哨兵 + 体内新建;list(tags) 顺带防御外部共享引用。"""
    tags = [] if tags is None else list(tags)
    tags.append("new")
    return item, tags


def collect_point(x, y, seen=()):
    """方案二:不可变序列当默认值,天然无跨调用副作用。"""
    return x + y, seen


@dataclasses.dataclass
class Cart:
    """方案三:dataclass 的 default_factory,每实例新建。"""
    items: list = dataclasses.field(default_factory=list)
    meta: dict = dataclasses.field(default_factory=dict)


def registry_default(box, _registry={}):
    """反例转正用:刻意利用共享默认值做进程内登记,必须注释声明意图。"""
    _registry[box] = box
    return _registry


if __name__ == "__main__":
    _, ta = add_tag("apple")
    _, tb = add_tag("pear")
    print("两次调用互不影响:", ta, tb)

    shared = ["x"]
    _, t1 = add_tag("a", shared)
    print("外部列表未被污染:", shared, "| 返回的是副本:", t1)

    print("不可变默认值:", collect_point(1, 2, seen=("keep",)))

    cart = Cart()
    cart.items.append("book")
    other = Cart()
    print("default_factory 每实例新建:", cart.items, other.items)

    registry_default("first")
    print("有意共享的登记表:", list(registry_default("second").values()))
```

**追问**:1) 为什么 None 哨兵里还要 list(tags) 而不是直接用传入的列表?——调用方传进来的列表会被函数 append 污染,违背最小惊讶;除非契约明确「就地修改入参」,否则函数只动自己的副本。2) 三种替代的适用面?——None 哨兵:通用(每调用新对象);不可变收编 tuple:防修改但调用方要改类型;有意共享:文档化「就地修改」的 API(如 list.sort)。3) 与 Q2085/2374 的闭环?——None 双语义升级哨兵;默认参数求值时机;工厂思想(dataclass default_factory)——同一主题的完整决策树。4) 生产陷阱?——可变默认参数共享(经典);函数污染调用方列表(本题);把「收编 tuple」的 API 又传回 list 混用。
