---
title: [Q890] EXISTS / IN / JOIN: 半连接语义与 NULL 陷阱
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q890 · EXISTS / IN / JOIN: 半连接语义与 NULL 陷阱

> 难度:★★★★ | 标签:子查询, NULL

**问**:EXISTS 与 IN 有什么区别?NOT IN 遇到 NULL 为什么会"全军覆没"?

**答**:语义上,`x IN (子查询)` 与 `EXISTS(相关子查询)` 在"判断存在性"场景等价,优化器通常都能转成半连接(semi-join),性能差异更多来自旧版本实现而非语法本身。真正的分水岭是 NULL:IN 列表里出现 NULL 时,`x NOT IN (1, NULL)` 对任何 x 都无法判定为真——三值逻辑下要么 FALSE 要么 UNKNOWN,结果集直接为空;NOT EXISTS 不受影响,这就是"NOT IN 遇 NULL 必出事"的经典坑。工程规则:NOT 场景优先 NOT EXISTS 或 LEFT JOIN ... IS NULL;IN 的子查询列保证 NOT NULL;大数据量时把子查询物化或改 JOIN 由优化器接管。

```python
# file: code/04_数据库与缓存/q890_not_in_null.py
"""复现 NOT IN 遇 NULL 结果为空, 对照 NOT EXISTS 的正确语义"""
import sqlite3

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
        conn.execute("CREATE TABLE banned (user_id INT)")
        conn.executemany("INSERT INTO users (name) VALUES (?)",
                         [("a",), ("b",), ("c",)])
        conn.executemany("INSERT INTO banned (user_id) VALUES (?)",
                         [(2,), (None,)])         # 含 NULL

        not_in = "SELECT name FROM users WHERE id NOT IN (SELECT user_id FROM banned)"
        not_exists = ("SELECT u.name FROM users u WHERE NOT EXISTS "
                      "(SELECT 1 FROM banned x WHERE x.user_id = u.id)")
        print("NOT IN 结果:", [r[0] for r in conn.execute(not_in)], "<- 因 NULL 全空")
        print("NOT EXISTS:", [r[0] for r in conn.execute(not_exists)], "<- 正常排除 id=2")
        print("计划对照:")
        for sql in (not_in, not_exists):
            print(" ", [r[3] for r in conn.execute("EXPLAIN QUERY PLAN " + sql).fetchall()])
```

**追问**:
- IN 大列表有什么风险?——几千个常量的 IN 会让解析与计划开销巨大,应改临时表 JOIN 或分批;MySQL 还受 max_allowed_packet 限制。
- EXISTS 一定比 IN 快吗?——不一定,半连接物化后 IN 子查询只执行一次,EXISTS 反而逐行触发;让优化器基于统计选择,代码层面保持语义清晰。

---
