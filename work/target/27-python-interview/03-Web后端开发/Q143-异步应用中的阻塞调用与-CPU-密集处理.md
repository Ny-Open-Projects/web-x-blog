---
title: [Q143] 异步应用中的阻塞调用与 CPU 密集处理
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q143 · 异步应用中的阻塞调用与 CPU 密集处理

> 难度:★★★ | 标签:asyncio, 性能

**问**:async 路由里调了阻塞函数会怎样?CPU 密集任务怎么不拖垮事件循环?

**答**:async 路由中的阻塞调用(同步 requests、time.sleep、重 CPU 计算)会卡住整个事件循环,所有并发请求一起超时——这是 ASGI 应用最常见的事故。解法:IO 阻塞换成异步库(aiohttp/asyncpg/redis.asyncio)或用 `run_in_threadpool`(FastAPI 对同步 def 路由自动这么做的机制);CPU 密集用 `loop.run_in_executor` 抛给进程池,或干脆拆成独立 worker/任务队列。混合部署时同步与异步 worker 分池。

```python
# file: code/03_Web后端开发/q143_blocking_offload.py
import asyncio
import time
from concurrent.futures import ProcessPoolExecutor
try:
    from fastapi import FastAPI
    from fastapi.concurrency import run_in_threadpool
    import httpx   # pip install httpx
except ImportError:
    print("该题演示需要第三方库 fastapi:pip install fastapi[all],原理见正文")
    raise SystemExit(0)

app = FastAPI()
process_pool = ProcessPoolExecutor(max_workers=2)

def heavy_cpu(n: int) -> int:          # CPU 密集,放进程池
    return sum(i * i for i in range(n))

def blocking_io() -> str:              # 阻塞 IO,放线程池
    time.sleep(1)
    return 'done'

@app.get('/cpu/{n}')
async def cpu_route(n: int):
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(process_pool, heavy_cpu, n)
    return {'result': result}

@app.get('/io')
async def io_route():
    # 错误示范: time.sleep(1) 直接写在 async 里会阻塞事件循环
    out = await run_in_threadpool(blocking_io)
    async with httpx.AsyncClient() as client:   # 正确: 异步 HTTP
        await client.get('https://httpbin.org/get')
    return {'out': out}
```

**追问**:
- 怎么发现 async 路由里的阻塞调用?——压测 P99 与并发不匹配、事件循环延迟指标告警、debug 模式慢回调日志;三件套任一异常都要查。
- run_in_threadpool 的线程池多大?——Starlette 默认 anyio 线程池(默认 40);全应用共享,慢调用会挤占,要单独池隔离。
- 同步 def 路由 FastAPI 会怎么处理?——自动丢线程池执行,所以同步路由不会卡事件循环,但并发受线程池大小限制。
