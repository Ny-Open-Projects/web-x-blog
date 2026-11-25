---
title: [ALG-405] 手写 BIT 多维偏序计数（三维简化）：多条件筛选计数
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-405：手写 BIT 多维偏序计数（三维简化）：多条件筛选计数

**答**：
- 题目：记录 (a, b, c) 三元组，查「a<=x 且 b<=y 且 c<=z 的记录数」。三维偏序 = CDQ 分治 + BIT 经典；面试给简化：离线按 a 排序，扫 a 时 BIT 维护 (b,c) 二维（b 一维 BIT + c 值列表不行——退化为按 b 排序后 c 的逆序计数）。
- 思路：CDQ 思想——按 a 归并分治，左半对右半的贡献 = b、c 的二维偏序（把右半查询转为「b<=y 且 c<=z」计数，对左半按 b 排序后用 BIT 维护 c）。
- 评分点：CDQ 分治框架；降维过程（3 维 → 2 维 → BIT）；复杂度 O(n log² n)。

```javascript
function partialOrder3D(points) {                          // 统计每点被多少点支配
  const sorted = [...points].sort((p, q) => p.a - q.a);     // 维度 1：排序
  const bit = new BIT(1e5);
  const ans = new Array(points.length);
  function cdq(lo, hi) {                                    // 维度 2/3：分治
    if (lo >= hi) return;
    const mid = (lo + hi) >> 1;
    cdq(lo, mid); cdq(mid + 1, hi);
    const left = sorted.slice(lo, mid + 1).sort((p, q) => p.b - q.b);
    const right = sorted.slice(mid + 1, hi + 1).sort((p, q) => p.b - q.b);
    let i = 0;
    for (const p of right) {                                // 左半贡献给右半
      while (i < left.length && left[i].b <= p.b) { bit.add(left[i].c, 1); i++; }
      ans[p.idx] += bit.sum(p.c);
    }
    for (let j = 0; j < i; j++) bit.add(left[j].c, -1);     // 清 BIT
  }
  sorted.forEach((p, i) => p.idx = i);
  cdq(0, sorted.length - 1);
  return ans;
}
```
