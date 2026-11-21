---
title: [Q887] ORDER BY 与 filesort: 排序从哪来
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q887 · ORDER BY 与 filesort: 排序从哪来

> 难度:★★★★ | 标签:排序, 优化

**问**:什么是 filesort?为什么建了索引还排序?LIMIT 对排序有什么影响?

**答**:filesort 不是"写文件",而是 MySQL 中"索引顺序给不出结果顺序"时在 sort_buffer 里做排序的代称,内存不够还会落盘临时文件、多路归并。消除办法是让排序键落在索引里:`ORDER BY a, b` 需要 (a, b) 或带等值前缀 (c, a, b) 的索引;方向不一致(ASC/DESC 混排)在 8.0 前需要倒序索引,8.0 支持降序索引。LIMIT 的影响:只取 TopN 时优化器用优先队列,内存开销受控,但深 LIMIT 与大偏移仍是老问题。SQLite 里排序显示为 `USE TEMP B-TREE FOR ORDER BY`,加对齐索引后消失。

```python
# file: code/04_数据库与缓存/q887_orderby_filesort.py
"""对比 ORDER BY 是否命中索引: TEMP B-TREE 出现与消失"""
import sqlite3

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.execute("CREATE TABLE t (id INTEGER PRIMARY KEY, a INT, b INT)")
        conn.executemany("INSERT INTO t (a, b) VALUES (?, ?)",
                         [(i % 50, i % 7) for i in range(20000)])

        q1 = "SELECT * FROM t ORDER BY a, b"
        q2 = "SELECT * FROM t WHERE a = 3 ORDER BY b"

        conn.execute("CREATE INDEX idx_ab ON t (a, b)")
        for q in (q1, q2):
            print(q, "->", [r[3] for r in
                  conn.execute("EXPLAIN QUERY PLAN " + q).fetchall()])

        conn.execute("DROP INDEX idx_ab")
        conn.execute("CREATE INDEX idx_a ON t (a)")
        print("仅 a 索引时:", [r[3] for r in
              conn.execute("EXPLAIN QUERY PLAN " + q2).fetchall()])
```

**追问**:
- ORDER BY 列在索引里但方向相反会走索引吗?——MySQL 8.0 支持降序索引可完全消除排序;8.0 前只能整体反向扫描,混合方向仍需排序。
- sort_buffer 调多大合适?——按典型结果集宽度估,过大会挤占连接内存,几十万级排序结果应先在索引或业务层收敛。

---
