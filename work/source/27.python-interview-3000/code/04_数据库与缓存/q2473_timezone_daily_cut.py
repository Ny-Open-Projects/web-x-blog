"""跨时区业务的日切统计: 同一时刻在不同时区属于不同的'今天'"""
import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()
# 统一存 UTC (unix 时间戳), 这是跨时区设计的地基
c.execute("CREATE TABLE orders (id INTEGER PRIMARY KEY, user_tz TEXT, paid_at INTEGER)")
rows = [
    # 2026-11-05 17:30 北京时间(UTC+8) = 09:30 UTC
    (1, "+8", 1793880600),
    # 2026-11-05 23:50 北京时间 = 15:50 UTC (北京是 5 号, UTC 也是 5 号)
    (2, "+8", 1793946600),
    # 2026-11-06 01:10 北京时间 = 2026-11-05 17:10 UTC (北京的 6 号, UTC 的 5 号!)
    (3, "+8", 1793992200),
]
c.executemany("INSERT INTO orders VALUES(?,?,?)", rows)

# 错误做法: 直接按 UTC 日期聚合
q_utc = "SELECT date(paid_at, 'unixepoch') d, COUNT(*) n FROM orders GROUP BY d ORDER BY d"
# 正确做法: 先按用户时区平移, 再切日
q_tz = ("SELECT date(paid_at, 'unixepoch', user_tz || ' hours') d, COUNT(*) n "
        "FROM orders GROUP BY d ORDER BY d")
print("按 UTC 切日:      ", dict(c.execute(q_utc).fetchall()))
print("按用户时区切日:   ", dict(c.execute(q_tz).fetchall()))

# 关键演示: 订单 3 在 UTC 里是 5 号, 在用户时区里是 6 号
row = c.execute("SELECT date(paid_at, 'unixepoch'), "
                "date(paid_at, 'unixepoch', user_tz || ' hours') "
                "FROM orders WHERE id=3").fetchone()
print("订单3: UTC 日期=%s, 用户时区日期=%s (运营日报必须用后者)" % row)
print("纪律: 存储永远 UTC, '哪一天'是展示层按业务时区裁剪的, 别把 GROUP BY 直接打在 UTC 上")
