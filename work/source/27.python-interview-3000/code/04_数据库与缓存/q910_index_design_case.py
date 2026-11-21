"""订单表五类高频查询的索引方案与逐条 EXPLAIN 验证"""
import sqlite3

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.execute("""CREATE TABLE orders (
            id INTEGER PRIMARY KEY, order_no TEXT UNIQUE,
            user_id INT, merchant_id INT, status TEXT,
            expire_at INT, created_at INT)""")
        conn.executemany(
            "INSERT INTO orders (order_no, user_id, merchant_id, status, expire_at, created_at) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            [(f"NO{i:07d}", i % 1000, i % 50, ["pending", "paid", "done"][i % 3],
              1700000000 + i % 3600, 1700000000 + i) for i in range(50000)])

        conn.executescript("""
            CREATE INDEX idx_user_time    ON orders (user_id, created_at);
            CREATE INDEX idx_mch_status   ON orders (merchant_id, status, created_at);
            CREATE INDEX idx_status_exp   ON orders (status, expire_at);
        """)

        queries = {
            "订单号详情": "SELECT * FROM orders WHERE order_no = 'NO0000123'",
            "用户近期订单": "SELECT * FROM orders WHERE user_id = 7 "
                            "ORDER BY created_at DESC LIMIT 20",
            "商家状态统计": "SELECT count(*) FROM orders "
                            "WHERE merchant_id = 3 AND status = 'paid'",
            "超时扫描": "SELECT id FROM orders WHERE status = 'pending' "
                        "AND expire_at < 1700000100",
        }
        for name, sql in queries.items():
            plan = conn.execute("EXPLAIN QUERY PLAN " + sql).fetchall()
            uses_index = any("USING INDEX" in r[3] or "USING" in r[3] for r in plan)
            print(f"{name}: 走索引={uses_index}  {[r[3] for r in plan]}")
