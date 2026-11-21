---
title: [Q1407] 大字段拆分: TEXT/BLOB 出主表的理由与做法
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1407 · 大字段拆分: TEXT/BLOB 出主表的理由与做法

> 难度:★★★☆ | 标签:表设计, 大字段

**问**:详情页、正文这类大字段为什么不放在主表里?

**答**:三个理由:读放大——InnoDB 行超过页大小的约一半时大字段溢出到溢出页,列表查询即使不 SELECT 大列,扫描聚簇索引也可能承担额外 IO;缓存效率——buffer pool 被大字段挤占,热点小行的命中率下降;运维灵活性——大字段表单独归档、单独备份、单独迁移,比拖在主表里轻得多。做法:大字段拆到一对一详情表,主表保留摘要列;访问路径是列表查主表、详情按 id 补查。注意拆分不是免费的:多一次 JOIN/查询、事务边界变大,所以只拆"大且低频访问"的字段,几百字节内的 JSON 留在主表完全合理。

```python
# file: code/04_数据库与缓存/q1407_split_lob.py
"""大字段拆分: 主表瘦身前后的大小与页数对比"""
import os
import sqlite3

DETAIL = "x" * 8000

def build(with_detail):
    path = "/tmp/q1407_%s.db" % ("with" if with_detail else "split")
    if os.path.exists(path):
        os.remove(path)
    conn = sqlite3.connect(path)
    if with_detail:
        conn.execute("CREATE TABLE t(id INTEGER PRIMARY KEY, title TEXT, detail TEXT)")
        conn.executemany("INSERT INTO t VALUES(?,?,?)",
                         [(i, "t%d" % i, DETAIL) for i in range(300)])
    else:
        conn.execute("CREATE TABLE t(id INTEGER PRIMARY KEY, title TEXT)")
        conn.execute("CREATE TABLE t_detail(id INTEGER PRIMARY KEY, detail TEXT)")
        conn.executemany("INSERT INTO t VALUES(?,?)", [(i, "t%d" % i) for i in range(300)])
        conn.executemany("INSERT INTO t_detail VALUES(?,?)",
                         [(i, DETAIL) for i in range(300)])
    conn.commit()
    pages = conn.execute("PRAGMA page_count").fetchone()[0]
    conn.close()
    return os.path.getsize(path), pages

s1, p1 = build(True)
s2, p2 = build(False)
print(f"合并存储: {s1} 字节 {p1} 页; 拆分后主表库: {s2} 字节 {p2} 页")
print("列表查询只触主表, 读放大显著下降; 详情按需查 t_detail")
```

**追问**:
- MySQL 的 TEXT 溢出页机制是什么?——行内只留 20 字节指针,内容放溢出页,SELECT 不带该列时可以不读,但扫表与备份的代价仍在,这也是拆表的底层依据。
- 拆表后详情查询会不会反而变慢?——列表路径因主表页密度上升而变快,详情多一次主键点查,通常毫秒级;取舍点是高频列表与低频详情的读放大差。
- 溢出的判定阈值是什么?——InnoDB 要求行至少放进页的一半,超出时最长列先溢出,DYNAMIC 行格式行内只留 20 字节指针,这是默认行为。
- 生产陷阱?——表拆了,查询却仍 SELECT * 把大列拉回来,等于白拆;ORM 默认全列查询必须改成显式投影,列表接口限定列清单。

---
