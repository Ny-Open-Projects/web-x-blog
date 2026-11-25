---
title: [ALG-471] 手写数位 DP 与位运算结合：二进制特征编号
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-471：手写数位 DP 与位运算结合：二进制特征编号

**答**：
- 题目：统计「二进制表示中 1 的个数为质数」的编号个数（如 3=11 有 2 个 1）。数位 DP 在二进制上做（base 2），状态 = 已用的 1 的个数。
- 思路：dp(pos, ones, tight, started)：填 0/1，ones 累加；终态判断 ones 是否质数（预置小质数表）。进制泛化：进制 b，每位 0..b-1。
- 评分点：进制参数化（10 → 2）；ones 计数状态；质数判定表预置。

```javascript
function countPrimeBits(N) {                               // [1, N] 二进制 1 的个数为质数
  const bits = N.toString(2).split('').map(Number);
  const primes = new Set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]);
  const memo = new Map();
  function dfs(pos, ones, started, tight) {
    if (pos === bits.length) return started && primes.has(ones) ? 1 : 0;
    const key = pos * 64 + ones + (tight ? 64 : 0) + (started ? 128 : 0);
    if (!tight && memo.has(key)) return memo.get(key);
    const maxD = tight ? bits[pos] : 1;                    // 二进制：每位 0/1
    let total = 0;
    for (let d = 0; d <= maxD; d++)
      total += dfs(pos + 1, ones + (d === 1 && started ? 1 : started ? 1 : d === 1 ? 1 : 0),
        started || d === 1, tight && d === maxD);
    if (!tight) memo.set(key, total);
    return total;
  }
  return dfs(0, 0, false, true);
}
// 进制泛化：10 进制版本同构——每位 0..9，状态「数位和」或「某数字出现次数」
```
