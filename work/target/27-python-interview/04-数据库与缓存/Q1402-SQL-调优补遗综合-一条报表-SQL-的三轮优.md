---
title: [Q1402] SQL 调优补遗综合: 一条报表 SQL 的三轮优化
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1402 · SQL 调优补遗综合: 一条报表 SQL 的三轮优化

> 难度:★★★★ | 标签:SQL 调优, 综合案例

**问**:一条按城市汇总月度订单金额的报表 SQL,你怎么一步步把它调快?

**答**:三轮递进:第一轮消灭函数包列——WHERE substr(created,1,7)='2024-06' 让索引彻底失效,改写成范围条件 created >= '2024-06-01' AND < '2024-07-01',这一步立竿见影;第二轮补 created 索引让过滤走范围扫描;第三轮改写连接顺序——先在订单侧按 user_id 聚合,聚合结果(几万行)再 JOIN 用户表拿城市,驱动侧从 20 万明细缩到聚合中间表,最后在城市层二次聚合。方法论:先让过滤有索引可走,再缩小参与 JOIN 的行数,最后才考虑参数与硬件;每一步用 EXPLAIN 验证证据,用结果一致性校验保证改写语义不变。

```python
# file: code/04_数据库与缓存/q1402_report_tuning.py
"""报表 SQL 的三轮优化: 函数包列 -> 范围条件 -> 提前聚合"""
import random
import sqlite3
import time

random.seed(2)
conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, city TEXT)")
conn.execute(
    "CREATE TABLE orders(id INTEGER PRIMARY KEY, user_id INTEGER, amount REAL, created TEXT)")
conn.executemany("INSERT INTO users VALUES(?,?)",
                 [(i, "city%d" % (i % 30)) for i in range(1, 50001)])
conn.executemany("INSERT INTO orders VALUES(?,?,?,?)",
                 [(i, random.randrange(1, 50001), round(random.uniform(10, 500), 2),
                   "2024-06-%02d" % random.randrange(1, 29)) for i in range(1, 200001)])

def timed(sql):
    t0 = time.perf_counter()
    rows = conn.execute(sql).fetchall()
    return rows, (time.perf_counter() - t0) * 1000

v0, ms0 = timed(
    "SELECT u.city, SUM(o.amount) FROM orders o JOIN users u ON o.user_id = u.id "
    "WHERE substr(o.created, 1, 7) = '2024-06' GROUP BY u.city")
conn.execute("CREATE INDEX idx_created ON orders(created)")
v1, ms1 = timed(
    "SELECT u.city, SUM(o.amount) FROM orders o JOIN users u ON o.user_id = u.id "
    "WHERE o.created >= '2024-06-01' AND o.created < '2024-07-01' GROUP BY u.city")
v2, ms2 = timed(
    "SELECT u.city, SUM(t.total) FROM (SELECT user_id, SUM(amount) total FROM orders "
    "WHERE created >= '2024-06-01' AND created < '2024-07-01' GROUP BY user_id) t "
    "JOIN users u ON u.id = t.user_id GROUP BY u.city")
same = abs(sum(r[1] for r in v0) - sum(r[1] for r in v2)) < 0.01
print(f"v0 函数包列: {ms0:.1f} ms")
print(f"v1 范围条件+索引: {ms1:.1f} ms")
print(f"v2 先聚合再 join: {ms2:.1f} ms, 金额一致: {same}")
```

**追问**:
- 为什么不直接把城市冗余进订单表?——可以,城市属于用户属性、变更少时冗余是合理反范式,但要写清失效路径,属于第三轮之后的进阶选项。
- 函数包列为什么必须第一个改?——列上套函数后索引的有序性和范围定位全部失效,只能全扫;等价改写成范围条件零风险高收益,是调优的固定起手式。
- 先聚合再 JOIN 快的机制?——聚合把几十万明细压成键数级中间表,驱动侧基数骤降,JOIN 与二次聚合都在小结果集上做;本质是尽早削减参与连接的行数。
- 生产陷阱?——改写后只对总金额对账,分组数与城市集合没核,语义偏差悄悄溜过;改写类优化必须行数、分组数、汇总值三项对账。

---

```mermaid
graph LR
    A[v0 函数包列 全表扫描] -->|改写为范围条件| B[v1 created 索引范围扫描]
    B -->|明细行数仍大 回表多| C[v2 先聚合 降驱动行数]
    C --> D[聚合结果再 join 用户表]
    D --> E[耗时逐级下降 且金额可校验]
```
