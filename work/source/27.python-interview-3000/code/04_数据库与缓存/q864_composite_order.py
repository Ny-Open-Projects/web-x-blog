"""对比两种联合索引下同一查询的计划: 索引列序决定能否消除排序"""
import sqlite3

SQL = "SELECT id FROM t WHERE a = 1 AND b > 50 ORDER BY c LIMIT 10"

def plan(conn, label):
    rows = conn.execute("EXPLAIN QUERY PLAN " + SQL).fetchall()
    print(label, [r[3] for r in rows])

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.execute("CREATE TABLE t (id INTEGER PRIMARY KEY, a INT, b INT, c INT)")
        conn.executemany("INSERT INTO t (a, b, c) VALUES (?, ?, ?)",
                         [(i % 5, i % 100, i) for i in range(20000)])

        conn.execute("CREATE INDEX idx_a_b_c ON t (a, b, c)")
        plan(conn, "索引 a,b,c 范围列在前:")

        conn.execute("DROP INDEX idx_a_b_c")
        conn.execute("CREATE INDEX idx_a_c ON t (a, c)")
        plan(conn, "索引 a,c 排序列接等值列:")
