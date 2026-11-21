---
title: [Q2213] EXCEPT 与 INTERSECT: 隐式 DISTINCT 的语义边界
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2213 · EXCEPT 与 INTERSECT: 隐式 DISTINCT 的语义边界

> 难度:★★☆☆ | 标签:SQL, 集合运算

**问**:EXCEPT 和 NOT IN、LEFT JOIN IS NULL 是一回事吗?

**答**:不是。EXCEPT/INTERSECT 是集合运算,隐式做 DISTINCT:A EXCEPT B 等于"A 的去重结果减去 B 的去重结果",重复行只保留一份;NOT IN/NOT EXISTS 是逐行谓词,不去重、语义是"每一行是否满足条件"。所以带重复数据的差集必须想清楚口径:要"差几条"就得模拟 EXCEPT ALL(SQLite 不支持,用 GROUP BY 计数相减)。另外老三样陷阱照旧:NOT IN 遇到子查询里的 NULL 会整体落空,EXCEPT 不受 NULL 影响;INTERSECT 与 EXCEPT 的优先级高于 UNION,混写时要加括号。集合运算写集合语义,谓词写行语义,混用最容易在重复数据上翻车。

```python
# file: code/04_数据库与缓存/q2213_except_intersect.py
"""EXCEPT 与 INTERSECT: 隐式 DISTINCT 的语义与 ALL 缺失的替代"""
import sqlite3
from collections import Counter

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE a(x INTEGER)")
c.execute("CREATE TABLE b(x INTEGER)")
c.executemany("INSERT INTO a VALUES(?)", [(1,), (1,), (2,), (2,), (3,)])
c.executemany("INSERT INTO b VALUES(?)", [(2,), (2,)])

def show(label, sql):
    print("%-30s -> %s" % (label, [r[0] for r in c.execute(sql)]))

show("A EXCEPT B", "SELECT x FROM a EXCEPT SELECT x FROM b")
show("A INTERSECT B", "SELECT x FROM a INTERSECT SELECT x FROM b")
show("A UNION B", "SELECT x FROM a UNION SELECT x FROM b")
show("等价改写 去重差集", "SELECT DISTINCT x FROM a "
                        "WHERE x NOT IN (SELECT DISTINCT x FROM b)")

ca = Counter(r[0] for r in c.execute("SELECT x FROM a"))
cb = Counter(r[0] for r in c.execute("SELECT x FROM b"))
print("EXCEPT ALL 语义 按次数相减 ->", sorted((ca - cb).elements()))
print("EXCEPT 自动去重, 要保留重复次数必须按计数手工模拟")
```

**追问**:
- EXCEPT 的性能特征?—— 通常物化两侧去重后做合并,代价接近两次 DISTINCT;数据量大且只要判断存在性时 NOT EXISTS 加索引更便宜。
- 为什么 EXCEPT 不怕 NULL?—— 集合运算把 NULL 当成员做等值比较,而 NOT IN 的三值逻辑会让全表条件落空,这是两者最关键的行为差。

---
