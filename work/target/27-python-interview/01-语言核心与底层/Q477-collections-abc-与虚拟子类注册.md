---
title: [Q477] collections.abc 与虚拟子类注册
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q477 · collections.abc 与虚拟子类注册

> 难度:★★★☆ | 标签:ABC, 协议

**问**:一个没继承 Iterable 的类,如何让 isinstance 判定为 True?虚拟子类与 ABC 的抽象方法是什么关系?

**答**:ABC 的 `register()` 声明虚拟子类:isinstance/issubclass 返回 True,但不会继承任何实现、也不校验方法是否存在——是纯粹的「声明关系」。常规子类(直接继承)则必须实现全部抽象方法才能实例化,且免费获得 Mixin 实现(Sequence 给你 __contains__/__iter__)。collections.abc 通过 __subclasshook__ 还内置了结构化判定:有 __iter__ 就算 Iterable 子类。三条路的意义:register 用于「我知道它满足协议但没法改它的类」,hook 用于「按方法存在性自动判定」,显式继承用于「要实现要复用」。

```python
# file: code/01_语言核心与底层/q477_abc_virtual_subclass.py
from collections.abc import Sequence, Iterable

class Range3(Sequence):
    """正规子类:实现抽象方法,获得 Mixin 能力"""
    def __init__(self, n):
        self.n = n

    def __len__(self):
        return self.n

    def __getitem__(self, i):
        if i < 0:
            i += self.n
        if not 0 <= i < self.n:
            raise IndexError(i)
        return i * 10

class Bag:
    """从未继承 Iterable,却声称自己是"""
    def __iter__(self):
        return iter([1, 2, 3])

Iterable.register(Bag)

if __name__ == "__main__":
    r = Range3(3)
    print(list(r), r[1], len(r))          # Mixin 提供的 __iter__ 生效
    print(isinstance(r, Sequence), issubclass(Range3, Sequence))

    b = Bag()
    print(isinstance(b, Iterable))        # True:虚拟子类只改 isinstance
    print(list(b))
    print(issubclass(Bag, Iterable))
```

**追问**:1) 虚拟子类注册会影响 MRO 吗?——不影响,register 只在 ABC 的 _abc_registry 里记一笔;所以虚拟子类拿不到任何 Mixin 方法,缺的方法要自己实现。2) issubclass 判定的三条路径优先级?——__subclasshook__ 先行(返回 True/False/NotImplemented),NotImplemented 才落回常规 MRO 检查与 _abc_registry;Iterable 的 hook 检查 __iter__ 存在即 True,Bag 不 register 其实也已结构匹配。3) ABCMeta 的实现机制?——C 加速模块维护 _abc_registry/_abc_cache(正负缓存都有),register 写前者;抽象方法集合存 __abstractmethods__,实例化时非空即 TypeError。4) 生产陷阱?——register 一个实际不满足接口的类,isinstance 通过但运行时 AttributeError,声明成了谎言;虚拟子类要配协议满足性测试,或用 runtime_checkable Protocol 表达结构关系。
