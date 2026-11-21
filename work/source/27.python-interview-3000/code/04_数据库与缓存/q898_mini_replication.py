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
