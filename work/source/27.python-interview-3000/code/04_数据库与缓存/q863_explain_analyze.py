"""SQLite: QUERY PLAN 看计划, ANALYZE 维护统计信息; MySQL/PG 才有 EXPLAIN ANALYZE"""
import sqlite3

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.execute("CREATE TABLE t (id INTEGER PRIMARY KEY, v INT)")
        conn.executemany("INSERT INTO t (v) VALUES (?)",
                         [(i % 10,) for i in range(5000)])
        conn.execute("CREATE INDEX idx_v ON t (v)")

        print("计划:", [r[3] for r in conn.execute(
            "EXPLAIN QUERY PLAN SELECT * FROM t WHERE v = 3").fetchall()])
        print("MySQL8/PG: EXPLAIN ANALYZE 给出 估算行 vs 实际行 vs 实际耗时")
        print("SQLite 替代: EXPLAIN 字节码计数 + ANALYZE 统计信息交叉验证")

        conn.execute("ANALYZE")
        print("ANALYZE 后统计:", conn.execute(
            "SELECT tbl, idx, stat FROM sqlite_stat1").fetchall())
