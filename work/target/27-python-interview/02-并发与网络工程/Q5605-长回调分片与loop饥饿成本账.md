---
title: [Q5605] 长回调分片与 loop 饥饿成本账
date: 2026-11-21
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5605 · 长回调分片与事件循环饥饿成本账

> 难度:★★★★☆ | 标签:成本工程, 事件循环, 协作式调度

**问**:一个 50ms 的 CPU 密集回调跑在事件循环里，为什么所有连接的 P99 全被拖高？分片的账怎么算？

**答**:结论：asyncio 是协作式调度，单回调执行期间整个 loop 完全停摆——这 50ms 里所有就绪 IO 事件、定时器、其他协程的调度都被推迟，P99 = 自身耗时 + 同 tick 内最长回调，尾延迟被"最重的邻居"支配。成本账两条：① 分片收益——把 50ms 切成 N 片、片间 `await asyncio.sleep(0)`，单次阻塞降到片长，代价是总吞吐下降约 (N-1)×每次让出调度开销（µs 级，通常 <5%），换来的是 P99 抖动归位；② 分片上限——片越小调度开销占比越高，经验片长 1~5ms。CPU 密集任务的终解是进程池（Q5593），分片只适合"必须留在 loop 内"的中间形态（如纯 Python 状态机）。观测手段：`loop.slow_callback_duration` + debug 模式的 "Executing ... took X seconds" 日志，或 perf 工具（Q6010）。

```python
import asyncio, time

TICK_MS = 50
def work_slice(ms=1.0):
    end = time.perf_counter() + ms / 1000
    while time.perf_counter() < end:
        pass

async def heavy_unsharded():
    work_slice(50)                    # 一次阻塞 50ms：全 loop 停摆

async def heavy_sharded(total_ms=50, slice_ms=2):
    for _ in range(int(total_ms / slice_ms)):
        work_slice(slice_ms)
        await asyncio.sleep(0)        # 让出：就绪事件与定时器得以上车

async def main():
    lat = []
    async def probe():
        t0 = time.perf_counter()
        await asyncio.sleep(0.001)
        lat.append((time.perf_counter() - t0) * 1000)

    await asyncio.gather(probe(), heavy_unsharded())
    print(f"不分片：探针延迟 {lat[0]:.1f}ms（≥50ms，被整块回调拖住）")
    lat.clear()
    await asyncio.gather(probe(), heavy_sharded())
    print(f"分片 2ms：探针延迟 {lat[0]:.1f}ms（≈片长级）")

asyncio.run(main())
loop_slow = 0.1   # 生产建议：loop.set_debug(True) + loop.slow_callback_duration = 0.1
print("建议 slow_callback_duration =", loop_slow, "s")
```

**追问一层**:`sleep(0)` 与 `sleep(0.001)` 的让出语义差异？为什么 0 才是纯让出？
**追二层**:分片方案在 free-threading（no-GIL）构建下还必要吗？什么变了、什么没变？

**背诵要点**
- 协作式调度下单回调阻塞=全 loop 停摆，P99 由最重邻居决定。
- 分片 1~5ms + sleep(0)，吞吐代价 <5% 换尾延迟归位。
- CPU 密集终解是进程池；分片只是留在 loop 时的过渡方案。

**复盘追问**
- 慢回调日志只在 debug 模式开，生产的低开销替代是什么？提示：py-spy / perf（Q6010）周期采样。
- 分片和限流（Q1573）如何组合？提示：先分片保调度，再限流保下游。
