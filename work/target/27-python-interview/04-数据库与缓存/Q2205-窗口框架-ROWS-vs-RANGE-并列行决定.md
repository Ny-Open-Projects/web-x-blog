---
title: [Q2205] 窗口框架 ROWS vs RANGE: 并列行决定累计值
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2205 · 窗口框架 ROWS vs RANGE: 并列行决定累计值

> 难度:★★★☆ | 标签:SQL, 窗口函数

**问**:同样是累计求和,ROWS 与 RANGE 框架结果为什么不一样?什么场景必须用哪个?

**答**:ROWS 按物理行数取框,CURRENT ROW 就是当前这一行;RANGE 按排序列的值域取框,与当前行排序列相同的"并列行"(peers)会被整体纳入。所以有并列时,RANGE 的累计会把同一组一次性加进去,ROWS 则逐行推进——日累计报表里,同一订单日的多笔交易在 RANGE 下显示的是"当日合计",在 ROWS 下显示的是"滚动到本笔为止"。移动平均同理:ROWS 2 PRECEDING 是固定最近三行,RANGE 2 PRECEDING 是值域在 day-2 到 day 之间的所有行,窗口大小随数据密度变化。选型口诀:要"每行一个新值"用 ROWS,要"按业务分组边界"用 RANGE;用 RANGE 时必须想清楚排序列的值域语义,文本列上的数值偏移是无意义的。

```python
# file: code/04_数据库与缓存/q2205_window_frame.py
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
```

**追问**:
- 同一天内的累计想逐笔递增怎么办?—— ORDER BY day, id 加二级排序列消掉并列,ROWS 与 RANGE 就一致了,这是最常用的兜底手法。
- RANGE 的默认框架是什么?—— 不写框架时默认 RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW,所以"以为在逐行累计、其实并列行被合并"是高频事故。

---
