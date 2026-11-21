"""SQLite 日期函数实战: strftime 区间统计与补齐缺失日期"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE pay(id INTEGER PRIMARY KEY, ts TEXT, amount REAL)")
rows = []
for d in (1, 2, 4, 5, 7, 8):          # 故意缺 3 号与 6 号
    for h in range(3):
        rows.append((len(rows) + 1, "2026-11-%02d %02d:30:00" % (d, h), 10.0 + h))
conn.executemany("INSERT INTO pay VALUES(?,?,?)", rows)
conn.commit()

print("按天汇总:")
for r in conn.execute(
        "SELECT date(ts), COUNT(*), SUM(amount) FROM pay GROUP BY date(ts) ORDER BY 1"):
    print("  ", r)

# 报表要求连续日期: 递归 CTE 造日历再 LEFT JOIN 补零
print("补零后的连续日报:")
for r in conn.execute("""
WITH RECURSIVE cal(day) AS (
  SELECT '2026-11-01'
  UNION ALL SELECT date(day, '+1 day') FROM cal WHERE day < '2026-11-08'
)
SELECT cal.day, COALESCE(SUM(p.amount), 0)
FROM cal LEFT JOIN pay p ON date(p.ts) = cal.day
GROUP BY cal.day ORDER BY cal.day"""):
    print("  ", r)

print("常用函数: strftime('%Y-%m', ts) 按月;  julianday(ts) 算天数差;")
print("          date(ts, '+1 month') 做偏移;  修饰符 'localtime' 处理本地时区")
print("注意: 存储一律 UTC 文本或时间戳, 展示层才转时区; 周口径 strftime('%W') 要与业务对齐")
