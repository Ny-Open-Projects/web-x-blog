"""模拟锁等待并用 sqlite 库内视图还原排查动作"""
import sqlite3

if __name__ == "__main__":
    holder = sqlite3.connect("q899_demo.db", isolation_level=None)
    waiter = sqlite3.connect("q899_demo.db", isolation_level=None)
    holder.execute("PRAGMA busy_timeout=1000")
    waiter.execute("PRAGMA busy_timeout=1000")
    holder.execute("CREATE TABLE IF NOT EXISTS t (id INTEGER PRIMARY KEY, v INT)")
    holder.execute("DELETE FROM t")
    holder.execute("INSERT INTO t VALUES (1, 0)")

    holder.execute("BEGIN")
    holder.execute("UPDATE t SET v = 1 WHERE id = 1")   # 持锁未提交的嫌疑事务
    try:
        waiter.execute("BEGIN")
        waiter.execute("UPDATE t SET v = 2 WHERE id = 1")
        waiter.execute("COMMIT")
    except sqlite3.OperationalError as e:
        print("等待方报错:", e)
        print("排查1: 查谁在持有 -> sqlite3_... 类似 innodb_trx/innodb_lock_waits")
        print("排查2: 持有事务状态:",
              holder.execute("PRAGMA journal_mode").fetchone(),
              "存在未提交事务 -> kill 或促其回滚")
    holder.execute("ROLLBACK")
    waiter.close(); holder.close()
