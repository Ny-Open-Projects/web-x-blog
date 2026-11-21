---
title: [Q907] SQLite 的适用边界与并发写
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q907 · SQLite 的适用边界与并发写

> 难度:★★★☆ | 标签:SQLite, 选型

**问**:什么场景该用 SQLite,什么场景必须换 MySQL/PostgreSQL?多线程写要注意什么?

**答**:SQLite 适合嵌入式、桌面应用、移动端、单机小服务、测试夹具与只读分析库——它的优势是零运维、单文件、性能在单机读场景极佳。必须换的场景:多机并发写(网络文件系统上不可靠)、高并发写入竞争(整个库同一时刻仅一个写事务)、需要丰富权限/存储过程/水平扩展的体系。多线程纪律:默认连接不可跨线程共享(check_same_thread),每线程独立连接;写并发用 busy_timeout+WAL;短事务快速提交,别在事务里做 IO。它的写吞吐天花板是单写者,写并发量大的业务尽早换 C/S 数据库。

```python
# file: code/04_数据库与缓存/q907_sqlite_concurrency.py
"""多线程并发写: busy_timeout 兜底 + 短事务, 失败重试"""
import sqlite3
import threading

def writer(n, results):
    conn = sqlite3.connect("q907.db", isolation_level=None)  # 每线程独立连接
    conn.execute("PRAGMA busy_timeout=2000")
    for i in range(5):
        for _ in range(3):                    # 有限重试
            try:
                conn.execute("BEGIN IMMEDIATE")   # 显式拿写锁, 快进快出
                conn.execute("INSERT INTO t (tid, i) VALUES (?, ?)", (n, i))
                conn.execute("COMMIT")
                break
            except sqlite3.OperationalError:
                conn.execute("ROLLBACK")
        else:
            results.append((n, i, "fail"))

if __name__ == "__main__":
    setup = sqlite3.connect("q907.db", isolation_level=None)
    setup.execute("CREATE TABLE IF NOT EXISTS t (id INTEGER PRIMARY KEY, tid INT, i INT)")
    setup.execute("DELETE FROM t")
    setup.close()

    results = []
    threads = [threading.Thread(target=writer, args=(k, results)) for k in range(4)]
    [t.start() for t in threads]
    [t.join() for t in threads]
    conn = sqlite3.connect("q907.db")
    print("成功写入:", conn.execute("SELECT COUNT(*) FROM t").fetchone()[0],
          "失败:", len(results))
```

**追问**:
- SQLite 真的不能并发写吗?——同一时刻只有一个写事务,但配合 WAL、IMMEDIATE 事务和短事务,中低频写并发完全够用。
- 为什么测试夹具爱用 SQLite?——内存模式零 IO、毫秒级建库,单测里跑真实 SQL 验证逻辑,但方言差异(RR 之外的锁行为)要与生产库做集成测试互补。

---
