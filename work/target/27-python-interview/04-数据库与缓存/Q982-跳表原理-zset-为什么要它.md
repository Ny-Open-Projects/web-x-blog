---
title: [Q982] 跳表原理: zset 为什么要它
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q982 · 跳表原理: zset 为什么要它

> 难度:★★★★ | 标签:跳表, 数据结构

**问**:跳表是怎么做到 O(logN) 的?为什么 Redis 选跳表而不是平衡树?

**答**:跳表在有序链表上加多层"快速通道":每个节点以 1/2(或 1/4)概率晋升到上一层,查询从顶层向右下走,期望每层跳过一半节点,层数期望 O(logN),插入删除只改指针无需旋转。Redis 选它的理由(antirez 原话):实现简单于红黑树、范围查询天然顺着底层链表走、并发/调试更容易,且概率层数在性能上与平衡树相当。工程细节:Redis 跳表层高上限 32、每向上概率 1/4(期望层高 1.33),节点带 backward 指针支持反向遍历(zrevrange)。

```python
# file: code/04_数据库与缓存/q982_skip_list.py
"""最小跳表: 概率层高 + 插入 + 范围查询"""
import random

class Node:
    def __init__(self, key, level):
        self.key = key
        self.forward = [None] * level

class SkipList:
    MAX = 8
    P = 0.5

    def __init__(self):
        self.head = Node(None, self.MAX)
        self.level = 1

    def _rand_level(self):
        lvl = 1
        while random.random() < self.P and lvl < self.MAX:
            lvl += 1
        return lvl

    def insert(self, key):
        update = [self.head] * self.MAX           # 顶层之上统一指向 head
        node = self.head
        for i in reversed(range(self.level)):
            while node.forward[i] and node.forward[i].key < key:
                node = node.forward[i]
            update[i] = node
        lvl = self._rand_level()
        self.level = max(self.level, lvl)
        new = Node(key, lvl)
        for i in range(lvl):
            new.forward[i] = update[i].forward[i]
            update[i].forward[i] = new

    def range_(self, lo, hi):
        out, node = [], self.head
        for i in reversed(range(self.level)):
            while node.forward[i] and node.forward[i].key < lo:
                node = node.forward[i]
        node = node.forward[0]
        while node and node.key <= hi:
            out.append(node.key)
            node = node.forward[0]
        return out

if __name__ == "__main__":
    random.seed(7)
    sl = SkipList()
    for k in [3, 1, 4, 1, 5, 9, 2, 6]:
        sl.insert(k)
    print("范围 [2,6):", sl.range_(2, 6), "<- 底层有序链表天然支持")
    print("查找路径: 从顶层逐层向右下, 期望 O logN")
```

**追问**:
- 跳表怎么实现 ZRANK?——节点 span 字段记录跨层跨越的节点数,查询时累加 span 得排名,仍是 O(logN)。
- 并发跳表怎么加锁?——Redis 单线程无此问题;通用并发跳表用无锁 CAS 或细粒度锁,属于加分延伸。

---
