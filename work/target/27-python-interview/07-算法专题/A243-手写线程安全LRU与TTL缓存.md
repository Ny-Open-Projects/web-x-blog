---
title: [A243] 手写线程安全 LRU + TTL 缓存：双向链表、过期清理与并发读写
date: 2026-11-23
categories: [Python算法笔试]
tags: [Python面试, 笔试题, 27]
type: 笔试题
---

### A243 · 线程安全 LRU + TTL 缓存

> 难度:★★★★ | 标签:LRU, TTL, 双向链表, 并发

**问**（笔试·编程题）：手写一个生产可用的内存缓存：① 容量上限 `capacity`，按 LRU 淘汰；② 每个键可带 TTL（默认取全局值），过期后 `get` 必须返回 miss；③ `get`/`put` 平均 O(1)；④ 多线程并发读写不能把链表搞坏、不能返回已过期的值；⑤ 容量满时**过期键不能把活键挤掉**。请说清为什么不用 `OrderedDict` 一把梭（Q478 已经能用 `move_to_end`/`popitem` 实现 LRU，Q444 也有 TTL 装饰器，本题增量在哪），锁的粒度怎么选（单锁 vs 分段锁），过期清理用惰性还是主动 sweep，以及大容量下 sweep 的 O(n) 怎么降。写完给出并发压测验证。

**答**：① 与已有卡的分工：Q478 证明 `OrderedDict` 的两个重排原语足以表达 LRU，Q444 给的是「函数结果缓存装饰器」、按最旧写入时间近似淘汰、单线程语义；本题要的是**数据结构级**实现——per-key TTL、两种序（访问序 vs 过期序）分离、以及并发正确性。`OrderedDict` 只能维护一条序，TTL 到期清理需要另一条索引，且它内部是一把锁，做不了分段。② 结构：`dict[key] -> node` 负责 O(1) 定位，**带哨兵的双向链表**维护访问序（`head.next` 最新、`tail.prev` 最旧），哨兵省掉所有 `None` 判断;`get` 命中就摘链再头插（等价 `move_to_end`），`put` 超容从尾部淘汰。③ 并发：单锁（`threading.Lock`）最简单且正确，临界区内只做指针与字典操作，**绝不调用用户代码/IO/日志回调**（否则锁被外部阻塞，尾延迟爆炸）。关键点是「检查过期 → 摘链 → 删字典 → 返回」必须是**一个原子临界区**：两个线程同时判定同一节点过期会重复 `_unlink`，第二次把已置空的 `prev/next` 解引用直接 `AttributeError`；CPython 的 GIL 只保证单条字节码原子，复合操作不原子（Q5002）。④ 过期策略：**惰性 + 主动双轨**。`get` 命中时判过期（保证正确性，绝不返回脏值）；后台 `sweep()` 周期性全扫（保证内存）。淘汰顺序上有个坑：容量满时**必须先清过期再按 LRU 淘汰**——链表尾是「最久未访问」，不一定是「已过期」，而快过期的键可能刚好在头部附近；不清死键就会出现「缓存显示满了、实际一半是尸体、活键被挤掉」的假满。⑤ 成本与取舍：全扫 sweep 是 O(n)，容量到十万级会卡住读请求——生产用**最小堆**（`heapq` 按 `expire_at`，惰性删除 + 版本号去重）或**增量 sweep**（每次只处理固定条数，游标轮转），把待删节点先摘链、出锁后再释放引用。分段锁（按 key 哈希分 N 片、每片独立 LRU + 独立锁）能把吞吐抬一个量级，但全局 LRU 语义退化为「分片内 LRU」，容量要按负载倾斜分配，热点片仍会频繁淘汰。⑥ 其它实战点：时钟必须用 `time.monotonic`（墙钟回拨会让 TTL 变负或永不过期，Q5075）；缓存击穿用 singleflight 合并回源；`value` 若是可变对象，要么存副本要么在文档里约定调用方不得改写。

```python
# 全部标准库；双向链表 + 字典 + 单锁；惰性过期 + 主动 sweep + 死键优先清理
import threading
import time


class _Node:
    __slots__ = ("key", "val", "expire_at", "prev", "next")

    def __init__(self, key=None, val=None, expire_at=0.0):
        self.key = key
        self.val = val
        self.expire_at = expire_at
        self.prev = None
        self.next = None


_MISS = object()          # 区分「没命中」与「命中了 None」


class TTLCache:
    """容量上限 + 每键 TTL 的线程安全 LRU。"""

    def __init__(self, capacity, default_ttl, clock=time.monotonic):
        if capacity <= 0:
            raise ValueError("capacity 必须为正")
        self._cap = capacity
        self._ttl = default_ttl
        self._clock = clock
        self._lock = threading.Lock()
        self._map = {}
        self._head = _Node()               # 哨兵：head.next 最新
        self._tail = _Node()               # 哨兵：tail.prev 最旧
        self._head.next = self._tail
        self._tail.prev = self._head
        self.hits = 0
        self.misses = 0
        self.evicted = 0                   # 容量淘汰
        self.expired = 0                   # 过期清理

    # ---- 以下三个链表操作要求调用方已持锁 ----
    def _unlink(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = node.next = None

    def _push_front(self, node):
        node.next = self._head.next
        node.prev = self._head
        self._head.next.prev = node
        self._head.next = node

    def _purge_expired_locked(self, now):
        """全扫清过期：正确但 O(n)；大容量用最小堆或增量 sweep 替代。"""
        dead = []
        node = self._head.next
        while node is not self._tail:
            if node.expire_at <= now:
                dead.append(node)
            node = node.next
        for n in dead:
            self._unlink(n)
            del self._map[n.key]
            self.expired += 1
        return len(dead)

    def get(self, key):
        now = self._clock()
        with self._lock:
            node = self._map.get(key)
            if node is None:
                self.misses += 1
                return _MISS
            if node.expire_at <= now:      # 判定 + 摘链 + 删表在同一临界区
                self._unlink(node)
                del self._map[key]
                self.expired += 1
                self.misses += 1
                return _MISS
            self._unlink(node)             # 命中：移到最前，维持 LRU 序
            self._push_front(node)
            self.hits += 1
            return node.val

    def put(self, key, val, ttl=None):
        now = self._clock()
        expire_at = now + (self._ttl if ttl is None else ttl)
        with self._lock:
            node = self._map.get(key)
            if node is not None:           # 覆盖写：刷新值、TTL 与位置
                node.val = val
                node.expire_at = expire_at
                self._unlink(node)
                self._push_front(node)
                return
            if len(self._map) >= self._cap:
                self._purge_expired_locked(now)   # 先清死键，别让死键挤掉活键
            while len(self._map) >= self._cap:
                victim = self._tail.prev
                if victim is self._head:
                    break
                self._unlink(victim)
                del self._map[victim.key]
                self.evicted += 1
            node = _Node(key, val, expire_at)
            self._map[key] = node
            self._push_front(node)

    def sweep(self):
        """后台线程周期性调用，返回清掉的条数。"""
        with self._lock:
            return self._purge_expired_locked(self._clock())

    def __len__(self):
        with self._lock:
            return len(self._map)


class FakeClock:
    def __init__(self, start=1000.0):
        self.t = start

    def __call__(self):
        return self.t

    def advance(self, dt):
        self.t += dt


if __name__ == "__main__":
    clock = FakeClock()
    cache = TTLCache(2, 10, clock=clock)
    cache.put("a", 1)
    cache.put("b", 2)
    assert cache.get("a") == 1
    cache.put("c", 3)                       # 淘汰最久未访问的 b
    assert cache.get("b") is _MISS
    assert cache.get("c") == 3
    assert cache.evicted == 1
    print("LRU: a 被访问后续命，b 被淘汰 ✅")

    clock.advance(11)                       # 过了默认 TTL
    assert cache.get("a") is _MISS          # 惰性过期：绝不返回脏值
    assert cache.get("c") is _MISS
    assert cache.expired == 2 and len(cache) == 0
    print("TTL: 到期惰性清理，读到的都是 miss ✅")

    # 死键不能挤掉活键：容量 2，两个键都过期后再 put 新键
    c2 = FakeClock()
    small = TTLCache(2, 5, clock=c2)
    small.put("dead1", 1)
    small.put("dead2", 2)
    c2.advance(6)
    small.put("alive", 3)
    assert small.evicted == 0 and small.expired == 2
    assert small.get("alive") == 3
    print("容量满: 先清 2 个死键，活键零淘汰 ✅")

    # 主动 sweep：批量过期一次清完
    c3 = FakeClock()
    sweeper = TTLCache(10, 1, clock=c3)
    for i in range(5):
        sweeper.put(f"k{i}", i)
    c3.advance(2)
    assert sweeper.sweep() == 5 and len(sweeper) == 0
    print("sweep: 一次清 5 条 ✅")

    # 并发压测：8 线程 × 3000 次读写，链表不得损坏、容量不得越界
    shared = TTLCache(64, 60)
    errors = []

    def worker(seed):
        try:
            for i in range(3000):
                key = f"k{(seed * 37 + i) % 256}"
                if i % 3:
                    shared.put(key, i, ttl=30)
                else:
                    val = shared.get(key)
                    assert val is _MISS or isinstance(val, int)
        except Exception as exc:            # 竞态一旦存在，这里必炸
            errors.append(repr(exc))

    threads = [threading.Thread(target=worker, args=(s,)) for s in range(8)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert not errors, errors
    assert len(shared) <= 64
    print("并发: 8 线程 24000 次操作零异常，size =", len(shared), "<= 64 ✅")
```

**追问**：1) 容量满时为什么不能直接淘汰链表尾？——尾节点只保证「最久未被访问」，不保证「已过期」；反过来，刚写入但 TTL 极短的节点可能紧贴头部。只按 LRU 淘汰会让过期键长期占位：命中率虚低、内存虚高，还会把仍然有效的键提前挤走（本 demo 第二个用例就是验证这条）。正确顺序是「先按过期索引清死键，再按 LRU 序淘汰」，这也是为什么要额外维护一条按 `expire_at` 的索引而不是只靠链表。2) 分段锁之后 LRU 语义变成了什么？容量怎么分？——每片独立维护 LRU，全局最久未访问的键不一定最先被淘汰（它可能落在热点片里被反复续命），严格说是「分片内 LRU」，命中率会比全局 LRU 低几个点。容量若平均切 `cap/N`，热点片会频繁淘汰、冷片白占内存；生产要么按实测倾斜度分配，要么做片间借用（复杂），多数场景接受这种不均衡换吞吐。3) `sweep()` 在锁内全扫会不会把读请求卡死？——会，容量十万级时一次 O(n) 遍历就是几十毫秒的停等，P99 直接起飞。三种降法：增量 sweep（每次最多处理 K 条，游标轮转）、最小堆按到期时间批量取（堆的惰性删除要配「版本号/存在性校验」防误删新值）、把节点先摘链收集到局部列表、出锁后再做引用释放与统计。

## 背诵要点
1. 结构 = `dict` 定位 + 哨兵双向链表排序；`get` 摘链头插、`put` 尾淘汰，均摊 O(1)。
2. 「查过期 + 摘链 + 删表」必须一个临界区完成；锁内不调用用户代码。淘汰前先清死键，否则死键挤活键。
3. 惰性过期保正确、主动 sweep 保内存；O(n) 全扫靠增量/最小堆降本；时钟用 `monotonic`。分段锁换吞吐但 LRU 退化为分片内 LRU。

## 复盘追问
1. 缓存里存的是 10MB 的大对象，`get` 返回引用会不会出问题？（提示：调用方改了对象等于绕过缓存写；要么深拷贝（成本高）、要么存不可变结构、要么约定只读并在 code review 里守住——这是「缓存一致性」在单机内存层的体现）
2. TTL 集中到期（同一批 key 同时写入、同时过期）会发生什么，怎么破？（提示：过期瞬间大量回源打穿到 DB（缓存雪崩），给 TTL 加 ±10% 随机抖动，并配 singleflight 合并同 key 回源）
