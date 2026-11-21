---
title: [Q1947] rowid 与 AUTOINCREMENT: ID 复用行为
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1947 · rowid 与 AUTOINCREMENT: ID 复用行为

> 难度:★★★☆ | 标签:主键, SQLite

**问**:删掉最大 id 的行再插入, 新行会复用这个 id 吗?AUTOINCREMENT 到底保证什么?

**答**:SQLite 的普通表每行都有隐式 rowid, 新行默认取 max rowid 加一, 但一旦最大行被删掉, 这个值会被新行复用, 本文件实测删尾再插确实复用了 3。INTEGER PRIMARY KEY 就是 rowid 的别名, 行为相同。AUTOINCREMENT 用 sqlite_sequence 表记录历史最大值, 保证新 id 严格单调不复用, 实测清空表后再插入返回 4 而不是 1。这个保证不是免费的:每次插入要维护 sequence 表, 略有开销。选型建议:内部代理键无所谓复用;ID 会暴露给外部、进审计日志或与外部系统对账时, 复用会引发张冠李戴, 值得上 AUTOINCREMENT 或干脆用应用层发号。

```python
# file: code/04_数据库与缓存/q1947_rowid_autoincrement.py
"""rowid 与 AUTOINCREMENT: 隐式主键与 ID 复用行为"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE t(name TEXT)")                                  # 隐式 rowid
conn.execute("CREATE TABLE a(id INTEGER PRIMARY KEY, name TEXT)")          # id 是 rowid 别名
conn.execute("CREATE TABLE s(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")
conn.executemany("INSERT INTO t(name) VALUES(?)", ["x"] * 3)
conn.executemany("INSERT INTO a(name) VALUES(?)", ["x"] * 3)
conn.executemany("INSERT INTO s(name) VALUES(?)", ["x"] * 3)

print("t 的 rowid       ->", [r[0] for r in conn.execute("SELECT rowid FROM t")])
print("a 的 id 与 rowid ->", conn.execute("SELECT id, rowid FROM a").fetchall(),
      " INTEGER PRIMARY KEY 就是 rowid 的别名")

# 删掉最大 rowid 的行后, 新行会复用这个 id
conn.execute("DELETE FROM t WHERE rowid = 3")
conn.execute("INSERT INTO t(name) VALUES('new')")
print("普通表删尾再插   ->", [r[0] for r in conn.execute("SELECT rowid FROM t")], "(3 被复用)")

# AUTOINCREMENT 由 sqlite_sequence 记录历史最大值 保证永不复用
conn.execute("DELETE FROM s")
conn.execute("INSERT INTO s(name) VALUES('new')")
print("AUTOINCREMENT 清空再插 ->", [r[0] for r in conn.execute("SELECT id FROM s")], " 单调不复用")
print("sqlite_sequence  ->", conn.execute("SELECT * FROM sqlite_sequence").fetchall())
print("结论: 默认 rowid 是实现细节且会被复用, 对外暴露 ID 或有审计续号需求时才值得上 AUTOINCREMENT")
```

**追问**:
- rowid 复用会破坏外键引用吗?—— 被删行的引用本来就不该存在, 风险在导出数据与日志里旧 id 与新行混淆, 属于审计问题而非引用完整性问题。
- 为什么 InnoDB 自增也有类似问题?—— 回滚与重启后自增值可能回退复用, 原理相同, 暴露型 ID 一律不要依赖不复用语义。

---
