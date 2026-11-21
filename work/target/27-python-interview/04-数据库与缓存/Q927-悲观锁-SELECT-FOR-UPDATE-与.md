---
title: [Q927] 悲观锁: SELECT FOR UPDATE 与 SQLite 等价物
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q927 · 悲观锁: SELECT FOR UPDATE 与 SQLite 等价物

> 难度:★★★★ | 标签:并发控制, 悲观锁

**问**:SELECT FOR UPDATE 做了什么?SQLAlchemy 怎么写?没有 FOR UPDATE 的库怎么替代?

**答**:FOR UPDATE 在读取行时同步加排他行锁,其他事务对这些行的读(非锁定读除外)与写会被阻塞,直到当前事务提交,把"读-计算-写"变成受保护临界区,适合冲突率高的热点行。SQLAlchemy 用 `select(...).with_for_update()`,可加 nowait/skip_locked 控制等待策略:nowait 立即报错,skip_locked 跳过被锁行(任务队列取活的标配)。MySQL 支持 FOR UPDATE;SQLite 没有行锁,等价物是 `BEGIN IMMEDIATE`——把整个库当成临界区;PG 完整支持。纪律:FOR UPDATE 必须在事务里,用完尽快提交,别在锁内调外部接口。

```python
# file: code/04_数据库与缓存/q927_pessimistic_lock.py
"""SQLite 用 BEGIN IMMEDIATE 模拟悲观锁: 并发扣减库存不超卖"""
import sqlite3
import threading

def purchase(db_path, results):
    conn = sqlite3.connect(db_path, isolation_level=None)
    conn.execute("PRAGMA busy_timeout=3000")
    try:
        conn.execute("BEGIN IMMEDIATE")          # 相当于对库加写锁
        qty = conn.execute("SELECT qty FROM stock WHERE id=1").fetchone()[0]
        if qty > 0:
            conn.execute("UPDATE stock SET qty = qty - 1 WHERE id = 1")
            conn.execute("COMMIT")
            results.append("ok")
        else:
            conn.execute("COMMIT")
            results.append("sold out")
    except sqlite3.OperationalError as e:
        conn.execute("ROLLBACK")
        results.append(f"blocked: {e}")

if __name__ == "__main__":
    db = "q927.db"
    setup = sqlite3.connect(db, isolation_level=None)
    setup.execute("CREATE TABLE IF NOT EXISTS stock (id INTEGER PRIMARY KEY, qty INT)")
    setup.execute("DELETE FROM stock")
    setup.execute("INSERT INTO stock VALUES (1, 2)")
    setup.close()

    results = []
    threads = [threading.Thread(target=purchase, args=(db, results))
               for _ in range(5)]
    [t.start() for t in threads]
    [t.join() for t in threads]
    print("结果:", results)
    print("剩余库存:", sqlite3.connect(db).execute(
        "SELECT qty FROM stock WHERE id=1").fetchone()[0])
```

**追问**:
- FOR UPDATE 与普通 SELECT 的区别?——普通 SELECT 在 MVCC 下是无锁快照读,锁不住任何东西;FOR UPDATE 是当前读并加排他锁。
- skip_locked 的典型场景?——多个 worker 抢任务:`WHERE status='pending' ... FOR UPDATE SKIP LOCKED LIMIT 1`,各拿各的不互相阻塞。

---
