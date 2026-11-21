---
title: [Q2206] 字符串聚合的次序敏感: group_concat 的顺序不是契约
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2206 · 字符串聚合的次序敏感: group_concat 的顺序不是契约

> 难度:★★★☆ | 标签:SQL, 聚合

**问**:group_concat 拼出来的列表,顺序可以依赖吗?要确定顺序该怎么写?

**答**:不能依赖。字符串聚合的输入顺序取决于扫描顺序,而扫描顺序由计划决定——换了索引、换了驱动表,同一行数据会拼出不同的串,这就是"次序敏感"。要确定性,只有三条路:子查询里显式 ORDER BY 后再聚合(SQLite 实践中稳定,但仍是方言行为)、在应用层取行后排序拼接(最可控,代价是多一次传输)、或升级到支持聚合内 ORDER BY 的版本(SQLite 3.44+/PostgreSQL string_agg/MySQL GROUP_CONCAT 的 ORDER BY 子句)。另外注意两个隐藏坑:分隔符是参数不是语法;group_concat_max_len 会静默截断超长结果,长度敏感的场景要检查长度而不是假设完整。

```python
# file: code/04_数据库与缓存/q2206_list_order.py
"""字符串聚合的次序敏感: group_concat 不保证顺序, 需要显式定序"""
import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE logs(id INTEGER PRIMARY KEY, user TEXT, event TEXT)")
c.executemany("INSERT INTO logs VALUES(?,?,?)",
              [(1, "u1", "login"), (2, "u1", "view"), (3, "u2", "login"),
               (4, "u1", "buy"), (5, "u2", "view"), (6, "u1", "logout")])

a = c.execute("SELECT group_concat(event, '->') FROM logs WHERE user='u1'").fetchone()[0]
b = c.execute("SELECT group_concat(event, '->') FROM "
              "(SELECT event FROM logs WHERE user='u1' ORDER BY id DESC)").fetchone()[0]
print("自然扫描顺序:", a)
print("倒序子查询  :", b, " <- 同一份数据两种串")

d1 = c.execute("SELECT group_concat(event, '->') FROM "
               "(SELECT event FROM logs WHERE user='u1' ORDER BY id)").fetchone()[0]
d2 = " -> ".join(r[0] for r in c.execute("SELECT event FROM logs WHERE user='u1' ORDER BY id"))
print("子查询正序  :", d1)
print("应用层聚合  :", d2)

try:
    c.execute("SELECT group_concat(event, '->' ORDER BY id) FROM logs WHERE user='u1'")
    print("聚合内 ORDER BY: 本机支持")
except sqlite3.OperationalError as e:
    print("聚合内 ORDER BY: 本机 SQLite 版本不支持 ->", e)
```

**追问**:
- 超长被截断怎么发现?—— 比对 count 与分隔符出现次数是否差一,或干脆在应用层拼接,把长度控制权拿回来。
- 为什么要先按 id 正序去重再去聚合?—— 聚合不消重,重复行会原样进入列表;去重键也必须在 ORDER BY 里,否则列表内容仍不确定。

---
