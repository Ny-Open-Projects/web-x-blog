---
title: [ALG-078] Vue3 diff 里最长递增子序列（LIS）用来决定"哪些节点不需要移动"。为什么 diff 要用 LIS？请手写 O(n log n) 版本？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-078：Vue3 diff 里最长递增子序列（LIS）用来决定"哪些节点不需要移动"。为什么 diff 要用 LIS？请手写 O(n log n) 版本？
**答**：新旧 children 复用后剩余节点要保持相对稳定：LIS 找出"下标保持递增（即不用动）的最长节点集"，其余节点才需要真实 DOM 移动，移动次数最少。Vue3 的 `getSequence` 返回的是"LIS 的下标数组"：贪心 + 二分维护当前最小尾部，`p` 数组记录前驱用于回溯出真正的子序列（直接取 res 会是"长度对但元素不对"的序列）。特殊值 0 表示新增节点，跳过。时间 O(n log n)，空间 O(n)。

```javascript
function getSequence(arr) { // 返回最长递增子序列的下标数组
  const res = [0];         // 存下标，贪心保证尾部最小
  const p = new Array(arr.length);
  for (let i = 0; i < arr.length; i++) {
    const val = arr[i];
    if (val === 0) continue;           // Vue3 中 0 表示新增节点
    const tail = arr[res[res.length - 1]];
    if (tail < val) { p[i] = res[res.length - 1]; res.push(i); }
    else {                              // 二分找第一个 >= val 的位置替换
      let lo = 0, hi = res.length - 1;
      while (lo < hi) {
        const mid = (lo + hi) >> 1;
        if (arr[res[mid]] < val) lo = mid + 1; else hi = mid;
      }
      if (arr[res[lo]] > val && lo > 0) p[i] = res[lo - 1];
      if (arr[res[lo]] > val) res[lo] = i;
    }
  }
  let len = res.length, last = res[len - 1];
  while (last !== undefined) { res[--len] = last; last = p[last]; } // 回溯前驱
  return res;
}
```
