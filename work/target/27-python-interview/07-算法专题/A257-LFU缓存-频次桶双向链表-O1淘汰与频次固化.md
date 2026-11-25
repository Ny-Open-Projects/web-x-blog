---
title: [A257] LFU 缓存：频次桶双向链表、O(1) 淘汰与频次固化
date: 2026-11-24
categories: [Python算法笔试]
tags: [Python面试, 笔试题, 27]
type: 笔试题
---

### A257 · 精确 LFU 缓存

> 难度:★★★★ | 标签:LFU, 频次桶, 双向链表, O(1) 淘汰, 缓存污染

**问**（笔试·编程题）：实现一个生产语义明确的 LFU 缓存，要求：① `get` / `put` 平均 **O(1)**，**不允许任何排序或扫描**（不能每次淘汰时 `min(items, key=freq)`，也不能用「按频次排序的列表」）；② 淘汰频次最低的 key，**同频次淘汰最久未使用的**（tie-break 必须显式实现，否则同频次内退化成随机，行为不可测、命中率也跟着掉）；③ `put` 已存在的 key 要更新值并提频，**不触发淘汰、不产生重复节点**；④ `capacity=0` 时不缓存也不抛异常；⑤ 要能导出内部结构快照，让「淘汰顺序」可被断言；⑥ 用 80/20 + 扫描的混合负载证明它比 LRU 抗扫描，并解释这个优势在什么负载下会反转。请先说清与 A243（线程安全 LRU + TTL）、A010 / Q1009（LRU = 哈希表 + 双向链表）、Q6727（Redis 的概率 LFU：8 bit 对数计数 + 衰减）的分工——同样是「缓存淘汰」，这四张各在回答什么问题，为什么工程上几乎没人部署精确 LFU。

**答**：① 分工：A010 / Q1009 讲 **LRU 的骨架**（`map + 双向链表`，O(1) 靠「链表天然有序」）；A243 在同一骨架上加 **TTL 与并发**（锁粒度、过期键不许挤掉活键）；Q6727 是 **Redis 的近似**（`ldt` 衰减 + 8 bit Morris 计数，用 1 字节换掉整张频次表）。本题只解决一个问题：**在没有排序结构的前提下，怎么 O(1) 找到「频次最小且最久没用」的那条**。它既不是并发题也不是 TTL 题，增量全在数据结构。② 核心洞察：需要排序的键是 **频次**，不是条目。频次是整数、每次访问只 **+1**，所以它构成一条**稠密**的整数轴——不需要堆、不需要跳表，只需要「每个频次一个桶」，再加一个 `min_freq` 指针。命中时把条目从桶 f 摘下来挂到桶 f+1 的**头部**；桶 f 空了就删掉，若它正好是 `min_freq` 则 `min_freq = f+1`。淘汰时取 `min_freq` 桶的**尾部**。三步全是常数操作，且没有任何一步依赖容器规模——这才是 O(1) 的来源。③ 为什么不能用堆：把 `(freq, ts)` 压进小顶堆，读起来很像 O(log n)，但频次每变一次就要 push 一条新记录，堆里堆满**僵尸条目**；出堆时必须校验「这条记录的 freq 是否等于条目当前 freq」，否则会把高频键当低频键淘汰——这就是经典的「堆 + 懒惰删除」双份内存 + 判定漏洞。桶方案的桶数是 `max_freq`（受访问次数上限约束，通常几千），远小于条目数，且条目只在桶之间移动，不产生垃圾。④ tie-break 的工程意义：只按频次淘汰时，同频次的几条谁先死是**实现细节**（哈希序、插入序），压测里表现为「同一条数据有时留着有时被淘汰」，命中率抖动且无法复盘。给定「同频次按 LRU」后，淘汰序列变成**确定性函数**，可以被单测钉死——本题第 1、2 个用例就是钉这个。⑤ `min_freq` 的三个必踩坑：**(a)** 桶空时必须 `del`，否则高频短生命周期 key 会把 `freq` 字典撑成几千个空桶，长跑后内存只增不减；**(b)** `min_freq` 只在「最小桶被抽空」时 +1，不能在每次访问时重算，重算就是 O(桶数)；**(c)** 新插入统一进桶 1 并把 `min_freq` 置 1，不能沿用旧值，否则容量满时 `self._buckets[self._min]` 直接 KeyError。⑥ 契约要写死：`put` 已存在的键**算一次访问**（提频），否则「写多读少」的键永远停在低频、被频繁写的热键反复淘汰，这是业务侧最常投诉的「刚写的就没了」；代价是「一次写风暴把所有键推到高频」，需要靠衰减解决（见 ⑧）。⑦ 抗扫描与反转：LFU 记住的是**历史频次**，所以 20% 热 key 一旦被压热，2000 个一次性冷 key 冲进来也只能淘汰彼此（都在桶 1），LRU 则会被扫描整体冲掉热集。实测 6 万次访问、容量 20：LFU 命中 45769 次 vs LRU 33479 次。但反过来，**负载相位切换**（早高峰是 A 类商品、晚高峰换成 B 类）时，LFU 的历史频次变成负资产——新热点全是 freq=1，进不来；老热点 freq 上万，赶不走。这就是 **cache pollution / 频次固化**，也是 Redis 一定要给计数器做时间衰减的原因。⑧ 工程上不部署精确 LFU 的三个现实理由：**内存**（每条要频次 + 4 个链表指针，Redis 的 8 bit 是有意的）；**并发**（`min_freq` 是全局量，分段锁之后每段各有一个 min_freq，跨段比较又要加锁，退化严重）；**相位漂移**（精确频次对历史过度拟合）。所以主流是 W-TinyLFU：窗口 LRU（吸收突发）+ Count-Min sketch 估频（固定内存、只高估不低估）+ 准入判定（新 key 的估频要赢过淘汰候选才让进），把「精确」换成「可调误差的近似」。

```python
# 全部标准库；精确 LFU：频次桶双向链表 + min_freq 指针，get/put 均 O(1)
import random


class _Entry:
    """缓存条目，同时是所在频次桶双向链表里的节点。"""
    __slots__ = ("key", "val", "freq", "prev", "next")

    def __init__(self, key=None, val=None, freq=0):
        self.key, self.val, self.freq = key, val, freq
        self.prev = self.next = None


class _Bucket:
    """同一频次的所有条目：head 侧最新、tail 侧最旧（同频次内退化成 LRU 顺序）。"""
    __slots__ = ("freq", "head", "tail", "size")

    def __init__(self, freq):
        self.freq = freq
        self.head = _Entry()          # 哨兵，head.next 是最新
        self.tail = _Entry()          # 哨兵，tail.prev 是最旧
        self.head.next, self.tail.prev = self.tail, self.head
        self.size = 0

    def push_front(self, e):
        e.prev, e.next = self.head, self.head.next
        self.head.next.prev = e
        self.head.next = e
        self.size += 1

    def unlink(self, e):
        e.prev.next, e.next.prev = e.next, e.prev
        e.prev = e.next = None
        self.size -= 1

    def pop_back(self):
        if not self.size:
            return None
        e = self.tail.prev
        self.unlink(e)
        return e


class LFUCache:
    def __init__(self, capacity):
        if capacity < 0:
            raise ValueError("capacity 不能为负")
        self.cap = capacity
        self._map = {}                # key -> _Entry，O(1) 定位，杜绝任何扫描
        self._buckets = {}            # freq -> _Bucket，只存非空桶
        self._min = 0                 # 当前最小频次；只可能在 +1 与 1 两个方向跳
        self.hits = self.misses = self.evictions = 0

    # ---------- 内部：频次 +1 ----------
    def _bucket(self, freq, create=True):
        b = self._buckets.get(freq)
        if b is None and create:
            b = self._buckets[freq] = _Bucket(freq)
        return b

    def _promote(self, e):
        old = self._buckets[e.freq]
        old.unlink(e)
        nf = e.freq + 1
        e.freq = nf
        self._bucket(nf).push_front(e)
        if old.size == 0:                      # 空桶必须删，否则 freq 字典无界增长
            del self._buckets[old.freq]
            if self._min == old.freq:          # min 桶空了，最小频次只能是 nf
                self._min = nf

    def _evict(self):
        b = self._buckets[self._min]
        e = b.pop_back()                       # 同频次里最久未使用的那条
        del self._map[e.key]
        if b.size == 0:
            del self._buckets[b.freq]
        self.evictions += 1
        return e.key

    # ---------- 公开 API ----------
    def get(self, key):
        e = self._map.get(key)
        if e is None:
            self.misses += 1
            return None
        self._promote(e)
        self.hits += 1
        return e.val

    def put(self, key, val):
        if self.cap == 0:                      # 容量 0：不缓存，也不报错
            return False
        e = self._map.get(key)
        if e is not None:                      # 覆盖写：更新值 + 提频，不触发淘汰
            e.val = val
            self._promote(e)
            return True
        if len(self._map) >= self.cap:
            self._evict()
        e = _Entry(key, val, 1)
        self._map[key] = e
        self._bucket(1).push_front(e)
        self._min = 1
        return True

    # ---------- 诊断 ----------
    def snapshot(self):
        """按 (频次升序, 新→旧) 导出，便于断言结构与淘汰顺序。"""
        out = []
        for f in sorted(self._buckets):
            b, e = self._buckets[f], self._buckets[f].head.next
            while e is not b.tail:
                out.append((e.key, e.val, e.freq))
                e = e.next
        return out

    def bucket_count(self):
        return len(self._buckets)


class LRUCache:
    """对照组：只记最近使用，容量同构，用来量化「扫描型负载」下的命中率差。"""

    def __init__(self, capacity):
        from collections import OrderedDict
        self.cap, self.d, self.hits, self.misses = capacity, OrderedDict(), 0, 0

    def get(self, key):
        if key not in self.d:
            self.misses += 1
            return None
        self.d.move_to_end(key)
        self.hits += 1
        return self.d[key]

    def put(self, key, val):
        if self.cap == 0:
            return
        if key in self.d:
            self.d.move_to_end(key)
        self.d[key] = val
        if len(self.d) > self.cap:
            self.d.popitem(last=False)


if __name__ == "__main__":
    # 1) 基准序列（LeetCode 460）：同频次的淘汰顺序必须是 LRU
    c = LFUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    assert c.get(1) == 1                 # 1 频次 2，2 频次 1
    c.put(3, 3)                          # 淘汰频次最低的 2
    assert c.get(2) is None and c.get(3) == 3
    c.put(4, 4)                          # 1 与 3 同为频次 2 → 淘汰更久未用的 1
    assert c.get(1) is None and c.get(3) == 3 and c.get(4) == 4
    print("基准序列: 频次优先 + 同频 LRU，淘汰顺序 2 → 1 ✅")

    # 2) 同频次内的淘汰顺序显式验证：三条各命中一次，最久未用的先出
    c = LFUCache(3)
    for k in "abc":
        c.put(k, k)
        c.get(k)                          # 全部频次 2
    c.get("a")                            # a 频次 3；b、c 仍 2，c 更旧
    c.put("d", "d")
    assert [x[0] for x in c.snapshot()] == ["d", "c", "a"], c.snapshot()
    assert c.get("b") is None and c.evictions == 1
    print("tie-break: 同频次淘汰最久未用的 b，频次更高的 a 保留 ✅")

    # 3) 覆盖写：更新值并提频，且不触发淘汰、不产生重复节点
    c = LFUCache(2)
    c.put("x", 1)
    c.put("y", 2)
    c.put("x", 100)                       # 提频，不该淘汰 y
    assert c.get("x") == 100 and c.get("y") == 2
    assert len(c._map) == 2 and sum(b.size for b in c._buckets.values()) == 2
    print("覆盖写: 值已更新、频次提升、无重复节点、未误淘汰 ✅")

    # 4) 容量 0 与容量 1
    z = LFUCache(0)
    assert z.put("k", 1) is False and z.get("k") is None and z.evictions == 0
    one = LFUCache(1)
    one.put("a", 1)
    one.put("b", 2)
    assert one.get("a") is None and one.get("b") == 2
    print("边界: capacity=0 全部 miss；capacity=1 每次 put 必淘汰 ✅")

    # 5) min_freq 正确性：把最小频次桶抽空后，min 必须立刻指向下一个非空桶
    c = LFUCache(4)
    for k in range(4):
        c.put(k, k)                       # 全部频次 1
    for k in range(4):
        c.get(k)                          # 全部频次 2，频次 1 的桶已空
    assert c._min == 2 and 1 not in c._buckets and c.bucket_count() == 1
    c.put(9, 9)                           # 容量满，淘汰 freq=2 桶的尾部（0）
    assert c.get(0) is None and c._min == 1
    print("min_freq: 空桶即删，最小频次指针不悬空 ✅")

    # 6) 结构性 O(1)：操作数与容器规模无关（无任何遍历），且淘汰次数可精确对账
    c = LFUCache(10000)
    for i in range(60000):
        c.put(i % 20000, i)
    assert c.evictions == 50000, c.evictions
    assert len(c._map) == 10000 and sum(b.size for b in c._buckets.values()) == 10000
    print("规模不变量: 6 万次 put 后条目数 %d、淘汰 %d、桶内节点数与 map 一致 ✅"
          % (len(c._map), c.evictions))

    # 7) 抗扫描：80% 访问打在 20 个热 key 上，20% 是 2000 个一次性冷 key
    def workload(seed=0, n=60000):
        rng = random.Random(seed)
        hot = ["hot%d" % i for i in range(20)]
        for _ in range(n):
            if rng.random() < 0.8:
                yield rng.choice(hot)
            else:
                yield "cold%d" % rng.randrange(2000)

    a, b = LFUCache(20), LRUCache(20)
    for k in workload():
        if a.get(k) is None:
            a.put(k, 1)
        if b.get(k) is None:
            b.put(k, 1)
    assert a.hits > b.hits * 1.3, (a.hits, b.hits)
    print("抗扫描: LFU 命中 %d vs LRU 命中 %d（扫描把 LRU 的热集冲掉了）✅"
          % (a.hits, b.hits))
```

**追问**：1) 并发场景怎么加锁？—— 单锁最省事但把读写全串行化；朴素分段（按 key 哈希分 16 段）会让 `min_freq` 变成「每段一个」，全局淘汰时你要么扫 16 段的 min 取最小（O(段数)，可接受），要么改成「近似全局 LFU」——这已经是 Caffeine/Redis 的思路：**不追求精确**，用每段的近似频次 + 采样淘汰。更麻烦的是 `_promote` 要同时改两条桶链表（旧桶摘除、新桶插入），跨段锁根本做不到原子，所以工业实现通常把「频次」与「LRU 链表」解耦：频次放 sketch（近似、无锁/原子加），淘汰只在窗口 LRU 上做——**LFU 只作为准入判据，不直接决定淘汰顺序**。2) 频次固化除了衰减还有什么解法？—— 三条：**滑动窗口计数**（只统计最近 N 分钟，老热度自然流失）、**新 key 保护**（probation 区，新条目先给一个观察期，跑赢淘汰候选才晋升）、**多级频次**（把绝对次数换成排名/分位，避免长尾差异被无限放大）。衰减最简单但要在计数器上做乘法，浮点误差与并发写会打架，所以 Redis 用对数计数 + 随机衰减（概率性减 1），用统计正确换掉精确。3) 为什么 Count-Min sketch 的误差方向很关键？—— sketch 只会**高估**（哈希冲突导致计数偏大），不会低估。放进准入判定里：低估会让真热 key 被误杀（不可接受），高估只是「偶尔让一个不那么热的 key 进来」，代价是暂时的命中率损失，下一次淘汰会纠正。**误差方向可控比误差大小更重要**，这条原则同样适用于限流器（宁可少放不可超放）与布隆过滤器（宁可误判存在）。

## 背诵要点
1. LFU 的 O(1) 来自「桶的键是频次」：`key→节点` + `freq→双向链表` + `min_freq`；命中摘到 `freq+1` 桶头，淘汰 `min_freq` 桶尾。
2. 同频次必须按 LRU 兜底，否则淘汰顺序不可测；空桶要立刻删，`min_freq` 只在最小桶被抽空时 +1，新插入统一进桶 1。
3. 精确 LFU 有三宗罪：内存（每条约 5 个指针）、并发（min_freq 是全局量）、频次固化（老热点永不淘汰）→ 工业界用 W-TinyLFU（窗口 LRU + Count-Min 估频 + 准入），Redis 用 8bit 对数计数 + 概率衰减。

## 复盘追问
1. 缓存跑一周后命中率缓慢下降、新上架商品几乎进不了缓存，怎么解释？（提示：频次固化——老 key 频次高到淘汰不到，新 key 停在 1 反复被踢；解法是频次衰减、窗口计数或新 key probation 保护区）
2. 把这张单线程 LFU 直接套到多线程会发生什么？（提示：`_promote` 要同时改两条桶链表，分段锁下无法原子；`min_freq` 又是全局量，只能单锁或退化成「近似频次 + 采样淘汰」）
