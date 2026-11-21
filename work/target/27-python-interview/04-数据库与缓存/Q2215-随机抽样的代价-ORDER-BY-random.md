---
title: [Q2215] 随机抽样的代价: ORDER BY random() 是全表排序
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2215 · 随机抽样的代价: ORDER BY random() 是全表排序

> 难度:★★★☆ | 标签:SQL, 抽样

**问**:SELECT ... ORDER BY random() LIMIT 5 为什么慢?正确的抽样姿势有哪些?

**答**:ORDER BY random() 给每一行生成随机键后必须全量排序,代价 O(N log N),LIMIT 再小也省不掉——优化器无法提前终止,因为最小的五个随机键可能在任何地方。替代方案按场景选:行号连续表用"随机起点区间"(WHERE id >= 随机值 ORDER BY id LIMIT n),快但样本是连续段、有偏;应用层蓄水池抽样(单趟流式读取、O(N) 时间 O(k) 空间、数学上等概率),适合导出与离线分析;真要高质量在线随机,可以维护随机键列加索引,或预生成洗牌序号。判断标准:抽样语义要"无偏"就上蓄水池,要"够快够随机"就接受有偏的起点法,别用全表排序硬扛。

```python
# file: code/04_数据库与缓存/q2215_random_sample.py
"""随机抽样的代价: ORDER BY random() 全表排序 vs 蓄水池抽样"""
import random
import sqlite3
import time

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE t(id INTEGER PRIMARY KEY, v TEXT)")
c.executemany("INSERT INTO t VALUES(?,?)", [(i, "v%d" % i) for i in range(1, 50001)])

plan = " | ".join(r[3] for r in
                  c.execute("EXPLAIN QUERY PLAN SELECT id FROM t ORDER BY random() LIMIT 5"))
print("ORDER BY random() 计划:", plan)

t0 = time.perf_counter()
rows = c.execute("SELECT id FROM t ORDER BY random() LIMIT 5").fetchall()
print("全表排序取 5 条   : %6.1f ms, 样本 %s" % ((time.perf_counter() - t0) * 1000, [r[0] for r in rows]))

t0 = time.perf_counter()
rows2 = c.execute("SELECT id FROM t WHERE id >= (abs(random()) % 49996) + 1 "
                  "ORDER BY id LIMIT 5").fetchall()
print("随机起点区间      : %6.2f ms, 样本 %s 有偏" % ((time.perf_counter() - t0) * 1000, [r[0] for r in rows2]))

t0 = time.perf_counter()
sample, n = [], 0
for (rid,) in c.execute("SELECT id FROM t"):
    n += 1
    if len(sample) < 5:
        sample.append(rid)
    else:
        j = random.randrange(n)
        if j < 5:
            sample[j] = rid
print("蓄水池抽样 O N 一趟: %6.1f ms, 样本 %s 等概率" % ((time.perf_counter() - t0) * 1000, sorted(sample)))
```

**追问**:
- 蓄水池为什么等概率?—— 第 i 行被保留概率 5/i,与后续替换复合后每行恰为 5/N,可归纳证明。
- 表很大且有洞时起点法怎么办?—— 找不到足够行就向后补抽多次,或改用 rowid 分桶后桶内随机,接受轻微不均。

---
