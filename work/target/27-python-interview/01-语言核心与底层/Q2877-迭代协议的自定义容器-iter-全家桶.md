---
title: [Q2877] 迭代协议的自定义容器:__iter__ 全家桶
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2877 · 迭代协议的自定义容器:__iter__ 全家桶

> 难度:★★★☆☆ | 标签:迭代协议, 容器, 魔法方法

**问**:让你实现一个自定义容器类,除了存取还要支持 for、in、reversed 和 len,你会实现哪些方法?各自的语义要点是什么?

**答**:最小迭代面是四个魔法方法:`__len__` 报告大小、`__iter__` 返回独立迭代器、`__contains__` 自定义成员判定、`__reversed__` 自定义逆序。三个要点:第一,`__iter__` 用生成器实现时每次调用都创建新的迭代器,两个循环互不干扰,这是「容器」与「一次性迭代器」的分界线;第二,`__contains__` 不写也能工作——`in` 会回退到 `__iter__` 逐元素比较,显式实现可以换成更快的算法或不同语义;第三,`__reversed__` 同理,`reversed()` 的回退路径是 `__getitem__` 从尾部倒序索引,自己实现后容器就不需要支持下标访问。没实现 `__getitem__` 时 `pl[0]` 会明确抛 TypeError,这是「最小接口」的自觉:不承诺的能力就让它报错,而不是顺手全实现一遍。

```python
# file: code/01_语言核心与底层/q2877_custom_container.py
"""自定义容器的迭代协议全家桶:__iter__、__len__、__contains__、__reversed__。"""


class Playlist:
    """一个只进不改的播放列表:演示容器该实现的最小迭代面。"""

    def __init__(self, title):
        self.title = title
        self._tracks = []

    def add(self, name):
        self._tracks.append(name)
        return self            # 链式添加

    def __len__(self):
        return len(self._tracks)

    def __iter__(self):
        # 每次调用返回独立生成器:多个循环互不干扰
        index = 0
        while index < len(self._tracks):
            yield self._tracks[index]
            index += 1

    def __reversed__(self):
        yield from reversed(self._tracks)

    def __contains__(self, name):
        return name in self._tracks

    def __repr__(self):
        return f"Playlist({self.title!r}, {len(self)} tracks)"


if __name__ == "__main__":
    pl = Playlist("面试歌单").add("Map").add("Filter").add("Reduce")
    print(pl)
    print("顺序:", list(pl))
    print("倒序:", list(reversed(pl)))
    print("Filter 在列表里:", "Filter" in pl)     # 走 __contains__
    print("Zip 不在列表里:", "Zip" in pl)

    it1, it2 = iter(pl), iter(pl)
    next(it1)
    print("两个独立迭代器互不干扰:", next(it1), next(it2))

    try:
        pl[0]
    except TypeError as e:
        print("未实现 __getitem__ 时的下标访问:", e)
```

**追问**:1) 什么时候容器反而应该只支持一次迭代?——流式数据(文件行、网络包)天然只能消费一遍,此时 `__iter__` 返回 self 与同一个生成器,第二次 for 会静默拿到空,这正是 Q1296 讲过的事故来源。2) 全家桶的完整矩阵?——__iter__(可重复迭代的核心)、__next__(迭代器)、__len__/__getitem__/__contains__/__reversed__;实现了 __iter__ 返回新迭代器,其余多可由 Mixin(Sequence)或自动回退获得。3) 与生成器实现的取舍?——容器类要「可重复 + 协议齐全」;一次性流用生成器函数;两者按生命周期语义选(Q437)。4) 生产陷阱?——把生成器当容器返回(二次为空);__getitem__ 旧协议混入新代码;__len__ 与实际产出不一致破坏 len 语义。
