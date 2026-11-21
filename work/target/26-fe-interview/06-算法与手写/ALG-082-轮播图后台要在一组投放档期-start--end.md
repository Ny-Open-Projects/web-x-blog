---
title: [ALG-082] 轮播图后台要在一组投放档期 `[start, end]` 里选出"互不冲突且数量最多"的档期（区间调度）。为什么按结束时间贪心是对的？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-082：轮播图后台要在一组投放档期 `[start, end]` 里选出"互不冲突且数量最多"的档期（区间调度）。为什么按结束时间贪心是对的？
**答**：按 end 升序排序后，每次选"结束最早且与已选不冲突"的区间：交换论证——任何最优解的第一个区间都可以换成结束最早的而不会更差，归纳可得贪心解最优。若按 start 贪会选到超长区间导致数量变少。时间 O(n log n)，空间 O(n)。

```javascript
function maxBanners(items) { // items: [{start, end}]
  const sorted = [...items].sort((a, b) => a.end - b.end); // 结束早者优先
  let count = 0, lastEnd = -Infinity;
  for (const { start, end } of sorted) {
    if (start >= lastEnd) {  // 与已选档期不冲突
      count++;
      lastEnd = end;
    }
  }
  return count;
}
```
