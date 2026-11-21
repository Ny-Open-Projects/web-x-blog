---
title: [Q1431] NULL 语义: NULL 与空串的混用治理
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1431 · NULL 语义: NULL 与空串的混用治理

> 难度:★☆☆☆ | 标签:数据质量, NULL

**问**:为什么 phone 字段里 NULL 和 '' 要严格区分?统计口径会出什么问题?

**答**:NULL 是"值未知",'' 是"已知为空",两者语义不同但应用常混写:有的接口用 NULL 表未填、有的用空串,结果 count(distinct)、WHERE phone != '138' 的行为都不符合直觉——特别是 phone = NULL 永远返回 false,判空必须 IS NULL 或 COALESCE。混用的直接后果:统计"已填手机号"的用户数时口径漂移;唯一索引上 '' 与 NULL 的约束行为不同(多数数据库允许多个 NULL 但只允许一个 '');报表侧 GROUP BY 会多出组。治理:先定规范——同一列只用一种"空"表示(常用 NULL 表未填),再写检测规则统计混用比例,然后 COALESCE 归一,最后在应用层入库前统一转换。这是数据质量里成本最低但收益最稳的一项。

```python
# file: code/04_数据库与缓存/q1431_null_semantics.py
"""NULL 与空串: 语义混用的检测与归一"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, phone TEXT)")
conn.executemany("INSERT INTO users VALUES(?,?)",
                 [(1, '138'), (2, ''), (3, None), (4, '139')])
print("NULL 计数:", conn.execute("SELECT COUNT(*) FROM users WHERE phone IS NULL").fetchone()[0],
      "空串计数:", conn.execute("SELECT COUNT(*) FROM users WHERE phone=''").fetchone()[0])
print("phone = NULL 永远不成立: 判空必须 IS NULL 或 COALESCE")
conn.execute("UPDATE users SET phone=NULL WHERE phone=''")   # 归一: 空串视同未填
print("归一后 NULL:", conn.execute("SELECT COUNT(*) FROM users WHERE phone IS NULL").fetchone()[0])
```

**追问**:
- 唯一索引下 NULL 和空串的行为差异是什么?——多数数据库允许多行同为 NULL(NULL 互不相等),但空串是具体值只允许一行,unique(phone) 挡不住两个 NULL 却挡得住第二个 ''。
- phone != '138' 为什么查不出 NULL 行?——NULL 与任何值比较都是 UNKNOWN,WHERE 只保留 TRUE 行;三值逻辑是这类"漏统计"的共同根。
- 三种 count 差在哪?——count(*) 数行数,count(phone) 与 count(distinct phone) 跳过 NULL;口径漂移多半是计数函数选错,不是数据真错。
- 生产陷阱?——多客户端对"未填"各写各的,规范只在文档里;入库边界统一转换(未填=NULL),混用比例做成巡检规则进 Q1429 框架。

---
