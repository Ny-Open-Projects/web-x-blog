"""子查询物化: 相关子查询逐行重算, 非相关子查询一次计算语句内复用"""
import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE big(id INTEGER PRIMARY KEY, cat TEXT, amt REAL)")
c.executemany("INSERT INTO big VALUES(?,?,?)",
              [(i, "abc"[i % 3], float(i % 50)) for i in range(1, 3001)])
c.execute("CREATE TABLE small(id INTEGER PRIMARY KEY, cat TEXT)")
c.executemany("INSERT INTO small VALUES(?,?)", [(i, "abc"[i % 3]) for i in range(1, 6)])

print("相关子查询: 引用了外层列 s.cat, 计划里挂着 SCALAR SUBQUERY")
for r in c.execute("EXPLAIN QUERY PLAN "
                   "SELECT (SELECT max(amt) FROM big b WHERE b.cat = s.cat) FROM small s"):
    print("   ", r[3])

print("非相关标量子查询: 与外层无关, 只算一次")
for r in c.execute("EXPLAIN QUERY PLAN "
                   "SELECT * FROM big WHERE amt > (SELECT avg(amt) FROM big)"):
    print("   ", r[3])

print("WITH AS MATERIALIZED: 强制先算完进临时结构, 计划出现 MATERIALIZE")
for r in c.execute("EXPLAIN QUERY PLAN "
                   "WITH stat AS MATERIALIZED (SELECT cat, avg(amt) a FROM big GROUP BY cat) "
                   "SELECT * FROM stat WHERE a > 10"):
    print("   ", r[3])

print("默认 CTE: 被折叠成 CO-ROUTINE 边算边流")
for r in c.execute("EXPLAIN QUERY PLAN "
                   "WITH stat AS (SELECT cat, avg(amt) a FROM big GROUP BY cat) "
                   "SELECT * FROM stat WHERE a > 10"):
    print("   ", r[3])
