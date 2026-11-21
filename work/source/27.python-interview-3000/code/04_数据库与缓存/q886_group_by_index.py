"""对比无索引与有索引时 GROUP BY 的执行计划"""
import sqlite3

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.execute("CREATE TABLE t (id INTEGER PRIMARY KEY, g INT, v REAL)")
        conn.executemany("INSERT INTO t (g, v) VALUES (?, ?)",
                         [(i % 100, i * 1.0) for i in range(50000)])
        sql = "SELECT g, SUM(v) FROM t GROUP BY g"

        print("无索引:", [r[3] for r in
              conn.execute("EXPLAIN QUERY PLAN " + sql).fetchall()])
        conn.execute("CREATE INDEX idx_g ON t (g)")
        print("有索引:", [r[3] for r in
              conn.execute("EXPLAIN QUERY PLAN " + sql).fetchall()])
        print("MySQL 对照: Extra 出现 Using index for group-by 即松散扫描")
