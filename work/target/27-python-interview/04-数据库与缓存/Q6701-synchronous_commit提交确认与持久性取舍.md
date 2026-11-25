---
title: "[Q6701] synchronous_commit 提交确认与持久性的取舍"
date: 2026-11-23
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6701 · synchronous_commit 提交确认与持久性的取舍

难度：P6 ｜ 标签：事故复盘、PostgreSQL、持久性、性能取舍

基线：Python 3.12；PostgreSQL 12+；sqlite3 标准库做等价语义演示（`PRAGMA synchronous`）。

**问**：为了把写吞吐拉上去，DBA 把 `synchronous_commit` 从 on 改成 off，压测 QPS 近乎翻倍。结果一次机房断电后，几百笔"已经返回成功"的订单不见了。既然 WAL 还在写，为什么会丢？这跟 `fsync=off` 是一回事吗？

**答**：
- **结论**：`synchronous_commit=off` 并不是关掉 WAL，而是把"提交时同步等待 WAL 刷盘"这一步异步化——事务提交立即返回成功，WAL 由 walwriter 后台周期性批量落盘。崩溃时那些尚未落盘的 WAL 对应的事务就丢失，但数据库文件本身仍一致（不会损坏）。它与 `fsync=off` 有本质区别：后者连 OS 刷盘都不保证，崩溃可能损坏数据文件；前者只是"提交确认提前"，丢的是已确认事务，库仍一致。
- **取舍**：适合丢几秒数据可接受、吞吐优先的场景（日志、埋点、可重算中间结果）；绝不适合订单、支付、账务。折中做法：全局保持 on，仅在批处理会话里 `SET LOCAL synchronous_commit = off`；同步复制场景用 `remote_apply` 保证备库已重放后再确认。
- **实战**：审计所有非默认 GUC（`SHOW synchronous_commit`），确认没有全局 off；用 `pg_stat_wal` 的 wal_records/wal_bytes 观察 walwriter 压力；做断电演练验证 RPO 是否满足业务承诺；把"提交成功但数据可能丢"写进 SLO 风险清单。

```python
import os
import sqlite3
import tempfile
import time


def measure(mode: str, n: int = 200) -> float:
    path = os.path.join(tempfile.gettempdir(), f"q6701_{mode}.db")
    if os.path.exists(path):
        os.remove(path)
    conn = sqlite3.connect(path)
    conn.execute(f"PRAGMA synchronous={mode}")
    conn.execute("CREATE TABLE t (x INTEGER)")
    t0 = time.perf_counter()
    for i in range(n):
        conn.execute("INSERT INTO t VALUES (?)", (i,))
        conn.commit()
    elapsed = time.perf_counter() - t0
    conn.close()
    return elapsed


if __name__ == "__main__":
    for mode in ("FULL", "NORMAL", "OFF"):
        print(f"sqlite synchronous={mode}: {measure(mode):.4f}s / 200 commits")
    # FULL 每次 commit 都等落盘最慢；OFF 不等待最快，但崩溃会丢已提交事务。
```

**追问一**：`synchronous_commit=off` 和 `fsync=off` 有什么本质区别？
→ 解析：前者只让提交确认提前，崩溃丢的是"已确认但未落盘"的事务，数据文件仍一致、库可正常启动；后者连 OS 刷盘都跳过，崩溃可能损坏数据文件本身，风险高一个量级。

**追问二**：同步复制下 `remote_apply` 比 `on` 强在哪？
→ 解析：`on`（等价于 remote_flush）只保证备库收到并刷盘 WAL；`remote_apply` 保证备库已重放完成，切主后数据立即可见、读己之写有保证，代价是提交延迟更高。
