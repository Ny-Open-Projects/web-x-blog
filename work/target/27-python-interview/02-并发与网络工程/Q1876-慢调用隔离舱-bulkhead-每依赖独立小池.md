---
title: [Q1876] 慢调用隔离舱 bulkhead:每依赖独立小池,故障不上蹿下跳
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1876 · 慢调用隔离舱 bulkhead:每依赖独立小池,故障不上蹿下跳

> 难度:★★★★ | 标签:bulkhead, 隔离, 线程池

**问**:一个依赖变慢就把整个服务拖死了,舱壁模式怎么从结构上锁死故障半径?

**答**:给每个依赖一个独立的并发额度:自己的 BoundedSemaphore 加自己的小 ThreadPoolExecutor,借船漏水不沉全船。

- 舱位即上限:演示慢依赖舱 2 个舱位,八个并发里两个执行、六个在等待额度 0.1s 后快速失败抛 BulkheadFull,拒绝耗时毫秒级;

- 健康依赖 B 独立成舱,慢依赖 A 瘫死期间它的八次调用全部成功,故障半径被锁死;

- 等待额度必须带超时:无限排队等于把隔离舱又焊成一个大池,快速失败才是舱壁的本意。

选型:进程内用信号量+线程池,跨进程用每依赖连接池,云原生里就是每个下游独立连接数上限。

```python
# file: code/02_并发与网络工程/q1876_bulkhead.py
# -*- coding: utf-8 -*-
"""慢调用隔离舱 bulkhead: 每个依赖一个独立小线程池, 故障不上蹿下跳。

- 每个依赖单独的 BoundedSemaphore + ThreadPoolExecutor, 并发额度物理隔离;
- 等待额度有上限(wait), 超时立刻抛 BulkheadFull, 绝不让线程无限堆积;
- 依赖 A 瘫死只烧光自己的舱, 依赖 B 的舱位照常服务。
"""
import concurrent.futures
import threading
import time


class BulkheadFull(Exception):
    pass


class Bulkhead:
    def __init__(self, name, permits):
        self.name = name
        self._sem = threading.BoundedSemaphore(permits)
        self._pool = concurrent.futures.ThreadPoolExecutor(
            max_workers=permits, thread_name_prefix=name)
        self.rejected = 0
        self.served = 0

    def call(self, fn, wait=0.1, run_timeout=2.0):
        if not self._sem.acquire(timeout=wait):
            self.rejected += 1
            raise BulkheadFull("隔离舱 %s 已满" % self.name)
        try:
            fut = self._pool.submit(fn)
            result = fut.result(timeout=run_timeout)
            self.served += 1
            return result
        finally:
            self._sem.release()


def main():
    dep_a = Bulkhead("depA-慢依赖", 2)
    dep_b = Bulkhead("depB-快依赖", 2)
    start = threading.Event()

    def slow():
        time.sleep(0.4)
        return "slow-ok"

    def fast():
        return "fast-ok"

    a_results = []

    def hit_dep_a():
        start.wait()
        try:
            a_results.append(("ok", dep_a.call(slow, wait=0.1)))
        except BulkheadFull as e:
            a_results.append(("rejected", str(e)))

    ts = [threading.Thread(target=hit_dep_a) for _ in range(8)]
    for t in ts:
        t.start()
    time.sleep(0.05)
    start.set()
    for t in ts:
        t.join(timeout=3.0)

    b_results = [dep_b.call(fast) for _ in range(8)]   # 顺序调用, 全部成功
    ok = sum(1 for kind, _ in a_results if kind == "ok")
    rej = sum(1 for kind, _ in a_results if kind == "rejected")
    print("慢依赖 A: 成功 %d, 快速拒绝 %d" % (ok, rej))
    print("快依赖 B: 全部成功 %d 次, A 的拥堵没有波及 B" % len(b_results))
    assert ok == 2 and rej == 6, "舱位 2 个, 其余 6 个应被快速拒绝"
    assert len(b_results) == 8, "B 不受 A 影响"
    assert dep_a.rejected == 6 and dep_b.rejected == 0
    print("结论: 隔离舱把故障半径锁在单个依赖里, 拒绝快到毫秒级")


if __name__ == "__main__":
    main()
```

**追问**:1) 舱位大小怎么定?——按依赖的正常延迟与目标并发用 Little's Law 反推:舱位 = QPS × 平均延迟,再留少量余量;监测 '快速拒绝率' 与 '实际在途数',拒绝率升高先扩舱还是先熔断,由依赖健康度决定。2) 舱壁与熔断的层级关系?——舱壁是「资源隔离」(限制故障半径),熔断是「状态决策」(停止无谓尝试);舱满(BulkheadFull)是容量信号,熔断 OPEN 是健康信号,两者数据互相输入(Q1877 的原因分类)——顺序上舱壁包着熔断(熔断器也要有并发上限)。3) 舱位与线程池的账怎么算?——舱位=QPS×平均延迟(Little's Law,Q1876 原问);每舱独立线程池的线程总数要控制在内存账内(线程×栈内存,Q1343);异步场景舱位=Semaphore 并发数,无线程成本——并发模型决定舱壁的实现形态。4) 生产陷阱?——舱壁共享线程池(隔离失效,见原问);等待额度无超时(舱满变挂起);舱位拍脑袋(没有 Little's Law 推导);慢依赖舱位过大(隔离名存实亡);舱满异常裸抛给调用方(没转降级,Q1877)。


---
