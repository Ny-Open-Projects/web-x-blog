---
title: [Q898] 半同步复制与 GTID 概念
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q898 · 半同步复制与 GTID 概念

> 难度:★★★★ | 标签:复制, MySQL

**问**:异步复制、半同步复制有什么区别?GTID 解决了什么问题?

**答**:异步复制:主库提交即返回,从库收到 binlog 才应用,主库宕机可能丢最新事务;半同步复制(5.5+):主库等待至少一个从库"已接收 binlog"的 ack 才向客户端返回成功,折衷了可用性与不丢数据(after_sync 等待的是写入 relay log,不是应用完成,性能损失有限);GROUP Replication/MGR 则更进一步用 Paxos 多数派。GTID = server_uuid:sequence,给事务全局身份,带来三件事:从库自动定位复制位点、主从切换不再手工算 binlog pos、容易判断某事务是否已在全拓扑执行。工程要点:半同步退化(ack 超时降级为异步)要监控,切换演练要覆盖 GTID 缺口检查。

```python
# file: code/04_数据库与缓存/q898_mini_replication.py
"""sqlite 模拟主从复制: oplog 表 + 位点应用, 体会 GTID 式位点思想"""
import sqlite3

def apply_oplog(replica, rows, start):
    applied = start
    for pos, cmd, arg in rows:
        if pos > start:
            replica.execute(cmd, (arg,))
            applied = pos
    replica.commit()
    return applied

if __name__ == "__main__":
    master = sqlite3.connect(":memory:")
    master.execute("CREATE TABLE log_replica (pos INTEGER PRIMARY KEY, cmd TEXT, arg INT)")
    for i, (cmd, arg) in enumerate([("INSERT INTO kv VALUES (?)", 1),
                                    ("INSERT INTO kv VALUES (?)", 2)], 1):
        master.execute("INSERT INTO log_replica VALUES (?, ?, ?)", (i, cmd, arg))
    master.execute("CREATE TABLE kv (k INTEGER PRIMARY KEY)")
    master.commit()

    replica = sqlite3.connect(":memory:")
    replica.execute("CREATE TABLE kv (k INTEGER PRIMARY KEY)")

    rows = master.execute("SELECT pos, cmd, arg FROM log_replica ORDER BY pos").fetchall()
    last = apply_oplog(replica, rows, start=0)
    print("从库已应用位点:", last,
          "数据:", replica.execute("SELECT * FROM kv").fetchall())
    # 增量: 从库记录自己的位点, 只应用新 oplog, 等价 GTID 断点续传
    master.execute("INSERT INTO log_replica VALUES (3, 'INSERT INTO kv VALUES (?)', 3)")
    last = apply_oplog(replica, rows + master.execute(
        "SELECT pos, cmd, arg FROM log_replica WHERE pos > ?", (last,)).fetchall(),
        start=last)
    print("增量后位点:", last, "数据:", replica.execute("SELECT * FROM kv").fetchall())
```

**追问**:
- 半同步等待的是"接收"还是"执行"?——标准 after_sync 只等从库把 binlog 落到 relay log,不等重放,所以延迟小但不保证从库已可读。
- GTID 缺口是什么?——同一 GTID 集合在不同节点缺失某些事务,切换前必须校验补齐,否则数据分叉。

---
