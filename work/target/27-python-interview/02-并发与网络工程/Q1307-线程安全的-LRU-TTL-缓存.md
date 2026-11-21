---
title: [Q1307] 线程安全的 LRU + TTL 缓存
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1307 · 线程安全的 LRU + TTL 缓存

> 难度:★★★☆ | 标签:LRU, TTL, 缓存

**问**:手写一个线程安全的 LRU 缓存,要求带 TTL,你会怎么做?哪些操作必须是原子的?

**答**:容器用 OrderedDict,命中时 move_to_end 把键挪到队尾,容量超限时 popitem(last=False) 弹出队头——LRU 语义就绪。TTL 只需在每个条目上记一个过期时间戳,get 时发现过期就当作未命中并删除。原子性是关键:get 的"读、判过期、move_to_end"三步必须整体持锁,否则两个读者同时 move_to_end 或一边读一边被淘汰都会出诡异状态;put 的"写入 + 驱逐超限"同样整体持锁。锁的粒度已经足够细(纳秒级操作),不需要再分段;若真要降竞争,可以按 key 哈希分片。可选优化:过期清理不做后台线程,而是写在 put 时顺带抽查几个键,避免定时器复杂度。下面的演示验证容量驱逐、TTL 过期与并发计数。

```python
# file: code/02_并发与网络工程/q1307_lru_ttl_cache.py
import collections
import threading
import time


class LRUTTLCache:
    def __init__(self, capacity: int, ttl: float) -> None:
        self._capacity = capacity
        self._ttl = ttl
        self._data = collections.OrderedDict()  # key -> (value, expire_at)
        self._lock = threading.Lock()
        self.hit = 0
        self.miss = 0
        self.evicted = 0
        self.expired = 0

    def get(self, key):
        now = time.monotonic()
        with self._lock:
            item = self._data.get(key)
            if item is None:
                self.miss += 1
                return None
            value, expire_at = item
            if expire_at <= now:
                del self._data[key]
                self.expired += 1
                return None
            self._data.move_to_end(key)
            self.hit += 1
            return value

    def put(self, key, value) -> None:
        now = time.monotonic()
        with self._lock:
            self._data[key] = (value, now + self._ttl)
            self._data.move_to_end(key)
            while len(self._data) > self._capacity:
                self._data.popitem(last=False)
                self.evicted += 1


def main() -> None:
    cache = LRUTTLCache(capacity=3, ttl=0.1)
    cache.put("a", 1)
    cache.put("b", 2)
    cache.put("c", 3)
    cache.put("d", 4)                    # 挤出最久未用的 a
    assert cache.get("a") is None
    assert cache.get("d") == 4
    cache.put("e", 5)                    # 挤出 b
    assert cache.get("b") is None
    time.sleep(0.15)                     # 全部过期
    assert cache.get("c") is None and cache.get("e") is None

    cache2 = LRUTTLCache(capacity=100, ttl=10)
    def worker(seed: int) -> None:
        for i in range(2000):
            k = (i * seed) % 50
            if i % 3 == 0:
                cache2.put(k, k)
            else:
                v = cache2.get(k)
                assert v is None or v == k
    threads = [threading.Thread(target=worker, args=(s + 1,)) for s in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(f"驱逐 {cache.evicted}, 过期 {cache.expired}; "
          f"并发后 命中 {cache2.hit} 未命中 {cache2.miss}, 容量守恒 {len(cache2._data) <= 100}")
    print("LRU + TTL 语义验证通过")


if __name__ == "__main__":
    main()
```

**追问**:1) 为什么过期判断不用后台线程统一扫?——惰性过期在读写路径顺带完成,实现简单且无额外线程;后台扫描只在大容量、冷键堆积时才有必要,而且要与写锁配合避免扫到一半被改。2) get 里「判过期就删」的并发细节?——过期删除也要持锁(或确认 OrderedDict 的单操作原子边界);更隐蔽的是「读时过期未删+写时驱逐」交错,条目计数与实际不符;最简纪律:所有容器变更都进锁,锁内只做纳秒级操作。3) 什么时候才需要分片?——基准先行:CPython 锁开销在微秒级,单锁 LRU 通常扛到数万 QPS;真有瓶颈再按 key 哈希分片(每片独立锁),分片数取 2 的幂,代价是全局聚合(全量快照/统计)要按固定序拿全部片锁防死锁(Q572)。4) 生产陷阱?——move_to_end 放在锁外引发竞态;TTL 用 time.time(NTP 跳变,用 monotonic);缓存对象可变且被调用方改坏;命中统计与驱逐统计不一致,容量诊断失真。

---
