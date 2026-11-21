---
title: [Q2333] G-Counter 合并:分布式计数器概念
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2333 · G-Counter 合并:分布式计数器概念

> 难度:★★★☆ | 标签:分布式, CRDT, 计数

**问**:三个机房各自累加计数,定时同步,怎么保证合并后总数不丢不重?加锁同步太重了怎么办?

**答**:G-Counter 是最简 CRDT:每个节点只递增自己的槽位,值是全部槽位之和;合并时逐槽取最大值而不是相加。为什么取最大:槽位值只会增,两个副本对同一槽位的观测必然一个是另一个的前缀,最大值即最新事实。三条性质自动成立:交换律(合并顺序无关)、幂等(重复同步不重复计数)、单调(只增不减)。对比天真做法——直接把对端总数加上来,重复同步一次就翻倍。限制也要知道:G-Counter 只能增,要减用 PN-Counter 两个 G-Counter 相减;节点槽位随节点数增长,海量节点要分代滚动。它展示了 CRDT 的核心思路:把"并发无冲突"设计进数据结构,而不是事后加锁。

```python
# file: code/06_Agent与LLM及系统设计/q2333_gcounter_merge.py
"""G-Counter:每个节点只增自己的槽位,合并取各槽最大值,离线增量不丢求和无重复。"""
class GCounter:
    def __init__(self, nid, peers):
        self.nid = nid
        self.slots = {p: 0 for p in peers}

    def inc(self, n=1):
        self.slots[self.nid] += n

    def value(self):
        return sum(self.slots.values())

    def merge(self, other):
        for p, v in other.slots.items():
            self.slots[p] = max(self.slots[p], v)

    def state(self):
        return dict(self.slots)


if __name__ == "__main__":
    a, b, c = GCounter("A", "ABC"), GCounter("B", "ABC"), GCounter("C", "ABC")
    a.inc(5)
    b.inc(3)
    b.inc(2)
    a.merge(b)
    assert a.value() == 10, "合并后求和 5 加 5"
    c.inc(7)
    b.merge(c)
    a.merge(b)
    assert a.value() == 17, "三方合并 5+5+7"
    before = a.value()
    a.merge(b)
    assert a.value() == before, "合并幂等 重复同步不重复计数"
    a.inc(1)
    b.merge(a)
    c.merge(a)
    assert a.state() == b.state() == c.state(), "交换律与收敛 三副本状态一致"
    assert a.value() == 18
    offline = GCounter("C", "ABC")
    offline.slots = dict(c.state())
    offline.inc(100)
    a.merge(offline)
    assert a.value() == 118, "离线增量带着原状态回来不丢"
    print("G-Counter 通过:只增己槽 逐槽取大 幂等交换 离线不丢")
```

**追问**:
- 为什么逐槽取大而不是全和取大? 答:全和取大在"一方本地又加了值"时会把新增量回滚掉,槽位级最大才能保单调合并
- 槽位对象下线了怎么办? 答:槽位冻结保留不删除,删了它的历史增量就从总数里消失,新节点用新槽位
