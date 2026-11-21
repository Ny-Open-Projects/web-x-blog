---
title: [Q496] deque 与 array:结构选型
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q496 · deque 与 array:结构选型

> 难度:★★☆☆ | 标签:容器, deque

**问**:list、deque、array 三者各自的甜点区在哪?maxlen 的 deque 解决什么问题?

**答**:list 是全能动态数组:随机访问 O(1)、尾部增删摊还 O(1),但头部插入 O(n)。deque 是双向链表块结构:两端增删 O(1),牺牲随机访问(O(n));maxlen 版自动丢弃旧元素,天然实现滑动窗口(最近 N 条日志、限流的请求队列)。array 是类型固定的紧凑数组:元素按 C 类型('i'、'd')存储,百万级同类型数值比 list 省内存 5-10 倍且可直接与二进制交互;但只能存一种类型,写入会强制转换或报错。选择口诀:随机访问选 list,两端操作选 deque,纯数值海量存储选 array/numpy。

```python
# file: code/01_语言核心与底层/q496_deque_array.py
from array import array
from collections import deque

if __name__ == "__main__":
    dq = deque(range(5), maxlen=5)
    dq.append(99)                         # 右进:左端自动挤出
    print(dq)
    dq.appendleft(0)                      # 左进:右端挤出
    print(dq)
    dq.rotate(2)                          # 旋转:环形缓冲语义
    print(dq)

    arr = array("i", [1, 2, 3])
    arr.append(4)
    print(arr, "itemsize:", arr.itemsize)
    try:
        arr.append(2.5)
    except TypeError as e:
        print("typed container:", e)
```

**追问**:1) deque 随机访问为什么是 O(n)?——内部是块级双向链表,定位第 i 个元素要从最近端逐块走;需要「两端快 + 随机访问也快」时选 sortedcontainers 这类分层数组结构。2) array 与 list 的选型标准?——array 紧密存 C 原生类型(每元素 4/8 字节),适合大数值流与 C 交互;list 存 PyObject* 指针,元素任意类型但有指针与对象开销;两者都是可变序列。3) deque 的底层结构?——定长块(~64 元素)组成双向链表加中央索引表,两端 append/pop O(1),maxlen 满员自动挤掉另一端,天然适合滑动窗口。4) 生产陷阱?——大流量随机读用 deque 性能塌方;deque(maxlen=n) 静默丢弃旧元素,在「不能丢」的场景是隐性 bug;array 与 C 交互忽略 itemsize/字节序导致数据错位。
