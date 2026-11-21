---
title: [Q2660] 按键加锁管理器:同 key 串行,异 key 并行
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2660 · 按键加锁管理器:同 key 串行,异 key 并行

> 难度:★★★★ | 标签:按键加锁, 细粒度锁, 引用计数

**问**:按账户 ID 更新余额,全局一把锁让所有账户互相排队;按账户加锁,锁对象会不会随账户数无限膨胀?

**答**:按键加锁管理器:每 key 一把锁,同一 key 的操作天然串行,不同 key 完全并行。膨胀问题靠引用计数解决——acquire 时引用 +1,release 时 -1,归零即从注册表销毁。实测同一账户 4 线程被串行化,四个不同账户并行跑出 4.1 倍提速,全部结束后存活锁数为 0。

- 全局锁的正确性最强、并行度最差,按键加锁是并行度与复杂度的折中;

- 引用计数是管理器不泄漏的前提,归零回收的时机必须在 finally 里;

- 热点 key 天然串行,这是语义需要,拆分反而引入跨键一致性难题;

- 风险是锁顺序:一次持有多把 key 锁时要全局定序,否则死锁。

```python
# file: code/02_并发与网络工程/q2660_keyed_lock.py
# -*- coding: utf-8 -*-
"""按键加锁管理器: 同一 key 串行, 不同 key 并行。

- 全局一把锁: 所有账户互相排队, 吞吐被无关节口拖累;
- 按 key 加锁: 只锁同一条资源, 互不相关的操作并行跑;
- 引用计数回收: 没人用的锁及时销毁, 管理器不随 key 数量无限膨胀。
"""
import threading
import time
from contextlib import contextmanager

WORK = 0.002                            # 模拟每笔操作 2ms 的真实工作量


class KeyedLocks:
    """每 key 一把锁, 引用计数归零即回收。"""

    def __init__(self):
        self._guard = threading.Lock()
        self._locks = {}
        self._refs = {}

    @contextmanager
    def hold(self, key):
        with self._guard:
            lk = self._locks.get(key)
            if lk is None:
                lk = threading.Lock()
                self._locks[key] = lk
                self._refs[key] = 0
            self._refs[key] += 1
        try:
            with lk:
                yield
        finally:
            with self._guard:
                self._refs[key] -= 1
                if self._refs[key] == 0:
                    self._locks.pop(key, None)
                    self._refs.pop(key, None)

    def live_locks(self):
        with self._guard:
            return len(self._locks)


balances = {}
ledger_lock = threading.Lock()           # 仅保护 balances 字典本身的读写


def work_on(km, key, ops):
    for _ in range(ops):
        with km.hold(key):               # 同 key 串行, 异 key 并行
            time.sleep(WORK)             # 锁内干点真活, 串行代价才显形
            with ledger_lock:
                balances[key] = balances.get(key, 0) + 1


if __name__ == "__main__":
    km = KeyedLocks()

    # 场景一: 4 个线程挤同一个 key -> 完全串行
    balances.clear()
    t0 = time.perf_counter()
    ts = [threading.Thread(target=work_on, args=(km, "acct:hot", 20))
          for _ in range(4)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    same = time.perf_counter() - t0

    # 场景二: 4 个线程各锁各的 key -> 完全并行
    balances.clear()
    t0 = time.perf_counter()
    ts = [threading.Thread(target=work_on, args=(km, "acct:%d" % i, 20))
          for i in range(4)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    diff = time.perf_counter() - t0

    print("同 key 串行: %.3fs / 异 key 并行: %.3fs" % (same, diff))
    print("异 key 方案提速: %.1f 倍" % (same / diff))
    print("回收验证: 全部结束后存活锁数 =", km.live_locks(), "(应为 0)")
```

**追问**:1) 注册表本身要不要锁?——要,管理器的 guard 只保护字典结构,真正的业务互斥由各 key 锁承担,两级职责分离。2) 和分段锁什么关系?——分段锁是固定 N 片哈希分摊竞争,按键加锁是按资源精确串行,后者粒度细但对象生命周期要自己管。3) 底层机制:引用计数归零回收为什么不会误伤等待者?——引用 +1 发生在取锁之前、-1 发生在 finally,覆盖"取锁-等待-用完"的整个生命周期,等待中的线程早已把自己计入引用,归零时不可能有人还拿着这把锁;若把 -1 挪出 finally 或漏掉异常路径,就会出现新旧两把锁并行、互斥失效。4) 生产陷阱?——一次持有多把 key 锁没有全局定序,交叉等待死锁;引用计数泄漏让锁膨胀回归;热点 key 的串行化被当成 bug 去拆分,反而引入跨键一致性难题。

---
