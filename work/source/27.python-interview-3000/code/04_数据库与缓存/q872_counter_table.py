"""用计数器表替代全表 count: 事务内同步增减, 查询 O1"""
import sqlite3

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.executescript("""
            CREATE TABLE orders (id INTEGER PRIMARY KEY, status TEXT);
            CREATE TABLE counter (name TEXT PRIMARY KEY, cnt INT);
            INSERT INTO counter VALUES ('paid_orders', 0);
        """)

        def create_order(cur, status):
            cur.execute("INSERT INTO orders (status) VALUES (?)", (status,))
            if status == "paid":
                cur.execute(
                    "INSERT INTO counter (name, cnt) VALUES ('paid_orders', 1) "
                    "ON CONFLICT (name) DO UPDATE SET cnt = cnt + 1")

        for i in range(1000):
            with conn:
                create_order(conn.cursor(), "paid" if i % 2 else "new")

        print("全表 count:", conn.execute(
            "SELECT COUNT(*) FROM orders WHERE status='paid'").fetchone()[0])
        print("计数器表:", conn.execute(
            "SELECT cnt FROM counter WHERE name='paid_orders'").fetchone()[0])
