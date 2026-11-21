---
title: [Q612] 无锁计数:per-thread 分片聚合
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q612 · 无锁计数:per-thread 分片聚合

> 难度:★★★☆ | 标签:无锁, 计数器, 性能

**问**:高频指标计数(每秒百万次)怎么做才不成为锁瓶颈?

**答**:per-thread 缓冲聚合:每个线程只写自己的本地计数(threading.local,无任何竞争),读取方聚合所有分片求和——写路径零锁零竞争,读路径 O(线程数)。这正是 metrics 库(Prometheus client)和数据库统计的经典做法。对比实验里,全局单锁版本随线程数线性恶化,分片版本基本平坦。注意点:分片发现需要注册表(新线程首次写时登记);读到的总和允许毫秒级滞后(弱一致),监控场景完全可接受。

```python
# file: code/02_并发与网络工程/q612_per_thread_counter.py
import threading
import time


class PerThreadCounter:
    def __init__(self) -> None:
        self._local = threading.local()
        self._shards: list = []
        self._reg = threading.Lock()  # 只在首次注册时竞争

    def incr(self) -> None:
        shard = getattr(self._local, "shard", None)
        if shard is None:
            shard = self._local.shard = [0]
            with self._reg:
                self._shards.append(shard)
        shard[0] += 1  # 本地计数: 无锁无竞争

    def total(self) -> int:
        return sum(s[0] for s in self._shards)  # 弱一致快照


class LockedCounter:
    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._n = 0

    def incr(self) -> None:
        with self._lock:
            self._n += 1

    def total(self) -> int:
        return self._n


def bench(counter, n_threads=4, n_iter=300000) -> float:
    ts = [
        threading.Thread(
            target=lambda: [counter.incr() for _ in range(n_iter)]
        )
        for _ in range(n_threads)
    ]
    t0 = time.perf_counter()
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    return time.perf_counter() - t0


if __name__ == "__main__":
    p, l = PerThreadCounter(), LockedCounter()
    tp = bench(p)
    tl = bench(l)
    print(f"per-thread: {tp:.3f}s, 单锁: {tl:.3f}s, 提速约 {tl / tp:.1f}x")
    print("计数校验:", p.total(), l.total(), "(期望均 1200000)")
    assert p.total() == l.total() == 4 * 300000
```

**追问**:1) 本地分片会不会丢数据?——线程活着就不会;线程退出前不 flush 的话其分片仍在 _shards 里可被聚合,除非你按线程生命周期清理,这时的取舍要写进文档。2) per-thread 分片的实现?——threading.local 或按 thread ident 的 dict;聚合时遍历分片求和(读端加锁或快照);与全局锁计数对比:写端零竞争、读端聚合 O(分片数)。3) 与 Q612 场景的适配?——高频写(计数、指标)收益大;需要强一致单值时不用;聚合的「瞬间一致性」语义要文档化。4) 生产陷阱?——分片随线程创建无限增长(线程池固定则可控);聚合与写并发时轻微误差;监控拿「聚合值」当「实时值」。

---
