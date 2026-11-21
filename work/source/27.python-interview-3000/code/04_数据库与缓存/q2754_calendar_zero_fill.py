"""日历表补零: 统计区间里没有数据的日子也要出现"""
import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()
# 递归 CTE 生成 6 月 1 日到 10 日的连续日历, 物化成表
c.execute("CREATE TABLE calendar (d TEXT PRIMARY KEY)")
c.execute("""INSERT INTO calendar
  WITH RECURSIVE cal(d) AS (
    SELECT date('2026-06-01')
    UNION ALL SELECT date(d, '+1 day') FROM cal WHERE d < date('2026-06-10')
  )
  SELECT d FROM cal""")
c.execute("CREATE TABLE pay (id INTEGER PRIMARY KEY, day TEXT, amt REAL)")
c.executemany("INSERT INTO pay(day, amt) VALUES(?,?)",
              [("2026-06-0%d" % d, d * 100) for d in (1, 2, 4, 7)])

rows = c.execute("""SELECT cal.d, IFNULL(SUM(p.amt), 0) AS total
  FROM calendar cal LEFT JOIN pay p ON p.day = cal.d
  GROUP BY cal.d ORDER BY cal.d""").fetchall()
for d, s in rows:
    print("%s  %6.0f" % (d, s))
assert len(rows) == 10 and dict(rows)["2026-06-03"] == 0
print("10 天一天不缺, 无数据的 3 号 5 号 6 号 8 号 9 号 10 号补零")
