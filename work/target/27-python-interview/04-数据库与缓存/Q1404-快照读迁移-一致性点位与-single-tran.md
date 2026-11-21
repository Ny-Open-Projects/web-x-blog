---
title: [Q1404] 快照读迁移: 一致性点位与 single-transaction
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1404 · 快照读迁移: 一致性点位与 single-transaction

> 难度:★★★★ | 标签:数据迁移, 快照

**问**:迁移历史数据时业务还在写,怎么保证导出的数据是"某一个时刻的完整一致视图"?

**答**:靠快照读。MySQL 的标准做法是 mysqldump --single-transaction:开启一个 REPEATABLE READ 长事务,InnoDB 的 MVCC 让整个导出过程读到的都是事务开始时的版本,业务照常写入互不阻塞;同时记录当时的 binlog 位点/GTID,后续增量追平就从这个点位开始。前提是表都是 InnoDB 事务表,MyISAM 混在其中时快照对它无效。大表长事务要警惕两个副作用:undo 链增长、以及它会让 DDL 的 MDL 排队(Q884),所以快照事务要限时、限高峰。SQLite 等价物是 WAL 模式下的读者快照,本节代码直接演示这个语义。

```python
# file: code/04_数据库与缓存/q1404_snapshot_migrate.py
"""快照读迁移: WAL 模式下长事务读到的始终是开始时的快照"""
import os
import sqlite3

path = "/tmp/q1404_demo.db"
if os.path.exists(path):
    os.remove(path)
writer = sqlite3.connect(path)
writer.execute("PRAGMA journal_mode=WAL")
writer.execute("CREATE TABLE t(id INTEGER PRIMARY KEY, v TEXT)")
writer.execute("INSERT INTO t VALUES(1,'v0')")
writer.commit()

reader = sqlite3.connect(path)
reader.execute("BEGIN")                       # 迁移读事务开启
print("迁移读起点:", reader.execute("SELECT v FROM t WHERE id=1").fetchone()[0])

writer.execute("UPDATE t SET v='v1' WHERE id=1")
writer.commit()
print("源库已提交 v1, 迁移事务内再读:",
      reader.execute("SELECT v FROM t WHERE id=1").fetchone()[0], "<- 仍是快照")
reader.commit()                               # 事务结束 快照释放
print("迁移事务结束后再读:", sqlite3.connect(path).execute("SELECT v FROM t WHERE id=1").fetchone()[0])
print("类比: mysqldump --single-transaction 就是借 MVCC 拿一致性点位, 再用 binlog 位点追增量")
```

**追问**:
- 快照读能不能代替锁?——导数据场景可以,这就是它比 FTWRL 温和的原因;但它不提供"读到最新"语义,需要实时一致时要回到锁或停写窗口。
- --single-transaction 内部做了什么?——开 REPEATABLE READ 事务并 START TRANSACTION WITH CONSISTENT SNAPSHOT,瞬时加锁记下 binlog 位点后即释放,导出与位点同刻。
- MVCC 凭什么保证全程一个版本?——事务开始即固定 read view,之后快照读沿 undo 链回溯到该版本;业务写入生成新版本,互不阻塞。
- 生产陷阱?——表里混着 MyISAM 快照对它无效,导出期间撞上 DDL 会被 MDL 卡死并堵住后续全部查询(Q884);导出前核对引擎并冻结 DDL 窗口。

---
