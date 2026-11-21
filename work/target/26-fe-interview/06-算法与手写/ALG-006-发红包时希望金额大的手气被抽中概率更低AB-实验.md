---
title: [ALG-006] 发红包时希望金额大的手气被抽中概率更低；AB 实验按 90/10 流量分流。如何实现"按权重随机选择"？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-006：发红包时希望金额大的手气被抽中概率更低；AB 实验按 90/10 流量分流。如何实现"按权重随机选择"？
**答**：把权重铺成一条数轴：累加得到总和 total，随机取 `[0, total)` 中的一个点 r，遍历时用 r 依次减去每项权重，减到负数即落在该项区间。频率高时可预构建前缀和数组，用二分查找把单次抽取降到 O(log n)。时间 O(n)（或 O(log n)），空间 O(n)。

```javascript
function weightedPick(items, weightFn) {
  const weights = items.map(weightFn);
  const total = weights.reduce((s, w) => s + w, 0);
  let r = Math.random() * total;
  for (let i = 0; i < items.length; i++) {
    r -= weights[i];
    if (r < 0) return items[i];
  }
  return items[items.length - 1];
}
// AB 分流：weightedPick(['A', 'B'], i => i === 'A' ? 90 : 10)
// 高频调用可预建前缀和 + 二分：prefix = [90, 100]，二分找第一个 > r 的位置
```
