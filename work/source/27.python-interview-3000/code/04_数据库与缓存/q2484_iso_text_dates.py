"""文本存日期: ISO 8601 的字典序才等于时间序"""
import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE events (id INTEGER PRIMARY KEY, day TEXT NOT NULL)")
# 同一天的三种写法: 未补零的文本破坏了可比性
c.executemany("INSERT INTO events VALUES(?,?)",
              [(1, "2026-01-05"), (2, "2026-1-5"), (3, "2026-11-05"), (4, "2025-12-31")])

# 补零 ISO 文本: 字典序即时间序, 排序与范围都正确
q_sorted = "SELECT day FROM events WHERE length(day) = 10 ORDER BY day"
print("规范 ISO 文本排序:", [r[0] for r in c.execute(q_sorted)])
q_range = "SELECT day FROM events WHERE day >= '2026-01-01' AND day < '2026-06-01' AND length(day)=10"
print("规范 ISO 范围 [2026上半年]:", [r[0] for r in c.execute(q_range)])

# 未补零的写法把这一切砸了: '2026-1-5' 在字典序里小于 '2026-01-05' 却又是同一天
all_days = [r[0] for r in c.execute("SELECT day FROM events ORDER BY day")]
print("混入未补零后排序: %s  <- '2026-1-5' 乱入" % all_days)
missed = c.execute("SELECT COUNT(*) FROM events WHERE day >= '2026-01-01' AND day < '2026-06-01' "
                   "AND day NOT LIKE '____-__-__'").fetchone()[0]
print("未补零行被范围查询漏掉:", missed)

# 修复: 用 date() 归一化, 但注意 date() 包住的列会失去普通索引资格
fixed = c.execute("SELECT date(day) FROM events WHERE day = '2026-1-5'").fetchone()[0]
print("date() 归一化 '2026-1-5' ->", fixed)
c.execute("CREATE INDEX idx_day_norm ON events(date(day))")
plan = " | ".join(r[3] for r in c.execute(
    "EXPLAIN QUERY PLAN SELECT * FROM events WHERE date(day) = '2026-01-05'"))
print("归一化表达式的计划: %s" % plan)
print("结论: 文本日期只有在严格 YYYY-MM-DD 补零时才可比; 要么入库前统一格式, 要么付出表达式索引的代价")
