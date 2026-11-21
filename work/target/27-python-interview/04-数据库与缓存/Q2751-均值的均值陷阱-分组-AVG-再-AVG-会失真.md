---
title: [Q2751] 均值的均值陷阱: 分组 AVG 再 AVG 会失真
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2751 · 均值的均值陷阱: 分组 AVG 再 AVG 会失真

> 难度:★★☆☆ | 标签:SQL, 聚合

**问**:子查询按天算平均时长,外层再对天平均,这样算月均对吗?

**答**:不对,均值的均值只在各组分母相等时才等于全局均值。分组 AVG 丢掉了每组的行数,外层再 AVG 时每天权重相同,而真正的全局均值应该按行数加权——数据倾斜时偏差可以到几倍。修法有三:直接对明细一层 AVG;分组后带 COUNT 出来,外层用 SUM(avg*cnt)/SUM(cnt) 加权;或用 SUM(dur)/COUNT(dur) 的总量比,在可加性上最干净。同类陷阱还有"占比的占比"和"中位数的中位数"。凡是两层聚合嵌套,先问一句:内层丢掉的分布信息,外层是否真的不需要。

```python
# file: code/04_数据库与缓存/q2751_avg_of_avg.py
"""均值的均值不是均值: 分组 AVG 直接再 AVG 的偏差与两种修法"""
import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE session (id INTEGER PRIMARY KEY, grp TEXT, dur REAL)")
rows = []
i = 0
for g, ds in [("a", [1, 2, 3]), ("b", [10.0] * 10)]:
    for d in ds:
        i += 1
        rows.append((i, g, d))
c.executemany("INSERT INTO session VALUES(?,?,?)", rows)

wrong = c.execute("""SELECT AVG(avg_dur) FROM
    (SELECT grp, AVG(dur) AS avg_dur FROM session GROUP BY grp)""").fetchone()[0]
right = c.execute("SELECT AVG(dur) FROM session").fetchone()[0]
weighted = c.execute("""SELECT SUM(cnt * avg_dur) / SUM(cnt) FROM
    (SELECT grp, AVG(dur) AS avg_dur, COUNT(*) AS cnt FROM session GROUP BY grp)""").fetchone()[0]
print("均值的均值 %.2f | 全局均值 %.2f | 按行数加权 %.2f" % (wrong, right, weighted))
print("a 组 3 行 b 组 10 行, 简单平均把 a 的权重抬到了一半, 偏差 %.0f%%"
      % (abs(wrong - right) / right * 100))
```

**追问**:
- 什么时候均值的均值恰好等于全局均值?—— 各组的样本数完全相等时,此时权重天然一致。
- 中位数能分层算吗?—— 不能,中位数不可加,分层必须保留明细或在层间传递分位结构,直接平均会错。

---
