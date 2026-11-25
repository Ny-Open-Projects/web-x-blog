---
title: [ALG-394] 手写逆序对计数（BIT）：拖拽排序代价
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-394：手写逆序对计数（BIT）：拖拽排序代价

**答**：
- 题目：用户把推荐列表从初始序拖成目标序，评估「改动代价」= 目标序相对初始序的逆序对数。经典 BIT 求逆序对。
- 思路：从右往左扫，BIT 统计「已出现的比当前小的个数」——即当前元素的逆序贡献；或从左往右查「已出现中比当前大的个数」。值域大时先离散化。
- 评分点：扫描方向与统计语义；离散化（大值域）；归并排序解法的对比。

```javascript
function inversionCount(arr) {
  const sorted = [...new Set(arr)].sort((a, b) => a - b);
  const rank = new Map(sorted.map((v, i) => [v + 1, i + 1]));   // 离散化
  const bit = new BIT(sorted.length);
  let inv = 0;
  for (let i = arr.length - 1; i >= 0; i--) {               // 从右往左
    const r = rank.get(arr[i]);
    inv += bit.sum(r - 1);                                  // 右侧已出现且比当前小的个数
    bit.add(r, 1);
  }
  return inv;                                               // O(n log n)
}
// 归并排序解法同为 O(n log n)：merge 时统计右侧提前量——面试可两解对比
```
