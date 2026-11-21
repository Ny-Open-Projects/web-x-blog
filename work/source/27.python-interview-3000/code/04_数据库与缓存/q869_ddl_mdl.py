"""演示未提交事务持锁导致 DDL 被阻塞: 对应 MySQL MDL 排队事故模型"""
import sqlite3
import time

if __name__ == "__main__":
    conn_a = sqlite3.connect("q869_demo.db", isolation_level=None)
    conn_b = sqlite3.connect("q869_demo.db", isolation_level=None)
    conn_a.execute("PRAGMA busy_timeout=1500")
    conn_b.execute("PRAGMA busy_timeout=1500")
    conn_a.execute("CREATE TABLE IF NOT EXISTS t (id INTEGER PRIMARY KEY, v TEXT)")
    conn_a.execute("DELETE FROM t")

    conn_a.execute("BEGIN")
    conn_a.execute("INSERT INTO t (v) VALUES ('uncommitted')")
    print("连接A: 开启事务未提交, 持有写锁")

    t0 = time.perf_counter()
    try:
        conn_b.execute("ALTER TABLE t ADD COLUMN extra TEXT")
        print("连接B: DDL 成功")
    except sqlite3.OperationalError as e:
        print(f"连接B: DDL 被阻塞超时 {time.perf_counter() - t0:.1f}s -> {e}")
    finally:
        conn_a.execute("ROLLBACK")
        conn_b.close()
        conn_a.close()
