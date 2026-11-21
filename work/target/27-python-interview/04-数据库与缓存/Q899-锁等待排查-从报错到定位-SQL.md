---
title: [Q899] 锁等待排查: 从报错到定位 SQL
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q899 · 锁等待排查: 从报错到定位 SQL

> 难度:★★★★ | 标签:锁, 排查

**问**:线上出现 `Lock wait timeout exceeded`,你的排查步骤是什么?

**答**:第一步找到阻塞链:MySQL 8 查 `performance_schema.data_lock_waits` 与 `sys.innodb_lock_waits` 视图,直接给出"谁持有、谁等待、各自 SQL 与线程 id";第二步看持有者是不是"僵尸事务"——`information_schema.innodb_trx` 里 trx_started 很早、状态 sleeping 的连接,通常是应用层忘记提交或长事务,kill 之并修复代码;第三步评估策略:锁等待超时 innodb_lock_wait_timeout 默认 50s 太长,核心业务可调短快速失败+重试;第四步治本:缩小事务、给热点行加索引避免锁放大、统一加锁顺序。SQLite 场景对应 busy_timeout 与 SQLITE_BUSY 处理。

```python
# file: code/04_数据库与缓存/q899_lock_waits.py
"""模拟锁等待并用 sqlite 库内视图还原排查动作"""
import sqlite3

if __name__ == "__main__":
    holder = sqlite3.connect("q899_demo.db", isolation_level=None)
    waiter = sqlite3.connect("q899_demo.db", isolation_level=None)
    holder.execute("PRAGMA busy_timeout=1000")
    waiter.execute("PRAGMA busy_timeout=1000")
    holder.execute("CREATE TABLE IF NOT EXISTS t (id INTEGER PRIMARY KEY, v INT)")
    holder.execute("DELETE FROM t")
    holder.execute("INSERT INTO t VALUES (1, 0)")

    holder.execute("BEGIN")
    holder.execute("UPDATE t SET v = 1 WHERE id = 1")   # 持锁未提交的嫌疑事务
    try:
        waiter.execute("BEGIN")
        waiter.execute("UPDATE t SET v = 2 WHERE id = 1")
        waiter.execute("COMMIT")
    except sqlite3.OperationalError as e:
        print("等待方报错:", e)
        print("排查1: 查谁在持有 -> sqlite3_... 类似 innodb_trx/innodb_lock_waits")
        print("排查2: 持有事务状态:",
              holder.execute("PRAGMA journal_mode").fetchone(),
              "存在未提交事务 -> kill 或促其回滚")
    holder.execute("ROLLBACK")
    waiter.close(); holder.close()
```

**追问**:
- 怎么提前发现长事务?——定期巡检 information_schema.innodb_trx 中运行时间超阈值的连接,并给应用层的"事务里调用外部接口"加静态检查。
- 死锁和锁等待超时的区别?——死锁是等待成环被 InnoDB 主动检测并回滚一方;锁等待超时是单方面等太久没人成环,持有方可能只是慢或忘了提交。

---
