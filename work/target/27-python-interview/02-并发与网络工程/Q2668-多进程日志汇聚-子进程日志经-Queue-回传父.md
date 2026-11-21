---
title: [Q2668] 多进程日志汇聚:子进程日志经 Queue 回传父进程
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2668 · 多进程日志汇聚:子进程日志经 Queue 回传父进程

> 难度:★★★ | 标签:多进程, 日志, QueueHandler

**问**:4 个进程同时写一个日志文件,怎么保证不写花?

**答**:每个子进程只挂一个 QueueHandler:日志记录被 pickle 后送进队列;父进程扮演 listener,单点收日志、统一格式、统一输出。实测 2 个 worker 的 8 条日志全部经队列汇聚,listener 收到 8 条、格式一处可控。写同一文件抢的是文件偏移,队列方案从根上消灭了竞争。

- logging.handlers.QueueHandler 负责序列化记录,listener 端 logger.handle 原地重放;

- listener 是独立进程,收工靠哨兵(None)或超时,别让 daemon 子进程直接蒸发;

- 记录里带不上无法 pickle 的对象,日志消息要用参数化格式而不是 f-string 拼对象;

- 队列方案顺带解决了多进程写文件与按进程翻页的所有坑。

```python
# file: code/02_并发与网络工程/q2668_multiproc_logging.py
# -*- coding: utf-8 -*-
"""多进程日志汇聚: 子进程日志经 Queue 回传父进程统一落盘。

- 子进程只挂一个 QueueHandler: 日志记录被 pickle 后送进队列;
- 父进程跑 QueueListener 角色: 单点收日志、统一格式、统一输出;
- 好处: 不抢同一个日志文件, 格式一处可改, 也不会写花。
"""
import logging
import logging.handlers
import multiprocessing as mp
import sys
import time
from multiprocessing import Process, Queue


def listener_proc(q, counter):
    relay = logging.getLogger("relay")
    relay.setLevel(logging.INFO)
    h = logging.StreamHandler(sys.stdout)
    h.setFormatter(logging.Formatter("[来自 %(name)s] %(message)s"))
    relay.addHandler(h)
    n = 0
    while True:
        rec = q.get()
        if rec is None:                  # 收工哨兵
            break
        relay.handle(rec)
        n += 1
    counter.value = n


def worker_init(q):
    root = logging.getLogger()
    root.setLevel(logging.INFO)
    root.addHandler(logging.handlers.QueueHandler(q))


def wjob(i):
    logging.getLogger("worker.%d" % (i % 2)).info("task %d done", i)
    return i


if __name__ == "__main__":
    q = Queue()
    counter = mp.Value("i", 0)
    lp = Process(target=listener_proc, args=(q, counter), daemon=True)
    lp.start()

    with mp.Pool(2, initializer=worker_init, initargs=(q,)) as pool:
        pool.map(wjob, range(8))

    time.sleep(0.3)                      # 等子进程的记录飞到队列
    q.put(None)
    lp.join(timeout=3)
    print("listener 汇聚了 %d 条日志(应为 8)" % counter.value)
```

**追问**:1) 为什么不用每个进程写各自文件?——文件数随进程数膨胀,聚合视图要自己拼,而且滚动策略要复制 N 份。2) 队列满了会怎样?——QueueHandler 的 emit 会阻塞或丢弃(取决于实现),日志洪峰要靠级别过滤与限流控制。3) 底层机制:多进程直写同一文件为什么会写花?——logging 的 emit 是"格式化+可能多次 write",即便 O_APPEND 让单次 write 原子,两次 write 之间也会插入别的进程,行内交错;QueueHandler 把格式化与落盘集中到 listener 单点,竞争从根上消失。4) 生产陷阱?——日志记录携带不可 pickle 的对象,QueueHandler 序列化报错;listener 是 daemon 进程,主进程退出时被斩,尾部日志丢失;worker 里残留 FileHandler,直写与队列双路并存。

---
