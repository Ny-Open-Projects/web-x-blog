---
title: [Q878] SQL 改写: OR 条件拆 UNION ALL
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q878 · SQL 改写: OR 条件拆 UNION ALL

> 难度:★★★☆ | 标签:改写, 索引

**问**:`WHERE a = 1 OR b = 2` 为什么常常全表扫描?怎么改?

**答**:OR 连接两个不同列的条件时,单棵索引无法同时服务两侧,优化器若没有 index_merge(如 SQLite 常见 `OR 优化`、MySQL 的 index_merge union)就会退化为全表扫描。改写思路是拆成两个子查询各走各的索引,再用 UNION ALL 合并:同一行只在其中一侧命中,天然不重;若同一行可能两侧同时命中需用 UNION(带去重)或对结果再排重。注意 UNION ALL 不去重、不排序,代价最小;改写后用 EXPLAIN 确认两个分支都走了索引才算成功。若两列命中率都很高,保留全表扫描反而可能更快,量化的依据仍是扫描行数对比。

```python
# file: code/04_数据库与缓存/q878_or_union.py
"""OR 跨列条件拆 UNION ALL, 对比执行计划"""
import sqlite3

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.execute("CREATE TABLE t (id INTEGER PRIMARY KEY, a INT, b INT)")
        conn.executemany("INSERT INTO t (a, b) VALUES (?, ?)",
                         [(i % 100, i % 7) for i in range(50000)])
        conn.execute("CREATE INDEX idx_a ON t (a)")
        conn.execute("CREATE INDEX idx_b ON t (b)")

        or_sql = "SELECT * FROM t WHERE a = 1 OR b = 2"
        plan = conn.execute("EXPLAIN QUERY PLAN " + or_sql).fetchall()
        print("OR 写法:", [r[3] for r in plan])

        split_sql = ("SELECT * FROM t WHERE a = 1 UNION ALL "
                     "SELECT * FROM t WHERE b = 2 AND a <> 1")
        plan2 = conn.execute("EXPLAIN QUERY PLAN " + split_sql).fetchall()
        print("UNION ALL:", [r[3] for r in plan2])
        print("行数一致:", conn.execute(or_sql).fetchall().__len__(),
              conn.execute(split_sql).fetchall().__len__())
```

**追问**:
- 为什么第二段要加 `a <> 1`?——防止 a=1 且 b=2 的行在两个分支重复出现,保证与原 OR 语义等价;若用 UNION 则可自动去重但多一步哈希去重成本。
- index_merge 是什么?——MySQL 对同一张表用多个索引分别定位再合并结果集的机制,有时可用但常被改成显式 UNION 更稳定。

---
