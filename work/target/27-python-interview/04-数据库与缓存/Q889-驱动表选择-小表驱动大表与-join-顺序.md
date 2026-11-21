---
title: [Q889] 驱动表选择: 小表驱动大表与 join 顺序
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q889 · 驱动表选择: 小表驱动大表与 join 顺序

> 难度:★★★☆ | 标签:JOIN, 优化

**问**:为什么说"小表驱动大表"?优化器选错了怎么办?

**答**:NLJ 的总代价近似"驱动表行数 × 被驱动表单次访问代价",驱动表越小,内层访问次数越少,所以用过滤后结果集小的表做驱动。注意"小"指过滤后的行数而非表的物理大小——WHERE 条件先把 1 亿行的表筛到 100 行,它就是"小表"。优化器基于统计信息自己选驱动顺序,失真时可用 STRAIGHT_JOIN(MySQL)或调整 SQL 写法强制;PG 用 join_collapse_limit 与语法顺序影响。SQLite 的查询计划能看到谁在前。另一个要点:被驱动表的连接列必须有索引,否则任何顺序都逃不掉 BNL/hash 全扫。

```python
# file: code/04_数据库与缓存/q889_driving_table.py
"""调整 join 顺序观察 sqlite 计划: 过滤后的表应做驱动"""
import sqlite3

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.execute("CREATE TABLE big (id INTEGER PRIMARY KEY, uid INT, flag INT)")
        conn.execute("CREATE TABLE small (id INTEGER PRIMARY KEY, tag TEXT)")
        conn.executemany("INSERT INTO big (uid, flag) VALUES (?, ?)",
                         [(i % 1000, i % 200) for i in range(50000)])
        conn.executemany("INSERT INTO small (tag) VALUES (?)",
                         [(f"tag{i}",) for i in range(50)])
        conn.execute("CREATE INDEX idx_big_uid ON big (uid)")
        conn.execute("CREATE INDEX idx_big_flag ON big (flag)")

        j1 = ("SELECT s.tag, count(*) FROM big b JOIN small s ON s.id = b.uid "
              "WHERE b.flag = 7 GROUP BY s.tag")
        j2 = ("SELECT s.tag, count(*) FROM small s JOIN big b ON s.id = b.uid "
              "WHERE b.flag = 7 GROUP BY s.tag")
        for label, sql in (("big 驱动", j1), ("small 驱动", j2)):
            print(label, [r[3] for r in
                          conn.execute("EXPLAIN QUERY PLAN " + sql).fetchall()])
        print("两结果一致, 驱动顺序由优化器决定; 统计失真时用 STRAIGHT_JOIN 干预")
```

**追问**:
- STRAIGHT_JOIN 是什么?——MySQL 的 join 修饰符,强制按书写顺序驱动,优化器选错时的急救手段,但要写注释说明原因防止后续误改。
- 驱动表选错最坏会差多少?——内层访问次数从"过滤后几百行"变成"千万行",差几个数量级,所以统计信息与索引一样重要。

---
