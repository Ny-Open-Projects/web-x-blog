"""演示统计信息对估算的作用: ANALYZE 前后 sqlite_stat1 的变化"""
import sqlite3

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.execute("CREATE TABLE t (id INTEGER PRIMARY KEY, status TEXT)")
        conn.executemany("INSERT INTO t (status) VALUES (?)",
                         [(v,) for v in ["done"] * 9900 + ["pending"] * 100])
        conn.execute("CREATE INDEX idx_status ON t (status)")

        print("ANALYZE 前统计信息表:",
              bool(conn.execute(
                  "SELECT count(*) FROM sqlite_master "
                  "WHERE name='sqlite_stat1'").fetchone()[0]))
        conn.execute("ANALYZE")
        for row in conn.execute("SELECT tbl, idx, stat FROM sqlite_stat1"):
            print("统计:", row, "含义: 表行数 索引平均每个键值对应行数")

        # 手工直方图思路: 按值分桶存频数, 应用层据此提示倾斜
        hist = dict(conn.execute(
            "SELECT status, COUNT(*) FROM t GROUP BY status"))
        print("简易直方图:", hist)
