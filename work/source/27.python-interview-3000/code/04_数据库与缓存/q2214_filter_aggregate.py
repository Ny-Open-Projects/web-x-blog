"""FILTER 条件聚合: 一趟扫描出多口径统计"""
import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE pay(id INTEGER PRIMARY KEY, channel TEXT, status TEXT, amt REAL)")
c.executemany("INSERT INTO pay VALUES(?,?,?,?)",
              [(1, "wx", "ok", 100.0), (2, "wx", "fail", 50.0), (3, "ali", "ok", 200.0),
               (4, "ali", "refund", 30.0), (5, "wx", "ok", 70.0), (6, "ali", "ok", 120.0)])

sql_filter = """
SELECT channel,
       count(*) FILTER (WHERE status = 'ok')     AS ok_cnt,
       sum(amt) FILTER (WHERE status = 'ok')     AS ok_amt,
       count(*) FILTER (WHERE status = 'fail')   AS fail_cnt,
       count(*) FILTER (WHERE status = 'refund') AS refund_cnt
FROM pay GROUP BY channel
"""
print("FILTER 写法   channel  ok笔数  ok金额  fail  refund")
for r in c.execute(sql_filter):
    print("   %-5s %6d %8.1f %5d %6d" % r)

sql_case = """
SELECT channel,
       sum(CASE WHEN status='ok' THEN 1 ELSE 0 END),
       sum(CASE WHEN status='ok' THEN amt ELSE 0 END),
       sum(CASE WHEN status='fail' THEN 1 ELSE 0 END),
       sum(CASE WHEN status='refund' THEN 1 ELSE 0 END)
FROM pay GROUP BY channel
"""
print("CASE WHEN 等价:", [tuple(r) for r in c.execute(sql_case)])
print("两种写法同结果, FILTER 条件只写一遍, 口径不易漂移, MySQL 用 CASE WHEN 兜底")
