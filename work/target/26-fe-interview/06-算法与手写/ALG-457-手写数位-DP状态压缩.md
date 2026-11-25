---
title: [ALG-457] 手写数位 DP+状态压缩：出现过的数字集合（唯一数字编号）
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-457：手写数位 DP+状态压缩：出现过的数字集合（唯一数字编号）

**答**：
- 题目：「各位数字互不相同」的编号统计（如 123 合法、112 非法）。状态需 bitmask 记录已用数字。
- 思路：dp(pos, mask, started, tight)：mask = 已出现数字集合（0~1023）；填 d 前查 mask & (1<<d)；首位 1~9，后续可 0。
- 评分点：bitmask 状态；已用位判断与置位；状态数 = 位数 × 1024（可接受）。

```javascript
function countUniqueDigits(N) {                            // 各位互不相同的编号数
  const digits = String(N).split('').map(Number);
  const memo = new Map();
  function dfs(pos, mask, started, tight) {
    if (pos === digits.length) return started ? 1 : 0;
    const key = pos * 2048 + mask + (tight ? 2048 : 0) + (started ? 2048 * 2 : 0);
    if (!tight && memo.has(key)) return memo.get(key);
    const maxD = tight ? digits[pos] : 9;
    let total = 0;
    for (let d = 0; d <= maxD; d++) {
      if (started && (mask >> d) & 1) continue;            // 已用过：跳过
      const nMask = started ? mask | (1 << d) : (d > 0 ? 1 << d : 0);   // 置位
      total += dfs(pos + 1, nMask, started || d > 0, tight && d === maxD);
    }
    if (!tight) memo.set(key, total);
    return total;
  }
  return dfs(0, 0, false, true);
}
```
