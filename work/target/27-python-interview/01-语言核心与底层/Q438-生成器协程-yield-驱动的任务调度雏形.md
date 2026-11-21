---
title: [Q438] 生成器协程:yield 驱动的任务调度雏形
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q438 · 生成器协程:yield 驱动的任务调度雏形

> 难度:★★★★ | 标签:协程, 调度器

**问**:不依赖 asyncio,如何用生成器实现一个单线程多任务调度器?这和 asyncio 的差距在哪?

**答**:把 yield 当作「暂停并把控制权交给调度器」的指令,每个任务就是一个生成器,调度器维护就绪队列,轮询 send 驱动它们。任务内部可以 yield 出「我需要什么」(如睡眠时长),调度器据此决定何时再唤醒——这正是 Twisted/Tornado 时代基于 yield from 的协程调度的核心思想。与 asyncio 的本质差距在就绪通知:轮询调度器不区分「能跑」与「在等 IO」,空转浪费;asyncio 用 selector 把等待变成事件驱动,只有就绪的任务才进队列。

```python
# file: code/01_语言核心与底层/q438_generator_scheduler.py
from collections import deque

def task(name, steps):
    for i in range(steps):
        yield f"{name} step {i}"          # 暂停点:交还控制权

def scheduler(tasks):
    queue = deque(tasks)
    started = set()
    tick = 0
    while queue:
        current = queue.popleft()
        try:
            if current in started:
                current.send(f"tick {tick}")
            else:
                started.add(current)
                next(current)             # 首次调度:先预激
        except StopIteration:
            continue                      # 任务完成,不再入队
        queue.append(current)             # 未完成的任务回到队尾
        tick += 1

if __name__ == "__main__":
    scheduler([task("A", 2), task("B", 3)])
```

**追问**:1) 怎么在这个雏形上支持「任务睡眠 3 tick 再唤醒」?——任务 yield 出睡眠时长,调度器把它放进延时队列,每 tick 检查到期任务再放回就绪队列,这就是最原始的定时器轮。2) 这个雏形与 asyncio 的决定性差距?——轮询不区分「能跑」与「在等 IO」,空转烧 CPU;asyncio 用 selector 事件驱动,只有就绪的任务才进就绪队列,这是协程库从玩具到生产的那一步。3) 一次任务切换的成本构成?——yield/send 是 Python 帧级切换(保存/恢复 f_lasti 与求值栈),比 OS 线程上下文切换便宜两三个数量级,协程高并发的根基在此;但纯 Python 调度循环仍有解释器开销。4) 生产陷阱?——某任务两次 yield 之间跑长计算,饿死同循环所有任务(阻塞事件循环的同源问题);要用 run_in_executor 卸载或拆分计算粒度。
