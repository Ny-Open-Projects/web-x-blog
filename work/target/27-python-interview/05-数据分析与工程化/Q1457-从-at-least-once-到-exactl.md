---
title: [Q1457] 从 at-least-once 到 exactly-once
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1457 · 从 at-least-once 到 exactly-once

> 难度:★★★★ | 标签:exactly-once, 去重

**问**:面试官:消息队列保证 at-least-once,你的入库管道凭什么宣称 exactly-once?

**答**:先讲清楚不可能免费拿到:exactly-once 端到端永远是"at-least-once 投递 + 幂等消费"合成出来的。核心机制是去重登记与业务写入放在同一事务:消费批次时先向"已见批次表"插入批次号,再写数据行,任何一步失败整体回滚;生产端重放同一批次时,批次号插入触发唯一键冲突,整个事务回滚,数据行零重复。批次号的来源是生产端的批次标识(分区 + offset 区间或业务批次 ID),它必须跨重放保持稳定。两个容易答错的点:一是去重表若与数据表分开提交,中间崩溃就退化成 at-least-once,所以"同事务"是命门;二是去重表的清理策略,批次登记要按保留期滚动删除,否则无限膨胀。这套思想在 Flink 的两阶段提交 sink、Kafka 事务、以及所有 CDC 管道里都是同一个骨架。

```python
# file: code/05_数据分析与工程化/q1457_exactly_once.py
"""at-least-once 到 exactly-once:去重表与数据写入同一事务"""

import sqlite3

DDL = """
CREATE TABLE ingest_rows (
    row_id TEXT PRIMARY KEY,
    batch_id TEXT NOT NULL,
    payload TEXT NOT NULL
);
CREATE TABLE seen_batches (
    batch_id TEXT PRIMARY KEY
);
"""


def consume_batch(conn, batch_id, rows):
    """整批写入与'批次登记'放在同一事务:任何一步失败整体回滚"""
    cur = conn.cursor()
    cur.execute("BEGIN IMMEDIATE")
    try:
        cur.execute("INSERT INTO seen_batches (batch_id) VALUES (?)", (batch_id,))
        cur.executemany(
            "INSERT INTO ingest_rows (row_id, batch_id, payload) VALUES (?, ?, ?)",
            [(r[0], batch_id, r[1]) for r in rows])
        conn.commit()
        return "committed"
    except sqlite3.IntegrityError:
        conn.rollback()
        return "duplicate batch skipped"


if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    conn.executescript(DDL)
    batch = [("r1", "order o1"), ("r2", "order o2")]

    print("第一次消费 batch-1:", consume_batch(conn, "batch-1", batch))
    # at-least-once 语义下,生产端一定会重放
    print("重放 batch-1   :", consume_batch(conn, "batch-1", batch))
    print("消费 batch-2   :", consume_batch(conn, "batch-2", [("r3", "order o3")]))

    n = conn.execute("SELECT COUNT(*) FROM ingest_rows").fetchone()[0]
    b = conn.execute("SELECT COUNT(*) FROM seen_batches").fetchone()[0]
    print(f"最终行数 {n}(期望 3),已登记批次 {b}(期望 2)")
    print("要点:去重登记与业务写入必须同事务,分开写就退化成 at-least-once")
```

**追问**:
- 追问 1:目标库不支持事务怎么办?—— 退而求其次做"幂等键 + 行级去重",或先写可重放的中间层再原子切换,牺牲实时性换正确性。
- 追问 2:大事务的性能问题怎么解?—— 控制批次大小,或用"去重表先落、数据行异步幂等写"的折中,但要接受窗口期内可查询但未终态。
