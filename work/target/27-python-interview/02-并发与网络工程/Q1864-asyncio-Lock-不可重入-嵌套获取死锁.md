---
title: [Q1864] asyncio.Lock 不可重入:嵌套获取死锁与可重入锁实现
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1864 · asyncio.Lock 不可重入:嵌套获取死锁与可重入锁实现

> 难度:★★★ | 标签:asyncio.Lock, 可重入, 死锁

**问**:线程锁有 RLock,asyncio.Lock 为什么嵌套获取就死锁?真需要重入怎么办?

**答**:内建 asyncio.Lock 没有属主概念,它不知道 '持锁的就是我自己',同一任务第二次 acquire 永远等不到自己释放,挂起点无异常无日志,只能靠 wait_for 兜底暴露。

- 可重入锁的实现:记录属主 task 与深度,同任务重入只加计数直接放行,退出计数归零才真正释放底层锁;

- 释放校验属主:别的任务代为释放是 bug,抛 RuntimeError;

- 不同任务之间依然互斥,重入是属主特权,互斥是任务间义务,两者不冲突。

更根本的解法是重构调用链消除重入需求:把 '持锁后的再入' 改为内部函数直调,锁只出现在最外层入口。

```python
# file: code/02_并发与网络工程/q1864_async_reentrant.py
# -*- coding: utf-8 -*-
"""asyncio.Lock 不可重入: 嵌套获取死锁, 需要时自己实现可重入版。

- 内建 asyncio.Lock 没有属主概念, 同一任务重复 acquire 永远等不到自己释放;
- 死锁现场是 await 挂起, 没有异常没有日志, 只能靠 wait_for 兜底暴露;
- 可重入锁: 记住属主 task 与深度, 同任务重入只加计数, 退出计数归零才真正放锁。
"""
import asyncio


async def nested_acquire(lock):
    async with lock:
        await asyncio.sleep(0.01)
        async with lock:                       # 同一任务重复获取 -> 死锁
            return "nested-ok"


class AsyncReentrantLock:
    def __init__(self):
        self._lock = asyncio.Lock()
        self._owner = None
        self._depth = 0

    async def acquire(self):
        me = asyncio.current_task()
        if self._owner is me:
            self._depth += 1                   # 重入只加计数
            return
        await self._lock.acquire()
        self._owner = me
        self._depth = 1

    async def release(self):
        me = asyncio.current_task()
        if self._owner is not me:
            raise RuntimeError("锁属于别的任务, 不能代为释放")
        self._depth -= 1
        if self._depth == 0:
            self._owner = None
            self._lock.release()

    async def __aenter__(self):
        await self.acquire()
        return self

    async def __aexit__(self, *exc):
        await self.release()


async def main():
    plain = asyncio.Lock()
    try:
        await asyncio.wait_for(nested_acquire(plain), timeout=0.4)
        raise AssertionError("不应到达这里")
    except asyncio.TimeoutError:
        print("内建 asyncio.Lock 嵌套获取: 死锁, 被 wait_for 兜底发现")

    rlock = AsyncReentrantLock()
    r = await asyncio.wait_for(nested_acquire(rlock), timeout=1.0)
    print("可重入锁嵌套获取:", r)
    assert r == "nested-ok"

    order = []

    async def user(tag):
        async with rlock:                      # 不同任务仍然互斥
            order.append(tag + "-in")
            await asyncio.sleep(0.02)
            order.append(tag + "-out")

    await asyncio.gather(user("A"), user("B"))
    print("两任务互斥序列:", order)
    assert order in (["A-in", "A-out", "B-in", "B-out"],
                     ["B-in", "B-out", "A-in", "A-out"]), "不同任务必须互斥"
    print("结论: 重入是属主特权, 互斥是任务间义务, 二者不冲突")


if __name__ == "__main__":
    asyncio.run(main())
```

**追问**:1) asyncio.Lock 嵌套死锁和线程死锁排查方式一样吗?——不一样,asyncio 死锁是单线程内的 await 挂起,线程栈 dump 看不出来;要用 asyncio 的调试模式、任务列表和 wait_for 超时来定位。2) asyncio 死锁为什么比线程死锁更隐蔽?——await 挂起无异常无日志,任务列表里状态是 pending;定位手段:调试模式(loop.set_debug)、asyncio.all_tasks 快照看谁在等谁、wait_for 兜底把「永久」变成「超时+可观测」;线程死锁还有 jstack/py-spy 的栈 dump,asyncio 的「栈」在任务图里。3) 可重入锁的属主校验为什么必要?——release 校验属主(别人的 release 是 bug,抛 RuntimeError);没有校验,「A 任务释放了 B 的锁」这种竞态会静默破坏互斥——锁的「属主语义」与「计数语义」要一起实现。4) 生产陷阱?——嵌套 acquire(挂起死锁,见原问);把线程 RLock 直接在协程里用(阻塞事件循环);可重入锁被跨任务误 release;用 wait_for 包住所有 acquire(掩盖设计问题,嵌套结构该重构);重入深度无上限(递归失控)。


---
