---
title: [Q1936] GROUP BY 严格模式: ONLY_FULL_GROUP_BY 在拦什么
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1936 · GROUP BY 严格模式: ONLY_FULL_GROUP_BY 在拦什么

> 难度:★★★☆ | 标签:SQL, GROUP BY

**问**:SELECT 里出现不在 GROUP BY 也不在聚合函数里的列, MySQL 为什么会报错, SQLite 却放行?

**答**:这是宽松模式与严格模式的分界。SQLite 等宽松实现允许裸列, 但组内选哪一行是任意的, 结果不可复现, 属于把不确定性交给运气;MySQL 5.7 起默认 ONLY_FULL_GROUP_BY 严格模式, 直接拒绝这种写法, 逼你把语义写清楚:要么该列进 GROUP BY, 要么进聚合。SQLite 有一个贴心的特例:裸列与 min 或 max 同用时, 裸列取自命中极值的那一行, 是少数有确定语义的放行。跨库迁移时严格模式是保护而不是麻烦, 老代码里靠裸列碰运气的结果往往正是隐性 bug。本文件另附一个正则版严格检查器, 可以在代码评审里预检。

```python
# file: code/04_数据库与缓存/q1936_groupby_strict.py
"""GROUP BY 严格模式: ONLY_FULL_GROUP_BY 与裸列的任意性"""
import re
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE scores(id INTEGER PRIMARY KEY, class TEXT, name TEXT, score INTEGER)")
conn.executemany("INSERT INTO scores VALUES(?,?,?,?)", [
    (1, 'A', 'alice', 90), (2, 'A', 'amber', 85), (3, 'B', 'bob', 77), (4, 'B', 'bella', 92)])

# 宽松模式: name 不在 GROUP BY 也不聚合, SQLite 允许但值来自组内任意一行
rows = conn.execute("SELECT class, name, MAX(score) FROM scores GROUP BY class").fetchall()
print("SQLite 宽松模式 ->", rows, "(name 来自组内任意一行 不可依赖)")

# SQLite 特例: 裸列与 min/max 同用时, 裸列取自命中 min/max 的那一行
hi = conn.execute("SELECT class, name, MAX(score) FROM scores GROUP BY class").fetchall()
lo = conn.execute("SELECT class, name, MIN(score) FROM scores GROUP BY class").fetchall()
print("MAX 同用裸列    ->", hi, "(与最高分同行)")
print("MIN 同用裸列    ->", lo, "(与最低分同行)")

# 严格模式等价写法: 裸列进 GROUP BY 或用聚合与子查询明确定义
strict = conn.execute("""
SELECT s.class, s.name, s.score FROM scores s
JOIN (SELECT class, MAX(score) AS m FROM scores GROUP BY class) t
  ON s.class = t.class AND s.score = t.m""").fetchall()
print("严格模式等价写法 ->", strict, "(MySQL ONLY_FULL_GROUP_BY 下必须写清这种语义)")

# 模拟严格模式检查器: 找出 SELECT 里既不在 GROUP BY 也不在聚合里的裸列
def strict_check(sql):
    m = re.search(r"SELECT (.+?) FROM", sql, re.I)
    cols = [c.strip() for c in m.group(1).split(",")]
    g = re.search(r"GROUP BY (.+?)\s*(?:HAVING|$)", sql, re.I)
    allowed = set(c.strip() for c in g.group(1).split(",")) if g else set()
    agg = re.compile(r"(MAX|MIN|SUM|COUNT|AVG)\s*\(", re.I)
    return [c for c in cols if c not in allowed and not agg.search(c)]

print("宽松 SQL 的裸列  ->", strict_check("SELECT class, name, MAX(score) FROM scores GROUP BY class"))
print("严格 SQL 的裸列  ->", strict_check("SELECT class, MAX(score) FROM scores GROUP BY class"))
print("结论: 宽松模式的裸列值不确定 严格模式逼你把语义写进 GROUP BY 或聚合 可移植性更好")
```

**追问**:
- GROUP_CONCAT 这类聚合里裸列的顺序稳定吗?—— 不保证, 未指定 ORDER BY 的聚合串接顺序是实现细节, 需要稳定输出就显式写 ORDER BY。
- 怎么临时关闭严格模式?—— 会话级 SET sql_mode 去掉 ONLY_FULL_GROUP_BY 可以做到, 但建议修 SQL 而不是关检查。

---
