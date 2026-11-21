---
title: [Q2503] BEGIN DEFERRED 与 IMMEDIATE: 升级死锁
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2503 · BEGIN DEFERRED 与 IMMEDIATE: 升级死锁

> 难度:★★★☆ | 标签:SQLite, 锁

**问**:两个连接都"先读后写",为什么卡死了?

**答**:这是 DEFERRED 事务的锁升级死锁:DEFERRED 开始时不拿锁,首次读拿共享锁,首次写尝试升级为写锁。两个连接都完成读后,A 先升级成功;B 升级失败(保留锁已属于 A);同时 A 想提交也被挡——B 的共享读锁没放,提交阶段拿不到独占权,双方僵持,唯一出路是一方放弃。解法:明知事务要写就用 BEGIN IMMEDIATE 起手,写锁在事务门口就位,冲突退化为排队(busy_timeout 控制),不再有半路升级;或切 WAL 模式,读写不互斥,升级死锁自然消失。

```python
# file: code/04_数据库与缓存/q2503_deferred_immediate.py
"""BEGIN DEFERRED 与 IMMEDIATE: 读后写事务的锁升级死锁"""
import os
import shutil
import sqlite3
import tempfile

tmp = tempfile.mkdtemp()
db = os.path.join(tmp, "lock.db")
try:
    conn0 = sqlite3.connect(db, isolation_level=None)
    conn0.execute("CREATE TABLE t (id INTEGER PRIMARY KEY, v INTEGER)")

    a = sqlite3.connect(db, isolation_level=None, timeout=0.3)
    b = sqlite3.connect(db, isolation_level=None, timeout=0.3)

    # DEFERRED: 事务开始不上锁, 首次读拿共享锁, 首次写尝试升级
    a.execute("BEGIN DEFERRED")
    a.execute("SELECT COUNT(*) FROM t").fetchone()
    b.execute("BEGIN DEFERRED")
    b.execute("SELECT COUNT(*) FROM t").fetchone()      # 两个读者相安无事
    a.execute("INSERT INTO t VALUES(1, 1)")             # a 升级为保留锁, 成功
    try:
        b.execute("INSERT INTO t VALUES(2, 2)")         # b 也要升级 -> 升级失败
        print("b 升级成功 (不应发生)")
    except sqlite3.OperationalError as e:
        print("b 的写升级失败: %s (a 已持有保留锁)" % e)
    try:
        a.execute("COMMIT")                             # a 想提交, 但 b 的共享读锁未放
        print("a 提交成功 (不应发生)")
    except sqlite3.OperationalError as e:
        print("a 的提交也被挡: %s (升级死锁成立: 谁都动不了)" % e)
    b.execute("ROLLBACK")                               # 唯一出路: 放弃者释放读锁
    a.execute("COMMIT")
    print("b 回退后 a 才能提交 -> 死锁的解法是有一方先退出")

    # IMMEDIATE: 开始就抢写锁, 冲突退化为门口排队
    a.execute("BEGIN IMMEDIATE")
    a.execute("INSERT INTO t VALUES(3, 3)")
    try:
        b.execute("BEGIN IMMEDIATE")                    # b 在事务起点排队
        b.execute("INSERT INTO t VALUES(4, 4)")
        b.execute("COMMIT")
        print("b 的 IMMEDIATE 排队成功 (不应发生, a 还没提交)")
    except sqlite3.OperationalError as e:
        print("b 排队超时: %s (等待发生在门口而不是半路)" % e)
    a.execute("COMMIT")
    b.execute("BEGIN IMMEDIATE")                        # a 提交后 b 正常进入
    b.execute("INSERT INTO t VALUES(4, 4)")
    b.execute("COMMIT")
    n = sqlite3.connect(db).execute("SELECT COUNT(*) FROM t").fetchone()[0]
    print("最终行数: %d" % n)
    print("结论: 先读后写的事务在 DEFERRED 下可能互相卡死, 明知要写就用 IMMEDIATE 起手,")
    print("      或切 WAL 模式让读不再挡写")
finally:
    shutil.rmtree(tmp, ignore_errors=True)
```

**追问**:
- WAL 模式下还有升级死锁吗?—— 没有同款:读写不互斥,写写仍是单写者排队;但"读旧快照后写"要防 SQLITE_BUSY_SNAPSHOT。
- MySQL 有对应概念吗?—— 有,InnoDB 的意向锁与间隙锁让"先读后写"冲突以死锁形式出现,检测后回滚一方,语义等价。

---
