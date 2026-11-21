"""写入放大实测: 同样的数据 逐行提交与整批提交的 WAL 峰值对比"""
import os
import sqlite3
import tempfile

d = tempfile.mkdtemp()

def scenario(label, rows, per_tx):
    db = os.path.join(d, "wa_%s.db" % label)
    conn = sqlite3.connect(db, isolation_level=None)
    conn.execute("PRAGMA page_size=4096")
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA wal_autocheckpoint=1000000")   # 关闭自动检查点, 只看本次写入
    conn.execute("CREATE TABLE t (id INTEGER PRIMARY KEY, v TEXT)")
    wal_peak = 0
    done = 0
    while done < rows:
        conn.execute("BEGIN")
        for _ in range(min(per_tx, rows - done)):
            done += 1
            conn.execute("INSERT INTO t VALUES(?,?)", (done, "x" * 100))
        conn.execute("COMMIT")
        wal = db + "-wal"
        if os.path.exists(wal):
            wal_peak = max(wal_peak, os.path.getsize(wal))
    logical = rows * 108                                 # 每行约 108 字节逻辑数据
    conn.execute("PRAGMA wal_checkpoint(TRUNCATE)")
    conn.close()
    print("%s: 逻辑数据约 %.0f KB, WAL 峰值 %.0f KB, 放大 %.0f 倍"
          % (label, logical / 1024.0, wal_peak / 1024.0, wal_peak / max(1, logical)))

scenario("逐行提交", 200, 1)
scenario("整批提交", 200, 200)
print("同样的数据, 事务粒度决定了同一个页被写出多少次, 这就是写入放大的主项")
