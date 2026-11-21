"""对比有无索引时同一查询的 EXPLAIN QUERY PLAN 访问方式"""
import sqlite3

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.execute("CREATE TABLE orders (id INTEGER PRIMARY KEY, user_id INT, amount REAL)")
        conn.executemany("INSERT INTO orders (user_id, amount) VALUES (?, ?)",
                         [(i % 1000, i * 1.0) for i in range(10000)])

        plan1 = conn.execute(
            "EXPLAIN QUERY PLAN SELECT * FROM orders WHERE user_id = 42").fetchall()
        print("无索引:", plan1)

        conn.execute("CREATE INDEX idx_user ON orders (user_id)")
        plan2 = conn.execute(
            "EXPLAIN QUERY PLAN SELECT * FROM orders WHERE user_id = 42").fetchall()
        print("有索引:", plan2)
