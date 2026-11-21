---
title: [Q2201] 排序规则对索引的影响: COLLATE 不匹配就弃用索引
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2201 · 排序规则对索引的影响: COLLATE 不匹配就弃用索引

> 难度:★★★☆ | 标签:SQL, 索引, COLLATE

**问**:列上声明了 COLLATE NOCASE,查询时比较规则不一致会发生什么?为什么有时候加了索引还是全表扫描?

**答**:索引的键是按列上声明的排序规则排好序的,等值查找能不能走 seek,取决于"本次比较使用的排序规则"与"索引键的排序规则"是否一致。SQLite 里比较规则按"左操作数显式声明优先,其次列的隐式声明"确定,所以在 NOCASE 列上用 COLLATE BINARY 比较,等于在按大小写排好序的索引里做二进制匹配,有序性作废,优化器只能全表扫描。反过来,在默认 BINARY 列上套 NOCASE 比较也一样失效。这不仅是性能问题,还是语义问题:NOCASE 列上 WHERE name='bob' 会同时命中 BOB 与 bob 两行。工程结论是:排序规则属于 Schema 契约,建索引、写查询、跨库迁移三处必须对齐。

```python
# file: code/04_数据库与缓存/q2201_collation_index.py
"""排序规则对索引的影响: 比较排序规则与索引排序规则不一致时无法 seek"""
import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE users_bin (name TEXT NOT NULL)")            # 默认 BINARY
c.execute("CREATE TABLE users_ci  (name TEXT COLLATE NOCASE NOT NULL)")
rows = [("Alice",), ("BOB",), ("bob",), ("Carol",)]
c.executemany("INSERT INTO users_bin VALUES(?)", rows)
c.executemany("INSERT INTO users_ci  VALUES(?)", rows)
c.execute("CREATE INDEX idx_bin ON users_bin(name)")
c.execute("CREATE INDEX idx_ci  ON users_ci(name)")

cases = [
    ("BINARY 列  name = 'BOB'",                "users_bin", "'BOB'"),
    ("NOCASE 列  name = 'BOB'",                "users_ci", "'BOB'"),
    ("NOCASE 列  加 COLLATE NOCASE 比较",       "users_ci", "'BOB' COLLATE NOCASE"),
    ("NOCASE 列  加 COLLATE BINARY 比较",       "users_ci", "'BOB' COLLATE BINARY"),
    ("BINARY 列  加 COLLATE NOCASE 比较",       "users_bin", "'BOB' COLLATE NOCASE"),
]
for label, table, rhs in cases:
    plan = c.execute("EXPLAIN QUERY PLAN SELECT * FROM %s WHERE name = %s" % (table, rhs)).fetchone()[3]
    print("%-28s -> %s" % (label, "用索引 " + plan if plan.startswith("SEARCH") else "全表扫描"))

print("NOCASE 列 WHERE name='bob' 命中:",
      [r[0] for r in c.execute("SELECT name FROM users_ci WHERE name='bob'")])
print("BINARY 列 套 NOCASE 比较命中:",
      [r[0] for r in c.execute("SELECT name FROM users_bin WHERE name='BOB' COLLATE NOCASE")])
print("结论: 索引键按列的 COLLATE 排序, 查询比较规则必须与之一致, 否则优化器放弃 seek")
```

**追问**:
- 建索引时能改排序规则吗?—— 可以,CREATE INDEX ... ON t(col COLLATE NOCASE) 让索引键用 NOCASE 排序,查询套同样的 COLLATE 即可命中,但一张表上不同排序规则的索引要各建各的。
- 跨库迁移最常踩的坑是什么?—— MySQL 的 utf8mb4_general_ci 与 utf8mb4_0900_ai_ci 排序结果不同,JOIN 两列排序规则不一致时不仅弃用索引,还可能直接报 illegal mix of collations。

---
