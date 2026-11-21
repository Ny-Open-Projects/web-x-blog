"""完整调优演示: 单列索引 + filesort 优化为三列联合索引直取"""
import sqlite3
import time

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.execute("""CREATE TABLE orders (id INTEGER PRIMARY KEY,
                        user_id INT, status TEXT, created_at INT)""")
        conn.executemany("INSERT INTO orders (user_id, status, created_at) VALUES (?,?,?)",
                         [(i % 200, "paid" if i % 4 else "new", i)
                          for i in range(200000)])
        conn.execute("CREATE INDEX idx_user ON orders (user_id)")

        sql = ("SELECT id, created_at FROM orders "
               "WHERE user_id = 7 AND status = 'paid' "
               "ORDER BY created_at DESC LIMIT 20")

        t0 = time.perf_counter()
        conn.execute(sql).fetchall()
        slow = (time.perf_counter() - t0) * 1000
        plan_slow = conn.execute("EXPLAIN QUERY PLAN " + sql).fetchall()

        conn.execute("DROP INDEX idx_user")
        conn.execute("CREATE INDEX idx_best ON orders (user_id, status, created_at)")
        t1 = time.perf_counter()
        conn.execute(sql).fetchall()
        fast = (time.perf_counter() - t1) * 1000
        plan_fast = conn.execute("EXPLAIN QUERY PLAN " + sql).fetchall()

        print("优化前计划:", [r[3] for r in plan_slow], f"{slow:.1f} ms")
        print("优化后计划:", [r[3] for r in plan_fast], f"{fast:.1f} ms")
