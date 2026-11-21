---
title: [Q556] getsizeof 与 __sizeof__:浅大小
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q556 · getsizeof 与 __sizeof__:浅大小

> 难度:★★★☆ | 标签:内存, 内省

**问**:sys.getsizeof([1,2,3]) 返回的是整个列表的内存吗?为什么容器嵌套时它「骗人」?

**答**:getsizeof 只算对象自身(C 层 __sizeof__):容器对象的结构头 + 指针数组,不含元素指向的对象——列表 1000 个大字符串,列表自身约 8KB,字符串内容另算,不递归。真实占用要遍历引用树累加(gc.get_referents 递归,注意去重防环),或用 tracemalloc 的实际分配统计(含碎片与分配器开销)。getsizeof 的价值是对比结构开销:slots 实例 vs dict 实例、tuple vs list、同一 int 不同大小(int 是变长的)。面试答题要点:它是「对象头大小」不是「深大小」。

```python
# file: code/01_语言核心与底层/q556_getsizeof.py
import sys

class Plain:
    pass

class Slotted:
    __slots__ = ("a",)

if __name__ == "__main__":
    print("empty list:", sys.getsizeof([]))
    print("1000-int list:", sys.getsizeof(list(range(1000))))
    print("1000-int tuple:", sys.getsizeof(tuple(range(1000))))

    print("small int:", sys.getsizeof(1), "| big int:", sys.getsizeof(2 ** 100))
    print("plain instance:", sys.getsizeof(Plain()), "| slotted:", sys.getsizeof(Slotted()))

    nested = [list(range(1000))]          # 外层列表只算自己的指针
    print("shallow outer only:", sys.getsizeof(nested))
    print("content is not counted — walk references for deep size")
```

**追问**:1) 怎么写一个「深大小」函数?——用 gc.get_referents 做 BFS,对每对象 sys.getsizeof 累加,以 id 集合去重防环;仍不含分配器碎片,精确到字节级要用 tracemalloc。2) getsizeof 为什么是浅大小?——只返回对象自身分配(__sizeof__ 加 GC 头),不递归引用;容器存的是指针,元素大小不计入——「1M 元素的 list 存 1M 个指针」就是这么来的。3) 对齐与分配器视角?——大小按 pymalloc 块对齐;str 紧凑表示、list 的 capacity 预留都体现在返回值;__sizeof__ 自定义时必须自己含这些余量。4) 生产陷阱?——用 getsizeof 评估复合结构差一个数量级;自定义 __sizeof__ 忘 GC 头;pymalloc 不还内存给 OS,「对象删了 RSS 不降」不是泄漏,要用 tracemalloc/RSS 双视角判断。
