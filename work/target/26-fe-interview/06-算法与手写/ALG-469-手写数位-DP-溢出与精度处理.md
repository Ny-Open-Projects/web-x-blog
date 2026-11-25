---
title: [ALG-469] 手写数位 DP 溢出与精度处理：大数计数
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-469：手写数位 DP 溢出与精度处理：大数计数

**答**：
- 题目：区间 [1, 10^18] 计数——结果本身超 Number 精度（可到 10^18 级），计数需 BigInt。数位 DP 全程 BigInt。
- 思路：memo 值与累加用 BigInt；digits 从字符串取；除法/取模在 BigInt 上进行（性能可接受，位数仅 18）。
- 评分点：BigInt 计数；Number 何时够用（< 2^53）；mixed 精度的边界测试。

```javascript
function countBig(N) {                                     // N 可为 19 位字符串
  const digits = N.split('').map(Number);
  const memo = new Map();
  function dfs(pos, mod, tight) {
    if (pos === digits.length) return mod === 0 ? 1n : 0n;   // BigInt 计数
    const key = pos * 13 + mod;
    if (!tight && memo.has(key)) return memo.get(key);
    const maxD = tight ? digits[pos] : 9;
    let total = 0n;
    for (let d = 0; d <= maxD; d++)
      total += dfs(pos + 1, (mod * 10 + d) % 13, tight && d === maxD);
    if (!tight) memo.set(key, total);
    return total;
  }
  return dfs(0, 0, true);
}
// 结果对比：Number 精度上限 2^53 ≈ 9e15——计数结果可能超过
// 混合策略：中间统计用 Number（安全时），最终差值用 BigInt
```
