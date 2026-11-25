---
title: [Q6124] FastAPI 同步路由的默认线程池容量推导（40 的账）
date: 2026-11-21
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6124 · FastAPI 同步路由的默认线程池容量推导（40 的账）

> 难度:★★★★☆ | 标签:容量规划, FastAPI, 线程池

**问**:FastAPI 里 `def`（非 `async def`）路由跑在哪里？默认 40 个线程怎么来的？这 40 个线程同时被"同步 ORM 慢查询"占满时，其他普通请求会怎样？调大和调小的账各怎么算？

**答**:结论：`def` 路由被丢进 **anyio 的线程池**执行，默认 `total_tokens = 40`（`anyio.to_thread.current_default_thread_limiter()`），这是"每个进程内同步代码的总并发上限"。事故形态：40 个线程全卡在同步 ORM 慢查询上 → **所有** `def` 路由排队（包括毫秒级健康检查）→ 上游超时重试 → 雪崩；而 `async def` 路由不受影响——两种路由是两个并发池，这也是排查"部分接口卡死、部分正常"的钥匙。容量推导：`tokens ≈ p99_sql_ms × 目标同步 QPS / 1000`，例：同步接口 P99 200ms、目标 100 QPS → 需要 20 线程；若数据库连接池只有 10 个连接，线程配 40 也只是排队前移——**线程池与 DB 池必须对齐**（呼应 Q6046）。调大的代价：每线程 8MB 虚拟栈 + 上下文切换，40→200 线程 RSS 增量可控（几十 MB）但调度毛刺上升；调小的收益是"隔离慢 SQL 不拖垮全站"。实战三板斧：a) `RunVar`/lifespan 里显式设 limiter 并写进容量文档；b) 同步重查询独立 limiter（`anyio.to_thread.run_sync(fn, limiter=...)` 分池）；c) 监控线程池利用率（active/40）而不是只看 QPS。

```python
# 基线: FastAPI>=0.100 / Starlette>=0.27 / anyio>=4；缺库降级为纯演示
import asyncio, time

def get_limiter_tokens() -> int:
    """anyio 的默认线程池 token 数须在事件循环内查询。"""
    async def read():
        import anyio.to_thread
        return anyio.to_thread.current_default_thread_limiter().total_tokens
    try:
        return asyncio.run(read())
    except ImportError:
        return 40                                   # anyio 默认值
print("默认同步线程池 tokens:", get_limiter_tokens())

# ---- 1) 复现'40 线程被占满 -> 后续 def 路由排队' ----
async def fake_def_route(sql_ms: float):
    """模拟 FastAPI def 路由: 实际在线程池里跑。"""
    await asyncio.sleep(0)

def run_pool_saturation():
    async def main():
        limiter = asyncio.Semaphore(40)             # 模拟 anyio 的 40 tokens
        occupied = []

        async def slow_route():
            async with limiter:                      # 占住一个线程
                await asyncio.sleep(0.3)             # 模拟 300ms 慢 SQL

        async def fast_route():
            async with limiter:
                occupied.append("ok")

        await asyncio.gather(*[slow_route() for _ in range(40)])
        t0 = time.perf_counter()
        await asyncio.gather(*[fast_route() for _ in range(1)])
        cost = time.perf_counter() - t0
        print(f"40 线程被慢 SQL 占满后, 快路由排队耗时 {cost*1000:.0f}ms（正常应 <1ms）")
    asyncio.run(main())
run_pool_saturation()

# ---- 2) 容量推导公式 ----
p99_ms, target_qps = 200, 100
tokens_needed = p99_ms * target_qps / 1000
print(f"推导: tokens ≈ {p99_ms}ms × {target_qps}QPS / 1000 = {tokens_needed:.0f}（并核对 DB 连接池 ≥ 此值）")

# ---- 3) 显式调参（生产写法, lifespan 内执行） ----
TUNE = """
# FastAPI lifespan 内:
import anyio.to_thread
anyio.to_thread.current_default_thread_limiter().total_tokens = 64
# 或路由级分池:
from anyio.to_thread import run_sync
result = await run_sync(blocking_fn, limiter=HeavyLimiter)   # 慢 SQL 独立配额
"""
print("生产调参模板:", TUNE)
```

**追问一层**:为什么 `async def` 里跑同步阻塞代码更糟而不是更糟一点点？（阻塞发生在事件循环线程上，整个 loop 的**所有**任务停摆，包括 async 路由、心跳、健康检查——是全局级故障，线程池模型只是池级故障）。
**追问二层**:anyio 的 limiter 和 Starlette 的 `run_in_threadpool` 是什么关系？（Starlette 用 `anyio.to_thread.run_sync`，天然共享默认 limiter；所以所有 def 路由+部分同步依赖共享同一 40 配额，依赖里的同步调用也算）。
**追问三层**:如何在线上观测这个池？（线程数曲线（`psutil`/`/proc`）、anyio limiter borrowed_tokens 指标埋点、慢接口按"同步路由"维度分组对比 async 路由 P99）。

## 背诵要点
- FastAPI `def` 路由跑在 anyio 线程池，默认 40 tokens；同步依赖同样占池。
- 40 池被慢查询占满 → 全部同步接口（含健康检查）排队；async 路由不受影响，是排障分界线。
- 容量公式 tokens ≈ P99(ms)×QPS/1000，且必须与 DB 连接池对齐；慢查询用独立 limiter 分池。

## 复盘追问
- 线上"一半接口卡死一半正常"，如何 5 分钟内定位到同步线程池饱和而非 DB 故障？
- 容量评审：新增一个 500ms 的同步报表接口，预期 QPS 5，需要多少 tokens、要不要分池？
