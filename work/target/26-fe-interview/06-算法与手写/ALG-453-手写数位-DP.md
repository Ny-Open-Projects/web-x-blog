---
title: [ALG-453] 手写数位 DP：数位和整除计数（优惠券编号）
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-453：手写数位 DP：数位和整除计数（优惠券编号）

**答**：
- 题目：优惠券编号要求「各位数字之和能被 7 整除」，统计号段内合法编号数。状态带「当前数位和 mod 7」。
- 思路：dp(pos, sumMod7, tight)：填数时 sumMod = (sumMod + d) % 7；终态 sumMod === 0 计 1。状态数 = 位数 × 7。
- 评分点：模数状态传递；终态判定；可推广到任意模数（mod 3 判 3 的倍数等）。

```javascript
function countDivisibleBy7(N) {
  const digits = String(N).split('').map(Number);
  const memo = new Map();
  function dfs(pos, mod, tight) {
    if (pos === digits.length) return mod === 0 ? 1 : 0;   // 数位和 % 7 == 0
    const key = pos * 8 + mod;
    if (!tight && memo.has(key)) return memo.get(key);
    const maxD = tight ? digits[pos] : 9;
    let total = 0;
    for (let d = 0; d <= maxD; d++)
      total += dfs(pos + 1, (mod + d) % 7, tight && d === maxD);
    if (!tight) memo.set(key, total);
    return total;
  }
  return dfs(0, 0, true);
}
// 通用化：把 7 换成任意 m——状态数 位数×m，m 大时（>100）状态爆炸需换思路
```
