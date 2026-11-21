"""条件 UPDATE 原子扣减: 单条 SQL 自带校验, 无需显式锁"""
import sqlite3
import threading

def deduct(db, amount, results):
    conn = sqlite3.connect(db, isolation_level=None)
    conn.execute("PRAGMA busy_timeout=3000")
    try:
        conn.execute("BEGIN IMMEDIATE")
        n = conn.execute("UPDATE acct SET bal = bal - ? WHERE id = 1 AND bal >= ?",
                         (amount, amount)).rowcount
        conn.execute("COMMIT")
        results.append("ok" if n else "insufficient")
    except sqlite3.OperationalError as e:
        conn.execute("ROLLBACK")
        results.append(f"busy: {e}")

if __name__ == "__main__":
    db = "q928.db"
    s = sqlite3.connect(db, isolation_level=None)
    s.execute("CREATE TABLE IF NOT EXISTS acct (id INTEGER PRIMARY KEY, bal INT)")
    s.execute("DELETE FROM acct")
    s.execute("INSERT INTO acct VALUES (1, 300)")
    s.close()

    results = []
    ts = [threading.Thread(target=deduct, args=(db, 100, results)) for _ in range(5)]
    [t.start() for t in ts]
    [t.join() for t in ts]
    print(results, "最终余额:", sqlite3.connect(db).execute(
        "SELECT bal FROM acct").fetchone()[0])
    print("要点: 条件 UPDATE 把锁竞争压缩进引擎, 应用层只见成功或不足")
