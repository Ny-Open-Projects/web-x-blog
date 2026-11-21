---
title: [Q909] EXPLAIN 方言差异: MySQL 与 PostgreSQL 侧重点
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q909 · EXPLAIN 方言差异: MySQL 与 PostgreSQL 侧重点

> 难度:★★★☆ | 标签:执行计划, PostgreSQL

**问**:MySQL 与 PostgreSQL 的执行计划体系有什么主要差异?读计划时各关注什么?

**答**:MySQL EXPLAIN 输出每张表的访问行(type/key/rows/Extra),8.0 加 EXPLAIN ANALYZE 真实执行;它的优化器相对保守,依赖统计信息+hint,常见结论是"看 type 梯度与 Extra 标记"。PostgreSQL 计划是树形节点(Seq Scan/Index Scan/Nested Loop/Hash Join/Sort),自带成本估算与实际行数的对比(EXPLAIN ANALYZE),BUFFER 选项能看页面读取;PG 的优化器对 join 重排与并行查询更激进。共同方法论:先看扫描方式与估算偏差,再看排序/哈希的内存溢出,最后用 ANALYZE 修正统计。SQLite 则用 EXPLAIN QUERY PLAN 的扁平列表,SCAN/SEARCH 关键字对应全扫与索引定位。

```python
# file: code/04_数据库与缓存/q909_explain_dialects.py
"""打印 sqlite 计划并给出三大数据库计划读法对照表"""
import sqlite3

MAPPING = """
三大数据库计划速查:
  SQLite   SCAN t            ~ 全表扫描       | SEARCH t USING INDEX ~ 索引定位
  MySQL    type=ALL           ~ 全表扫描       | type=ref/range       ~ 索引访问  Extra: Using filesort
  PG       Seq Scan           ~ 全表扫描       | Index Scan           ~ 索引访问  Sort 节点表示显式排序
"""

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.execute("CREATE TABLE t (id INTEGER PRIMARY KEY, a INT, b TEXT)")
        conn.executemany("INSERT INTO t (a, b) VALUES (?, ?)",
                         [(i % 100, f"x{i}") for i in range(3000)])
        conn.execute("CREATE INDEX idx_a ON t (a)")

        for sql in ("SELECT * FROM t WHERE a = 5 ORDER BY b",
                    "SELECT * FROM t"):
            plan = conn.execute("EXPLAIN QUERY PLAN " + sql).fetchall()
            print(sql, "\n  ->", [r[3] for r in plan])
    print(MAPPING)
```

**追问**:
- 为什么同一 SQL 在两家数据库计划不同?——优化器实现、统计模型、join 算法(PG 有 hash join 更早)与成本参数不同,迁移 SQL 必须重新看计划而不是照搬索引。
- EXPLAIN ANALYZE 有副作用吗?——它真的执行语句,UPDATE/DELETE 会真实生效,测试要包在事务里回滚。

---
