"""对比 ORDER BY 是否命中索引: TEMP B-TREE 出现与消失"""
import sqlite3

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.execute("CREATE TABLE t (id INTEGER PRIMARY KEY, a INT, b INT)")
        conn.executemany("INSERT INTO t (a, b) VALUES (?, ?)",
                         [(i % 50, i % 7) for i in range(20000)])

        q1 = "SELECT * FROM t ORDER BY a, b"
        q2 = "SELECT * FROM t WHERE a = 3 ORDER BY b"

        conn.execute("CREATE INDEX idx_ab ON t (a, b)")
        for q in (q1, q2):
            print(q, "->", [r[3] for r in
                  conn.execute("EXPLAIN QUERY PLAN " + q).fetchall()])

        conn.execute("DROP INDEX idx_ab")
        conn.execute("CREATE INDEX idx_a ON t (a)")
        print("仅 a 索引时:", [r[3] for r in
              conn.execute("EXPLAIN QUERY PLAN " + q2).fetchall()])
