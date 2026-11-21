---
title: [Q863] EXPLAIN ANALYZE 与估算偏差
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q863 · EXPLAIN ANALYZE 与估算偏差

> 难度:★★★☆ | 标签:执行计划, 统计信息

**问**:EXPLAIN 的 rows 估算和实际执行差很远会发生什么?怎么发现和修正?

**答**:EXPLAIN 只展示优化器"打算怎么做",行数来自统计信息(索引基数、采样)的估算;估算失真会让优化器选错 join 顺序或索引,比如把 10 行估成 10 万行后放弃索引。用 MySQL 8 或 PostgreSQL 的 `EXPLAIN ANALYZE` 可以看到每步"估算行 vs 实际行 vs 实际耗时"的偏差;SQLite 没有 EXPLAIN ANALYZE,对应手段是 `EXPLAIN QUERY PLAN` 看计划、`EXPLAIN` 看字节码、`ANALYZE` 维护统计信息。修正手段:执行 `ANALYZE TABLE` 更新统计信息,或针对倾斜列加直方图;应用层避免"刚批量导入就查询"导致的统计陈旧。面试时能讲出"估算驱动优化器,统计信息是优化器的眼睛"即可。

```python
# file: code/04_数据库与缓存/q863_explain_analyze.py
"""SQLite: QUERY PLAN 看计划, ANALYZE 维护统计信息; MySQL/PG 才有 EXPLAIN ANALYZE"""
import sqlite3

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.execute("CREATE TABLE t (id INTEGER PRIMARY KEY, v INT)")
        conn.executemany("INSERT INTO t (v) VALUES (?)",
                         [(i % 10,) for i in range(5000)])
        conn.execute("CREATE INDEX idx_v ON t (v)")

        print("计划:", [r[3] for r in conn.execute(
            "EXPLAIN QUERY PLAN SELECT * FROM t WHERE v = 3").fetchall()])
        print("MySQL8/PG: EXPLAIN ANALYZE 给出 估算行 vs 实际行 vs 实际耗时")
        print("SQLite 替代: EXPLAIN 字节码计数 + ANALYZE 统计信息交叉验证")

        conn.execute("ANALYZE")
        print("ANALYZE 后统计:", conn.execute(
            "SELECT tbl, idx, stat FROM sqlite_stat1").fetchall())
```

**追问**:
- 统计信息多久更新一次?——MySQL 5.7 起默认自动重采样(innodb_stats_auto_recalc,表变化超 10% 触发),大变更后也可手动 ANALYZE。
- 优化器估算错还能强行干预吗?——可以,用 FORCE INDEX / 直方图 / 调整 join 顺序等 hint,但应作为最后手段并记录原因。

---
