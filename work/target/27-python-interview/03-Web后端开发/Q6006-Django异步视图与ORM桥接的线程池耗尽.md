---
title: [Q6006] Django 异步视图与 ORM 桥接的线程池耗尽
date: 2026-11-18
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6006 · Django 5 异步视图与 ORM sync 桥接的线程池耗尽

> 难度:★★★ | 标签:Django 4.2+/5, sync_to_async, 容量规划

**问**：async view 里直接调 ORM 会发生什么？用 `sync_to_async` 桥接后，高并发下为什么会把线程池和数据库连接一起拖垮？

**答**：Django 为防止在事件循环上跑阻塞代码，async 上下文里直接调 ORM 抛 `SynchronousOnlyOperation`。桥接有两种姿势，事故模式各不相同：1) `sync_to_async(fn)` 默认 `thread_sensitive=True`——所有这类调用**串行在同一个线程**执行，结果正确但吞吐等于单线程，QPS 被这一条隐形队列封顶；2) `thread_sensitive=False` 进进程级线程池并行，真正的坑在这：线程池容量有限（Django 用 `asgiref` 的 executor，默认可调但有限），并发桥接请求数超过池容量就开始排队，排队时间叠加进 P99；同时**每个并发桥接各取一个数据库连接**（ORM 是按线程绑定连接的），线程池被打满时 DB 连接池同步打满，报「连接过多」。容量约束链：`线程池大小 ≤ DB 连接池可用额度`，且要为每实例的并发峰值留余量；如果不设，默认值之间是不对齐的，这正是「压测时异步视图反而不如同步稳」的经典根因。另外 `async` ORM 接口（`aget`/`acreate` 等）底层同样走桥接，成本模型相同，不是免费午餐。

```python
# 基线:Django 4.2+/Python 3.9+。缺库降级:用 concurrent.futures 模拟同容量线程池的排队曲线。
import asyncio, time

try:
    import django
    from django.conf import settings
except ImportError:
    # 降级:用线程池模拟 thread_sensitive=False 的排队效应
    from concurrent.futures import ThreadPoolExecutor
    def db_like_query(i): time.sleep(0.02); return i          # 模拟 20ms DB 调用
    async def bridged(fn, pool):
        return await asyncio.get_event_loop().run_in_executor(pool, fn)
    async def main():
        pool = ThreadPoolExecutor(max_workers=4)               # 模拟受限线程池
        t0 = time.perf_counter()
        await asyncio.gather(*[bridged(lambda: db_like_query(i), pool) for i in range(20)])
        print(f"降级模拟:20 个并发桥接/池容量 4 → 耗时 {time.perf_counter()-t0:.2f}s(排队等待可见)")
    asyncio.run(main())
    raise SystemExit(0)

settings.configure(DEBUG=True, DATABASES={"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}}, USE_TZ=True)
django.setup()
from asgiref.sync import sync_to_async
from django.db import connection

def setup_and_query():
    with connection.cursor() as c:
        c.execute("CREATE TABLE IF NOT EXISTS t(id INTEGER)")
        c.execute("SELECT COUNT(*) FROM t"); return c.fetchone()[0]

async def main():
    # thread_sensitive=True:所有桥接串行在同一个线程 → 结果确定,吞吐封顶
    t0 = time.perf_counter()
    for _ in range(5):
        await sync_to_async(setup_and_query)()
    print(f"thread_sensitive=True  串行 5 次: {(time.perf_counter()-t0)*1000:.1f} ms")

    # thread_sensitive=False:进线程池并行 → 单次更快,但并发受池容量与 DB 连接数约束
    t0 = time.perf_counter()
    await asyncio.gather(*[sync_to_async(setup_and_query, thread_sensitive=False)() for _ in range(5)])
    print(f"thread_sensitive=False 并行 5 次: {(time.perf_counter()-t0)*1000:.1f} ms(注意容量链:线程池≤DB连接额度)")

asyncio.run(main())
```

**追问**：
1) 同一请求里两个 `thread_sensitive=False` 的 ORM 调用并发跑，有什么隐患？——两个线程各自拿连接，事务不再共享：`atomic()` 块内并发桥接会造成「事务在另一个线程看不到未提交数据」甚至连接状态错乱；事务内必须用默认的 thread_sensitive=True 或干脆把整段逻辑包成单个同步函数再桥接。
2) 怎么调线程池大小？——`asgiref` 层面可 `sync_to_async` 自定义 executor 或设置 `DJANGO_ASYNC_*` 风格的环境变量（Django 5.1+ 提供 `DJANGO_ASGI_THREAD_GROUP` 类配置）；更直接的是自建 `ThreadPoolExecutor` 传入。公式：池大小 ≈ DB 连接上限 − 主进程其他用途 − 安全余量，而不是拍脑袋设 CPU 核数（这是 IO 型线程池，CPU 数无关）。
3) 为什么说 async ORM 不是性能免费午餐？——`aget()` 等价于 `sync_to_async(get)`，同样占一个线程池槽位；真正的收益只在「单请求内并发发起多个独立查询」（`asyncio.gather`）时减少等待，不能提升单查询本身的吞吐。
