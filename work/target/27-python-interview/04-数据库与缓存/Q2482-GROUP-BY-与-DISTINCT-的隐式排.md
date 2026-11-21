---
title: [Q2482] GROUP BY 与 DISTINCT 的隐式排序神话
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2482 · GROUP BY 与 DISTINCT 的隐式排序神话

> 难度:★★☆☆ | 标签:SQL, 排序

**问**:GROUP BY 的结果看起来总是有序的,可以依赖这个顺序吗?

**答**:不可以。"看起来有序"是执行计划的副产品:走索引扫描时按索引序输出,走临时 B 树时按排序结构输出——两种今天都恰好有序,但契约不存在。实测同一查询,把索引从 ASC 重建为 DESC,DISTINCT 与 GROUP BY 的输出顺序整个翻转;删掉索引退回临时结构,顺序又变。老版 MySQL 的 GROUP BY 曾隐式排序,8.0 起官方明确移除该行为。规则:面向人展示、或喂给 INSERT SELECT 的结果,一律显式 ORDER BY;"现在碰巧有序"不是可以省一行代码的理由。

```python
# file: code/04_数据库与缓存/q2482_groupby_order_flip.py
"""GROUP BY 与 DISTINCT 的隐式排序神话: 输出顺序是计划的副产品"""
import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE t (id INTEGER PRIMARY KEY, cat TEXT)")
c.executemany("INSERT INTO t VALUES(?,?)",
              [(i, "cat%d" % (i % 7)) for i in range(1, 20001)])

# 场景一: ASC 索引在手, 优化器走索引扫描, 输出'恰好'有序
c.execute("CREATE INDEX idx_cat_asc ON t(cat)")
plan = [r[3] for r in c.execute("EXPLAIN QUERY PLAN SELECT DISTINCT cat FROM t")]
out = [r[0] for r in c.execute("SELECT DISTINCT cat FROM t")]
print("ASC 索引: %s" % out)
print("  计划: %s" % plan[0])

# 场景二: 同一条查询, 重建一个 DESC 索引, 输出顺序整个翻转
c.execute("DROP INDEX idx_cat_asc")
c.execute("CREATE INDEX idx_cat_desc ON t(cat DESC)")
plan = [r[3] for r in c.execute("EXPLAIN QUERY PLAN SELECT DISTINCT cat FROM t")]
out = [r[0] for r in c.execute("SELECT DISTINCT cat FROM t")]
print("DESC 索引: %s" % out)
print("  计划: %s" % plan[0])
plan = [r[3] for r in c.execute("EXPLAIN QUERY PLAN SELECT cat, COUNT(*) FROM t GROUP BY cat")]
out = [r[0] for r in c.execute("SELECT cat, COUNT(*) FROM t GROUP BY cat")]
print("GROUP BY 同样跟着索引方向走: %s" % out)

# 没有任何契约说它必须有序; 今天靠计划白捡的顺序, 明天一次 ANALYZE 就能收走
c.execute("DROP INDEX idx_cat_desc")
plan = [r[3] for r in c.execute("EXPLAIN QUERY PLAN SELECT DISTINCT cat FROM t")]
out = [r[0] for r in c.execute("SELECT DISTINCT cat FROM t")]
print("无索引回退临时结构: %s | 计划: %s" % (out, plan[0]))
print("结论: 输出顺序取决于优化器选了哪条路, 面向人或喂给 INSERT SELECT 的结果必须显式 ORDER BY")
```

**追问**:
- 子查询里的 ORDER BY 会被保留吗?—— 多数优化器对无 LIMIT 的子查询排序直接忽略,排序契约只属于最外层。
- 为什么"看起来有序"这么稳定?—— 索引扫描与临时 B 树两类计划都恰好产出有序,稳定的是计划不是语义,计划本身会漂移。

---
