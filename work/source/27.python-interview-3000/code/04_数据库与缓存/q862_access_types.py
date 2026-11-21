"""用 SQLite 展示 SCAN 与 SEARCH 两类访问路径, 对应 MySQL 的 ALL 与 ref"""
import sqlite3

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.execute("CREATE TABLE t (id INTEGER PRIMARY KEY, a INT, b TEXT)")
        conn.executemany("INSERT INTO t (a, b) VALUES (?, ?)",
                         [(i % 500, f"k{i}") for i in range(5000)])
        conn.execute("CREATE INDEX idx_a ON t (a)")

        for sql in ("SELECT * FROM t", "SELECT * FROM t WHERE a = 7"):
            plan = conn.execute("EXPLAIN QUERY PLAN " + sql).fetchall()
            print(sql, "->", [p[3] for p in plan])
        print("MySQL 对照: 前者 type=ALL, 后者 type=ref")
