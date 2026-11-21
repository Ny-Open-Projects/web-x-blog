---
title: [Q2338] in 的回退链:__contains__、__iter__ 与 __getitem__
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2338 · in 的回退链:__contains__、__iter__ 与 __getitem__

> 难度:★★★☆☆ | 标签:__contains__, __iter__, 旧式协议

**问**:一个类什么容器协议都没完整实现,`in` 还能工作吗?解释器按什么顺序找方法?

**答**:`in` 的分派是一条三级回退链:优先调 `__contains__`(O(1) 与否由实现决定);没有就退回 `__iter__`,用 `==` 逐元素扫描,天然 O(n);连 `__iter__` 都没有,还会退到旧式协议 `__getitem__`,从下标 0 起试探,直到 IndexError 认定遍历结束——这是 Python 2 时代遗留的兼容路径。三者全无才抛 TypeError。这解释了两个工程现象:只实现 `__getitem__` 的类「意外地」可迭代、可 in 检查;以及为什么把 O(n) 的迭代查找升级为 O(1),只需补一个 `__contains__`(底层换 set)。设计只读容器时,实现 `__iter__` 通常就够,`__getitem__` 回退只是保底。

```python
# file: code/01_语言核心与底层/q2338_in_fallback.py
"""in 的回退链:__contains__ 优先,其次 __iter__,最后旧式 __getitem__。"""


class OnlyContains:
    def __init__(self, data):
        self.data = data

    def __contains__(self, item):
        print(f"    OnlyContains.__contains__({item!r})")
        return item in self.data


class OnlyIterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        print("    OnlyIterable 走迭代逐元素比较")
        return iter(self.data)


class OnlyGetItem:
    """只实现 __getitem__:旧式协议,in 按下标从 0 起试探。"""

    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        print(f"    OnlyGetItem.__getitem__({index})")
        return self.data[index]


class Nothing:
    pass


if __name__ == "__main__":
    print("2 in OnlyContains:")
    print("    结果:", 2 in OnlyContains([1, 2, 3]))

    print("3 in OnlyIterable:")
    print("    结果:", 3 in OnlyIterable([1, 2, 3]))

    print("'b' in OnlyGetItem:")
    print("    结果:", "b" in OnlyGetItem("abc"))

    try:
        1 in Nothing()
    except TypeError as exc:
        print("in Nothing:", exc)
```

**追问**:1) 只有 `__getitem__` 的类,for 循环也能跑吗?——能,for 与 in 共用这条回退链,按下标试探到 IndexError 停;但它没有 `__iter__` 的显式迭代器语义,不建议新代码这么写。2) 回退链的完整顺序?——__contains__ 优先;没有则 __iter__(迭代器逐个 ==);再没有则 __getitem__(旧式序列协议从 0 试探到 IndexError,Q542);in 的语义随层级漂移(1:1 映射 / 精确元素相等 / 下标遍历)。3) 与 iter() 的关系?——iter() 同样回退到 __getitem__ 造旧式迭代器;in 的 str 特化(子串)是 __contains__ 的内建实现。4) 生产陷阱?——旧协议把业务 IndexError 当终止信号;自定义 __contains__ 改变 in 语义(子串 vs 元素);判断「可迭代」用 isinstance 而不是 try iter(Q542)。
