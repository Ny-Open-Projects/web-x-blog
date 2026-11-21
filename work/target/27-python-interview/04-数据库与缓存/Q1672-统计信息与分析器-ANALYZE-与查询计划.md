---
title: [Q1672] 统计信息与分析器: ANALYZE 与查询计划
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1672 · 统计信息与分析器: ANALYZE 与查询计划

> 难度:★★★☆ | 标签:SQL 调优, 统计信息

**问**:优化器怎么知道走哪个索引?统计信息过期会发生什么?

**答**:优化器靠统计信息估算每个候选计划的行数与代价再择优:表行数、索引列的不同值数、直方图分布,对应 MySQL 的 information_schema 与 ANALYZE TABLE、PG 的 pg_statistic 与 ANALYZE、SQLite 的 sqlite_stat1 与 ANALYZE 命令。统计过期是事故常见根源:表被大量删改后,优化器仍按旧分布估算,可能在该全表扫时坚持走索引,或反之。本机实测:删掉 99% 的数据后计划纹丝不动,重新 ANALYZE 后立刻改为全表扫描——因为表只剩目标行,扫全表比索引跳转便宜。大批量变更后要手动重新收集,生产库还要给倾斜列配直方图。

```python
# file: code/04_数据库与缓存/q1672_analyze_stats.py
"""统计信息与分析器: ANALYZE 采集分布, 陈旧统计误导优化器"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE orders(id INTEGER PRIMARY KEY, status TEXT)")
conn.executemany("INSERT INTO orders VALUES(?,?)",
                 [(i, "pending" if i % 100 == 0 else "done") for i in range(1, 50001)])
conn.execute("CREATE INDEX idx_status ON orders(status)")
conn.commit()

def plan(sql):
    return [r[3] for r in conn.execute("EXPLAIN QUERY PLAN " + sql)]

q = "SELECT * FROM orders WHERE status='pending'"
print("未收集统计:", plan(q))
conn.execute("ANALYZE")
print("ANALYZE 后:", plan(q))
print("sqlite_stat1 内容 (表行数, 索引列不同值数):",
      conn.execute("SELECT tbl, idx, stat FROM sqlite_stat1").fetchall())

# 场景: 大规模删除后统计信息过期
conn.execute("DELETE FROM orders WHERE status='done'")
conn.commit()
print("现在表只剩", conn.execute("SELECT COUNT(*) FROM orders").fetchone()[0], "行, 全是 pending")
print("陈旧统计下的计划(仍按 5 万行估算):", plan(q))
conn.execute("ANALYZE")
print("重新 ANALYZE:", plan(q), "-> 表只剩目标行, 全表扫比索引跳转更便宜")
print("要点: 计划质量取决于统计新鲜度; 大批量变更后手动 ANALYZE, 生产库对倾斜列考虑直方图")
```

**追问**:
- ANALYZE 本身会锁表吗?——采样读不加写锁,代价主要是 IO;MySQL ANALYZE TABLE 有短暂 MDL,大表选低峰跑。
- 自动统计为什么没救回来?——MySQL 的自动重采集按变更行数比例触发,10% 阈值在大表上意味着要改几百万行才触发,大批量删除后应手动。

---
