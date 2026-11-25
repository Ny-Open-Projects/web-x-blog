---
title: [ALG-452] 手写数位 DP：不含连续相同数字的计数（验证码池）
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-452：手写数位 DP：不含连续相同数字的计数（验证码池）

**答**：
- 题目：生成验证码号码池，要求「不含连续两位相同数字」，统计 [L, R] 内合法号码数。状态需带「上一位数字」。
- 思路：dp(pos, prev, tight)：当前位 d 必须不等于 prev；首位 prev = -1 特判。状态数 = 位数 × 10。
- 评分点：prev 状态引入；首位无约束；记忆化 key 含 prev。

```javascript
function countNoRepeatDigits(N) {
  const digits = String(N).split('').map(Number);
  const memo = new Map();
  function dfs(pos, prev, tight) {
    if (pos === digits.length) return 1;                   // 走到底：合法 +1
    const key = pos * 11 + (prev + 1);
    if (!tight && memo.has(key)) return memo.get(key);
    const maxD = tight ? digits[pos] : 9;
    let total = 0;
    for (let d = 0; d <= maxD; d++) {
      if (d === prev) continue;                            // 连续相同：跳过
      total += dfs(pos + 1, d, tight && d === maxD);
    }
    if (!tight) memo.set(key, total);
    return total;
  }
  return dfs(0, -1, true);
}
// [L, R] 合法数 = f(R) - f(L-1)
```
