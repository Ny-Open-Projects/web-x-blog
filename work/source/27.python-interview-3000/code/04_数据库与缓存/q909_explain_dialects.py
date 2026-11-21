"""打印 sqlite 计划并给出三大数据库计划读法对照表"""
import sqlite3

MAPPING = """
三大数据库计划速查:
  SQLite   SCAN t            ~ 全表扫描       | SEARCH t USING INDEX ~ 索引定位
  MySQL    type=ALL           ~ 全表扫描       | type=ref/range       ~ 索引访问  Extra: Using filesort
  PG       Seq Scan           ~ 全表扫描       | Index Scan           ~ 索引访问  Sort 节点表示显式排序
"""

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.execute("CREATE TABLE t (id INTEGER PRIMARY KEY, a INT, b TEXT)")
        conn.executemany("INSERT INTO t (a, b) VALUES (?, ?)",
                         [(i % 100, f"x{i}") for i in range(3000)])
        conn.execute("CREATE INDEX idx_a ON t (a)")

        for sql in ("SELECT * FROM t WHERE a = 5 ORDER BY b",
                    "SELECT * FROM t"):
            plan = conn.execute("EXPLAIN QUERY PLAN " + sql).fetchall()
            print(sql, "\n  ->", [r[3] for r in plan])
    print(MAPPING)
