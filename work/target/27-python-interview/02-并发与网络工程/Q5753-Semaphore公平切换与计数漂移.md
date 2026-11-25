---
title: "[Q5753] asyncio.Semaphore 的公平切换与计数漂移：handoff、取消补偿与多调 release"
date: 2026-11-25
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5753 · asyncio.Semaphore 的公平切换与计数漂移：handoff、取消补偿与多调 release

难度：P6 ｜ 标签：asyncio.Semaphore、FIFO、handoff、取消补偿、BoundedSemaphore、计数漂移、并发上限

**问**：一个下游限流器用 `asyncio.Semaphore(20)` 控制并发，某次发布后监控显示实际并发冲到 60，但代码里没有改过任何 `release`；另一次压测发现"先到的请求反而最后拿到配额"，怀疑 Semaphore 不公平。`asyncio.Semaphore` 的等待队列是严格 FIFO 吗？释放时是"把值加一让所有人抢"还是"直接交给队首"？等待者被取消时，已经让渡出去的配额会不会丢？

**答**：

- **结论**：3.12 的 `asyncio.Semaphore` 是**严格 FIFO + 直接让渡（handoff）**：`release()` 先 `_value += 1`，然后从等待队列里找第一个未完成的 Future，`_value -= 1` 并 `set_result`——配额不是"放回池子让大家抢"，而是点名交给队首；同时 `locked()` 的定义是"`_value == 0` **或** 队列里还有未取消的等待者"，所以即使 `_value > 0`，新来的 `acquire` 也会排到队尾，不会插队。取消有两条路径：①等待者还在队列里就被取消 → Future 被 cancel，直接移除，不涉及配额；②配额已经让渡、等待者还没恢复时被取消 → `acquire` 的 `except CancelledError` 发现 `not fut.cancelled()`，会 `_value += 1` 并把配额让给下一个等待者——所以正常使用不会丢配额。真正会导致"计数漂移、并发超限"的是**多调了 `release`**：每多调一次，`_value` 就永久 +1，信号量不再是"最多 N 个"，而是"最多 N+多调次数"。`BoundedSemaphore` 会在 `release` 超过初始值时抛 `ValueError`，是排查这类 bug 的探针。

- **取舍**：a) 需要"严格并发上限"时用 `BoundedSemaphore`：它把"多调 release"从静默漂移变成显式异常，代价是必须在所有路径上保证 acquire/release 配对（`async with` 最省心）；b) 需要"公平排队"时 `Semaphore` 的 FIFO 已经够用，但要注意"队首的协程如果长时间不恢复（比如被调度饿死），后面都得等"——这是 handoff 的代价，换来的是无插队；c) 不要把 `Semaphore` 当"速率限制器"：它限的是**并发数**，不是 QPS；固定窗口/令牌桶要另写；d) `release` 必须与 `acquire` 成对：`async with sem:` 在异常/取消时会正确释放，手写 `acquire` 后一定要 `try/finally`，且不要在 `except` 里再补一次 `release`（双重释放）。

- **实战**：事故形态是"并发上限从 20 变 60"——代码在超时分支写了 `except TimeoutError: sem.release(); raise`，但 `asyncio.timeout` 的超时发生在 `async with sem` 内部，`__aexit__` 已经释放过一次，`except` 里又释放一次；每次超时多一个配额，跑一天后 `_value` 漂到 40+。修复：删掉手写 release，统一 `async with`；把 `Semaphore` 换成 `BoundedSemaphore`，让下一次多调立刻 `ValueError` 并带栈；再加一条运行时指标 `sem._value`（仅调试）或包装类记录"当前持有数"，超过初始值就告警。第二个事故是"取消后吞吐掉底"：某个等待者被取消后没恢复，团队以为配额丢了，实际是它在 `finally` 里做了阻塞清理，队首卡住导致后续全等——handoff 下队首的清理时间就是所有人的等待时间。

```python
# asyncio.Semaphore: FIFO handoff、取消补偿、多调 release 的计数漂移
import asyncio

async def fifo_and_no_barging():
    sem = asyncio.Semaphore(1)
    await sem.acquire()
    order = []

    async def worker(i):
        async with sem:
            order.append(i)
            await asyncio.sleep(0)

    t1 = asyncio.create_task(worker(1))
    t2 = asyncio.create_task(worker(2))
    await asyncio.sleep(0)

    sem.release()                       # 点名交给 t1, 不是放回池子
    t3 = asyncio.create_task(worker(3))  # 新来者: 即使 value 可能 >0 也要排队
    await asyncio.sleep(0.02)
    print("→ 释放后的完成顺序:", order)
    assert order == [1, 2, 3]           # 严格 FIFO, t3 没有插队

async def cancel_paths():
    # 路径一: 还在队列里就被取消, 不涉及配额
    sem = asyncio.Semaphore(1)
    await sem.acquire()

    async def waiter():
        await sem.acquire()

    t = asyncio.create_task(waiter())
    await asyncio.sleep(0)
    t.cancel()
    await asyncio.gather(t, return_exceptions=True)
    sem.release()
    await asyncio.wait_for(sem.acquire(), 0.1)   # 配额完整, 立即可拿
    print("→ 队列中取消: 配额未丢")

    # 路径二: 配额已 handoff, 恢复前取消, acquire 内部会归还
    sem2 = asyncio.Semaphore(1)
    await sem2.acquire()

    async def waiter2():
        await sem2.acquire()

    t2 = asyncio.create_task(waiter2())
    await asyncio.sleep(0)
    sem2.release()                      # 配额已经交给 t2
    t2.cancel()                         # t2 还没恢复就被取消
    await asyncio.gather(t2, return_exceptions=True)
    print("→ handoff 后取消: value =", sem2._value)
    assert sem2._value == 1             # 补偿逻辑把配额放回来了

async def drift():
    sem = asyncio.Semaphore(1)
    sem.release()                       # 没有配对的 acquire
    sem.release()
    print("→ 多调两次 release 后 value =", sem._value)
    assert sem._value == 3              # 上限从 1 漂到 3
    for _ in range(3):
        await sem.acquire()             # 三个并发都能进, 限流失效
    assert sem.locked()

    bounded = asyncio.BoundedSemaphore(1)
    msg = ""
    try:
        bounded.release()
    except ValueError as e:
        msg = str(e)
        print("→ BoundedSemaphore 立刻抓住多调:", e)
    assert "too many times" in msg

async def main():
    await fifo_and_no_barging()
    await cancel_paths()
    await drift()

asyncio.run(main())
```

**追问一**：为什么 `locked()` 要把"有等待者"也算作锁定？这不违反"信号量只看计数"的直觉吗？—— 这是为了**防止插队**。如果 `locked()` 只看 `_value`，那么 `release()` 把值加一之后、队首还没恢复的窗口里，新来的 `acquire` 会看到 `_value > 0` 直接拿走，队首继续睡——高并发下先到的请求可能永远抢不过新请求（饥饿）。把"有活跃等待者"纳入 `locked()`，新来的必须先排队，`release()` 的 handoff 才有意义。代价是"队首卡住会阻塞所有人"，所以等待者拿到配额后的临界区要短，不要在持锁期间做长 IO；如果业务允许"后来者优先"，就不该用 Semaphore，应该用显式的优先级队列。

**追问二**：`BoundedSemaphore` 能完全防住计数漂移吗？还有哪些"看起来配对了"的泄漏路径？—— 它只能防"release 次数超过初始值"这一种。仍会漂移/泄漏的路径：①**重复初始化**：同一个信号量被两个组件各自 `release` 一次、`acquire` 一次，净值为零但语义已经错位；②**跨事件循环复用**：3.10+ 的 Semaphore 绑定 loop，跨 loop 使用会报错或行为未定义；③**在 `__aexit__` 之外手动 release**：`async with` 已经释放，异常分支再补一刀，直接触发 BoundedSemaphore 的 ValueError（这是好事，能定位）；④**取消发生在 `async with` 的 `__aenter__` 与进入临界区之间**：`__aexit__` 仍会执行，不会泄漏。结论：BoundedSemaphore 是"最后一道断言"，真正的纪律是"一个 acquire 对应一个 release，全部用上下文管理器表达"，不要在业务分支里散落 release。

## 背诵要点

- asyncio.Semaphore 是 FIFO handoff：`release` 把配额点名交给队首（value 先 +1 再 -1），`locked()` 含"有等待者"，新来者不能插队。
- 取消两条路径都不丢配额：队列中取消只移除 Future；handoff 后取消会 `_value += 1` 并唤醒下一个（`not fut.cancelled()` 分支）。
- 真正的漂移来自多调 `release`（value 永久 +1，上限失效）；用 `BoundedSemaphore` 让多调立刻 ValueError，acquire/release 统一走 `async with`。

## 复盘追问

- 为什么 release 不是"value+1 让大家抢"，而是直接 set_result 给队首？（避免插队与饥饿；配合 locked() 的等待者判断保证 FIFO）
- 并发上限悄悄变大，最可能是什么 bug？怎么让它在测试期暴露？（acquire/release 不配对导致多调 release；换 BoundedSemaphore 并断言不抛 ValueError）
