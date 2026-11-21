---
title: [Q1675] SQLite 日期函数与区间统计
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1675 · SQLite 日期函数与区间统计

> 难度:★★☆☆ | 标签:SQL, 日期

**问**:SQLite 里怎么做按天、按月的报表?缺数据的日期怎么补零?

**答**:SQLite 提供五个核心函数:date、time、datetime、julianday、strftime,配合修饰符做偏移与本地化,如 date(ts, '+1 day')、strftime('%Y-%m', ts) 按月分组。报表要连续日期时,数据里缺号会造成跳行,标准解法是递归 CTE 生成日历序列再 LEFT JOIN 业务表,空档用 COALESCE 补零。两个纪律:存储一律 UTC 或时间戳,展示层才转时区,修饰符 localtime 只在最后一步用;周口径的 strftime('%W') 是周序号而非业务周,口径要和需求方对齐。这些函数在 MySQL/PG 有对应物,迁移时注意格式符差异。

```python
# file: code/04_数据库与缓存/q1675_sqlite_dates.py
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
```

**追问**:
- ts 上有索引,对 ts 用函数还能走索引吗?——对列包函数通常破坏索引区间;按天分组可改成 ts >= day AND ts < day + 1 的范围条件,或落预生成列。
- 递归日历生成一年 365 行会慢吗?——不会,每层一次 date 计算毫秒级;固定区间还可以用 WITH RECURSIVE 加上限防失控。

---
