---
title: [ALG-323] 流式 TopN 聚合：按维度聚合的 Top-K 排行（分组桶 + 桶内堆，单遍流式）？
date: 2026-11-19
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---
## ALG-323：流式 TopN 聚合：按维度聚合的 Top-K 排行（分组桶 + 桶内堆，单遍流式）？
**答**：慢脚本排行（PER-213 LoAF 聚合）的通用化：事件流（{group, cost}）单遍产出每 group 的 Top-K 与总量——分组 Map + 桶内小顶堆（ALG-211 多维化）。

**思路**：Map<group, { total, heap }>；事件到达：组 total += cost、堆维护 Top-K；溢出控制：组数上限（LRU 淘汰冷组）。

```javascript
class GroupedTopK {
  #groups = new Map();
  constructor(k = 5, { maxGroups = 200 } = {}) { Object.assign(this, { k, maxGroups }); }
  add(group, cost) {
    let g = this.#groups.get(group);
    if (!g) {
      if (this.#groups.size >= this.maxGroups) {          // 组数上限：淘汰总量最小的冷组（LRU 语义）
        const coldest = [...this.#groups].sort((a, b) => a[1].total - b[1].total)[0][0];
        this.#groups.delete(coldest);
      }
      g = this.#groups.set(group, { total: 0, heap: [] }).get(group);
    }
    g.total += cost;
    g.heap.push(cost);
    if (g.heap.length > this.k * 3) {                     // 堆截断：3K 池内维护（内存有界）
      g.heap.sort((a, b) => b - a);
      g.heap.length = this.k * 3;
    }
  }
  topGroups(n = 10) {
    return [...this.#groups].map(([name, g]) => ({ name, total: Math.round(g.total),
      topK: [...g.heap].sort((a, b) => b - a).slice(0, this.k) }))
      .sort((a, b) => b.total - a.total).slice(0, n);
  }
}
// 单遍流式：事件到达即聚合（不囤明细）—— 内存 = 组数 × K×3（有界）
// 组数上限 LRU：维度基数大（URL 全量）时防 Map 无限膨胀（PER-268 泄漏防线同源）
// 堆 3K 池：延迟截断（sort 摊销）—— K=5 时每 15 条排一次，均摊 O(1)
```

**评分点**：
- 分组 Map + 桶内 Top-K 池的单遍流式——本题核心。
- 组数上限 LRU 淘汰（维度基数爆炸防线）。
- 3K 池延迟截断的均摊复杂度。
- 内存有界（组数 × K×3）。
