---
title: [ALG-068] CDN 节点按"轮换制"调度，日志里节点 id 数组是"原升序数组在某个点旋转后"的结果，要求 O(log n) 找出最小值（轮换起点）。如何对旋转数组二分？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-068：CDN 节点按"轮换制"调度，日志里节点 id 数组是"原升序数组在某个点旋转后"的结果，要求 O(log n) 找出最小值（轮换起点）。如何对旋转数组二分？
**答**：与右端点 `nums[hi]` 比较：`nums[mid] > nums[hi]` 说明最小值在 mid 右侧（断点在右）；`nums[mid] < nums[hi]` 说明在 mid 及左侧；相等（重复元素）时 `hi--` 安全收缩。注意"与右端点比"而不是与左端点比，否则无法区分"整体有序"与"断点在左"。时间 O(log n)（重复元素最坏 O(n)），空间 O(1)。

```javascript
function findMin(nums) {
  let lo = 0, hi = nums.length - 1;
  while (lo < hi) {
    const mid = (lo + hi) >> 1;
    if (nums[mid] > nums[hi]) lo = mid + 1; // 断点在右半
    else if (nums[mid] < nums[hi]) hi = mid;
    else hi--; // 相等时收缩，兼容重复值
  }
  return nums[lo];
}
```
