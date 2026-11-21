---
title: [Q877] SQL 改写: 相关子查询转 JOIN
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q877 · SQL 改写: 相关子查询转 JOIN

> 难度:★★★☆ | 标签:改写, 优化

**问**:为什么说相关子查询慢?怎么把它改写成 JOIN?有语义陷阱吗?

**答**:相关子查询(Correlated Subquery)对外层每行执行一次,形如"对每个用户,数他的订单数",行数多时是 N 次重复执行,老版本 MySQL 表现尤差。改写通常有两条路:聚合后 JOIN——先 `GROUP BY user_id` 汇总,再与用户表 JOIN,把 N 次查询变成两次扫描;或直接 LEFT JOIN + GROUP BY。陷阱在于:若子查询里是 COUNT 这种无重复聚合,JOIN 后计数不变;若是 SUM 多行明细,JOIN 一对多再聚合会因中间表重复而行数膨胀,必须先聚合再 JOIN 或用 DISTINCT 去重。新版优化器对部分场景会自动做半连接/物化,但仍应写出让意图明确的形态。

```python
# file: code/04_数据库与缓存/q877_subquery_to_join.py
"""对比相关子查询与先聚合再 JOIN 两种写法的计划与结果一致性"""
import sqlite3
import time

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
        conn.execute("CREATE TABLE orders (id INTEGER PRIMARY KEY, user_id INT, amt REAL)")
        conn.executemany("INSERT INTO users (name) VALUES (?)",
                         [(f"u{i}",) for i in range(2000)])
        conn.executemany("INSERT INTO orders (user_id, amt) VALUES (?, ?)",
                         [(i % 2000, 10.0) for i in range(60000)])
        conn.execute("CREATE INDEX idx_o_user ON orders (user_id)")

        subq = ("SELECT u.name, (SELECT COUNT(*) FROM orders o "
                "WHERE o.user_id = u.id) AS cnt FROM users u")
        join = ("SELECT u.name, o.cnt FROM users u JOIN "
                "(SELECT user_id, COUNT(*) AS cnt FROM orders GROUP BY user_id) o "
                "ON o.user_id = u.id")

        t0 = time.perf_counter(); r1 = conn.execute(subq).fetchall(); t1 = time.perf_counter()
        r2 = conn.execute(join).fetchall(); t2 = time.perf_counter()
        print(f"相关子查询: {(t1-t0)*1000:.1f} ms, {len(r1)} 行")
        print(f"聚合后 JOIN: {(t2-t1)*1000:.1f} ms, {len(r2)} 行")
        print("结果一致:", sorted(r1) == sorted(r2))
```

**追问**:
- 什么情况子查询反而更快?——只需要判断存在性(EXISTS 语义)且外层行数少时,半连接短路很高效,不必教条全改。
- 怎么确认优化器是否已自动改写?——看 EXPLAIN 的 plan 形态:出现物化表或 MATERIALIZED/semi-join 相关提示即已转换。

---
