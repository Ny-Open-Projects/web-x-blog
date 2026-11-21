---
title: [Q906] SQLite 的 WAL 模式: 读写并发的钥匙
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q906 · SQLite 的 WAL 模式: 读写并发的钥匙

> 难度:★★★☆ | 标签:SQLite, 并发

**问**:SQLite 默认日志模式是什么问题?WAL 模式如何改善并发?

**答**:默认 rollback journal 模式下写事务要"备份原页 -> 改动 -> 提交时回滚备份或清除",写事务排斥读写,读写互堵。WAL(Write-Ahead Logging)把改动先追加到 -wal 文件,提交只需 fsync WAL;读者通过 WAL index 读"主库页 + WAL 中较新的页",于是读写不再互斥——一写多读并发,只有两个写事务之间互斥。代价:WAL 需要定期 checkpoint 合并回主库、不能跨网络文件系统、读到的可能是稍旧快照。Python 里 `PRAGMA journal_mode=WAL` 一句开启,配合 busy_timeout 使用,是桌面/小服务场景标配。

```python
# file: code/04_数据库与缓存/q906_wal_mode.py
"""开启 WAL 并验证: 写事务进行中读连接仍可读到快照"""
import sqlite3
import threading
import time

if __name__ == "__main__":
    w = sqlite3.connect("q906.db", isolation_level=None)
    r = sqlite3.connect("q906.db", isolation_level=None)
    w.execute("PRAGMA journal_mode=WAL")
    w.execute("CREATE TABLE IF NOT EXISTS t (v INT)")
    w.execute("DELETE FROM t")
    w.execute("INSERT INTO t VALUES (1)")
    print("日志模式:", r.execute("PRAGMA journal_mode").fetchone()[0])

    w.execute("BEGIN")
    w.execute("INSERT INTO t VALUES (2)")     # 未提交的写
    snapshot = r.execute("SELECT COUNT(*) FROM t").fetchone()[0]
    print("写事务未提交时读者看到:", snapshot, "行  <- MVCC 快照读, 不被阻塞")
    w.execute("COMMIT")
    print("提交后读者看到:", r.execute("SELECT COUNT(*) FROM t").fetchone()[0], "行")
    w.close(); r.close()
```

**追问**:
- WAL 什么时候把数据合回主库?——checkpoint(默认 WAL 达 1000 页或连接关闭时),可用 `PRAGMA wal_checkpoint(TRUNCATE)` 主动执行。
- WAL 下两个写事务并发会怎样?——仍互斥,后到者等 busy_timeout 后报 SQLITE_BUSY,写入吞吐仍是单写,只是读不再被写阻塞。

---
