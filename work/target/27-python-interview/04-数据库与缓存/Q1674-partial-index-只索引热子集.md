---
title: [Q1674] partial index: 只索引热子集
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1674 · partial index: 只索引热子集

> 难度:★★★☆ | 标签:SQL 调优, 索引

**问**:98% 的行都是 done 状态,任务表只有 pending 值得建索引吗?

**答**:这正是部分索引的用武之地:CREATE INDEX ... WHERE status='pending',只把满足谓词的行纳入索引,体积与维护成本按选择度等比例缩小。本机实测 5 万行的任务表,全量索引 5 万条目,部分索引只有 1000 条,查询 pending 直接命中且顺带覆盖了 priority 列。使用条件苛刻而明确:查询的 WHERE 必须蕴含建索引的谓词,优化器才会选用它;MySQL 至今不支持部分索引,近似方案是生成列加联合索引,PG 与 SQLite 原生支持。它同时是软删除唯一约束的经典解法,见后面 Q1679。

```python
# file: code/04_数据库与缓存/q1674_partial_index.py
"""partial index: 部分索引的概念与 sqlite 演示"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE jobs(id INTEGER PRIMARY KEY, status TEXT, priority INTEGER)")
conn.executemany("INSERT INTO jobs VALUES(?,?,?)",
                 [(i, "done" if i % 50 else "pending", i % 7) for i in range(1, 50001)])
conn.commit()
# 普通索引覆盖全部 5 万行, 其中 98% 是 done
conn.execute("CREATE INDEX idx_full ON jobs(status)")
# 部分索引只索引 pending 子集
conn.execute("CREATE INDEX idx_pending ON jobs(status, priority) WHERE status='pending'")
conn.commit()

def plan(sql):
    return [r[3] for r in conn.execute("EXPLAIN QUERY PLAN " + sql)]

print("查询 pending 的计划:", plan("SELECT * FROM jobs WHERE status='pending'"))
print("查询 done 的计划:   ", plan("SELECT * FROM jobs WHERE status='done'"))
print("普通索引行数:", conn.execute("SELECT COUNT(*) FROM jobs INDEXED BY idx_full").fetchone()[0])
print("部分索引行数:", conn.execute(
    "SELECT COUNT(*) FROM jobs INDEXED BY idx_pending WHERE status='pending'").fetchone()[0])
print("要点: 部分索引把热子集建成小而准的索引, 体积与维护成本按选择度比例缩小;")
print("      查询条件必须蕴含建索引的谓词, 优化器才会选用它")
```

**追问**:
- 部分索引的谓词能引用别的表或函数吗?——只能是本行的确定性表达式,不能用子查询与非确定性函数,这是它能高效维护的前提。
- 谓词写成 status <> 'done' 可以吗?——语义等价时优化器一般能匹配,但写成与查询完全一致的形式最稳,方言差异要实测。

---
