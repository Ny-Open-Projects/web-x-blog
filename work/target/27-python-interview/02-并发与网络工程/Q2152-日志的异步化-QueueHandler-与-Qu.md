---
title: [Q2152] 日志的异步化:QueueHandler 与 QueueListener
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2152 · 日志的异步化:QueueHandler 与 QueueListener

> 难度:★★★ | 标签:logging, QueueHandler, 异步日志

**问**:日志写盘慢拖垮业务线程,怎么把"打日志"和"写日志"分开?

**答**:QueueHandler 只把记录塞进内存队列,QueueListener 在独立线程里消费并交给真正的 handler;调用方与慢 sink 彻底解耦。

- 实测模拟远程 syslog 的慢 sink:异步化后单条 34us,同步 606us,约 18 倍;

- 三个业务线程并发打日志,同步版还要在 logging 模块锁上排队;

- listener.stop 保证退出前排干队列,实测落盘 100/100 行;

- 代价:崩溃时队列里未刷出的记录会丢,审计日志别走异步。

```python
# file: code/02_并发与网络工程/q2152_async_logging.py
# -*- coding: utf-8 -*-
"""日志的异步化: QueueHandler 与 QueueListener。

- 业务线程只往内存队列塞记录, 慢接收端由 listener 线程独占承担;
- 实测: 模拟远程 syslog 的慢 sink, 异步化把单条日志调用降到微秒级;
- 代价: 进程崩溃时队列里未刷出的日志会丢, 关键审计日志要另走同步路。
"""
import logging
import logging.handlers
import os
import queue
import tempfile
import threading
import time

q = queue.Queue(-1)


class SlowSink(logging.Handler):
    """模拟慢接收端: 远程 syslog / 审计中转, 每条要 0.3ms。"""

    def emit(self, record):
        time.sleep(0.0003)
        self.format(record)


def make_async_logger(sink, name="q2152-async"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.propagate = False
    logger.handlers = [logging.handlers.QueueHandler(q)]
    listener = logging.handlers.QueueListener(q, sink)
    listener.start()
    return logger, listener


def make_sync_logger(sink, name="q2152-sync"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.propagate = False
    logger.handlers = [sink]
    return logger


def bench(logger, n=200, threads=1):
    def worker(k):
        for i in range(n):
            logger.info("event-%d payload=%s", k * n + i, "x" * 64)
    ts = [threading.Thread(target=worker, args=(k,)) for k in range(threads)]
    t0 = time.monotonic()
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    return (time.monotonic() - t0) / (n * threads)


def main():
    sink = SlowSink()

    logger, listener = make_async_logger(sink)
    async_us = bench(logger, n=200, threads=3) * 1e6
    listener.stop()                       # 排干队列并停 listener
    print("异步化: 3 业务线程单条 %.1f us (只入队, 慢 IO 在 listener 线程)" %
          async_us)

    logger2 = make_sync_logger(sink, name="q2152-sync-2")
    sync_us = bench(logger2, n=200, threads=3) * 1e6
    print("同步写: 3 业务线程单条 %.1f us (每条都在等慢接收端)" % sync_us)
    print("提速约 %.0f 倍: 调用方与慢 sink 彻底解耦, 日志不再拖业务" %
          (sync_us / max(async_us, 1e-6)))

    path = tempfile.mktemp(prefix="q2152_file_")
    fh = logging.FileHandler(path)
    logger3, listener3 = make_async_logger(fh, name="q2152-file")
    bench(logger3, n=100, threads=1)
    listener3.stop()
    with open(path) as f:
        lines = sum(1 for _ in f)
    print("落盘核对: %d/100 行完整, listener.stop 保证退出前排干" % lines)
    os.remove(path)
    print("注意: 崩溃时队列内未刷出的记录会丢, 审计日志不要走异步")


if __name__ == "__main__":
    main()
```

**追问**:1) 队列满了怎么办?——标准库 QueueHandler 用无界队列,生产要换有界队列并定义丢弃策略,否则内存会被慢 sink 拖爆。2) 多进程下呢?——QueueListener 只管线程,多进程要用 QueueHandler 连到一个集中收集进程,或直接写本地文件让采集器收。3) QueueHandler 的队列选型与丢弃策略?——标准库 QueueHandler 无界队列(慢 sink 拖爆内存);生产换有界队列+丢弃策略(丢 DEBUG/INFO,保 WARNING+)+丢弃计数指标——日志丢失是可接受的(丢等级要设计),审计日志例外(Q709)。4) 多进程的日志架构怎么选?——QueueHandler 连集中收集进程(单点+复杂度);或各进程直接写本地文件由采集器收(简单、文件轮转交给 logrotate)——「集中 vs 分散」按运维能力选;QueueListener 只管线程不管进程(Q2152 原问)。5) 生产陷阱?——慢 sink 在 listener 里重试无限(队列积压);listener.stop 没调(退出丢日志,实测 100/100 依赖它);审计日志走异步(崩溃丢失);丢弃策略无指标(静默丢);多进程共享同一文件句柄(交叉写坏行)。

---
