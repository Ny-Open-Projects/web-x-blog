"""双写迁移模拟: 双写 -> 分批补齐 -> 对账 -> 切读"""
import sqlite3

def dual_write(conn, order):
    with conn:
        conn.execute("INSERT INTO orders (id, amt) VALUES (?, ?)",
                     (order["id"], order["amt"]))
        try:
            conn.execute("INSERT INTO new_orders (id, amt, extra) VALUES (?, ?, 'migrated')",
                         (order["id"], order["amt"]))
        except sqlite3.IntegrityError:
            conn.execute("UPDATE new_orders SET amt = ? WHERE id = ?",
                         (order["amt"], order["id"]))

def backfill(conn, batch=2):
    while True:
        with conn:
            rows = conn.execute(
                "SELECT id, amt FROM orders WHERE id NOT IN "
                "(SELECT id FROM new_orders) LIMIT ?", (batch,)).fetchall()
            for oid, amt in rows:
                conn.execute(
                    "INSERT INTO new_orders (id, amt, extra) VALUES (?, ?, 'backfill')",
                    (oid, amt))
            if not rows:
                break

if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    conn.executescript("""
        CREATE TABLE orders (id INTEGER PRIMARY KEY, amt REAL);
        CREATE TABLE new_orders (id INTEGER PRIMARY KEY, amt REAL, extra TEXT);
    """)
    for i in range(1, 6):
        dual_write(conn, {"id": i, "amt": i * 10.0})
    # 模拟历史存量
    for i in range(6, 11):
        conn.execute("INSERT INTO orders (id, amt) VALUES (?, ?)", (i, i * 10.0))
    conn.commit()
    backfill(conn)
    old = conn.execute("SELECT count(*) FROM orders").fetchone()[0]
    new = conn.execute("SELECT count(*) FROM new_orders").fetchone()[0]
    print(f"对账: 老表 {old} 新表 {new} -> {'一致可切读' if old == new else '继续修复'}")
