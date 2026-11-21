---
title: [Q1937] HAVING vs WHERE: 过滤时机与代价实测
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1937 · HAVING vs WHERE: 过滤时机与代价实测

> 难度:★★☆☆ | 标签:SQL, 聚合

**问**:HAVING 和 WHERE 都是过滤, 什么时候用哪个?用错了只是风格问题吗?

**答**:两者的过滤时机不同:WHERE 在分组前过滤原始行, 参与聚合的数据更少;HAVING 在聚合后过滤组, 常用于引用聚合结果的场景。行级条件错写成 HAVING 不是风格问题, 是实打实的性能浪费, 本机实测里全量分组再过滤比先过滤慢一截, 数据量越大差距越大。经验法则:能用 WHERE 过滤的条件绝不放进 HAVING, 只有 COUNT、SUM、AVG 这类聚合条件才必须用 HAVING。另一个细节是 HAVING 里可以引用 SELECT 别名, WHERE 里不行, 因为 WHERE 执行时别名还不存在。

```python
# file: code/04_数据库与缓存/q1937_having_where.py
"""HAVING vs WHERE: 过滤时机 聚合语义与代价实测"""
import sqlite3
import time

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE sales(id INTEGER PRIMARY KEY, region TEXT, amount INTEGER)")
conn.executemany("INSERT INTO sales(region, amount) VALUES(?,?)",
                 [("r%d" % (i % 50), i % 100) for i in range(200000)])
conn.execute("CREATE INDEX idx_region ON sales(region)")
conn.commit()

def timed(sql, n=5):
    t0 = time.perf_counter()
    for _ in range(n):
        conn.execute(sql).fetchall()
    return (time.perf_counter() - t0) / n * 1000

q_where = "SELECT region, SUM(amount) FROM sales WHERE amount >= 50 GROUP BY region"
q_having = "SELECT region, SUM(amount) FROM sales GROUP BY region HAVING MIN(amount) >= 50"
print(f"WHERE 先过滤再聚合 : {timed(q_where):7.2f} ms  进入分组的行数 "
      f"{conn.execute('SELECT COUNT(*) FROM sales WHERE amount >= 50').fetchone()[0]}")
print(f"HAVING 聚合后再过滤: {timed(q_having):7.2f} ms  进入分组的是全量 20 万行")

# 只能写在 HAVING 的条件: 引用聚合结果
agg_only = conn.execute(
    "SELECT COUNT(*) FROM (SELECT region FROM sales GROUP BY region HAVING COUNT(*) > 4100)"
).fetchone()[0]
print("聚合条件必须 HAVING -> 超大分组数:", agg_only)

# 行级条件两种写法结果相同 但 WHERE 便宜: 一边先少算一半行
same_w = timed("SELECT COUNT(*) FROM (SELECT region FROM sales WHERE region = 'r1' GROUP BY region)")
same_h = timed("SELECT COUNT(*) FROM (SELECT region FROM sales GROUP BY region HAVING region = 'r1')")
print(f"同语义 WHERE {same_w:.2f} ms vs HAVING {same_h:.2f} ms")
print("结论: 行级条件一律 WHERE 让过滤发生在聚合之前 组级条件才用 HAVING 别把能提前的过滤拖到最后")
```

**追问**:
- HAVING 能引用未聚合的普通列吗?—— 分组后普通列语义上属于组, MySQL 严格模式要求它同时出现在 GROUP BY 里, 否则报错。
- 聚合下推是什么意思?—— 优化器把 HAVING 里的非聚合条件移到 WHERE 提前过滤, MySQL 与 PG 都支持, 但显式写 WHERE 更可靠。

---
