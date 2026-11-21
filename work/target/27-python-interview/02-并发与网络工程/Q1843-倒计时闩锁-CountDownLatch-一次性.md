---
title: [Q1843] 倒计时闩锁 CountDownLatch:一次性计数汇聚点
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1843 · 倒计时闩锁 CountDownLatch:一次性计数汇聚点

> 难度:★★☆ | 标签:Latch, 同步, 优雅启动

**问**:Java 里遍地都是 CountDownLatch,Python 没有,它和 Event 差在哪?怎么自己实现一个?

**答**:Latch 是 '还差几个' 的量化汇聚:计数到零对所有人永久放行,之后任何 wait 都立即通过,永不复位;Event 是二态开关,天然可 set/clear,但数不了进度。

- 实现就是一个 Condition 加一个只减不增的计数,count_down 到零时 notify_all 广播放行;

- wait 必须支持 timeout,返回 True/False 而不是抛异常——'还没就绪' 是正常业务状态不是错误;

- 典型用途:主流程等 n 个子系统初始化完毕再对外服务,演示里 db、cache、config 三个倒计时者到齐后主流程放行。

和 Event 的分工:Event 管 '开关状态',Latch 管 '汇聚进度';需要重复开合的一组信号,还要上 Condition 自己维护。

```python
# file: code/02_并发与网络工程/q1843_countdown_latch.py
# -*- coding: utf-8 -*-
"""倒计时闩锁 CountDownLatch: 一次性计数到零的汇聚点。

- 与 Event 的差别: Event 是二态开关且天然可重置, Latch 表达 "还差几个" 的量化语义;
- count_down 只减不增, 到零后对所有人永久放行, wait 支持 timeout 非阻塞探测;
- 典型用途: 主流程等 n 个子系统就绪、汇聚多个并行任务的完成信号。
"""
import threading
import time


class CountDownLatch:
    def __init__(self, n):
        assert n >= 0
        self._cond = threading.Condition()
        self._count = n

    def count_down(self):
        with self._cond:
            if self._count > 0:
                self._count -= 1
                if self._count == 0:
                    self._cond.notify_all()   # 到零广播放行

    def wait(self, timeout=None):
        with self._cond:
            deadline = None if timeout is None else time.monotonic() + timeout
            while self._count > 0:
                if deadline is None:
                    self._cond.wait(0.5)
                else:
                    remain = deadline - time.monotonic()
                    if remain <= 0:
                        return False
                    self._cond.wait(remain)
            return True

    @property
    def count(self):
        with self._cond:
            return self._count


def main():
    # 场景一: 主线程等 3 个子系统就绪
    latch = CountDownLatch(3)
    ready_log = []

    def subsystem(name, cost):
        time.sleep(cost)
        ready_log.append(name)
        latch.count_down()

    for name, cost in [("db", 0.05), ("cache", 0.03), ("config", 0.08)]:
        threading.Thread(target=subsystem, args=(name, cost)).start()

    t0 = time.monotonic()
    ok = latch.wait(timeout=2.0)
    print("三个子系统就绪:", ready_log, "等待耗时: %.2fs" % (time.monotonic() - t0))
    assert ok and latch.count == 0, "latch 应当计数到零"

    # 场景二: 只有一个倒计时者, 探测超时返回 False 而不是抛异常
    latch2 = CountDownLatch(2)
    threading.Thread(target=latch2.count_down).start()
    ok2 = latch2.wait(timeout=0.2)
    print("缺一个倒计时者, 带超时 wait 返回:", ok2, "剩余计数:", latch2.count)
    assert ok2 is False and latch2.count == 1, "超时应返回 False 且计数不变"

    # 对照: Event 无法表达 "还差几个", 只能表达 "发生了没有"
    ev = threading.Event()
    print("对照 Event: 只有 set/clear 两态, 数不了进度")
    print("结论: Latch = 带计数的单次汇聚点, 超时探测返回 False 不抛异常")


if __name__ == "__main__":
    main()
```

**追问**:1) Latch 计数能再加回去吗?——不能,这正是它与 Semaphore 的本质区别;可重置的计数语义请用 Condition 自己实现,Semaphore 的 release 会加计数,语义完全不同。2) wait 返回 True/False 而不是抛异常为什么是对的?——「还没就绪」是正常业务状态不是错误:调用方要么再等要么放弃,用返回值表达比异常便宜且不会被 try/except 误吞;这也是 Latch 与 Barrier(broken 是真错误)的语义差异之一。3) Latch 与 gather/Event 的组合边界?——asyncio 世界里 gather 本身就是「等 N 个完成」的 Latch,线程世界才是自实现的主场;混合场景(线程初始化+主线程放行)用 Latch 做「线程→主线程」的汇聚点,Event 做不了计数只能做开关。4) 生产陷阱?——count_down 漏调(计数永远到不了零,全场挂起,要配超时);把 Latch 用成可重复开关(复位语义不支持);子任务异常没 count_down(finally 里补);wait 无 timeout(初始化失败永久阻塞服务启动)。


---
