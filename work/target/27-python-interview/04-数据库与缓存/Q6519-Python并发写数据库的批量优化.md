---
title: [Q6519] Python 并发写库的批量优化： executemany 与 pipeline
date: 2026-11-19
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6519 · 并发写库批量优化

> 难度:★★☆ | 标签:批量写入, 事务, 性能

**问**：写入 10 万条数据，「逐条 insert 提交」要 40 分钟，批量化能到多少——快在哪（RTT/事务/fsync 三层）？`executemany` 的两种执行模式（逐语句 vs 真批量）、Redis `pipeline` 与 `transaction` 的区别，批量与事务大小的平衡点怎么找？

**答**：慢的根源三层：① **网络 RTT**：每条一个往返（同机房 0.5ms×10 万 = 50s 起）；② **事务 fsync**：每 commit 一次磁盘刷盘（1-10ms/次，最大头）；③ **语句解析**：每条重新 prepare。批量解法：`executemany` + 单事务把 10 万条压成 N 批（每批 1 RTT + 1 fsync），40 分钟 → 秒级。`executemany` 两模式：DBAPI 逐条执行（没省 RTT）vs **真批量**（MySQL `executemany` 拼 multi-values 单语句；psycopg2 用 `execute_values`/psycopg3 `executemany` pipeline 模式）——必须确认驱动模式否则白搭。Redis pipeline：攒命令一次发送（省 RTT），`pipeline(transaction=True)`（默认）额外包 MULTI/EXEC（原子但服务端要缓存整批）；纯提速用 transaction=False。批量大小平衡：批越大 fsync 越省但**锁持有越久**（阻塞其他写）+ 失败重放成本越大；经验 500-5000 行/批，按「单批耗时 < 主从延迟预算」定。

```python
# 基线 SQLAlchemy 2.0 + SQLite（本机可跑）；MySQL/PG 口径见注释
import time, sqlalchemy as sa

meta = sa.MetaData()
t = sa.Table("rows", meta,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("val", sa.String(32)))

def seed(eng):
    meta.create_all(eng)

def insert_row_by_row(eng, n=2000):
    with eng.begin() as c:                      # 全在一个事务（已排除 fsync 差异）
        t0 = time.perf_counter()
        for i in range(n):
            c.execute(t.insert().values(id=i, val=f"v{i}"))   # 2000 次 RTT/解析
        return time.perf_counter() - t0

def insert_executemany(eng, n=2000, batch=500):
    rows = [{"id": i, "val": f"v{i}"} for i in range(n)]
    t0 = time.perf_counter()
    for i in range(0, n, batch):
        chunk = rows[i:i+batch]
        with eng.begin() as c:                  # 每批 1 事务 = 1 fsync
            c.execute(t.insert(), chunk)        # executemany 真批量路径（SQLAlchemy 2.0）
    return time.perf_counter() - t0

def redis_pipeline_semantics():
    """pipeline(transaction) 语义（无 redis 库时看注释口径）：
    pipe = r.pipeline(transaction=False)   # 只省 RTT：命令流水线发送，非原子
    pipe = r.pipeline(transaction=True)    # 包 MULTI/EXEC：原子（服务端缓存整批，占内存）
    大批量用 transaction=False + 业务幂等；要原子且批次小才用 True。
    """
    return "pipeline: False=省RTT / True=MULTI原子"

if __name__ == "__main__":
    eng1 = sa.create_engine("sqlite://"); seed(eng1)
    eng2 = sa.create_engine("sqlite://"); seed(eng2)
    slow = insert_row_by_row(eng1)
    fast = insert_executemany(eng2)
    print(f"逐条: {slow*1000:.0f}ms / executemany 分批: {fast*1000:.0f}ms "
          f"（SQLite 本机差 5-10×；网络 DB 差 50-100×）")
    assert fast < slow
    print(redis_pipeline_semantics())
    # MySQL 真批量口径：conn.cursor().executemany("INSERT ... VALUES(%s,%s)", rows)
    # 驱动自动拼 multi-values（rewrite_batched_statements=True 才生效！JDBC 同理）
    # PG 真批量口径：psycopg3 executemany pipeline / COPY（10 万+行首选 COPY）。
```

**追问**：1) 为什么「单批耗时 < 主从延迟预算」？——单批事务越大，从库重放该事务越久，主从延迟瞬时抬升；延迟又反过来放大只读业务感知——批大小是写吞吐与复制延迟的杠杆。2) COPY vs executemany 的分界？——psycopg3 executemany 管道模式省 RTT 但仍逐语句执行；`COPY FROM` 走二进制流直写数据文件（绕过语句解析与 WAL 常规路径优化），10 万行级别一个量级差距；触发器/复杂约束表 COPY 受限。3) 批量失败的重放语义？——批量插入部分成功部分失败（唯一键冲突）时，`executemany` 常见行为是整批回滚（事务内）——预清洗冲突键（先查存在集合）比捕获重放便宜。

## 背诵要点
1. 慢三层：RTT、commit fsync（最大头）、语句解析；批量 = N 批 × (1 RTT + 1 fsync)。
2. 驱动模式要确认：MySQL rewrite_batched_statements、PG execute_values/COPY——否则 executemany 是假批量。
3. 批大小平衡点：500-5000 行/批，单批耗时 < 主从延迟预算；Redis pipeline 省加速用 transaction=False。

## 复盘追问
1. 批量写入时另一个业务突然变慢，怀疑锁，怎么定位？（提示：锁等待视图（innodb_lock_waits/pg_locks）+ 单批时长与锁持有时间关系，缩小批）
2. 10 万行/批的 COPY 挂在约束冲突上，工程上怎么拆？（提示：预清洗（临时表 ON CONFLICT 合并）或分小批隔离坏行 + 死信重放）
