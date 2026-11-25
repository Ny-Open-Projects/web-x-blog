---
title: [ALG-408] 手写 BIT 与前缀异或结合：区间奇偶开关
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-408：手写 BIT 与前缀异或结合：区间奇偶开关

**答**：
- 题目：一排开关，操作「翻转区间 [l, r] 的开关」，查「某开关状态」或「区间内开启数」。xor 差分 BIT：区间翻转 = 两端 xor 1，单点查 = 前缀 xor。
- 思路：差分异或——flip(l,r)：d[l] ^= 1, d[r+1] ^= 1；状态(i) = d[1..i] 的 xor 累计。BIT 换成「xor 版 BIT」（合并操作 xor）。
- 评分点：差分的 xor 版本；xor BIT（add/sum 都换 xor）；区间开区数需另一棵和 BIT 配合。

```javascript
class XorBIT {
  constructor(n) { this.n = n; this.t = new Array(n + 1).fill(0); }
  add(i, v) { for (; i <= this.n; i += i & -i) this.t[i] ^= v; }   // xor 合并
  xorPrefix(i) { let s = 0; for (; i > 0; i -= i & -i) s ^= this.t[i]; return s; }
}
class SwitchBoard {
  constructor(n) { this.n = n; this.d = new XorBIT(n + 1); this.state = new Array(n + 1).fill(0); }
  flip(l, r) {                                              // 区间翻转
    this.d.add(l, 1); this.d.add(r + 1, 1);
    this.state[l] ^= 1; this.state[r + 1] ^= 1;
  }
  on(i) { return this.d.xorPrefix(i); }                     // 单点状态 = 前缀 xor
}
```
