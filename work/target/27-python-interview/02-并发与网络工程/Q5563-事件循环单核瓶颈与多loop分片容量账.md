---
title: [Q5563] 事件循环单核瓶颈与多 loop 分片容量账
date: 2026-11-21
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5563 · 事件循环单核瓶颈与多 loop 分片容量账

> 难度:★★★★ | 标签:容量规划, 事件循环, 多进程, 水位推导

**问**：单实例 asyncio 网关 8 核机器只能吃满 1 个核，QPS 卡在 3 万上不去。为什么 asyncio 天然单核？容量上限定怎么推？多 loop 分片（每核一个 loop）、多进程 worker、uvloop 三条路怎么选，各自的账怎么算？

**答**：容量推导：asyncio 事件循环是**单线程单循环**，一轮 = 收集就绪 fd 回调 + 执行回调 + 处理定时器；单核上限 ≈ 1 / (每任务调度成本 + 每任务业务 CPU)。典型账：每请求 3 个回调 × 每回调 50μs 纯调度 + 200μs 业务 CPU = 350μs → 单 loop 理论上限 ~2.8 万 QPS，与实测 3 万吻合——**卡在单核是模型必然，不是 bug**。三条扩容路：a) **多进程 worker**（uvicorn/gunicorn workers=N）：每进程独立 loop，横向吃满 N 核，最标准，成本是进程间不共享内存状态（会话/限流要外置）；b) **单进程多 loop 分片**（每核一个 loop + SO_REUSEPORT 分流，见既有 Q5507）：省 fork 后的进程间协议开销、共享启动态，但 Python 有 GIL，分片只适合"IO 转发类"轻 CPU 场景，CPU 密集照样单核；c) **uvloop**（见既有 Q5504）：把调度成本从 50μs 压到 ~20μs，单 loop 上限提高 ~40%，是所有方案的前置免费项。推导公式落地：**目标 QPS × 单请求 CPU 时间 ≤ 0.7 × 核数**（留 30% 水位给 GC/峰值），压测验证时看"loop 延迟"（`loop.time()` 采样 callback 间隔，P99 > 100ms 说明单核饱和）。分片数 = 核数而不是核数×2（IO 等待由多路复用消化，不像线程池要 2 倍补偿）。

```python
# file: code/02_并发与网络工程/q5563_loop_capacity.py
import asyncio, time, statistics

# 1) 实测单 loop 调度成本 -> 推单核上限
async def tick(n):
    for _ in range(n):
        await asyncio.sleep(0)

async def measure(n=20_000):
    t0 = time.perf_counter()
    await tick(n)
    per = (time.perf_counter() - t0) / n * 1e6
    print(f"每任务调度+让出: {per:.1f} us -> 纯调度上限 ~{1e6/per/3:,.0f} task/s (3回调/请求)")
    return per

asyncio.run(measure())

# 2) 多 loop 并行: 线程各跑一个 loop (IO 型任务可并行, CPU 型被 GIL 限制)
results = []
async def worker_loop(qps_budget):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    t0 = time.perf_counter()
    await asyncio.gather(*[simulate_io() for _ in range(2_000)])
    results.append(time.perf_counter() - t0)
    loop.close()

async def simulate_io():
    await asyncio.sleep(0)   # 模拟 IO 让出

import threading
def run_in_thread():
    asyncio.run(worker_loop(2_000))

ts = [threading.Thread(target=run_in_thread) for _ in range(4)]
t0 = time.perf_counter()
for t in ts: t.start()
for t in ts: t.join()
print(f"4 线程 x 2000 IO 任务总耗时 {time.perf_counter()-t0:.2f}s (IO 并行分片有效)")

# 3) loop 延迟监控: callback 间隔 P99 是单核饱和的水位计
async def lag_probe():
    lags = []
    for _ in range(200):
        t0 = time.perf_counter()
        await asyncio.sleep(0.005)
        lags.append((time.perf_counter() - t0 - 0.005) * 1000)
    lags.sort()
    print(f"loop 延迟 P50={statistics.median(lags):.2f}ms P99={lags[int(len(lags)*0.99)]:.2f}ms (P99>100ms => 单核饱和)")

asyncio.run(lag_probe())

# 4) 容量公式: 目标QPS x 单请求CPU <= 0.7 x 核数
cores, cpu_per_req = 8, 0.0002
print(f"8核0.2ms/请求: 单实例安全上限 ~{0.7*cores/cpu_per_req:,.0f} QPS, 每实例再除以核内单loop系数")
print("选型: uvloop 免费前置 -> 多进程 worker 标准解 -> 多loop分片限 IO 转发型")
```

**追问**：1) 为什么分片数不用核数×2？——线程池 ×2 是补偿"线程阻塞等 IO"的占用；事件循环的 IO 等待由 epoll 挂起消化，不占调度槽，×2 只会增加 GIL 争抢。2) 单 loop 内 `run_in_executor` 的 CPU 任务怎么影响容量账？——executor 线程的 CPU 与 loop 线程抢同一进程的 GIL，业务 CPU 账要合并算（这正是"asyncio 里 CPU 密集必须进进程池"的量化依据）；进程池序列化成本（见既有 Q5543）要在账里扣。3) 怎么观测"哪个回调把 loop 拖慢"？——`loop.slow_callback_duration`（默认 0.1s）+ debug 模式打日志（见既有 Q5565 asyncio 调试演进），生产用 py-spy 长驻采样看 `epoll.poll` 与回调占比。

## 背诵要点
- asyncio 单 loop 单核是模型必然：单核上限 ≈ 1/(调度+业务 CPU)，每任务调度 ~50μs、uvloop ~20μs。
- 扩容三路：uvloop 免费前置、多进程 worker 标准解、单进程多 loop 分片限 IO 转发型且分片数=核数。
- 容量公式：目标 QPS×单请求 CPU ≤ 0.7×核数；水位计是 loop 延迟 P99（>100ms 即单核饱和）。

## 复盘追问
- 你们的 asyncio 服务有没有按"单请求 CPU × 目标 QPS"推过单实例上限？压测时是否只压了单进程？（提示：对照本卡公式复算，检查 worker 数与核数配比）
- loop 延迟/慢回调有没有监控与告警？（提示：部署 lag probe 或 slow_callback_duration 日志；复盘 3 万 QPS 卡顶时的水位曲线）
