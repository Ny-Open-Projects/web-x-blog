---
title: [ALG-416] 手写 BIT 实现区间移动代价最小化：拖拽最优次数
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-416：手写 BIT 实现区间移动代价最小化：拖拽最优次数

**答**：
- 题目：列表从初始序调整到目标序，每次操作可把一个元素移到任意位置，求最少操作次数。结论：答案 = n - 最长「相对顺序保持」子序列（LIS 在目标序下标上的 LIS）。
- 思路：把初始序元素映射到目标序下标，求 LIS——不在 LIS 里的元素都要移动。LIS 用「贪心 + 二分」O(n log n)（ tails 数组）。
- 评分点：转化为 LIS 的论证（保持相对顺序的元素不需动）；贪心+二分 LIS； tails 数组含义。

```javascript
function minMoves(initial, target) {                       // 最少拖拽次数
  const posInTarget = new Map(target.map((v, i) => [v, i]));
  const seq = initial.map(v => posInTarget.get(v)).filter(x => x != null);   // 映射到目标下标
  const tails = [];                                         // LIS：tails[i] = 长度 i+1 的最小尾
  for (const x of seq) {
    let lo = 0, hi = tails.length;
    while (lo < hi) { const m = (lo + hi) >> 1;
      tails[m] < x ? lo = m + 1 : hi = m; }
    tails[lo] = x;                                          // 贪心替换
  }
  return initial.length - tails.length;                     // n - LIS
}
// 举例：initial [a,b,c,d] → target [c,a,d,b]，映射 [1,3,0,2]，LIS=[1,3]或[0,2] 长 2
// 答案 = 4 - 2 = 2 次移动
```
