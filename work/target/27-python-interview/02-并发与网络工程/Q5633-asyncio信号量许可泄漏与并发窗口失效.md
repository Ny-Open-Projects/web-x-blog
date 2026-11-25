---
title: [Q5633] asyncio 信号量许可泄漏与并发窗口失效账
date: 2026-11-21
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5633 · asyncio 信号量许可泄漏与并发窗口失效账

难度：P6 | 标签：Semaphore、许可泄漏、并发窗口、容量规划

**问**：用 `asyncio.Semaphore(50)` 保护对下游的并发请求，运行数小时后实际并发降到 5 以下、QPS 掉了九成，但没有报错。如何定位这类"许可泄漏"？为什么 acquire/release 不配对会造成单调性衰减？正确的写法与监控点是什么？

**答**：

**结论**：`Semaphore(50)` 内部是一个计数许可 + 等待队列，`acquire()` 减一、`release()` 加一。只要有一条执行路径 acquire 后未走到 release（异常路径漏 finally、提前 return、取消时被 `CancelledError` 打断清理段），许可就永久少一，且**单调不可恢复**——泄漏是累加的，50 个许可被一天内的几十次异常路径耗尽后，整个服务的并发窗口归零，表现为"越来越慢最后全部卡死在 acquire"。定位特征：等待 acquire 的协程数随时间单调上升，而下游本身健康。

**取舍**：写法上强制 `async with sem:`（进入/退出由编译器保证，即使取消也会 release）；手写 acquire/release 只允许出现在"跨任务转移许可"的复杂场景。注意 `asyncio.Semaphore` 不可跨事件循环/进程共享，多 worker 要么各自独立计数要么外置到 Redis。BoundedSemaphore(50) 额外防 release 超发（值>初值抛 ValueError），能暴露"双 release"这类反向泄漏。

**实战**：容量监控：暴露三个指标——可用许可数、等待者数、许可持有时长分布。持有时长账：并发上限 50、下游 P99 500ms，理论窗口吞吐 = 50/0.5 = 100 QPS；许可持有时间被锁内重试拉长到 5s 时，吞吐掉到 10 QPS，效果与泄漏一致——所以监控要区分"许可没归还"和"许可还不回来"。

```python
import asyncio

def demo_sem():
    return asyncio.Semaphore(3)

async def leaky(sem, should_fail):
    await sem.acquire()
    if should_fail:                      # 异常路径漏 release -> 泄漏
        raise RuntimeError("downstream boom")
    sem.release()

async def safe(sem):
    async with sem:                      # 取消/异常都保证归还
        await asyncio.sleep(0)

async def main():
    sem = demo_sem()
    for i in range(6):
        try:
            await leaky(sem, should_fail=(i == 0))       # 1 次异常路径泄漏
        except RuntimeError:
            pass
    print(f"泄漏后可用许可 = {sem._value} / 3")

    sem2 = asyncio.BoundedSemaphore(3)
    for _ in range(20):
        await safe(sem2)
    print("async with 200 次后可用许可 =", sem2._value)
    try:
        sem2.release()                   # 超发检测
    except ValueError as e:
        print("Bounded 超发 ->", e)

if __name__ == "__main__":
    asyncio.run(main())
```

**追问 1**：协程在 `async with sem` 内被 cancel，release 一定会执行吗？
答：会——`__aexit__` 在异常（含 CancelledError）展开时执行；但若清理段本身又被取消或被 `asyncio.shield` 误用包围，边界情况会失效，清理逻辑必须无 await 或用 shield 保护。

**追问 2**：`Semaphore` 公平吗？
答：CPython 实现按 FIFO 唤醒等待者（3.x 的 `_waiters` deque），先到先得，不存在抢锁饥饿；但排队头部阻塞意味着慢请求会拖住队列——高 P99 场景考虑超时 acquire + 放弃。

**追问 3**：为什么多进程部署时进程内 Semaphore 会低估总并发？
答：每个 worker 各有独立 50 许可，总并发 = 50×worker 数，下游实际承受被放大 N 倍；限流口径必须收敛到共享存储（Redis + Lua）或网关层。

## 背诵要点

- 许可泄漏是单调不可恢复的：漏一次 release 永久少一，表现为等待者数随时间上升。
- 一律 `async with sem`；BoundedSemaphore 可检测双 release 超发；清理段避免 await 或用 shield。
- 吞吐窗口 = 并发上限 / 持有时长；多进程下进程内信号量会把下游并发放大 N 倍，须外置计数。

## 复盘追问

- 线上如何把"许可泄漏"与"下游变慢"区分开？(提示：sem._value 与下游 P99 双指标对照)
- 已泄漏的进程如何止血而不重启？(提示：管理端点做 release 补偿或健康检查自动重启)
