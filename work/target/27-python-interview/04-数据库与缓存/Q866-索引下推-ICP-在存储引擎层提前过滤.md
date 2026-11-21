---
title: [Q866] 索引下推 ICP: 在存储引擎层提前过滤
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q866 · 索引下推 ICP: 在存储引擎层提前过滤

> 难度:★★★★ | 标签:索引, MySQL

**问**:什么是 Index Condition Pushdown?它解决了什么问题?

**答**:ICP(MySQL 5.6+)把"能用索引列判断的 WHERE 条件"下推到 InnoDB 存储引擎层,在索引上逐条判断后再决定是否回表。没有 ICP 时,联合索引 `(name, age)` 上 `name LIKE '张%' AND age = 20` 会把所有姓张的索引项全部回表,再由 server 层过滤 age;有了 ICP,age 条件在索引里先过滤,回表次数大幅减少。收益取决于索引无法继续定位的"残留条件"的选择性;EXPLAIN 的 Extra 出现 `Using index condition` 即生效。SQLite 没有独立存储引擎架构(过滤本来就在取行路径上做),概念上天然具备,面试主要考 MySQL 场景。

```python
# file: code/04_数据库与缓存/q866_icp_concept.py
"""用 sqlite 模拟 ICP 收益: 联合索引前缀模糊 + 残留条件, 观察扫描与回表差"""
import sqlite3

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.execute("CREATE TABLE user (id INTEGER PRIMARY KEY, name TEXT, age INT)")
        conn.executemany("INSERT INTO user (name, age) VALUES (?, ?)",
                         [(("张" if i % 2 else "李") + f"{i:05d}", i % 80)
                          for i in range(20000)])
        conn.execute("CREATE INDEX idx_name_age ON user (name, age)")

        sql = "SELECT * FROM user WHERE name LIKE '张%' AND age = 20"
        plan = conn.execute("EXPLAIN QUERY PLAN " + sql).fetchall()
        rows = conn.execute(sql).fetchall()
        print("计划:", [r[3] for r in plan])
        print(f"命中 {len(rows)} 行")
        print("MySQL 对照: 无 ICP 时全部张姓回表后过滤; 有 ICP 时在索引内先滤 age")
```

**追问**:
- ICP 和覆盖索引什么关系?——覆盖索引连回表都省了更优;ICP 是"必须回表但先在索引里过滤"的次优方案。
- 哪些条件推不下去?——涉及非索引列、函数计算、跨表的条件无法在引擎层判断,只能回表后由 server 层处理。

---
