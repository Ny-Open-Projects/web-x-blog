---
title: [Q1391] 排序补遗: ORDER BY + LIMIT 的 top-N 优先队列
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1391 · 排序补遗: ORDER BY + LIMIT 的 top-N 优先队列

> 难度:★★★☆ | 标签:SQL 调优, 排序

**问**:ORDER BY 加 LIMIT 一定比全量排序快吗?优化器在这里做了什么?

**答**:当 LIMIT k 较小时,MySQL 8 的 filesort 会从"全量快排"切换为"优先队列"模式:维护一个容量 k 的小顶堆流式扫表,每个元素只与堆顶比较,排序缓冲从"装下全部 n 行"降到"只装 k 行"。代价从 n·log(n) 次比较降到约 n·log(k) 次,内存峰值也线性下降,这是深翻页与 TopN 报表快的本质。但要注意:排序键没索引时仍要扫全表;LIMIT 很大(接近全表)时优先队列反而不如直接排序。根治办法是把排序键纳入索引,让 ORDER BY 走索引序,连排序都不用做。

```python
# file: code/04_数据库与缓存/q1391_order_limit_topn.py
"""ORDER BY 走索引与 top-N 优先队列: sqlite EXPLAIN QUERY PLAN 验证"""
import math
import random
import sqlite3

random.seed(7)
conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE orders(id INTEGER PRIMARY KEY, amount REAL)")
rows = [(i, round(random.uniform(1, 10000), 2)) for i in range(1, 100001)]
conn.executemany("INSERT INTO orders VALUES(?,?)", rows)

def plan(sql):
    return [r[3] for r in conn.execute("EXPLAIN QUERY PLAN " + sql)]

sql = "SELECT id, amount FROM orders ORDER BY amount DESC LIMIT 10"
print("无索引:", plan(sql))
conn.execute("CREATE INDEX idx_amount ON orders(amount)")
print("加 amount 索引:", plan(sql))

n, k = 100000, 10
print(f"无索引全排序约 {n * math.log2(n):.0f} 次比较")
print(f"top-N 优先队列约 {n * math.log2(k):.0f} 次比较, 排序缓冲只留 k 行")
```

**追问**:
- 什么情况下 LIMIT 大了反而更慢?——k 接近 n 时堆的反复替换成本超过一次性排序,优化器会自动改回普通 filesort,不必人工干预。
- sort_buffer_size 调大一定有用吗?——只对装不下的超大排序有帮助,盲目调大是全局变量会放大内存风险,先看是不是缺索引。

---
