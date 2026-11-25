---
title: [ALG-382] 手写区间第 k 小（整体二分思想简化）：薪资分位查询
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-382：手写区间第 k 小（整体二分思想简化）：薪资分位查询

**答**：
- 题目：员工薪资序列，查「区间内第 k 小的薪资」且薪资有更新。完整解法是树套树/整体二分，面试可给「离线 + 值域线段树上二分」简化：若无更新，排序+归并树思想；有更新用值域线段树套位置集合。
- 思路：简化版——离散化值域，对每个值维护出现位置 BIT；二分答案值 mid，数「区间内 <= mid 的个数」是否 >= k。单次查询 O(log^2 n)。
- 评分点：二分答案转化（值域二分）；计数 BIT；完整解（树套树）的意识与复杂度。

```javascript
function kthInRange(arr, l, r, k) {                        // 离线简化：区间第 k 小
  const sorted = [...new Set(arr)].sort((a, b) => a - b);
  // countLE(mid) = 区间 [l,r] 内 <= mid 的个数——用归并树或对每查询直接扫（简化演示）
  const countLE = (mid) => {
    let c = 0;
    for (let i = l; i <= r; i++) if (arr[i] <= mid) c++;
    return c;
  };
  let lo = 0, hi = sorted.length - 1;
  while (lo < hi) {                                        // 值域二分答案
    const mid = (lo + hi) >> 1;
    if (countLE(sorted[mid]) >= k) hi = mid;               // 够 k 个：答案在左
    else lo = mid + 1;
  }
  return sorted[lo];
}
// 带更新的完整解：值域线段树节点存「该值域出现位置的数量」，外层二分内层查 O(log^2)
```
