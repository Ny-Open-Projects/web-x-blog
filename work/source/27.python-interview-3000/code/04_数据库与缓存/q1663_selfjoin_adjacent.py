"""自连接应用: 相邻行比较做环比, 与窗口函数 LAG 对照"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE revenue(month INTEGER PRIMARY KEY, amount REAL)")
conn.executemany("INSERT INTO revenue VALUES(?,?)",
                 [(202601, 100.0), (202602, 120.0), (202603, 90.0),
                  (202604, 110.0), (202605, 135.0)])

# 自连接: 同一张表起两个别名, 让"本月"通过 join 条件匹配到"上月"
sql = """
SELECT a.month AS cur_month, a.amount AS cur_amt, b.amount AS prev_amt,
       ROUND((a.amount - b.amount) / b.amount * 100, 1) AS pct
FROM revenue a
JOIN revenue b ON a.month = b.month + 1
ORDER BY a.month
"""
print("自连接环比:")
for m, cur, prev, pct in conn.execute(sql):
    print(f"  {m}: {cur:.0f} (上月 {prev:.0f}) 环比 {pct:+.1f}%")

# INNER JOIN 会丢掉没有上月的首月, LEFT JOIN 补齐
print("LEFT JOIN 保留首月:", conn.execute(
    "SELECT a.month, a.amount, b.amount FROM revenue a "
    "LEFT JOIN revenue b ON a.month = b.month + 1 ORDER BY a.month LIMIT 1").fetchone())

# LAG 是现代等价写法: 只扫一遍, 且不依赖键值的连续性
sql_lag = """SELECT month, amount, LAG(amount) OVER (ORDER BY month) AS prev_amt
             FROM revenue ORDER BY month"""
print("LAG 窗口版:", conn.execute(sql_lag).fetchall()[:3])
print("注意: a.month = b.month + 1 这种匹配依赖键值连续, 跨年 202612 到 202701 会漏配;")
print("      键不连续时先按 ROW_NUMBER 生成行号再自连接, 或直接用 LAG")
