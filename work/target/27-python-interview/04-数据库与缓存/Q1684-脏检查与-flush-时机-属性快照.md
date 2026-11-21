---
title: [Q1684] 脏检查与 flush 时机: 属性快照
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1684 · 脏检查与 flush 时机: 属性快照

> 难度:★★★★ | 标签:ORM, Session

**问**:ORM 怎么知道哪些属性改过?为什么 UPDATE 语句里只有两列?

**答**:Session 在对象载入时保存一份属性快照,flush 前逐对象对比当前值与快照,差集就是脏属性,UPDATE 只写这些列——这就是"只更新 age 和 city,不碰 name"的原理。触发时机:flush 由 commit、查询前的 autoflush 或手动 flush 触发;flush 后快照刷新为当前值,再次 flush 零 SQL。理解这套机制能解释很多现象:绕过 ORM 直接 UPDATE 数据库不会更新任何对象的快照;expire 后属性标记失效,下次访问重发 SELECT 重建快照。性能上,上千个对象逐个脏检查不划算,批量修改应直接发批量 UPDATE。

```python
# file: code/04_数据库与缓存/q1684_dirty_check.py
"""脏检查与 flush 时机: 属性快照如何只发变更列"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT, age INTEGER, city TEXT)")
conn.execute("INSERT INTO users VALUES(1, 'alice', 30, 'hz')")
conn.commit()

COLS = ("id", "name", "age", "city")

class Tracked:
    def __init__(self, row):
        self.current = dict(zip(COLS, row))
        self.snapshot = dict(self.current)       # 载入时的属性快照

obj = Tracked(conn.execute(
    "SELECT id, name, age, city FROM users WHERE id=1").fetchone())

def flush(tracked, conn):
    changed = {k: v for k, v in tracked.current.items()
               if k != "id" and tracked.snapshot.get(k) != v}
    if not changed:
        print("flush: 无脏属性, 不发 SQL")
        return
    sets = ", ".join(f"{k} = ?" for k in changed)
    sql = f"UPDATE users SET {sets} WHERE id = ?"
    print("flush 发出:", sql, "参数:", list(changed.values()) + [tracked.current["id"]])
    conn.execute(sql, list(changed.values()) + [tracked.current["id"]])
    conn.commit()
    tracked.snapshot = dict(tracked.current)

obj.current["age"] = 31
obj.current["city"] = "sh"
flush(obj, conn)          # 只更新 age 与 city 两列, name 未变不进 UPDATE
flush(obj, conn)          # 快照已刷新, 二次 flush 零 SQL
print("要点: 快照在查询时建立; commit 前触发 flush; expire 后下次访问重发 SELECT 重建快照;")
print("      大批量修改绕过逐对象脏检查, 用批量 UPDATE 语句更划算")
```

**追问**:
- 为什么 commit 后再改属性不重算快照就检测不出来?——恰恰相反,commit 默认 expire 全部属性,访问时会重读;若配置 expire_on_commit=False,快照保留,改动仍会被下次 flush 捕获。
- Mutable 类型怎么被脏检查发现?——dict/list 就地修改不触发属性 set 事件,必须用 MutableList/MutableDict 包装或 JSON 序列化对比。

---
