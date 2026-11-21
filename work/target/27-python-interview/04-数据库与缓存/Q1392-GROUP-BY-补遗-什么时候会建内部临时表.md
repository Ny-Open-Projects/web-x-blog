---
title: [Q1392] GROUP BY 补遗: 什么时候会建内部临时表
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1392 · GROUP BY 补遗: 什么时候会建内部临时表

> 难度:★★★☆ | 标签:SQL 调优, GROUP BY

**问**:GROUP BY 的性能分水岭在哪?怎么让它不走临时表?

**答**:GROUP BY 有两条执行路径:一是"索引序分组"——分组列与某索引前缀对齐,扫描即按序聚合,无额外结构;二是"临时表分组"——先建内部临时表,逐行 upsert 计数,聚合完再可能对结果排序。分水岭就是"分组列能否吃到现成索引的有序性"。另外 count(distinct 多列)、union、派生表物化也都会触发临时表。定位方法看 EXPLAIN 的 Using temporary;优化思路是给分组列补索引,或用冗余列/生成列把分组键做成联合索引前缀。

```python
# file: code/04_数据库与缓存/q1392_groupby_temp.py
"""GROUP BY 的临时表代价: 索引序分组 vs 内部临时表"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE events(id INTEGER PRIMARY KEY, user_id INTEGER, kind TEXT)")
conn.execute("CREATE INDEX idx_user_kind ON events(user_id, kind)")
conn.executemany("INSERT INTO events VALUES(?,?,?)",
                 [(i, i % 500, "k%d" % (i % 4)) for i in range(5000)])

def plan(sql):
    print("SQL:", sql)
    for r in conn.execute("EXPLAIN QUERY PLAN " + sql):
        print("   ", r[3])

plan("SELECT user_id, COUNT(*) FROM events GROUP BY user_id")
plan("SELECT kind, COUNT(*) FROM events GROUP BY kind")
plan("SELECT user_id, kind, COUNT(*) FROM events GROUP BY user_id, kind")
print("结论: 分组列与索引前缀对齐则免临时表, 否则建内部临时表再聚合")
```

**追问**:
- GROUP BY user_id ORDER BY NULL 有意义吗?——老版本 MySQL 可以省去隐式排序,8.0 的 GROUP BY 本身不再保证排序,写 ORDER BY 才有意义。
- 临时表放内存还是磁盘由什么决定?——超过 tmp_table_size / max_heap_table_size 或含 TEXT/BLOB 就落盘,落盘后引擎从 MEMORY 变 TempTable/InnoDB,慢一个量级。

---
