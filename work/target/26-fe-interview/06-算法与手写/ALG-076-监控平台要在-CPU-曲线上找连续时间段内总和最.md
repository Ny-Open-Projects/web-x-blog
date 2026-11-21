---
title: [ALG-076] 监控平台要在 CPU 曲线上找"连续时间段内总和最大的区间"（最大子数组和），定位服务异常最严重的窗口。Kadane 算法如何一次遍历解决？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-076：监控平台要在 CPU 曲线上找"连续时间段内总和最大的区间"（最大子数组和），定位服务异常最严重的窗口。Kadane 算法如何一次遍历解决？
**答**：定义 `cur` 为"以当前元素结尾的最大子数组和"：`cur = max(cur + x, x)`——之前的累计是负收益就果断舍弃、从 x 重新开始；全局用 `max` 记录历史最优。时间 O(n)，空间 O(1)。

```javascript
function maxSubArray(nums) {
  let cur = 0, max = -Infinity;
  for (const x of nums) {
    cur = Math.max(cur + x, x); // 前缀是负收益则重新起头
    max = Math.max(max, cur);
  }
  return max;
}
```
