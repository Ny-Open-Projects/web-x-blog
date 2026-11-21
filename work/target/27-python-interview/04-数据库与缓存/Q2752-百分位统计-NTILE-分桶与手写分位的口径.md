---
title: [Q2752] 百分位统计: NTILE 分桶与手写分位的口径
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2752 · 百分位统计: NTILE 分桶与手写分位的口径

> 难度:★★☆☆ | 标签:SQL, 窗口函数

**问**:要给接口耗时出 P50/P95/P99,SQL 里怎么算才口径清楚?

**答**:两条路。窗口函数路:NTILE(4) OVER (ORDER BY ms) 把样本等频切成四份,每份的 min/max 就是四分位区间,直观但只给固定分位;PERCENT_RANK 配合取行可以精确到任意分位。手写路:把排序后的列拉出来,按位置取第 p% 个元素,逻辑透明且好做断言。关键是口径要钉死:P95 是"95% 的请求不慢于它",样本去不去重、四舍五入到哪一位、异常样本剔不剔除,都要在看板注释里写明,否则两个系统算出的 P99 差一截说不清谁错。另外长尾样本对 P99 极敏感,一个卡顿批次就能把它抬高,分位监控要和均值一起看。

```python
# file: code/04_数据库与缓存/q2752_ntile_percentile.py
"""百分位统计: NTILE 分桶与手写分位的口径对齐"""
import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE resp (id INTEGER PRIMARY KEY, ms REAL)")
c.executemany("INSERT INTO resp VALUES(?,?)",
              [(i, 10 + (i * 13) % 90 + ((i % 50) == 0) * 400) for i in range(1, 2001)])

rows = c.execute("""
  SELECT bucket, COUNT(*), MIN(ms), MAX(ms) FROM (
    SELECT ms, NTILE(4) OVER (ORDER BY ms) AS bucket FROM resp
  ) GROUP BY bucket ORDER BY bucket""").fetchall()
for b, n, lo, hi in rows:
    print("Q%d: %d 个样本, 区间 [%.0f, %.0f] ms" % (b, n, lo, hi))

allms = sorted(r[0] for r in c.execute("SELECT ms FROM resp"))
def pct(p):
    k = max(0, min(len(allms) - 1, int(round(p / 100.0 * (len(allms) - 1)))))
    return allms[k]
print("手写分位: P50=%.0f P95=%.0f P99=%.0f ms" % (pct(50), pct(95), pct(99)))
print("NTILE 顶桶的上界 %.0f ms 是 Q3 不是 P95, 口径不同不能互换" % rows[-1][3])
```

**追问**:
- NTILE 的桶能不等宽吗?—— 不能,NTILE 是等频切分,不等宽分桶要回到 CASE WHEN 条件聚合。
- 大表算分位太贵怎么办?—— 预聚合进小时表,或用近似算法(t-digest 类)在应用层维护可合并的草图。

---
