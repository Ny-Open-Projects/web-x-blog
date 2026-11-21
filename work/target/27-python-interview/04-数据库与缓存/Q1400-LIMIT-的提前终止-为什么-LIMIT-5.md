---
title: [Q1400] LIMIT 的提前终止: 为什么 LIMIT 5 快很多
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1400 · LIMIT 的提前终止: 为什么 LIMIT 5 快很多

> 难度:★★★☆ | 标签:SQL 调优, LIMIT

**问**:同样是排序,LIMIT 5 为什么能快一个量级?什么条件下提前终止会失效?

**答**:两个机制叠加:一是 top-N 优先队列让排序成本从 n·log(n) 降到 n·log(k);二是扫表本身可以提前终止——如果 ORDER BY 列有索引,LIMIT 5 意味着沿索引读 5 行就返回,扫描量与表大小无关。失效条件:排序方向与索引方向不一致(索引 ASC 查 DESC TOP 仍需反向,8.0 支持倒序索引扫描);排序键带表达式或函数;多表 JOIN 后排序,只能先连接出结果再排序,提前终止只作用于"没有中间加工"的单表路径。所以"ORDER BY id LIMIT n"这种 id 主键查询几乎是免费的,业务列表页应尽量把游标落在有序索引上。

```python
# file: code/04_数据库与缓存/q1400_limit_early_stop.py
"""LIMIT 与排序: 全排序 vs top-N 优先队列的比较次数"""
import heapq
import math
import random

random.seed(3)
n, k = 100000, 5
data = [random.random() for _ in range(n)]

def topn_comparisons():
    heap, cmp = [], 0
    for x in data:
        if len(heap) < k:
            heapq.heappush(heap, x)
            cmp += math.log2(len(heap))
        elif x > heap[0]:
            heapq.heapreplace(heap, x)
            cmp += 2 * math.log2(k)
    return cmp, sorted(heap, reverse=True)

c_full = n * math.log2(n)
c_top, top5 = topn_comparisons()
print(f"全排序: 约 {c_full:.0f} 次比较, 缓冲需容纳全部 n 行")
print(f"top-N 堆: 约 {c_top:.0f} 次比较, 缓冲只留 k={k} 行")
print("top5:", [round(x, 4) for x in top5])
```

**追问**:
- 为什么 ORDER BY 列加了索引但 EXPLAIN 还有 filesort?——常见原因是 SELECT 了不在索引里的列导致回表后重新排序,或排序方向与索引相反,补覆盖索引或倒序索引可解。
- 深翻页为什么还是慢?——LIMIT 1000000,20 仍要把前一百万行扫掉,提前终止只救头部页;深翻页改成游标条件 WHERE id > last_id LIMIT 20,扫描量与页深无关。
- 提前终止的底层机制?——有索引序时存储引擎流式返回,服务层计满 LIMIT 即终止扫描;没有索引序就先全量 filesort 再截断,这是快慢的分水岭。
- 生产陷阱?——列表接口支持按时间/价格/销量多口径排序,只有部分排序键有索引;没有索引支撑的排序入口限深页或下线,否则被翻页爬虫打穿。

---
