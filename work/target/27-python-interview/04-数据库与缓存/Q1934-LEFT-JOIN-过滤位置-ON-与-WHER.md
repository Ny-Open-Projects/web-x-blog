---
title: [Q1934] LEFT JOIN 过滤位置: ON 与 WHERE 的结果差异
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1934 · LEFT JOIN 过滤位置: ON 与 WHERE 的结果差异

> 难度:★★★★ | 标签:SQL, JOIN

**问**:把一个过滤条件从 LEFT JOIN 的 ON 挪到 WHERE, 结果集为什么会变?面试怎么答才完整?

**答**:对 LEFT JOIN, 右表列的过滤条件写在 ON 里发生在匹配阶段, 匹配不上仍保留左表行并把右侧置 NULL, 外连接语义完整;写在 WHERE 里则发生在连接之后, 右表行不存在时该列是 NULL, 条件判 UNKNOWN, 整行被删掉, LEFT JOIN 退化成 INNER JOIN。这是静默的, 不报错, 只丢数据。想找回语义要在 WHERE 里显式放行 IS NULL 行, 但混合状态下的统计口径仍然容易错。反向需求找无匹配的左表行, 正确姿势是过滤放 ON 加 WHERE right.key IS NULL。一句话结论:外连接的右表过滤放 ON, 左表过滤放 WHERE。

```python
# file: code/04_数据库与缓存/q1934_left_join_filter.py
"""LEFT JOIN 过滤位置: ON 保留行 WHERE 退化内连接"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.executescript("""
CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT);
CREATE TABLE orders(id INTEGER PRIMARY KEY, user_id INTEGER, amount INTEGER, status TEXT);
INSERT INTO users VALUES(1,'alice'),(2,'bob'),(3,'carol');
INSERT INTO orders VALUES(101,1,100,'paid'),(102,1,200,'void'),(103,2,300,'paid');
""")

def rows(sql):
    return conn.execute(sql).fetchall()

# 需求: 每个用户都要出现, 只统计 paid 订单
on_filter = rows("""
SELECT u.name, COUNT(o.id) AS cnt, COALESCE(SUM(o.amount), 0) AS total
FROM users u LEFT JOIN orders o ON o.user_id = u.id AND o.status = 'paid'
GROUP BY u.id ORDER BY u.id""")
print("过滤写在 ON   :", on_filter)

where_filter = rows("""
SELECT u.name, COUNT(o.id) AS cnt, COALESCE(SUM(o.amount), 0) AS total
FROM users u LEFT JOIN orders o ON o.user_id = u.id
WHERE o.status = 'paid'
GROUP BY u.id ORDER BY u.id""")
print("过滤写在 WHERE:", where_filter, "(carol 消失: NULL 状态判 UNKNOWN 被删行 退化成内连接)")

# WHERE 里显式放行 NULL 行能找回部分语义, 但有非 paid 订单的用户仍会整行被删
hybrid = rows("""
SELECT u.name, COUNT(o.id) AS cnt
FROM users u LEFT JOIN orders o ON o.user_id = u.id
WHERE o.status = 'paid' OR o.id IS NULL
GROUP BY u.id ORDER BY u.id""")
print("WHERE 放行 NULL:", hybrid, "(carol 回来了, alice 的 void 订单行仍被删 口径已经错)")

# 反向需求: 找没有 paid 订单的用户, 同样要靠 ON 过滤加 IS NULL
isnull = rows("""
SELECT u.name FROM users u
LEFT JOIN orders o ON o.user_id = u.id AND o.status = 'paid'
WHERE o.id IS NULL""")
print("无 paid 订单用户:", [r[0] for r in isnull])
print("结论: 右表过滤放 ON 才保住 LEFT JOIN 语义; 放 WHERE 会静默退化成 INNER JOIN")
```

**追问**:
- 左表的条件放 ON 里会怎样?—— 对 LEFT JOIN 左表条件放 ON 与放 WHERE 等价, 因为左表行无论匹配与否都保留, 优化器也会下推。
- FULL OUTER JOIN 下呢?—— 两侧的过滤放 WHERE 都会破坏外连接语义, 都应写进 ON, MySQL 没有全外连接需用 UNION 模拟。

---
