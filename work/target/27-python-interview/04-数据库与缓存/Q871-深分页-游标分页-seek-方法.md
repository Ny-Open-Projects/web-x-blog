---
title: [Q871] 深分页: 游标分页 seek 方法
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q871 · 深分页: 游标分页 seek 方法

> 难度:★★★★ | 标签:分页, 优化

**问**:除了延迟关联,还有什么办法彻底解决深分页?游标分页的原理和局限是什么?

**答**:seek 方法(keyset pagination)不用 OFFSET,而是记住上一页最后一行的排序键,下一页改为 `WHERE (sort_key, id) < (last_key, last_id) ORDER BY sort_key DESC, id DESC LIMIT n`,直接从索引定位起点,扫描行数恒定约等于页大小,与页深无关。复合键比较 `(a, b) < (x, y)` 是行值比较,SQLite 与 MySQL 8 都支持,老版本可展开成 `(a < x) OR (a = x AND b < y)`。局限:只能顺序翻页(或配合记录的游标跳转),不支持随机跳页,前端要改成"下一页"交互或存游标 token。

```python
# file: code/04_数据库与缓存/q871_seek_pagination.py
"""对比 OFFSET 与 seek 两种深分页的耗时, 行数越大 seek 优势越明显"""
import sqlite3
import time

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.execute("CREATE TABLE t (id INTEGER PRIMARY KEY, score INT)")
        conn.executemany("INSERT INTO t (score) VALUES (?)",
                         [(i % 10000,) for i in range(200000)])
        conn.execute("CREATE INDEX idx_score ON t (score, id)")

        t0 = time.perf_counter()
        conn.execute("SELECT * FROM t ORDER BY score DESC, id LIMIT 150000, 20").fetchall()
        t1 = time.perf_counter()

        row = conn.execute(
            "SELECT score, id FROM t ORDER BY score DESC, id LIMIT 1 OFFSET 149999"
        ).fetchone()
        cursor = conn.execute(
            "SELECT * FROM t WHERE (score, id) < (?, ?) "
            "ORDER BY score DESC, id LIMIT 20", (row[0], row[1]))
        seek_rows = cursor.fetchall()
        t2 = time.perf_counter()

        print(f"OFFSET 深分页: {(t1 - t0) * 1000:.1f} ms")
        print(f"seek 游标分页: {(t2 - t1) * 1000:.1f} ms, 取到 {len(seek_rows)} 行")
```

**追问**:
- seek 分页怎么知道有没有下一页?——多取一条(limit n+1),取到 n+1 条说明还有剩余,去掉最后一条返回。
- 用户坚持要跳转到第 1000 页怎么办?——限制最大可跳页数、预计算页首游标,或对跳页请求走延迟关联/搜索引擎方案。

---
