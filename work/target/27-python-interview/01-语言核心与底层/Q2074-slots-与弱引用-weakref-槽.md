---
title: [Q2074] __slots__ 与弱引用:__weakref__ 槽
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2074 · __slots__ 与弱引用:__weakref__ 槽

> 难度:★★★★☆ | 标签:__slots__, weakref, 内存

**问**:声明了 __slots__ 的类,weakref.ref 直接 TypeError,这是 bug 吗?

**答**:不是 bug,是 slots 布局的直接推论:普通实例除了 __dict__ 还隐式挂着 __weakref__ 头,弱引用机制靠它找到对象;改用 __slots__ 后属性表被固定槽位取代,解释器不会再隐式送你这两个结构——没有声明 __weakref__ 槽,就没有弱引用的挂载点,weakref.ref 当场抛 TypeError。修复很简单:在 __slots__ 元组里显式加一项 "__weakref__"(多继承时只能出现在一个基类里,重复声明会报错)。这个组合在工程上很常见:池化对象(Q1284)既要 slots 省内存,又要 weakref 兜底回收,声明 __weakref__ 槽就能两者兼得。

```python
# file: code/01_语言核心与底层/q2074_slots_weakref.py
"""__slots__ 类默认不能被弱引用:__weakref__ 槽要显式声明。"""
import weakref


class NoWeak:
    __slots__ = ("x",)             # 没有 __weakref__ 槽

    def __init__(self, x):
        self.x = x


class WithWeak:
    __slots__ = ("x", "__weakref__")   # 显式声明弱引用槽

    def __init__(self, x):
        self.x = x


if __name__ == "__main__":
    a = NoWeak(1)
    try:
        weakref.ref(a)
    except TypeError as e:
        print("无 __weakref__ 槽:", e)

    b = WithWeak(1)
    r = weakref.ref(b)
    print("声明槽后可弱引用:", r() is b)
    del b
    print("对象销毁后弱引用失效:", r() is None)
    print("普通类不受影响:实例天生带着隐式的 __weakref__ 结构")
```

**追问**:1) 多继承时 __weakref__ 声明在哪?——整个继承链只允许一个基类的 slots 含它,重复声明直接 TypeError;slots 与 key 共享实例字典谁更省?——slots 通常更省且访问等速,但失去动态属性能力,见 Q008 与 Q1262。2) __weakref__ 槽的必要性?——slots 类默认没有弱引用槽,对象进 WeakKeyDictionary/weakref.ref 直接 TypeError;显式加 "__weakref__" 槽恢复支持。3) 布局约束?——slots 成员按 MRO 排进固定槽位,继承链最多一个非空 slots 基类(Q559);混入类一律 slots=()。4) 生产陷阱?——slots 对象进弱引用容器报错的经典案例;漏声明 __weakref__ 导致缓存库失效;动态属性需求没想清就上 slots。
