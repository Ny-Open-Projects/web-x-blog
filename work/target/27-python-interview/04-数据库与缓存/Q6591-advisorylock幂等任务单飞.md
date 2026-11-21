---
title: [Q6591] PostgreSQL advisory lock 的幂等单飞与锁释放边界
date: 2026-11-18
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6591 · PostgreSQL advisory lock 的幂等单飞与锁释放边界

> 难度:★★★★ | 标签:PostgreSQL, 分布式锁, 任务调度

**问**：定时任务多副本部署，cron 到点全都会跑，想"只有一个实例执行"。用 advisory lock 怎么实现单飞？`pg_advisory_lock`、`pg_try_advisory_lock`、`pg_advisory_xact_lock` 三个函数在 Python 里怎么选、锁什么时候释放？

**答**：结论：任务单飞用 **`pg_try_advisory_lock(key)` 非阻塞尝试 + 拿不到直接退出**，锁绑定物理连接，`conn.close()`（或进程退出）自动释放；绝不选阻塞版 `pg_advisory_lock` 去抢——它会让 N-1 个副本排队干等。三个版本的生命周期：`pg_advisory_lock` 挂在会话（物理连接）上，必须显式 `unlock`，断连兜底释放；`pg_try_advisory_lock` 同上但立即返回布尔；`pg_advisory_xact_lock` 挂在事务上，commit/rollback 自动释放、不可手动解，适合"事务内互斥"。选型口诀：**调度单飞用 try+连接生命周期，业务互斥用 xact+事务生命周期**。

实战要点：
- key 分配：advisory lock 的 key 是全局 64 位命名空间，`hashtext('job:daily-report')` 式派生或集中登记，避免两个业务撞 key 互相"单飞"。
- 拿锁后先建心跳再干活：单飞锁只保证"同时只有一个"，不保证"一定跑完"——持锁实例 crash 后锁随连接断开自动释放，下一轮 cron 自然接管，这是 advisory lock 相优于外部锁文件的地方。
- 事故复盘：某副本持锁跑 40 分钟报表，期间连接池回收了这条"空闲"连接（pool_recycle 误伤），锁悄悄没了，第二副本拿到锁并发跑，双方都写中间表。修复：单飞连接独立于业务池（不走 SQLAlchemy pool），持锁期间发心跳查询保活。

```python
# 基线:Python 3.9+ / psycopg 或 SQLAlchemy(略) ;缺库降级用 sqlite 模拟生命周期
try:
    import psycopg
    HAS_PG = True
except ImportError:
    HAS_PG = False
import sqlite3, contextlib

@contextlib.contextmanager
def job_flylock(pg_conn, key: int):
    """单飞上下文:try advisory lock,拿不到则不进入。"""
    if HAS_PG:
        got = pg_conn.execute("SELECT pg_try_advisory_lock(%s)", (key,)).fetchone()[0]
        try:
            yield got
        finally:
            if got:
                pg_conn.execute("SELECT pg_advisory_unlock(%s)", (key,))
    else:
        conn = sqlite3.connect(":memory:")          # 降级:sqlite 布锁演示
        got = conn.execute("BEGIN EXCLUSIVE") is not None
        try:
            yield got
        finally:
            conn.close()                             # 连接断开=释放,与 PG 语义一致

if __name__ == "__main__":
    c = psycopg.connect() if HAS_PG else None
    with job_flylock(c, 871001) as got:
        print("拿到单飞锁,开始跑任务" if got else "另一副本在跑,本轮退出")
```

**追问**：
- 一层追问：为什么不用 Redis 锁做单飞？——Redis 锁有过期时间两难（太短误释放、太长故障期无人接手），且续期要 watchdog；advisory lock 的释放绑定 TCP 连接，进程死=连接断=锁释放，语义更强；代价是锁无法跨进程主动续期，超长任务要靠连接保活。
- 二层追问：锁等价的重复执行窗口在哪？——副本 A 的任务已跑完但结果未落库、连接断开锁释放、副本 B 立刻抢到锁重跑，期间 A 落库——靠任务本身的幂等（产出唯一键 + upsert）兜底，锁只防并发不防重放。
- 三层追问：xact 模式下回滚也释放锁，会不会出现"回滚后别人立刻抢到导致脏状态"？——会，所以事务级锁保护的是"事务内资源"而非"任务级产物"；任务级产物落库必须与持锁事务同事务提交，或用两阶段（占位表 + 完成标记）。
