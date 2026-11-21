---
title: [Q6501] SQLAlchemy 2.0 异步引擎的事务边界与超时传递
date: 2026-11-18
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6501 · SQLAlchemy 2.0 异步引擎的事务边界与超时传递

> 难度:★★★ | 标签:SQLAlchemy, 异步, 事务

**问**：我们把同步 SQLAlchemy 迁到 2.0 异步引擎后出现过两类事故：一是请求取消后事务没回滚、连接带脏状态回池；二是 `statement_timeout` 设了却不生效。异步引擎下事务边界到底该怎么划，超时又是怎么一层层传递的？

**答**：结论先行：异步下事务边界必须与"请求/任务生命周期"绑定，用 `async with engine.begin()` 或 `async with session.begin()` 块作为唯一边界，任何提前 `commit` 都是事故温床；超时则要分清三层——连接获取超时（池层）、语句超时（服务端 `statement_timeout`，经 connect args 传下去）、应用层取消（asyncio CancelledError），三者语义不同、必须显式各配各的。

取舍与原理：
- 连接归还 ≠ 事务清理。1.x 的 `pool` 在同步时代靠 `reset_on_return`（rollback）兜底，2.0 异步引擎同样会 reset，但如果协程在 `await` 点被取消（客户端断连、上游超时），**取消异常会从当前 await 点抛出**——如果这个点在 `session.execute()` 里，`AsyncSession` 的上下文管理器会正常走 `__aexit__` 回滚；但如果你手写 `try/finally` 却在 finally 里又 `await`（比如异步 commit），取消风暴下 finally 里的 await 本身会被打断，出现"半提交"。所以实战规则：清理路径尽量短，回滚优先于提交，回滚用 `session.rollback()`（同步方法，不 yield 协程点）。
- 超时传递链：`create_async_engine(..., connect_args={"server_settings": {"statement_timeout": "3000"}})`（asyncpg 方言）在**连接建立时**写入会话参数，对池中所有连接生效；而 `execution_options(timeout=...)` 之类是方言相关的 per-statement 手段，不要混着指望。池层配 `pool_timeout`（等连接的超时）和 `pool_pre_ping`（取连接前探活）。三层分别防：拿不到连接、单条 SQL 拖死、整请求超时。漏掉服务端 statement_timeout 是最常见事故——应用侧 `asyncio.wait_for` 只取消客户端等待，**服务端查询还在跑**，PG 连接被占满，看起来就是"取消了但负载没降"。
- 实战复盘：我们曾在网关层加了 3 秒 `asyncio.timeout`，但 DB 侧 QPS 没降，pg_stat_activity 里一堆 active 老查询。根因就是只有客户端取消。补救：connect_args 下发 statement_timeout + 慢查询 kill 脚本兜底。

```python
# 基线:Python 3.11+ / SQLAlchemy 2.0+ / asyncpg;未装库时本文件仅演示结构
# pip install sqlalchemy[asyncio] asyncpg  (缺库降级:可对照同步 Session 理解边界)
import asyncio

# from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
# engine = create_async_engine(
#     "postgresql+asyncpg://app:pw@db/app",
#     pool_size=10, max_overflow=5, pool_timeout=5,      # 池层:等连接最多 5s
#     pool_pre_ping=True,
#     connect_args={"server_settings": {"statement_timeout": "3000"}},  # 服务端单语句 3s
# )
# SessionLocal = async_sessionmaker(engine, expire_on_commit=False)


async def transfer(session_maker, from_id: int, to_id: int, amount: int) -> None:
    """事务边界与请求生命周期绑定的标准写法:begin 块即边界,异常自动回滚。"""
    try:
        # async with session_maker() as session:
        #     async with session.begin():          # 显式事务块:进入 BEGIN,异常 EXIT 回滚
        #         await session.execute(text("UPDATE acct SET bal=bal-:a WHERE id=:i"),
        #                              {"a": amount, "i": from_id})
        #         await session.execute(text("UPDATE acct SET bal=bal+:a WHERE id=:i"),
        #                              {"a": amount, "i": to_id})
        #     # 出块即 commit;取消会传播进来并回滚,无需手写 finally
        await asyncio.sleep(0)  # 演示占位(缺库降级)
    except asyncio.CancelledError:
        # 取消已由上下文管理器回滚;此处只做审计上报,不要再 await 业务提交
        raise


async def demo_timeout_layering() -> None:
    """应用层超时只防'整请求',服务端 statement_timeout 防单语句。"""
    async def slow_query() -> None:
        await asyncio.sleep(10)
    try:
        async with asyncio.timeout(3):          # Python 3.11+ 应用层
            await slow_query()
    except TimeoutError:
        print("客户端超时;但真实 DB 里服务端查询需靠 statement_timeout 终结")

if __name__ == "__main__":
    asyncio.run(demo_timeout_layering())
```

**追问**：
- 一层追问：`expire_on_commit=False` 为什么在异步下几乎是必配？——commit 后访问 ORM 属性会触发隐式懒加载 IO，在异步里抛 `MissingGreenlet` 错；关掉过期让 commit 后属性仍可读，把刷新变成显式操作。
- 二层追问：连接池打满时，你优先扩 `pool_size` 还是给 `pool_timeout` 加告警？——优先告警+定位慢查询。池打满是症状不是病因，扩池只是把问题传导给 PG（连接数、锁竞争），P6+ 的做法是用 pg_stat_activity 归因后再定量：`pool_size ≈ 单实例并发预算 × DB 可承受连接占比`。
- 三层追问：事务块里要调外部 HTTP 怎么办？——禁止。事务内做远程调用会拉长锁持有时间，取消/重试还会造成"本地回滚但远端已生效"的跨系统不一致；拆成事务发件箱或先外部调用再开短事务。
