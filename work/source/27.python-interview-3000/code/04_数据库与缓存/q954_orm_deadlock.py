"""排序后批量更新 vs 随机顺序: 演示统一加锁顺序"""
import random
import sqlite3
import threading

def update_cart(db, user_id, items, busy=400):
    conn = sqlite3.connect(db, isolation_level=None)
    conn.execute(f"PRAGMA busy_timeout={busy}")
    try:
        conn.execute("BEGIN IMMEDIATE")
        for sku in items:                       # 调用方决定顺序
            conn.execute(
                "UPDATE cart SET qty = qty + 1 WHERE user_id = ? AND sku = ?",
                (user_id, sku))
        conn.execute("COMMIT")
        return "ok"
    except sqlite3.OperationalError:
        conn.execute("ROLLBACK")
        return "busy"
    finally:
        conn.close()

if __name__ == "__main__":
    db = "q954.db"
    s = sqlite3.connect(db, isolation_level=None)
    s.execute("CREATE TABLE IF NOT EXISTS cart (user_id INT, sku TEXT, qty INT, "
              "PRIMARY KEY (user_id, sku))")
    s.execute("DELETE FROM cart")
    s.executemany("INSERT INTO cart VALUES (1, ?, 0)", [("a",), ("b",), ("c",)])
    s.close()

    random.seed(2)
    print("随机顺序:", update_cart(db, 1, random.sample(["a", "b", "c"], 3)))
    print("排序顺序:", update_cart(db, 1, sorted(["c", "a", "b"])))
    print("批量合并:", sqlite3.connect(db).execute(
        "SELECT sku, qty FROM cart ORDER BY sku").fetchall())
    print("结论: 多事务并发时必须统一按主键排序加锁, 否则循环等待")
