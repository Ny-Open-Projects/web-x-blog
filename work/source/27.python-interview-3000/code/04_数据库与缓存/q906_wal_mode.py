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
