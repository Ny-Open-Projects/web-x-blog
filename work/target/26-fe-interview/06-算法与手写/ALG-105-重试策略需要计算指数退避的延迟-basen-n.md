---
title: [ALG-105] 重试策略需要计算指数退避的延迟 `base^n`，n 可能很大；分片调度还需要在模意义下算 2^n 估算容量。如何 O(log n) 实现快速幂？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-105：重试策略需要计算指数退避的延迟 `base^n`，n 可能很大；分片调度还需要在模意义下算 2^n 估算容量。如何 O(log n) 实现快速幂？
**答**：把指数写成二进制，底数每次自乘平方、指数右移一位，指数二进制位为 1 时把当前底数累乘进答案。普通快速幂 O(log n) 次乘法；对大数取模版本每步取模防溢出，O(log n)。

```javascript
function quickPow(base, exp) {
  let ans = 1;
  while (exp > 0) {
    if (exp & 1) ans *= base; // 指数二进制最低位为 1 时累乘
    base *= base;             // 底数自平方，指数右移一位
    exp >>= 1;
  }
  return ans;
}
// 大数场景取模防溢出（如估算哈希分片容量 2^n % MOD）
function quickPowMod(base, exp, mod) {
  let ans = 1;
  base %= mod;
  while (exp > 0) {
    if (exp & 1) ans = (ans * base) % mod;
    base = (base * base) % mod;
    exp >>= 1;
  }
  return ans;
}
// quickPow(2, 10) => 1024；quickPowMod(2, 100, 1e9 + 7)
```
