---
title: [ALG-464] 手写数位 DP+模数余数状态：整除性筛选（双约束）
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-464：手写数位 DP+模数余数状态：整除性筛选（双约束）

**答**：
- 题目：编号要求「能被 7 整除 且 数字和为偶数」双约束。状态 = (rem7, sumParity) 二元组。
- 思路：dp(pos, rem, parity, tight)：填数时 rem 与 parity 同步转移；终态双判定。状态数 = 位数 × 7 × 2。
- 评分点：多约束状态组合；同步转移；状态数乘法增长与可行性评估。

```javascript
function countDualConstraint(N) {
  const digits = String(N).split('').map(Number);
  const memo = new Map();
  function dfs(pos, rem, parity, tight) {                   // mod 7 + 数字和奇偶
    if (pos === digits.length) return (rem === 0 && parity === 0) ? 1 : 0;
    const key = pos * 14 + rem * 2 + parity;
    if (!tight && memo.has(key)) return memo.get(key);
    const maxD = tight ? digits[pos] : 9;
    let total = 0;
    for (let d = 0; d <= maxD; d++)
      total += dfs(pos + 1, (rem * 10 + d) % 7, (parity + d) % 2, tight && d === maxD);
    if (!tight) memo.set(key, total);
    return total;
  }
  return dfs(0, 0, 0, true);
}
// 多约束状态数 = 各约束状态数乘积——超过 10⁴ 时考虑拉格朗日/分块等替代
```
