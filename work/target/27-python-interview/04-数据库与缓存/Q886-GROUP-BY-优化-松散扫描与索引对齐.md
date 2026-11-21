---
title: [Q886] GROUP BY 优化: 松散扫描与索引对齐
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q886 · GROUP BY 优化: 松散扫描与索引对齐

> 难度:★★★★ | 标签:聚合, 优化

**问**:GROUP BY 为什么会慢?什么样的索引能让它免排序直接分组?

**答**:GROUP BY 常见成本是"先排序再分组"或临时表:数据无序时要把全量行按分组键排序(或建哈希临时表)才能吐出每组。若索引顺序恰好与分组键一致(MySQL 的 loose index scan / tight index scan),可以沿着索引顺序跳读,每组直接从第一个成员开始,免排序免临时表。SQLite 同理:对 (g) 建索引后 `GROUP BY g` 计划变为按索引扫描。优化要点:分组键尽量与索引前缀对齐;WHERE 先行减少进入分组的行;避免对聚合结果再叠一层多余排序。

```python
# file: code/04_数据库与缓存/q886_group_by_index.py
"""对比无索引与有索引时 GROUP BY 的执行计划"""
import sqlite3

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.execute("CREATE TABLE t (id INTEGER PRIMARY KEY, g INT, v REAL)")
        conn.executemany("INSERT INTO t (g, v) VALUES (?, ?)",
                         [(i % 100, i * 1.0) for i in range(50000)])
        sql = "SELECT g, SUM(v) FROM t GROUP BY g"

        print("无索引:", [r[3] for r in
              conn.execute("EXPLAIN QUERY PLAN " + sql).fetchall()])
        conn.execute("CREATE INDEX idx_g ON t (g)")
        print("有索引:", [r[3] for r in
              conn.execute("EXPLAIN QUERY PLAN " + sql).fetchall()])
        print("MySQL 对照: Extra 出现 Using index for group-by 即松散扫描")
```

**追问**:
- loose 与 tight index scan 区别?——松散扫描每组只探首尾几行(适合 MIN/MAX 类);紧扫描仍需遍历组内行但顺序已就绪,无排序成本。
- 分组列不能全部进索引前缀怎么办?——退而求其次保证前缀对齐,剩余列在已分组的行上小规模处理,或改写为两次聚合。

---
