"""活动事务未提交时执行 ALTER: 直观演示 DDL 与长事务冲突"""
import sqlite3

if __name__ == "__main__":
    import os
    if os.path.exists("q884.db"):                     # 重复运行前清理
        os.remove("q884.db")
    conn = sqlite3.connect("q884.db", isolation_level=None)
    conn.execute("PRAGMA busy_timeout=1000")
    conn.execute("CREATE TABLE IF NOT EXISTS t (id INTEGER PRIMARY KEY)")
    conn.execute("BEGIN")
    conn.execute("INSERT INTO t DEFAULT VALUES")     # 长事务持锁中

    try:
        conn.execute("ALTER TABLE t ADD COLUMN c TEXT")
        print("DDL 成功")
    except sqlite3.OperationalError as e:
        print("DDL 被阻塞:", e, "-> 对应 MySQL MDL 排队, 应短超时快速失败")
    finally:
        conn.execute("ROLLBACK")
        conn.close()
