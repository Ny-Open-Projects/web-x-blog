---
title: [Q2664] 池内崩溃毒化全池:一个 worker 被杀,整个池进入残局
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2664 · 池内崩溃毒化全池:一个 worker 被杀,整个池进入残局

> 难度:★★★★ | 标签:进程池, BrokenProcessPool, 崩溃

**问**:任务抛异常池子还能用,那 worker 进程被 kill -9 杀掉呢?

**答**:性质完全不同:任务异常只是数据层面回传,池照常服务;worker 被 SIGKILL 是进程层面死亡,池被判 broken——实测崩溃任务本身抛 BrokenProcessPool,与它同池的在途任务一并失败,旧池继续提交也立即 BrokenProcessPool,唯一出路是重建一个新池。这就是"崩溃毒化全池":池无法确认死掉的 worker 手里有哪些任务,只能宣布全部作废。

- 业务异常与进程崩溃必须分诊:前者重试任务,后者重建池;

- os._exit、kill -9、段错误都会触发毒化,任务代码里绝不能裸调;

- 崩溃 worker 的退出码是负数(-9 表示 SIGKILL),监控上按"进程异常死亡"告警;

- 池重建要容忍在途任务丢失:上层必须能重发,这是至少一次语义的代价。

```python
# file: code/02_并发与网络工程/q2664_pool_crash.py
# -*- coding: utf-8 -*-
"""池内崩溃毒化全池: 一个 worker 被杀, 整个池进入残局。

- 任务抛异常只毒化自己: 异常回传, 池继续可用;
- worker 进程被 SIGKILL 杀掉(退出码 -9): 池被判 broken;
- broken 池对在途与后续所有提交一律 BrokenProcessPool, 只能重建。
"""
import os
import signal
import time
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures.process import BrokenProcessPool


def slow_good(x):
    time.sleep(0.4)                      # 慢任务, 保证崩溃时在途
    return x * 2


def suicide(_):
    """模拟 worker 被外部 kill -9: 进程直接消失, 没有异常回传。"""
    os.kill(os.getpid(), signal.SIGKILL)


def status(f):
    if f.cancelled():
        return "cancelled"
    if f.done():
        exc = f.exception()
        return type(exc).__name__ if exc else "ok"
    return "pending"


if __name__ == "__main__":
    ex = ProcessPoolExecutor(max_workers=2)
    print("崩溃前正常任务:", ex.submit(slow_good, 1).result())

    pending = [ex.submit(slow_good, i) for i in (2, 3, 4, 5)]
    boom = ex.submit(suicide, 0)
    try:
        boom.result()
        print("竟然没炸")
    except BrokenProcessPool as e:
        print("崩溃任务:", type(e).__name__, "->", str(e)[:52])

    for f in pending:
        try:
            f.result(timeout=10)
        except (BrokenProcessPool, Exception) as e:
            pass                         # 在途与排队的任务一并被毒化
    print("在途 4 个任务的结局:", [status(f) for f in pending])

    try:
        ex.submit(slow_good, 9).result(timeout=10)
        print("崩溃后旧池竟然还能用")
    except BrokenProcessPool:
        print("崩溃后旧池: 继续提交也是 BrokenProcessPool -> 池已毒化")

    ex.shutdown(wait=False, cancel_futures=True)

    with ProcessPoolExecutor(max_workers=2) as ex2:   # 重建才是出路
        print("重建新池后:", ex2.submit(slow_good, 42).result())
```

**追问**:1) 为什么池不自动拉起新 worker 继续干?——被杀 worker 可能正持有共享状态(锁、半写的文件),池无法保证续跑的正确性。2) maxtasksperchild 换班和崩溃是一回事吗?——不是,换班是任务边界上的正常退休,不会毒化在途任务。3) 底层机制:池怎么发现 worker 死了?——管理线程读到 worker 退出码非正常(如 -9)或结果管道 EOF,立即把池标记 broken,在途与排队的 future 全部 set_exception(BrokenProcessPool),后续 submit 直接拒绝;检测点是进程级信号而非应用层异常,异常回传与进程死亡是两套通道。4) 生产陷阱?——任务代码裸调 os._exit、C 扩展段错误触发毒化;把 BrokenProcessPool 当普通异常对旧池重试提交,永远失败;池重建后没重发在途任务,静默丢活(至少一次语义要上层兜底)。

---
