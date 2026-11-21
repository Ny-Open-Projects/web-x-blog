---
title: [Q2479] 随机抽样的系统替代: TABLESAMPLE 概念与蓄水池
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2479 · 随机抽样的系统替代: TABLESAMPLE 概念与蓄水池

> 难度:★★★☆ | 标签:SQL, 抽样

**问**:PostgreSQL 的 TABLESAMPLE 是什么?SQLite/MySQL 没有它怎么做随机抽样?

**答**:TABLESAMPLE 有两种方言:SYSTEM 按"页/块"抽取,块内全要,快但样本天然成簇有偏;BERNOULLI 逐行独立按概率抽,无偏但行数有波动。没有该语法的库,替代按场景选:行号连续的表用"随机起点区间"(快但有偏);流式读取用蓄水池抽样(单趟、恰好 k 行、数学等概率),这是无偏场景的标准答案;要反复在线随机就预生成随机键列加索引。判断标准:抽样语义要"无偏"就上蓄水池,要"够快够随机"就接受有偏的起点法,ORDER BY random() 全表排序则永远不该出现在大表上。

```python
# file: code/04_数据库与缓存/q2479_tablesample_concept.py
"""随机抽样的系统替代: TABLESAMPLE 概念与无偏的蓄水池"""
import random

random.seed(42)
N = 10000
rows = list(range(1, N + 1))            # 有序生成的行, id 即业务顺序

# 概念复刻一: TABLESAMPLE SYSTEM —— 按页抽取, 页内全要, 天然成簇有偏
PAGE = 100
pages = [rows[i:i + PAGE] for i in range(0, N, PAGE)]
picked_pages = random.sample(pages, 3)
system_sample = [r for p in picked_pages for r in p]
print("SYSTEM 风格: 抽 3 页得 %d 行, 样本 id 区间 %d~%d (挤在 3 个局部, 有偏)"
      % (len(system_sample), min(system_sample), max(system_sample)))

# 概念复刻二: TABLESAMPLE BERNOULLI —— 逐行独立以 p 抽取, 无偏但数量波动
p = 0.001
bern = [r for r in rows if random.random() < p]
print("BERNOULLI 风格: p=%.3f 抽得 %d 行 (期望 10, 实际有波动), id 分布: %s"
      % (p, len(bern), bern[:12]))

# 工程首选: 蓄水池抽样 —— 单趟流式, 恰好 k 行且等概率
def reservoir(stream, k):
    pool = []
    for i, item in enumerate(stream, 1):
        if i <= k:
            pool.append(item)
        else:
            j = random.randint(1, i)
            if j <= k:
                pool[j - 1] = item
    return pool

k = 10
pool = reservoir(iter(rows), k)
print("蓄水池: 恰好 %d 行: %s, id 跨越全表说明无位置偏倚" % (k, sorted(pool)))
assert len(pool) == k

# 等概率验证: 每行入选率应同为 k/N
hits = {}
for trial in range(300):
    random.seed(trial)
    for x in reservoir(iter(rows), k):
        hits[x] = hits.get(x, 0) + 1
rates = sorted(hits.values())
print("300 次重复实验: 被抽中的不同行数=%d, 单行入选次数 min=%d max=%d (接近则等概率)"
      % (len(hits), rates[0], rates[-1]))
print("结论: TABLESAMPLE 是方言且 SYSTEM 有偏; 要无偏抽样, 蓄水池是流式场景的标准答案")
```

**追问**:
- 蓄水池为什么等概率?—— 第 i 行以 k/i 概率入选,替换者以 k/i 概率被换出,归纳可得最终每行入选率均为 k/N。
- 抽样要"按分组各抽 k 条"怎么办?—— 按分组键分桶后对每桶独立蓄水池,或窗口函数 row_number 配合随机排序键。

---
