---
title: [Q884] 大表 DDL 的锁: MDL 与长事务排队事故
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q884 · 大表 DDL 的锁: MDL 与长事务排队事故

> 难度:★★★★ | 标签:DDL, 锁

**问**:加索引会锁表吗?"加索引不锁表"的 Online DDL 为什么还出过线上事故?

**答**:Online DDL 的 INPLACE 阶段允许并发 DML,但 DDL 开始要获取 MDL 写锁做准备、结束要短暂排他提交元数据——只要此刻有未提交事务持有该表 MDL 读锁,DDL 就排队,而 DDL 一排队,其后所有新查询全部堵死,这是"加个索引拖垮全站"的经典链路。防护:DDL 前检查长事务并清理、设置 lock_wait_timeout(如 5s)让 DDL 快速失败重试、低峰执行、大表走 gh-ost。8.0 的 INSTANT 算法仅改元数据,加列/改默认值秒级,但改列类型、加 FULLTEXT 等仍走重建。SQLite 演示:活动事务期间 ALTER 直接被拒,直观呈现"DDL 撞上长事务"。

```python
# file: code/04_数据库与缓存/q884_ddl_blocked.py
"""活动事务未提交时执行 ALTER: 直观演示 DDL 与长事务冲突"""
import sqlite3

if __name__ == "__main__":
    import os
    if os.path.exists("q884.db"):                     # 重复运行前清理
        os.remove("q884.db")
    conn = sqlite3.connect("q884.db", isolation_level=None)
    conn.execute("PRAGMA busy_timeout=1000")
    conn.execute("CREATE TABLE IF NOT EXISTS t (id INTEGER PRIMARY KEY)")
    conn.execute("BEGIN")
    conn.execute("INSERT INTO t DEFAULT VALUES")     # 长事务持锁中

    try:
        conn.execute("ALTER TABLE t ADD COLUMN c TEXT")
        print("DDL 成功")
    except sqlite3.OperationalError as e:
        print("DDL 被阻塞:", e, "-> 对应 MySQL MDL 排队, 应短超时快速失败")
    finally:
        conn.execute("ROLLBACK")
        conn.close()
```

**追问**:
- 怎么发现"谁堵住了 DDL"?——MySQL 8 查 performance_schema.metadata_locks 与 sys.schema_table_lock_waits,能直接给出持锁会话与等待链。
- 加索引到底会不会锁写?——INPLACE 建索引期间 DML 可并发,只在首尾短锁;gh-ost 方案全程 DML 无感。

---
