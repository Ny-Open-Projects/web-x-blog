---
title: [Q2756] 原子交换的两条 UPDATE: 唯一约束下的换位借道中转值
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2756 · 原子交换的两条 UPDATE: 唯一约束下的换位借道中转值

> 难度:★★★★ | 标签:事务, 约束

**问**:拖拽排序要交换两行的 pos 值,pos 上有唯一约束,直接两条 UPDATE 为什么会炸?

**答**:因为中间态非法:把第一行 pos 改成第二行现值的那一刻,唯一约束就撞了——两条 UPDATE 各自合法,但第一条执行完的瞬间表处于约束不允许的状态。解法是借道中转值,三步换位且全在一个事务里:先把第一行挪到一个肯定空闲的值(如取负数域或加一个巨大偏移),再把第二行落到目标值,最后把第一行落回目标值,COMMIT 时约束整体成立。PostgreSQL 可以用 DEFERRABLE 唯一约束把检查推迟到提交时,两步就够;MySQL 8 没有可延迟唯一约束,还是中转值稳。注意批量拖拽时按中转偏移统一挪一段,避免两两交换的中转值互相撞车。

```python
# file: code/04_数据库与缓存/q2756_atomic_swap.py
"""原子交换: 唯一约束下直接换位撞约束, 借道中转值三步完成"""
import sqlite3

conn = sqlite3.connect(":memory:", isolation_level=None)
c = conn.cursor()
c.execute("CREATE TABLE todo (id INTEGER PRIMARY KEY, pos INTEGER UNIQUE, title TEXT)")
c.executemany("INSERT INTO todo VALUES(?,?,?)", [(1, 1, "买牛奶"), (2, 2, "写周报")])

try:
    c.execute("BEGIN")
    c.execute("UPDATE todo SET pos=2 WHERE id=1")   # 第一步就撞上 id=2 现有的 pos=2
    c.execute("UPDATE todo SET pos=1 WHERE id=2")
    c.execute("COMMIT")
    print("直接交换竟然成功, 不应到这里")
except sqlite3.IntegrityError as e:
    c.execute("ROLLBACK")
    print("直接交换撞约束: %s (事务已整体回滚)" % e)

c.execute("BEGIN")
c.execute("UPDATE todo SET pos=-1 WHERE id=1")      # 借道负数域, 挪出冲突
c.execute("UPDATE todo SET pos=1 WHERE id=2")
c.execute("UPDATE todo SET pos=2 WHERE id=1")
c.execute("COMMIT")
print("借道换位后:", c.execute("SELECT id, pos, title FROM todo ORDER BY pos").fetchall())
print("要点: 中间态非法是约束的错也是设计的题, 中转值把非法中间态藏进事务内部")
```

**追问**:
- 中转值选什么才安全?—— 必须取值域外且不参与业务排序的区段,如负数或极大偏移,并防并发交换撞同一个中转段。
- 交换和并发拖拽怎么共存?—— 中转偏移带上请求维度(如 1e9 + 请求号)或对目标行加锁串行化。

---
