---
title: "[Q6085] uvicorn worker 拓扑与 async/sync 混部的容量配比"
date: 2026-11-21
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6085 · uvicorn worker 拓扑与 async/sync 混部的容量配比

难度：★★★★☆ ｜ 标签：容量规划 / uvicorn / worker / 混部

**问**：一个 FastAPI 服务 30% 接口是 async（快查 + 下游 HTTP），70% 是 def 接口（重 ORM 查询）。worker 数、uvicorn 的线程池大小怎么配？把 def 接口改 async 就一定更好吗？

**答**：
- **结论**：账要分开算：**worker 进程数** ≤ 物理核数（每 worker 一个事件循环，async 路径吃单核 CPU）；**def（sync）接口**不占事件循环，FastAPI/Starlette 把它丢进 AnyIO 线程池执行，**默认 40 线程**——这是最常被忽略的并发闸门：70% 流量是 def 时，40 线程 × (1/单请求耗时) = 线程路径 QPS 上限，超出后请求排队（用户看到延迟升高，不是报错）。配比推导：线程路径容量 = 40 / avg_sync_ms；若不够，调 `total_threads`（运行时 `anyio.to_thread.current_default_thread_limiter().total_tokens = N`）或把热点 def 改 async。**改 async 不是万能**：ORM 是同步的（Django/SQLAlchemy 传统形态），async def 里调同步 ORM 会**阻塞事件循环**——比丢线程池更糟（Q6006 的线程池耗尽反过来）。改 async 的前提是整条链路异步化（asyncpg/SQLAlchemy 2.0 async）。
- **取舍**：三种拓扑：① 全 async worker（链路全异步，最强吞吐，改造成本高）；② async+def 混部（现状兼容，注意 40 线程闸门与内存账：线程栈 + 每线程的连接占用）；③ 多 worker 纯 sync（WSGI/传统 Django，简单可预测，吃核）。混部的内存账：每线程 0.5-1MB 栈 + ORM 连接（线程路径的连接池要 ≥ 线程数），60 线程 × 30MB 连接上下文 = 1.8GB 起步——容器 limit 要对齐。
- **实战**：定位 40 线程闸门的信号：延迟上升但 CPU 空闲、py-spy 看到大量线程在 `anyio` 队列等待、uvicorn 日志无慢点。调优顺序：先测 sync 接口的 avg 耗时定线程数 → 连接池对齐 → CPU 用满再横向加 worker → 最后才做异步化改造。

```python
"""async/sync 混部的容量账与 AnyIO 线程池闸门（FastAPI 基线 0.100+）"""
try:
    import anyio, anyio.to_thread
except ImportError:
    raise SystemExit("缺 anyio：pip install 'fastapi>=0.100'（自带 anyio 依赖）")

import asyncio, os, time

# 1) 线程池闸门观测与调整（limiter 必须在事件循环内取）
async def main():
    limiter = anyio.to_thread.current_default_thread_limiter()
    print(f"默认线程池闸门 total_tokens = {limiter.total_tokens}")   # 40

    def sync_path_ms():
        """真实口径：压测拿 def 接口平均耗时（含 ORM），这里用 25ms 演示"""
        return 25.0

    threads = limiter.total_tokens
    print(f"sync 路径容量 ≈ {threads} 线程 ÷ {sync_path_ms():.0f}ms = {threads * 1000 / sync_path_ms():.0f} QPS/worker")

    # 2) 容量矩阵：worker 数 × 线程数 → 全实例容量
    workers = os.cpu_count() or 4
    for w, th in [(workers, 40), (workers, 100), (workers * 2, 40)]:
        print(f"worker={w} 线程={th} → sync 容量 ≈ {w * th * 1000 / sync_path_ms():.0f} QPS "
              f"（内存 ≈ {w * (20 + th * 0.7):.0f}MB 起步）")

    # 3) 运行时调闸门（放 lifespan 里做）
    limiter.total_tokens = 100
    print("闸门调至 100（须与 ORM 连接池、容器内存同步对齐）")

    # 4) 顺带演示线程池的实际占用：sync 路径跑在 to_thread 里
    await anyio.to_thread.run_sync(lambda: time.sleep(0.01))
    print("def 接口即经 run_sync 进入该线程池 —— 闸门排队就是这里发生")

asyncio.run(main())

import time

# 5) 红线演示：async def 里调同步阻塞 = 阻塞事件循环
async def anti_pattern():
    # 直接在协程里 time.sleep/同步 ORM → 整个 worker 所有请求卡住
    print("async def 中调用同步 IO 会阻塞事件循环 —— 改 async 前必须全链路异步化")

asyncio.run(anti_pattern())
print("结论：改 async 的收益前提是 asyncpg/SQLAlchemy2.0-async 全链路，半吊子改造比不改更糟")
```

**追问链**
1. 为什么默认线程池是 40？这个数怎么来的、改大有什么代价？
   1. AnyIO 的默认 token 数（历史默认值），与"线程切换 + 每线程内存"的保守平衡；改大直接涨内存（栈）与调度开销，且必须同步放大下游连接池（否则线程在等连接，闸门只是换位置）。正确思路是按 sync 接口耗时 × 目标 QPS 反推，而不是拍 100。
   2. 追问：sync 接口的连接池为什么必须 ≥ 线程数？——每个线程请求期间持有一条连接；池小于线程数时，多出的线程在池上排队，等于线程闸门失效换成连接闸门，监控上表现为"连接等待时长"占比上升。
2. 怎么监控"线程池排队"这个隐形成本？
   1. 打点两层：请求进入 handler 前后各记一个时间戳（排队耗时 = 差值）；或 anyio limiter 的 borrowed_tokens 水位。表现特征：P99 涨而 CPU 与 DB 指标平稳——是排队不是慢查询。
   2. 追问：uvicorn `--workers` 与 K8s 副本数怎么配合？——每副本 worker 数 × 副本数 ≤ 节点核数池；K8s 里通常 1 容器 1-2 worker，靠副本水平扩展，避免容器内多 worker 争抢 limit 的 CPU quota。

## 背诵要点
- worker 数 ≤ 物理核数（每 worker 一个事件循环）；def 接口走 AnyIO 线程池，默认 40 线程是隐形闸门，容量 = 40 ÷ avg 耗时。
- 改 async 的前提是全链路异步化；async def 里调同步 ORM 会阻塞事件循环，比丢线程池更糟。
- 调线程数必须同步对齐 ORM 连接池与容器内存（每线程栈 + 连接上下文），监控特征：P99 涨但 CPU/DB 平稳。

## 复盘追问
- "CPU 空闲但延迟飙升"的事故里，怎么用 borrowed_tokens 与排队耗时打点确认真凶是线程闸门？
- 灰度把热点 def 改 async 时，用什么指标判断"全链路异步化已完成、可以切流"？
