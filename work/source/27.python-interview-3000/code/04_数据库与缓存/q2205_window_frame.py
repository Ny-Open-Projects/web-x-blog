"""窗口框架 ROWS vs RANGE: 并列行的处理决定累计值"""
import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE sales(day INTEGER, rep TEXT, amt REAL)")
rows = [(1, "A", 10.0), (1, "B", 20.0), (1, "C", 30.0),
        (2, "A", 40.0), (2, "B", 50.0), (3, "A", 60.0)]
c.executemany("INSERT INTO sales VALUES(?,?,?)", rows)

sql = """
SELECT day, rep, amt,
       SUM(amt) OVER (ORDER BY day ROWS  BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS rows_sum,
       SUM(amt) OVER (ORDER BY day RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS range_sum
FROM sales ORDER BY day, rep
"""
print("day rep  amt | ROWS累计  RANGE累计")
for day, rep, amt, rs, rg in c.execute(sql):
    print(" %d   %s  %4.0f |  %6.0f   %6.0f" % (day, rep, amt, rs, rg))

sql2 = """
SELECT day, rep,
       AVG(amt) OVER (ORDER BY day ROWS  BETWEEN 2 PRECEDING AND CURRENT ROW) AS rows_avg,
       AVG(amt) OVER (ORDER BY day RANGE BETWEEN 2 PRECEDING AND CURRENT ROW) AS range_avg
FROM sales ORDER BY day, rep
"""
print("移动平均: ROWS 固定最近三行, RANGE 取值域 day-2 到 day 的全部行")
for day, rep, ra, rg in c.execute(sql2):
    print(" day=%d rep=%s  rows_avg=%5.1f  range_avg=%5.1f" % (day, rep, ra, rg))
