---
title: [Q2210] 乐观并发与 rowcount: 冲突信号藏在影响行数里
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2210 · 乐观并发与 rowcount: 冲突信号藏在影响行数里

> 难度:★★★☆ | 标签:SQL, 并发控制

**问**:为什么乐观锁必须看 UPDATE 的 rowcount,而不是先 SELECT 再判断?

**答**:乐观锁的判定期望值写在 WHERE 里(AND version=?),数据库原子地完成"比较并更新",rowcount 为 0 就说明版本已被别人改走,更新被安全拒绝;而"先 SELECT 再 UPDATE 无条件写"两个动作之间存在窗口,是典型的丢失更新。rowcount 的口径也有讲究:SQLite 的 rowcount 是真实被修改的行数;MySQL 默认返回"被修改"行数,值未变化时返回 0,客户端开启 CLIENT_FOUND_ROWS 后返回"被匹配"行数——同一个 SQL 两种口径,做冲突检测必须用"被修改"口径并把这一点写进约定。重试循环的标准姿势:rowcount 为 0 时重读最新版本、重放业务判断、再试,超过上限转人工或队列。

```python
# file: code/04_数据库与缓存/q2210_rowcount_optimistic.py
"""乐观并发: 条件 UPDATE 的 rowcount 才是冲突信号"""
import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE stock(sku TEXT PRIMARY KEY, qty INTEGER, version INTEGER)")
c.execute("INSERT INTO stock VALUES('A1', 10, 3)")

s1 = conn.cursor()   # 会话一
s2 = conn.cursor()   # 会话二

v1 = s1.execute("SELECT qty, version FROM stock WHERE sku='A1'").fetchone()
v2 = s2.execute("SELECT qty, version FROM stock WHERE sku='A1'").fetchone()
print("两个会话都读到 qty=%d version=%d" % v1)

cur = s1.execute("UPDATE stock SET qty=qty-2, version=version+1 "
                 "WHERE sku='A1' AND version=?", (v1[1],))
print("会话一扣减 rowcount =", cur.rowcount)

cur = s2.execute("UPDATE stock SET qty=qty-3, version=version+1 "
                 "WHERE sku='A1' AND version=?", (v2[1],))
print("会话二扣减 rowcount =", cur.rowcount, "-> 0 即版本已变, 丢失更新被拦截")

if cur.rowcount == 0:
    nv = s2.execute("SELECT qty, version FROM stock WHERE sku='A1'").fetchone()
    cur = s2.execute("UPDATE stock SET qty=qty-3, version=version+1 "
                     "WHERE sku='A1' AND version=?", (nv[1],))
    print("会话二重读重试 rowcount =", cur.rowcount)
print("最终状态:", c.execute("SELECT qty, version FROM stock WHERE sku='A1'").fetchone())
print("rowcount 是并发下的冲突信号, 匹配行数与修改行数口径必须分清")
```

**追问**:
- ORM 里怎么拿这个信号?—— SQLAlchemy 的 session.execute 返回 CursorResult.rowcount,批量 upsert 则要用 returning 或分支统计,不能只看总行数。
- rowcount 不可靠的场景?—— 批量 DML 之外的驱动差异、UPDATE 值未变的口径差、以及某些中间件改写 SQL 后的影响行数,关键链路要用 conn.total_changes 或显式版本表兜底。

---
