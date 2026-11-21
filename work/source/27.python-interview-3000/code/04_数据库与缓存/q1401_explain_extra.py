"""执行计划附加信号: sqlite EQP 输出与 MySQL Extra 列对照"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE t(id INTEGER PRIMARY KEY, a INTEGER, b TEXT)")
conn.execute("CREATE INDEX idx_a ON t(a)")
conn.executemany("INSERT INTO t VALUES(?,?,?)",
                 [(i, i % 50, "x" * 20) for i in range(5000)])

def show(sql, mysql_extra):
    print("SQL:", sql)
    for r in conn.execute("EXPLAIN QUERY PLAN " + sql):
        print("   sqlite:", r[3])
    print("   MySQL Extra 大致对应:", mysql_extra)
    print()

show("SELECT * FROM t WHERE a = 7", "Using index condition(可下推过滤)")
show("SELECT COUNT(*) FROM t WHERE a = 7", "Using index(覆盖索引 不回表)")
show("SELECT a, b FROM t WHERE b = 'x'", "Using where(无索引可用)")
show("SELECT DISTINCT a FROM t ORDER BY a DESC", "Using temporary + Using filesort 或索引免排序")
