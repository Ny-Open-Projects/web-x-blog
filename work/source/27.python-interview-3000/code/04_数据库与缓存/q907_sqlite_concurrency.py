"""多线程并发写: busy_timeout 兜底 + 短事务, 失败重试"""
import sqlite3
import threading

def writer(n, results):
    conn = sqlite3.connect("q907.db", isolation_level=None)  # 每线程独立连接
    conn.execute("PRAGMA busy_timeout=2000")
    for i in range(5):
        for _ in range(3):                    # 有限重试
            try:
                conn.execute("BEGIN IMMEDIATE")   # 显式拿写锁, 快进快出
                conn.execute("INSERT INTO t (tid, i) VALUES (?, ?)", (n, i))
                conn.execute("COMMIT")
                break
            except sqlite3.OperationalError:
                conn.execute("ROLLBACK")
        else:
            results.append((n, i, "fail"))

if __name__ == "__main__":
    setup = sqlite3.connect("q907.db", isolation_level=None)
    setup.execute("CREATE TABLE IF NOT EXISTS t (id INTEGER PRIMARY KEY, tid INT, i INT)")
    setup.execute("DELETE FROM t")
    setup.close()

    results = []
    threads = [threading.Thread(target=writer, args=(k, results)) for k in range(4)]
    [t.start() for t in threads]
    [t.join() for t in threads]
    conn = sqlite3.connect("q907.db")
    print("成功写入:", conn.execute("SELECT COUNT(*) FROM t").fetchone()[0],
          "失败:", len(results))
