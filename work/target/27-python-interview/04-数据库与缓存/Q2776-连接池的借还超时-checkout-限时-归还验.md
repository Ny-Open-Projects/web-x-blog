---
title: [Q2776] 连接池的借还超时: checkout 限时 归还验活
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2776 · 连接池的借还超时: checkout 限时 归还验活

> 难度:★★★☆ | 标签:连接池, 运维

**问**:连接池借不出连接时,应该一直等还是立刻报错?

**答**:都不是,正确语义是限时等待:checkout 带超时(几百毫秒量级),超时抛出明确异常,让上游快速失败并触发降级,而不是无限排队把线程池一起拖垮——"连接池打满"事故的放大器往往就是无限等待的 checkout。配套两个动作:借出前验活,拿到的连接先发一个轻量探测,坏连接当场丢弃换下一个,避免把断连交给业务在半路炸;归还时区分健康与异常,异常连接直接关闭不回池。观测上,checkout 等待时长与超时次数是池容量的直接信号,超时开始非零就该扩池或查慢查询占坑。借还语义写清楚了,池才是可运维的组件,不是黑盒。

```python
# file: code/04_数据库与缓存/q2776_pool_checkout_timeout.py
"""连接池的借还超时: checkout 限时, 借出前验活, 死连接丢弃"""
import queue
import sqlite3
import threading
from contextlib import contextmanager

class BrokenConn:
    def execute(self, *args):
        raise RuntimeError("连接已断")

class Pool:
    def __init__(self, size, checkout_timeout=0.3):
        self._free = queue.LifoQueue()
        self.timeout = checkout_timeout
        self.timed_out = 0
        self.discarded = 0
        for _ in range(size):
            conn = sqlite3.connect(":memory:")
            conn.execute("CREATE TABLE IF NOT EXISTS t (x)")
            self._free.put(conn)

    @contextmanager
    def borrow(self):
        conn = self._checkout()
        try:
            yield conn
        finally:
            self._free.put(conn)

    def _checkout(self):
        while True:
            try:
                conn = self._free.get(timeout=self.timeout)
            except queue.Empty:
                self.timed_out += 1
                raise TimeoutError("checkout 超时: 池已借空且等待超时")
            try:
                conn.execute("SELECT 1").fetchone()     # 借出前验活
                return conn
            except Exception:
                self.discarded += 1                     # 死连接丢弃, 换下一个
                if self._free.empty():
                    self.timed_out += 1
                    raise TimeoutError("池内连接全部失效")

# 1) 池里混进死连接: 验活当场发现并丢弃
pool = Pool(3)
pool._free.put(BrokenConn())
with pool.borrow() as conn:
    conn.execute("SELECT 1").fetchone()
print("验活: 死连接被丢弃 %d 个, 业务拿到的是好连接" % pool.discarded)

# 2) 借空超时: 2 连接池, 3 个借者各持有 0.4s, checkout 限时 0.3s
pool2 = Pool(2, checkout_timeout=0.3)
results = []
barrier = threading.Barrier(3)

def worker(i):
    barrier.wait()
    try:
        with pool2.borrow() as conn:
            conn.execute("SELECT 1").fetchone()
            threading.Event().wait(0.4)
        results.append("ok%d" % i)
    except TimeoutError:
        results.append("timeout%d" % i)

threads = [threading.Thread(target=worker, args=(i,)) for i in range(3)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print("借还结果:", sorted(results), "| 超时计数 %d (快速失败而不是无限等)" % pool2.timed_out)
```

**追问**:
- checkout 超时设多长?—— 略大于正常等待 P99,通常几百毫秒;设成池打满时的可接受排队时间,而不是数据库查询超时。
- 归还要不要验活?—— 不需要,归还路径要零开销,坏连接交给下次借出时的验活拦截。

---
