---
title: [ALG-536] 手写洗牌算法（Fisher-Yates）：随机抽样
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-536：手写洗牌算法（Fisher-Yates）：随机抽样

**答**：
- 题目：抽奖从 N 个用户均匀随机抽 K 个——Fisher-Yates 洗牌取前 K，或蓄水池抽样（流式）。证明均匀性（每个排列等概率）。
- 思路：Fisher-Yates：i 从后往前，j = rand(0..i) 交换；均匀性：每个位置取值独立均匀。偏置洗牌反例（朴素「随机交换」不均匀）。
- 评分点：Fisher-Yates 正确方向（从后往前）；均匀性证明；偏置洗牌反例。

```javascript
function fisherYates(arr) {                                // 均匀洗牌 O(n)
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));         // j ∈ [0, i] 均匀
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}
function sample(arr, k) { return fisherYates(arr).slice(0, k); }
// 偏置反例：「每次随机取两个位置交换」——某些排列概率不等（n=3 时 123 出现概率分布不均）
// Fisher-Yates 均匀性：第 i 步有 i+1 种等概率选择 → 共 n! 条等概率路径 → 每排列 1/n!
```
