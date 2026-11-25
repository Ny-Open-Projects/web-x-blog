---
title: [ALG-404] 手写 BIT 动态 TopK 近似：热搜榜
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-404：手写 BIT 动态 TopK 近似：热搜榜

**答**：
- 题目：热搜词实时变热度，查「热度 Top10 词」。BIT 维护热度分桶（热度→词数），TopK = 从高到低扫桶累计取 k 个 + 桶内明细堆。
- 思路：两层数据：BIT[heat] = 该热度词数（支持 O(log) 统计某热度以上词数）；明细 Map<word, heat> + 每热度桶内 Set。TopK：二分找「热度阈值」使 ≥ 阈值词数 >= 10，再扫阈值附近桶明细。
- 评分点：BIT 计数 + 明细桶双层；TopK 的二分定位；全排序 O(n log n) 的规避。

```javascript
class HotSearchTopK {
  constructor(maxHeat = 100000) { this.max = maxHeat; this.bit = new BIT(maxHeat);
    this.buckets = new Map(); this.words = new Map(); }
  update(word, heat) {
    const old = this.words.get(word) ?? 0;
    if (old) { this.bit.add(old, -1); this.buckets.get(old)?.delete(word); }
    this.words.set(word, heat);
    (this.buckets.get(heat) ?? this.buckets.set(heat, new Set()).get(heat)).add(word);
    this.bit.add(heat, 1);
  }
  topK(k = 10) {                                            // 二分热度阈值
    let lo = 0, hi = this.max, threshold = 0;
    while (lo <= hi) {                                      // 找最小阈值使 ≥阈值 词数 <= k
      const mid = (lo + hi) >> 1;
      const cnt = this.bit.sum(this.max) - this.bit.sum(mid - 1);
      if (cnt >= k) { threshold = mid; lo = mid + 1; } else hi = mid - 1;
    }
    const out = [];
    for (let h = this.max; h >= threshold && out.length < k; h--)
      for (const w of this.buckets.get(h) ?? []) { out.push({ word: w, heat: h });
        if (out.length >= k) break; }
    return out;
  }
}
```
