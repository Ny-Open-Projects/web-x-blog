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
