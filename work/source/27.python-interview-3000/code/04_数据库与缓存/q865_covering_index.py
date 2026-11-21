"""构造查询验证覆盖索引: 计划出现 USING COVERING INDEX 即免回表"""
import sqlite3

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.execute("""CREATE TABLE orders (
            id INTEGER PRIMARY KEY, user_id INT, status TEXT, created_at TEXT)""")
        conn.executemany("INSERT INTO orders (user_id, status, created_at) VALUES (?,?,?)",
                         [(i % 100, "paid" if i % 3 else "new", f"2024-{i % 12 + 1:02d}")
                          for i in range(20000)])

        sql = ("SELECT created_at FROM orders "
               "WHERE user_id = 7 AND status = 'paid' ORDER BY created_at")

        conn.execute("CREATE INDEX idx_user_status ON orders (user_id, status)")
        p1 = conn.execute("EXPLAIN QUERY PLAN " + sql).fetchall()
        print("普通索引:", [r[3] for r in p1])

        conn.execute("DROP INDEX idx_user_status")
        conn.execute("CREATE INDEX idx_cover ON orders (user_id, status, created_at)")
        p2 = conn.execute("EXPLAIN QUERY PLAN " + sql).fetchall()
        print("覆盖索引:", [r[3] for r in p2])
