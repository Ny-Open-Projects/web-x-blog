"""对比相关子查询与先聚合再 JOIN 两种写法的计划与结果一致性"""
import sqlite3
import time

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
        conn.execute("CREATE TABLE orders (id INTEGER PRIMARY KEY, user_id INT, amt REAL)")
        conn.executemany("INSERT INTO users (name) VALUES (?)",
                         [(f"u{i}",) for i in range(2000)])
        conn.executemany("INSERT INTO orders (user_id, amt) VALUES (?, ?)",
                         [(i % 2000, 10.0) for i in range(60000)])
        conn.execute("CREATE INDEX idx_o_user ON orders (user_id)")

        subq = ("SELECT u.name, (SELECT COUNT(*) FROM orders o "
                "WHERE o.user_id = u.id) AS cnt FROM users u")
        join = ("SELECT u.name, o.cnt FROM users u JOIN "
                "(SELECT user_id, COUNT(*) AS cnt FROM orders GROUP BY user_id) o "
                "ON o.user_id = u.id")

        t0 = time.perf_counter(); r1 = conn.execute(subq).fetchall(); t1 = time.perf_counter()
        r2 = conn.execute(join).fetchall(); t2 = time.perf_counter()
        print(f"相关子查询: {(t1-t0)*1000:.1f} ms, {len(r1)} 行")
        print(f"聚合后 JOIN: {(t2-t1)*1000:.1f} ms, {len(r2)} 行")
        print("结果一致:", sorted(r1) == sorted(r2))
