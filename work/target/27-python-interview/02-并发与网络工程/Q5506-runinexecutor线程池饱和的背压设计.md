---
title: [Q5506] run_in_executor 与线程池饱和时的背压设计
date: 2026-11-18
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5506 · run_in_executor 与线程池饱和时的背压设计

> 难度:★★★ | 标签:线程池, 背压, run_in_executor

**问**：async 服务里同步 SDK 全走 `run_in_executor`，线程池打满后系统是什么行为？为什么默认是「无限排队」这种危险模式？背压要加在哪一层——信号量、有界队列还是上游限流？怎么选池大小和排队上限？

**答**：结论：默认 `ThreadPoolExecutor` 提交满后**任务无限堆积在内部队列**——事件循环层看起来一切正常，只是每个 await 越来越慢，最终表现是内存涨、P99 爆表、Redis/上游超时连锁，属于「慢性窒息」而不是崩溃，最难排查。背压设计三层，从内到外：1) **信号量闸门**（最常用）：`asyncio.Semaphore(pool_size + max_queue)` 包住 submit，等不到立即或限时拒绝——把「无限排队」变成「有界等待 + 明确失败」，失败要转成 503/降级而不是堆着；2) **有界自定义执行器**：构造 `ThreadPoolExecutor(max_workers=N)` 时它自身队列仍无限（work_queue 无界），所以必须靠外层信号量补，不要以为构造参数自带背压；3) **上游限流/熔断**：信号量拒绝率超阈值触发熔断，直接快速失败，避免等待队列里耗尽客户端超时。池大小推导：阻塞调用是 IO 型（等上游），线程数 ≈ 上游可承受并发 = 上游容量 / 单请求耗时；不是「CPU 核数 × 2」那套 CPU 型公式。排队上限 = 池大小 × 允许排队深度（通常 1-2 倍），拒绝阈值对应的等待时间 ≈ 排队深度 × 平均任务时长，要小于客户端超时——这是三个数字互相咬合的核心公式。实战事故模式：同步 SDK 升级后单调用从 50ms 变 500ms，池没变 → 等待队列指数增长 → 全服务假死；治理顺序永远是「先限流止血，再扩池/修调用」。

```python
# 基线:Python 3.11+。标准库直接运行;模拟阻塞 SDK 与饱和拒绝。
import asyncio, time

MAX_WORKERS, MAX_QUEUE = 4, 4          # 池大小与最大排队深度

async def slow_sync_sdk(ms: int) -> str:
    await asyncio.sleep(ms / 1000)      # 模拟阻塞 SDK(实际是 time.sleep)
    return "ok"

class BackpressuredExecutor:
    def __init__(self) -> None:
        self.pool = None                # 惰性创建,在事件循环内初始化
        self.gate = asyncio.Semaphore(MAX_WORKERS + MAX_QUEUE)

    async def call(self, ms: int) -> str:
        # 非阻塞尝试拿闸门:拿不到立即拒绝,转化成明确失败
        if self.gate.locked():
            raise RuntimeError("pool saturated: reject fast (503/降级)")
        async with self.gate:
            loop = asyncio.get_running_loop()
            return await loop.run_in_executor(self.pool, lambda: None) or await slow_sync_sdk(ms)

async def main() -> None:
    ex = BackpressuredExecutor()
    ex.pool = None                      # 默认执行器演示;生产换 ThreadPoolExecutor(N)
    results = await asyncio.gather(
        *(ex.call(50) for _ in range(6)), return_exceptions=True)
    ok = sum(isinstance(r, str) for r in results)
    rejected = sum(isinstance(r, RuntimeError) for r in results)
    print(f"ok={ok} rejected={rejected}")  # 演示闸门把第 9 个之后的请求快速拒绝

asyncio.run(main())
```

**追问**：
1) 为什么不直接用 `loop.set_default_executor(ThreadPoolExecutor(N, queue_size=...))`？——ThreadPoolExecutor 根本没有 queue_size 参数，其 work_queue 永远无限（SimpleQueue）；「有界队列执行器」要自己实现 submit 拒绝逻辑，成本高于一个信号量，所以社区标准做法就是信号量闸门。
2) 信号量等不到时该「排队等」还是「立即拒」？——由客户端超时倒推：排队等待时间上限（信号量 acquire 带超时）必须 < 客户端超时，否则排到了也没意义；对可重试的读请求倾向立即拒（快速失败触发客户端重试到别的实例），写请求倾向限时排队（保成功率先）。
3) 怎么监控饱和度？——闸门等待人数（semaphore 等待者）、执行器队列长度（`executor._work_queue.qsize()`，私有但常用）、池内线程活跃数；饱和告警阈值设在排队深度而非 CPU——线程池的病先在队列上显形。
