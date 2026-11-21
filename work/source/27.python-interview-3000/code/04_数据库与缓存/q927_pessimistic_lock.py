"""SQLite 用 BEGIN IMMEDIATE 模拟悲观锁: 并发扣减库存不超卖"""
import sqlite3
import threading

def purchase(db_path, results):
    conn = sqlite3.connect(db_path, isolation_level=None)
    conn.execute("PRAGMA busy_timeout=3000")
    try:
        conn.execute("BEGIN IMMEDIATE")          # 相当于对库加写锁
        qty = conn.execute("SELECT qty FROM stock WHERE id=1").fetchone()[0]
        if qty > 0:
            conn.execute("UPDATE stock SET qty = qty - 1 WHERE id = 1")
            conn.execute("COMMIT")
            results.append("ok")
        else:
            conn.execute("COMMIT")
            results.append("sold out")
    except sqlite3.OperationalError as e:
        conn.execute("ROLLBACK")
        results.append(f"blocked: {e}")

if __name__ == "__main__":
    db = "q927.db"
    setup = sqlite3.connect(db, isolation_level=None)
    setup.execute("CREATE TABLE IF NOT EXISTS stock (id INTEGER PRIMARY KEY, qty INT)")
    setup.execute("DELETE FROM stock")
    setup.execute("INSERT INTO stock VALUES (1, 2)")
    setup.close()

    results = []
    threads = [threading.Thread(target=purchase, args=(db, results))
               for _ in range(5)]
    [t.start() for t in threads]
    [t.join() for t in threads]
    print("结果:", results)
    print("剩余库存:", sqlite3.connect(db).execute(
        "SELECT qty FROM stock WHERE id=1").fetchone()[0])
