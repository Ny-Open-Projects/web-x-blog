---
title: [ALG-400] 手写 BIT 单点最值的局限与解法：与线段树对比
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-400：手写 BIT 单点最值的局限与解法：与线段树对比

**答**：
- 题目：「单点改 + 区间查最大值」BIT 能做吗？——能做「单点改 + 前缀最大」（限单调场景），但任意区间 max 无法用 BIT 高效维护（max 不可减）。给出能做/不能做边界与线段树替代。
- 思路：BIT 的 range = 两个前缀差依赖「可减性」，max 不可减 → 区间 max 不行。特例：只增不减时可用 BIT 维护前缀 max（部分场景）。结论：最值类上线段树。
- 评分点：可减性是 BIT 的本质约束；「单点改+前缀 max」的特例写法；果断切线段树。

```javascript
class PrefixMaxBIT {                                       // 特例：值只增不减
  constructor(n) { this.n = n; this.t = new Array(n + 1).fill(0); }
  add(i, v) {                                               // 只允许变大
    for (; i <= this.n; i += i & -i) this.t[i] = Math.max(this.t[i], v);
  }
  prefixMax(i) {                                            // [1..i] 最大值
    let m = 0;
    for (; i > 0; i -= i & -i) m = Math.max(m, this.t[i]);
    return m;
  }
  // ⚠ 局限：不支持「变小」的单点改、不支持任意区间 max
  // 任意区间 max / 带减更新 → 必须线段树（可减性缺失）
}
// 选型结论表：可减运算（sum/xor）→ BIT；不可减（max/min/gcd 大部分）→ 线段树
```
