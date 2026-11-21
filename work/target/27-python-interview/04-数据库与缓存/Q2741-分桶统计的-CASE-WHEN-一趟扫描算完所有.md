---
title: [Q2741] 分桶统计的 CASE WHEN: 一趟扫描算完所有桶
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2741 · 分桶统计的 CASE WHEN: 一趟扫描算完所有桶

> 难度:★★★☆ | 标签:SQL, 聚合

**问**:报表要按金额段输出订单分布,你写四条 COUNT 还是别的?分桶统计怎么做最省?

**答**:用条件聚合:一段 SQL 里为每个桶写一个 SUM(CASE WHEN 区间 THEN 1 ELSE 0 END),一次扫描同时算出全部分桶,代替 N 条范围 COUNT 的 N 次扫描。分桶的关键纪律是桶边界必须恰好切分值域、不重不漏,写完先用"各桶之和等于 COUNT 总数"做断言再上线。桶定义通常来自业务枚举,写死在 SQL 里没问题;若桶会动态变化,就改成先生成桶边界再拼 CASE,或用窗口函数 NTILE 做等频桶。相比 GROUP BY 截断列(如 amt/50),CASE WHEN 的桶宽可以不等距,这是它最常见的使用理由。

```python
# file: code/04_数据库与缓存/q2741_bucket_case_when.py
"""分桶统计: 一趟扫描用 CASE WHEN 算完所有桶, 对比多趟扫描的代价"""
import sqlite3
import time

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE orders (id INTEGER PRIMARY KEY, amt REAL)")
c.executemany("INSERT INTO orders(amt) VALUES(?)",
              [(round((i * 37) % 997 / 7.0, 2),) for i in range(1, 50001)])

one_pass = """
SELECT
  SUM(CASE WHEN amt < 20 THEN 1 ELSE 0 END)                AS bucket_0_20,
  SUM(CASE WHEN amt >= 20 AND amt < 50 THEN 1 ELSE 0 END)  AS bucket_20_50,
  SUM(CASE WHEN amt >= 50 AND amt < 100 THEN 1 ELSE 0 END) AS bucket_50_100,
  SUM(CASE WHEN amt >= 100 THEN 1 ELSE 0 END)              AS bucket_100_up,
  COUNT(*)                                                 AS total
FROM orders
"""
t0 = time.perf_counter()
b = c.execute(one_pass).fetchone()
t1 = (time.perf_counter() - t0) * 1000
print("一趟 CASE WHEN: 桶分布 %s, 合计 %d, 耗时 %.1f ms" % (tuple(b[:4]), b[4], t1))
assert sum(b[:4]) == b[4], "桶边界必须恰好切分值域, 不重不漏"

t0 = time.perf_counter()
multi = [c.execute("SELECT COUNT(*) FROM orders WHERE amt >= ? AND amt < ?",
                   (lo, hi)).fetchone()[0]
         for lo, hi in ((0, 20), (20, 50), (50, 100), (100, 1e9))]
t2 = (time.perf_counter() - t0) * 1000
print("四趟范围 COUNT: 结果 %s, 耗时 %.1f ms (每桶一次全表扫描)" % (tuple(multi), t2))
```

**追问**:
- SQLite 里还有更短的写法吗?—— 有,COUNT(*) FILTER (WHERE ...) 是条件聚合的方言写法,CASE WHEN 版本的可移植性更好。
- 等宽分桶还需要 CASE 吗?—— 不需要,GROUP BY 强制转整数列(如 CAST(amt/20 AS INT))即可,等宽场景更简洁。

---
