---
title: [Q1850] 任务窃取 work stealing 概念模拟:自队尾取自队头偷
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1850 · 任务窃取 work stealing 概念模拟:自队尾取自队头偷

> 难度:★★★ | 标签:work stealing, 负载均衡, 双端队列

**问**:为什么有的运行时要给每个 worker 一个私有队列,而不是全局一个大队列?饿了怎么办?

**答**:全局队列是所有 worker 的争用热点,私有队列让大多数操作无锁无争;但私有队列带来负载不均,所以饿的 worker 去 '偷' 别人队列里的任务,这就是 work stealing。

- 方向约定:worker 从自己双端队列的尾部取(最新鲜、局部性好),从别人队列的头部偷(最老的任务,等得最久);

- 偷是逐个试探 victim 的锁,一次偷一个,争用被限制在单个 victim 上,不需要全局锁;

- 演示给四个 worker 播种 12、6、1、0 个任务,空队列的饿汉靠偷活了下来,十九个任务恰好各执行一次。

Python 的 multiprocessing.Pool 内部就是共享队列而非窃取,自研窃取池通常用每个 worker 一把锁的双端队列起步。

```python
# file: code/02_并发与网络工程/q1850_work_stealing.py
# -*- coding: utf-8 -*-
"""任务窃取 work stealing 概念模拟: 自己的队列尾取, 偷别人的队列头。

- 每个 worker 拥有双端队列: 自己从尾部取(局部性好), 饿了从别人头部偷(最老的先跑);
- 偷是逐个试探别人的锁, 不加全局锁, 争用被限制在单个 victim 上;
- 负载天然倾斜时, 饿汉 worker 只能靠偷活下来, 这就是窃取的负载均衡作用。
"""
import collections
import threading
import time

WORKERS = 4


class StealingPool:
    def __init__(self, n):
        self._own = [collections.deque() for _ in range(n)]
        self._locks = [threading.Lock() for _ in range(n)]
        self._exec = collections.defaultdict(list)   # worker -> task ids
        self._steals = []                            # (thief, victim)
        self._lock = threading.Lock()

    def seed(self, idx, task_ids):
        with self._locks[idx]:
            self._own[idx].extend(task_ids)

    def _pop_own(self, idx):
        with self._locks[idx]:
            return self._own[idx].pop() if self._own[idx] else None

    def _steal_one(self, idx):
        n = len(self._own)
        for step in range(1, n + 1):
            victim = (idx + step) % n
            with self._locks[victim]:
                if self._own[victim]:
                    t = self._own[victim].popleft()   # 偷最老的
                    with self._lock:
                        self._steals.append((idx, victim))
                    return t
        return None

    def worker(self, idx):
        while True:
            t = self._pop_own(idx)
            if t is None:
                t = self._steal_one(idx)
            if t is None:
                time.sleep(0.003)
                with self._lock:
                    total = sum(len(v) for v in self._exec.values())
                if total >= EXPECTED_TOTAL:
                    return
                continue
            time.sleep(0.002)                     # 模拟执行
            with self._lock:
                self._exec[idx].append(t)


EXPECTED_TOTAL = 19


def main():
    pool = StealingPool(WORKERS)
    pool.seed(0, ["t%02d" % i for i in range(12)])
    pool.seed(1, ["s%02d" % i for i in range(6)])
    pool.seed(2, ["u00"])
    pool.seed(3, [])                              # 饿汉, 只能偷

    ts = [threading.Thread(target=pool.worker, args=(i,)) for i in range(WORKERS)]
    for t in ts:
        t.start()
    for t in ts:
        t.join(timeout=10.0)
        assert not t.is_alive(), "窃取池应正常收敛退出"

    done = []
    for idx in range(WORKERS):
        done.extend(pool._exec[idx])
    print("各 worker 执行分布:", {("w%d" % i): len(pool._exec[i]) for i in range(WORKERS)})
    print("窃取事件数:", len(pool._steals), "样例:", pool._steals[:5])
    assert len(done) == EXPECTED_TOTAL and len(set(done)) == EXPECTED_TOTAL, \
        "所有任务恰好执行一次"
    assert len(pool._exec[3]) >= 1, "空队列的饿汉 worker 必须靠窃取获得任务"
    assert len(pool._steals) >= 1, "至少发生一次窃取"
    print("结论: 自队尾取自队头偷, 无全局锁也完成了负载均衡")


if __name__ == "__main__":
    main()
```

**追问**:1) 真实窃取为什么一次偷一半而不是一个?——一次偷一个会在饥饿与争用之间反复拉锯;偷一半(Java ForkJoinPool 的做法)摊薄探测开销,让重负载节点更快卸货。2) 「自尾取自头偷」的局部性原理是什么?——worker 刚放的任务在最尾(缓存/上下文还热),自尾取局部性最好;偷取从队头拿「等得最久」的,减少任务饥饿时间;两端分工让「自己人无争用+外人低争用」同时成立。3) 窃取与全局队列怎么混合?——主流设计(ForkJoin/Go):本地队列+全局队列双源,先取本地、再偷、最后吃全局;偷取是负载均衡的「最后手段」,探测顺序(随机 victim)避免热点;Python 的 free-threading 时代这类结构会更常见。4) 生产陷阱?——偷取无随机性(总偷同一个 victim,热点转移);victim 锁与 owner 操作死锁(拿 victim 锁时 owner 正在两端操作,要同一把锁或无锁 CAS);任务粒度过细(窃取开销超过任务本身);窃取计数不观测(负载不均问题被隐藏)。


---
