"""用 sqlite 演示锁升级型死锁: 双方都持读再都要写, 形成互相等待"""
import sqlite3

if __name__ == "__main__":
    a = sqlite3.connect("q874_demo.db", isolation_level=None)
    b = sqlite3.connect("q874_demo.db", isolation_level=None)
    a.execute("PRAGMA busy_timeout=800")
    b.execute("PRAGMA busy_timeout=800")
    a.execute("CREATE TABLE IF NOT EXISTS t (id INTEGER PRIMARY KEY, v INT)")
    a.execute("DELETE FROM t")
    a.execute("INSERT INTO t VALUES (1, 0)")

    a.execute("BEGIN")
    b.execute("BEGIN")
    a.execute("SELECT * FROM t WHERE id = 1")   # A 持读快照
    b.execute("SELECT * FROM t WHERE id = 1")   # B 持读快照
    a.execute("UPDATE t SET v = v + 1 WHERE id = 1")  # A 申请写锁成功
    try:
        b.execute("UPDATE t SET v = v + 1 WHERE id = 1")  # B 等待 A
    except sqlite3.OperationalError as e:
        print("B 被阻塞放弃:", e)
        b.execute("ROLLBACK")                   # B 放弃并释放共享锁
    a.execute("COMMIT")
    b.close()
    a.close()
    print("MySQL RR 下类似场景: 双方同持间隙锁后互相等插入 -> InnoDB 判死锁回滚一方")
