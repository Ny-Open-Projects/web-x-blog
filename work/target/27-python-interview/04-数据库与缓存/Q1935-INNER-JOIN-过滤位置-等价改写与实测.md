---
title: [Q1935] INNER JOIN 过滤位置: 等价改写与实测
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1935 · INNER JOIN 过滤位置: 等价改写与实测

> 难度:★★★☆ | 标签:SQL, JOIN

**问**:内连接里过滤条件写 ON 和写 WHERE 有区别吗?团队规范要求统一放一边有道理吗?

**答**:语义上完全等价:内连接先按 ON 匹配再用 WHERE 过滤, 与把全部条件堆进 ON, 数学结果相同。工程上现代优化器都会做谓词下推与连接重排, 两种写法生成同一个执行计划, 本机实测计划与耗时一致。所以规范要求统一位置是为了可读性与可维护性, 不是性能。真正要敏感的是外连接:一旦有人把 INNER JOIN 改成 LEFT JOIN 调试, ON 与 WHERE 的语义差异立刻显现, 统一的写法能减少这类改写事故。结论记一句:差异只在外连接, 内连接选哪种都是风格问题。

```python
# file: code/04_数据库与缓存/q1935_inner_join_filter.py
"""INNER JOIN 过滤位置: ON 与 WHERE 等价且计划相同"""
import sqlite3
import time

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE a(id INTEGER PRIMARY KEY, k INTEGER)")
conn.execute("CREATE TABLE b(id INTEGER PRIMARY KEY, a_id INTEGER, flag TEXT)")
conn.executemany("INSERT INTO a(k) VALUES(?)", [(i % 1000,) for i in range(100000)])
conn.executemany("INSERT INTO b(a_id, flag) VALUES(?,?)",
                 [((i * 3) % 100000 + 1, 'y' if i % 2 else 'n') for i in range(120000)])
conn.execute("CREATE INDEX idx_b_aid ON b(a_id)")
conn.commit()

sql_on = "SELECT COUNT(*) FROM a JOIN b ON a.id = b.a_id AND b.flag = 'y' WHERE a.k = 7"
sql_where = "SELECT COUNT(*) FROM a JOIN b ON a.id = b.a_id WHERE a.k = 7 AND b.flag = 'y'"
r1 = conn.execute(sql_on).fetchone()[0]
r2 = conn.execute(sql_where).fetchone()[0]
print("ON 混合条件结果:", r1, "  WHERE 混合条件结果:", r2, "  相同:", r1 == r2)

def plan(sql):
    return " | ".join(r[3] for r in conn.execute("EXPLAIN QUERY PLAN " + sql))

print("ON    计划:", plan(sql_on))
print("WHERE 计划:", plan(sql_where))

def timed(sql, n=5):
    t0 = time.perf_counter()
    for _ in range(n):
        conn.execute(sql).fetchone()
    return (time.perf_counter() - t0) / n * 1000

print(f"ON 耗时 {timed(sql_on):.2f} ms  WHERE 耗时 {timed(sql_where):.2f} ms")
print("结论: 内连接里 ON 与 WHERE 语义等价 计划与耗时相同; 位置差异只在外连接才有后果")
```

**追问**:
- 逗号连接写法算哪种?—— FROM a, b WHERE a.id = b.id 是老式内连接, 条件只能在 WHERE, 现代代码不推荐, 漏写条件会变笛卡尔积。
- 过滤条件位置会影响连接顺序吗?—— 现代优化器基于代价选择, 与书写位置无关;老版本 MySQL 5.x 的 straight_join 场景才需要手工控制。

---
