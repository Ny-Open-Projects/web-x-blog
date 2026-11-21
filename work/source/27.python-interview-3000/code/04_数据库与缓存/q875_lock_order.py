"""双线程按不同顺序更新两行触发 SQLITE_BUSY, 再用统一顺序修复"""
import sqlite3
import threading

def setup():
    conn = sqlite3.connect("q875_demo.db", isolation_level=None)
    conn.execute("PRAGMA busy_timeout=300")
    conn.execute("CREATE TABLE IF NOT EXISTS acct (id INT PRIMARY KEY, bal INT)")
    conn.execute("DELETE FROM acct")
    conn.executemany("INSERT INTO acct VALUES (?, ?)", [(1, 100), (2, 100)])
    return conn

def transfer(conn, src, dst, amt, expect_fail):
    try:
        conn.execute("BEGIN IMMEDIATE")
        conn.execute("UPDATE acct SET bal = bal - ? WHERE id = ?", (amt, src))
        conn.execute("UPDATE acct SET bal = bal + ? WHERE id = ?", (amt, dst))
        conn.execute("COMMIT")
        print(f"转账 {src}->{dst} 成功")
    except sqlite3.OperationalError as e:
        conn.execute("ROLLBACK")
        print(f"转账 {src}->{dst} 失败: {e}" + ("" if expect_fail else " 不应发生"))

if __name__ == "__main__":
    setup()
    c1, c2 = sqlite3.connect("q875_demo.db"), sqlite3.connect("q875_demo.db")
    for c in (c1, c2):
        c.execute("PRAGMA busy_timeout=300")
    # 反序: 线程1 走 1->2, 线程2 走 2->1, 高概率一方等待超时
    t1 = threading.Thread(target=transfer, args=(c1, 1, 2, 10, True))
    t2 = threading.Thread(target=transfer, args=(c2, 2, 1, 10, True))
    t1.start(); t2.start(); t1.join(); t2.join()
    # 修复: 两个方向都按主键升序锁定
    transfer(c1, *sorted((1, 2)), 10, False)
    transfer(c2, *sorted((2, 1)), 10, False)
    print("最终余额:", c1.execute("SELECT * FROM acct").fetchall())
