---
title: [ALG-458] 手写数位 DP：整除枚举的余数状态（批次倍数编号）
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-458：手写数位 DP：整除枚举的余数状态（批次倍数编号）

**答**：
- 题目：编号要求「能被 13 整除」，统计号段内合法编号。余数状态 mod 13。
- 思路：dp(pos, rem, tight)：填数 rem = (rem × 10 + d) % 13（注意进位乘 10）；终态 rem === 0。
- 评分点：逐位进位的余数递推（×10+d）；终态余数判定；模数大时状态数与记忆化收益。

```javascript
function countDivisible(N, m = 13) {
  const digits = String(N).split('').map(Number);
  const memo = new Map();
  function dfs(pos, rem, tight) {
    if (pos === digits.length) return rem === 0 ? 1 : 0;
    const key = pos * m + rem;
    if (!tight && memo.has(key)) return memo.get(key);
    const maxD = tight ? digits[pos] : 9;
    let total = 0;
    for (let d = 0; d <= maxD; d++)
      total += dfs(pos + 1, (rem * 10 + d) % m, tight && d === maxD);   // ×10 进位
    if (!tight) memo.set(key, total);
    return total;
  }
  return dfs(0, 0, true);
}
// 前导零注意：000013 mod 13 = 13 mod 13 = 0——余数语义不受前导零影响（乘 10 不变）
```
