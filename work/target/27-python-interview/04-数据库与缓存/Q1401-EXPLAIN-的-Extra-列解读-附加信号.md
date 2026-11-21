---
title: [Q1401] EXPLAIN 的 Extra 列解读: 附加信号全谱
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1401 · EXPLAIN 的 Extra 列解读: 附加信号全谱

> 难度:★★★☆ | 标签:EXPLAIN, 调优

**问**:Extra 列里 Using index、Using where、Using filesort、Using temporary 分别代表什么?哪些是好信号?

**答**:Using index 是好信号——覆盖索引生效,查询不回表;Using index condition 表示 ICP 下推,过滤提前到引擎层,也算正面。Using where 是中性的,表示服务层还有过滤,不一定是坏事。Using filesort 表示排序无法走索引序,要额外排序步骤;Using temporary 表示要建内部临时表(常见于 GROUP BY 不对齐索引、DISTINCT、派生表物化)。后两者出现时先问"能不能用索引消掉":把排序/分组键纳入联合索引,或用覆盖索引减少物化体积。解读 Extra 的心法是把它当成"额外工作清单",清单越长代价越大,而不是单看 type 列的访问类型。

```python
# file: code/04_数据库与缓存/q1401_explain_extra.py
"""执行计划附加信号: sqlite EQP 输出与 MySQL Extra 列对照"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE t(id INTEGER PRIMARY KEY, a INTEGER, b TEXT)")
conn.execute("CREATE INDEX idx_a ON t(a)")
conn.executemany("INSERT INTO t VALUES(?,?,?)",
                 [(i, i % 50, "x" * 20) for i in range(5000)])

def show(sql, mysql_extra):
    print("SQL:", sql)
    for r in conn.execute("EXPLAIN QUERY PLAN " + sql):
        print("   sqlite:", r[3])
    print("   MySQL Extra 大致对应:", mysql_extra)
    print()

show("SELECT * FROM t WHERE a = 7", "Using index condition(可下推过滤)")
show("SELECT COUNT(*) FROM t WHERE a = 7", "Using index(覆盖索引 不回表)")
show("SELECT a, b FROM t WHERE b = 'x'", "Using where(无索引可用)")
show("SELECT DISTINCT a FROM t ORDER BY a DESC", "Using temporary + Using filesort 或索引免排序")
```

**追问**:
- Backward index scan 出现在 Extra 里说明什么?——8.0 能倒序扫索引满足 ORDER BY col DESC,这是免 filesort 的新能力,5.7 只能正扫。
- Using index condition(ICP)省的是什么?——把能用的索引列条件下推到存储引擎,先在索引上过滤再回表,减少回表次数,联合索引的后缀列过滤收益最大。
- Using temporary 与 Using filesort 谁先谁后?——先物化再排序,两者常成对出现;Extra 的排列不代表执行顺序,要结合 type/key/rows 一起读。
- 生产陷阱?——只盯 type=ALL 下结论,漏掉 type=ref 却带着 temporary+filesort 的隐形大户;把 Extra 列固定纳入慢 SQL 审计字段。

---
