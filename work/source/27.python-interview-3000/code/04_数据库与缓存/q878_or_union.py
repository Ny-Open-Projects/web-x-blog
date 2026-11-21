"""OR 跨列条件拆 UNION ALL, 对比执行计划"""
import sqlite3

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.execute("CREATE TABLE t (id INTEGER PRIMARY KEY, a INT, b INT)")
        conn.executemany("INSERT INTO t (a, b) VALUES (?, ?)",
                         [(i % 100, i % 7) for i in range(50000)])
        conn.execute("CREATE INDEX idx_a ON t (a)")
        conn.execute("CREATE INDEX idx_b ON t (b)")

        or_sql = "SELECT * FROM t WHERE a = 1 OR b = 2"
        plan = conn.execute("EXPLAIN QUERY PLAN " + or_sql).fetchall()
        print("OR 写法:", [r[3] for r in plan])

        split_sql = ("SELECT * FROM t WHERE a = 1 UNION ALL "
                     "SELECT * FROM t WHERE b = 2 AND a <> 1")
        plan2 = conn.execute("EXPLAIN QUERY PLAN " + split_sql).fetchall()
        print("UNION ALL:", [r[3] for r in plan2])
        print("行数一致:", conn.execute(or_sql).fetchall().__len__(),
              conn.execute(split_sql).fetchall().__len__())
