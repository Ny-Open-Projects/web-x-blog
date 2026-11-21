---
title: [Q869] 大表 Online DDL: 加字段与加索引的锁影响
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q869 · 大表 Online DDL: 加字段与加索引的锁影响

> 难度:★★★★ | 标签:DDL, MySQL

**问**:给一张千万行的线上表加一列,直接 ALTER 会发生什么?MySQL 8 有哪些改进?

**答**:DDL 需要拿元数据锁 MDL:执行开始和结束各有一次短暂的 MDL 排他锁窗口,期间所有读写都被阻塞;若前面有长事务/慢查询持有该表 MDL 读锁,ALTER 会排队,后续所有新查询也会被它卡住,容易演变成全表不可用事故。MySQL 5.6+ 的 Online DDL 对多数操作(INPLACE)允许并发 DML,只在首尾短暂锁表;MySQL 8.0 的 `ALGORITHM=INSTANT` 让加列(末尾位置)只改元数据、秒级完成。工程纪律:先查 information_schema 的长事务,DDL 设 lock_wait_timeout 短超时,重试而非长等;超大表优先 gh-ost/pt-osc(Q870)。

```python
# file: code/04_数据库与缓存/q869_ddl_mdl.py
"""演示未提交事务持锁导致 DDL 被阻塞: 对应 MySQL MDL 排队事故模型"""
import sqlite3
import time

if __name__ == "__main__":
    conn_a = sqlite3.connect("q869_demo.db", isolation_level=None)
    conn_b = sqlite3.connect("q869_demo.db", isolation_level=None)
    conn_a.execute("PRAGMA busy_timeout=1500")
    conn_b.execute("PRAGMA busy_timeout=1500")
    conn_a.execute("CREATE TABLE IF NOT EXISTS t (id INTEGER PRIMARY KEY, v TEXT)")
    conn_a.execute("DELETE FROM t")

    conn_a.execute("BEGIN")
    conn_a.execute("INSERT INTO t (v) VALUES ('uncommitted')")
    print("连接A: 开启事务未提交, 持有写锁")

    t0 = time.perf_counter()
    try:
        conn_b.execute("ALTER TABLE t ADD COLUMN extra TEXT")
        print("连接B: DDL 成功")
    except sqlite3.OperationalError as e:
        print(f"连接B: DDL 被阻塞超时 {time.perf_counter() - t0:.1f}s -> {e}")
    finally:
        conn_a.execute("ROLLBACK")
        conn_b.close()
        conn_a.close()
```

**追问**:
- 为什么说"MDL 排队"比 DDL 本身更危险?——DDL 等待期间会堵住其后所有该表的查询,形成雪崩;所以要短超时快速失败并重试。
- 8.0 加列 INSTANT 有条件吗?——只支持加在末尾且不改存储格式时,其他操作仍需 INPLACE 甚至 COPY。

---
