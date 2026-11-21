---
title: [Q2652] BoundedSemaphore 抓超额归还:普通 Semaphore 的计数会漂
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2652 · BoundedSemaphore 抓超额归还:普通 Semaphore 的计数会漂

> 难度:★★ | 标签:BoundedSemaphore, 信号量, 防线

**问**:Semaphore 用作资源池时,如果某处代码多调了一次 release,会发生什么?

**答**:普通 Semaphore 只是个计数器,多 release 一次计数就涨一格:实测单槽临界区(初始计数 1)被超额归还后,两个线程同时进入,互斥不变量被静默打破。BoundedSemaphore 在 release 超过初始值时抛 ValueError,把 bug 挡在归还现场而不是几天后的数据错乱里。

- 实测:普通 Semaphore 超额 release 后最大并发观测到 2,不变量被打破;

- BoundedSemaphore 对同一场景直接抛 "Semaphore released too many times";

- 资源池语义下应一律用 BoundedSemaphore:借出几笔就必须归还几笔;

- 超额归还的常见来源:finally 里重复 release、把 release 写在会被执行两次的分支里。

```python
# file: code/02_并发与网络工程/q2652_bounded_sem.py
# -*- coding: utf-8 -*-
"""BoundedSemaphore 的超额归还防线: 普通 Semaphore 的计数会漂。

- 普通 Semaphore 只是个计数器, release 多调一次计数就涨上去;
- 计数从 1 漂到 2 后, 两个线程能同时进入"单槽"临界区, 不变量被打破;
- BoundedSemaphore 在 release 超过初始值时抛 ValueError, 把 bug 挡在原地。
"""
import threading
import time


def hammer(sem, barrier, conc, peak, lock):
    barrier.wait()
    sem.acquire()
    with lock:
        conc[0] += 1
        peak[0] = max(peak[0], conc[0])
    time.sleep(0.05)                 # 临界区有点工作量, 让并发重叠可观测
    with lock:
        conc[0] -= 1
    sem.release()


def run_two_workers(sem):
    """两个 worker 同时进临界区, 返回观测到的最大并发数。"""
    barrier = threading.Barrier(2)
    conc, peak, lock = [0], [0], threading.Lock()
    ts = [threading.Thread(target=hammer, args=(sem, barrier, conc, peak, lock))
          for _ in range(2)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    return peak[0]


if __name__ == "__main__":
    # 阶段一: 健康 Semaphore, 单槽同一时刻只放一人
    healthy = threading.Semaphore(1)
    print("健康 Semaphore(1) 的最大并发:", run_two_workers(healthy))

    # 阶段二: 普通 Semaphore 被多 release 一次, 计数漂到 2
    plain = threading.Semaphore(1)
    plain.release()                  # 多余的一次归还: 计数 1 -> 2
    peak = run_two_workers(plain)
    print("超额 release 后, '单槽'临界区最大并发:", peak)
    print("不变量是否被打破:", peak > 1)

    # 阶段三: BoundedSemaphore 拒绝超额归还
    bounded = threading.BoundedSemaphore(1)
    try:
        bounded.release()            # 多余的一次归还
        print("BoundedSemaphore 竟然放行了超额 release")
    except ValueError as e:
        print("BoundedSemaphore 抓到超额归还:", e)
    print("BoundedSemaphore 保护下最大并发:", run_two_workers(bounded))
```

**追问**:1) 计数漂移为什么难排查?——它不报错,只是让并发上限悄悄变大,表现为偶发的数据竞争,且只在流量高峰出现。2) with 语句和 Semaphore 配合安全吗?——安全,Python 没有原生的 with Semaphore 语义,但 acquire/release 恰好匹配协议,可用 try/finally 手工保证。3) 底层机制:BoundedSemaphore 拦在哪一步?——release 在内部锁里比较当前计数与构造时的初始值,越过初始值当场抛 ValueError;普通 Semaphore 的 release 是无条件计数 +1,没有上界,漂移因此完全静默。4) 生产陷阱?——finally 里重复 release(正常路径与异常补偿路径各放了一次);同一资源被两个模块各自包装、各自归还;资源池语义一律用 BoundedSemaphore,把 bug 挡在归还现场而不是几天后的数据错乱里。

---
