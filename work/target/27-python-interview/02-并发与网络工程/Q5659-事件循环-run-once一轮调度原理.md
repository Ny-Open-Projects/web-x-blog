---
title: "[Q5659] 事件循环 _run_once 一轮调度原理"
date: 2026-11-21
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5659 · 事件循环 _run_once 一轮调度原理

难度：P7 ｜ 标签：asyncio、_run_once、定时器堆、就绪队列、epoll 超时

**问**：`loop.run_forever()` 的每一轮 `_run_once` 内部做哪几件事？select 的超时值是怎么从"定时器堆 + 已就绪回调"算出来的？为什么"call_soon 的回调处理完才能进入下一次 poll"会导致延迟抖动，`call_later` 的精度上限由什么决定？

**答**：
结论：一轮 `_run_once` 五步：① **算 poll 超时**：`timeout = 0`（ready 队列非空，立刻处理不阻塞）→ 否则取定时器堆顶的到期差 `max(0, deadline - now)`，无定时器则 `None`（无限等）；② **`_selector.select(timeout)`** 阻塞等待 IO 就绪（epoll/kqueue），把就绪 fd 对应的 reader/writer 回调追加进 ready 队列；③ **到期定时器出堆**：把堆顶已到期的 `TimerHandle` 移入 ready（用 `heapq` + 惰性取消标记，取消的句柄出堆时丢弃）；④ **逐个执行 ready 队列**（`ntodo = len(ready)` 快照，本轮只处理这么多——**执行期间新 call_soon 的回调留到下一轮**）；⑤（旧版）gc 一轮。两个精度推论：call_later 的实际触发时间 = 理论时刻 + 本轮 ready 执行时长 + select 粒度，所以"循环里有慢回调"直接拉长所有定时器的延迟；每轮至少一次 syscall（select 无超时也返回 0 个事件时同样走流程），空闲成本不为零。

取舍：这个设计的含义——**回调分片不是可选优化而是精度契约**：单个回调跑 50ms，意味着同循环所有 10ms 定时器至少晚 50ms；把重活交给 `run_in_executor`/子进程不占 ready 队列。而"每轮快照 ready"保证不会因回调不断 call_soon 无限自延（饿死 IO），但也意味着 call_soon 链每链一至少一轮 poll 间隙。

实战：诊断延迟抖动先看 `_run_once` 的两侧——`select` 超时是否被定时器堆顶钉死（有短定时器会频繁唤醒），以及 ready 每轮执行的耗时（用 `loop.slow_callback_duration` + debug 模式抓慢回调）；定时器精度敏感的场景（心跳、限流窗口）必须隔离到无重负载的专用 loop。

```python
import asyncio, heapq, time

async def main():
    loop = asyncio.get_running_loop()

    # 1) 内部结构巡检：定时器堆（_scheduled）与就绪队列（_ready）
    print("selector backend :", type(loop._selector).__name__)
    print("scheduled before :", [(h.when() - loop.time()) for h in loop._scheduled])

    # 2) 定时器堆：call_later 按 when 入堆（heapq），取消是惰性的
    t1 = loop.call_later(0.10, lambda: None)
    t2 = loop.call_later(0.02, lambda: None)
    print("scheduled order  :", [round(h.when(), 3) for h in loop._scheduled])   # 堆序非严格升序但堆顶最小
    print("heap top is smallest:", loop._scheduled[0].when() == min(h.when() for h in loop._scheduled))
    t1.cancel()                                 # 惰性：句柄仍可能留在堆里直到到期被丢弃
    t2.cancel()

    # 3) poll 超时推导：有 ready 回调时 timeout=0，等待中的 select 不阻塞后续唤醒
    def poll_timeout(ready_len, scheduled_heap, now):
        if ready_len:
            return 0
        if scheduled_heap:
            return max(0, scheduled_heap[0].when() - now)
        return None                              # 无限期阻塞
    fake = type("H", (), {"when": lambda s: 12345.6})()
    now = 12340.0
    print("timeout with ready      :", poll_timeout(1, [fake], now))   # 0
    print("timeout with timer heap :", poll_timeout(0, [fake], now))   # ~5.6
    print("timeout with neither    :", poll_timeout(0, [], now))        # None

    # 4) 慢回调拉长同循环定时器精度：实测 call_later 的实际偏差
    async def probe():
        start = loop.time()
        loop.call_soon(lambda: time.sleep(0.08))            # 一个慢回调占住 ready
        await asyncio.sleep(0.02)
        fire = loop.time()
        return fire - start
    drift = await probe()
    print("sleep(0.02) actual drift: %.3fs (受慢回调影响)" % drift)

asyncio.run(main())

# 5) 快照语义：一轮最多处理 ntodo 个回调，处理期间新回调排队下轮
loop2 = asyncio.new_event_loop()
seen = []
def cb():
    seen.append(1)
    loop2.call_soon(cb)                    # 自续：每轮执行一次，绝不饿死 IO
loop2.call_soon(cb)
loop2.call_later(0.05, loop2.stop)
loop2.run_forever()
print("self-rescheduling callbacks executed:", len(seen), "（约 0.05s / 每轮间隔）")
loop2.close()
```

**追问一**：为什么定时器取消是"惰性"的、堆里留下已取消句柄有什么代价？——`TimerHandle.cancel()` 只标记 `_cancelled`，不立即从堆删除（堆删除 O(n) 或需索引结构）；代价是堆膨胀与每次出堆的丢弃检查，极端情况下"高频创建短定时器再取消"（Q5533 call_later handle 堆积事故）会拖慢每轮出堆扫描，治理靠复用句柄或改用 `call_at` 有界调度。

**追问二**：`select(timeout=None)` 无限期阻塞时，别的线程怎么唤醒这个循环？——通过自管道/self-pipe（`loop._self_pipe`）：跨线程代码必须走 `call_soon_threadsafe`，它向管道写字节触发 select 可读事件；直接调 `loop.call_soon` 只往内存队列塞回调、不唤醒阻塞中的 select，回调要等下一次"巧合的唤醒"——这就是跨线程误用导致回调丢失的机制根源。

## 背诵要点
- `_run_once` 五步：算 poll 超时（ready>0→0；堆顶到期差；否则 None）→ select → 到期定时器入 ready → 快照执行 ready → 收尾。
- call_later 精度 = 理论时刻 + ready 执行时长 + select 粒度；慢回调拉长全循环定时器，重活必须出循环。
- 取消惰性（句柄留堆）、跨线程唤醒靠 self-pipe（call_soon_threadsafe），裸 call_soon 不唤醒 select。

## 复盘追问
- 心跳定时器周期性迟到 40-100ms，如何用 _run_once 模型定位是"慢回调"还是"堆膨胀"？（debug 模式 slow_callback_duration + _scheduled 长度监控，讨论分 loop 隔离）
- 为什么"loop 里排队 10 万个 call_soon"会让 IO 延迟飙高而 CPU 只占一核？（每轮快照处理，回调间无法插入 select；讨论分片与 yield 策略）
