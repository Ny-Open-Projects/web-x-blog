---
title: [Q7146] SQLite 并发写与 WAL 容量账
date: 2026-11-21
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7146 · SQLite 并发写与 WAL 容量账

难度：P6-P7 | 标签：SQLite、容量规划、并发

**问**：边缘小服务/数据管道的本地元数据用 SQLite，多进程一写就报 `database is locked`。SQLite 的并发模型是什么账？WAL 模式能解决什么、解决不了什么？什么时候该放弃 SQLite？

**答**：结论：SQLite 是**单写者多读者**模型：默认 journal 模式下写锁排他（读者也挡写），WAL 模式放宽为"读者不挡写者"，但**同一时刻仍只允许一个写者**——多进程写就是排队，`busy_timeout` 只是让等待体面，不会提高写吞吐。所以账是：写并发需求 > 1 时，要么在应用层串行化（单写进程/单队列），要么换 Client-Server 数据库。WAL 的收益是读写不再互斥、写是追加（快），代价是 `-wal`/`-shm` 文件与 checkpoint 时机。

实战要点：
1. 标准配置三件套：`PRAGMA journal_mode=WAL`、`PRAGMA busy_timeout=5000`、`PRAGMA synchronous=NORMAL`（WAL 下 NORMAL 已持久，性能数量级提升）。
2. WAL 文件容量账：checkpoint 前 `-wal` 可增长到 `wal_autocheckpoint`（默认 1000 页 ≈ 4MB），但**有长读事务挂着时 checkpoint 无法推进**，-wal 会无限涨——长读（报表查询）要错峰。
3. 放弃 SQLite 的信号：写 QPS 稳定超过单盘 fsync 能力（百级/s）、或需要多机共享写、或写并发进程 > 10 且排队延迟进入秒级。

```python
"""SQLite WAL 配置与写串行化演示（标准库 sqlite3，可运行）"""
import sqlite3
import tempfile
from pathlib import Path

d = Path(tempfile.mkdtemp())
db = d / "meta.db"

def conn() -> sqlite3.Connection:
    c = sqlite3.connect(db, timeout=5)  # timeout 即 busy_timeout
    c.execute("PRAGMA journal_mode=WAL")
    c.execute("PRAGMA synchronous=NORMAL")
    c.execute("PRAGMA busy_timeout=5000")
    return c

c1 = conn(); c1.execute("CREATE TABLE t(k TEXT PRIMARY KEY, v INT)")
c1.execute("INSERT INTO t VALUES('a',1)"); c1.commit()

# 单写者演示：c2 持有未提交写事务时，c3 的写会等待直到 busy_timeout
c2 = conn()
c2.execute("INSERT INTO t VALUES('b',2)")   # 未提交：持有写锁
c3 = conn()
c3.execute("PRAGMA busy_timeout=300")       # 故意调短观察
try:
    c3.execute("INSERT INTO t VALUES('c',3)")
    c3.commit()
    print("c3 wrote (lock released in time)")
except sqlite3.OperationalError as e:
    print("c3 blocked:", e)
c2.rollback()

# WAL 的读写并行收益：读者不挡写者
r = conn()
print("read ok:", r.execute("SELECT count(*) FROM t").fetchone())
c1.execute("INSERT INTO t VALUES('d',4)"); c1.commit()
print("write ok:", r.execute("SELECT count(*) FROM t").fetchone())
```

**追问 1**：为什么 WAL 模式下读者读的是快照，可能读到旧数据？
**提示**：读者从 -wal 里自己起步时的快照读，写者的新提交对进行中的读者不可见——这就是 MVCC 式隔离，账上叫"可容忍陈旧"。

**追问 2**：多线程单进程里怎么用 SQLite 才对？
**提示**：`check_same_thread=False` + 串行写队列，或每线程独立连接 + busy_timeout；绝不要共享一个 Connection 不加锁。

## 背诵要点
- SQLite 单写者：WAL 解决"读挡写"，不解决"多写并发"，多写必须应用层串行化或换库。
- 三件套：journal_mode=WAL + busy_timeout + synchronous=NORMAL。
- 长 reader 挂着会阻止 checkpoint，-wal 无限膨胀；写 QPS 超过 fsync 能力即该换 Client-Server 库。

## 复盘追问
- `database is locked` 当时出现在哪些写路径？应用层串行化该收口到哪个模块？
- 如果元数据需要被多台机器读，SQLite 还剩哪些合理用法（只读快照分发）？
