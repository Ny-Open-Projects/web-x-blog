"""演示 sqlite TEXT 亲和性下的类型转换行为, 并说明 MySQL 的相反规则"""
import sqlite3

if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        conn.execute("CREATE TABLE t (phone TEXT)")
        conn.executemany("INSERT INTO t VALUES (?)",
                         [("13800000001",), ("13800000002",), ("bad_data",)])
        conn.execute("CREATE INDEX idx_phone ON t (phone)")

        plan_int = conn.execute("EXPLAIN QUERY PLAN SELECT * FROM t WHERE phone = ?",
                                (13800000001,)).fetchall()
        plan_str = conn.execute("EXPLAIN QUERY PLAN SELECT * FROM t WHERE phone = ?",
                                ("13800000001",)).fetchall()
        print("整型参数:", [r[3] for r in plan_int])
        print("字符串参数:", [r[3] for r in plan_str])
        print("MySQL 对照: TEXT 列 + 数字常量 -> 列转数字, 索引失效全表扫描")
        print("稳妥做法: 查询参数类型与列定义一致", conn.execute(
            "SELECT * FROM t WHERE phone = ?", ("13800000002",)).fetchall())
