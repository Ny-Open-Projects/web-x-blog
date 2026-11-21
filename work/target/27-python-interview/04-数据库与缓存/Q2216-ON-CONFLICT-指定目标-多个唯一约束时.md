---
title: [Q2216] ON CONFLICT 指定目标: 多个唯一约束时命中谁
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2216 · ON CONFLICT 指定目标: 多个唯一约束时命中谁

> 难度:★★★☆ | 标签:SQL, upsert

**问**:表上有两个 UNIQUE 约束,upsert 只声明了一个目标,冲突发生在另一个上会怎样?

**答**:指定目标的 ON CONFLICT(a) DO UPDATE 只处理 a 约束上的冲突;若实际冲突发生在未声明的 b 约束上,语句直接抛唯一约束错误,不会走 upsert——这是把"错误当兜底"的写法,通常正是想要的:目标之外的冲突说明数据有问题。不带目标的 ON CONFLICT DO UPDATE/DO NOTHING 则对任何唯一约束冲突都生效,SQLite 按约束声明顺序命中第一个,但"命中哪个"不再由调用方控制,语义变弱。最佳实践:能明确唯一键就写目标;多约束共存时,每个 upsert 语句只对"本语句的业务键"声明目标,其余冲突显式暴露;MySQL 的 ON DUPLICATE KEY UPDATE 没有目标概念,任何唯一键冲突都会触发更新,迁移时要注意行为差。

```python
# file: code/04_数据库与缓存/q2216_onconflict_target.py
"""ON CONFLICT 指定目标: 多个唯一约束时冲突到底命中谁"""
import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE kv(a TEXT UNIQUE, b TEXT UNIQUE, n INTEGER DEFAULT 0)")
c.execute("INSERT INTO kv VALUES('x', 'y', 1)")

c.execute("INSERT INTO kv(a, b, n) VALUES('x', 'z', 5) "
          "ON CONFLICT(a) DO UPDATE SET n = n + 1")
print("冲突 a 走指定目标 upsert:", c.execute("SELECT * FROM kv").fetchall())

try:
    c.execute("INSERT INTO kv(a, b, n) VALUES('w', 'y', 9) "
              "ON CONFLICT(a) DO UPDATE SET n = n + 1")
except sqlite3.IntegrityError as e:
    print("冲突 b 但目标写了 a     :", str(e)[:44], "-> 不走 upsert 直接报错")

c.execute("INSERT INTO kv(a, b, n) VALUES('w', 'y', 9) ON CONFLICT DO NOTHING")
print("不带目标 DO NOTHING    :", c.execute("SELECT * FROM kv WHERE a='w'").fetchall(),
      " <- b 冲突被静默吞掉")
c.execute("INSERT INTO kv(a, b, n) VALUES('x', 'y', 99) ON CONFLICT DO UPDATE SET n = 99")
print("不带目标 DO UPDATE     :", c.execute("SELECT * FROM kv").fetchall())
```

**追问**:
- DO UPDATE 里怎么引用旧值?—— 表名直引旧值,excluded.前缀引待插入值,如 SET n = kv.n + excluded.n 做累加。
- DO UPDATE 会触发外键动作吗?—— 会把它当普通 UPDATE 对待,子表带 CASCADE 时可能意外放大,热路径 upsert 要确认无级联悬挂。

---
