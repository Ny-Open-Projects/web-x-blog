---
title: [ALG-461] 手写数位 DP 求 Kth：第 N 个合法编号
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-461：手写数位 DP 求 Kth：第 N 个合法编号

**答**：
- 题目：求「第 N 个不含 4 的编号」（顺子号池分配）。数位 DP 先算计数函数 f(x)，再按位逐位确定 Kth 的每一位。
- 思路：逐位确定：对第 pos 位尝试 d = 0..9，计算「以该前缀开头的合法数个数 cnt」，若 N > cnt 则 N -= cnt 试下一个 d，否则固定 d 进下一位。需要「固定前缀下、剩余位数的合法数计数」。
- 评分点：计数函数复用做 Kth；逐位贪心确定；前缀计数与 tight 的解耦。

```javascript
function kthWithoutFour(n) {                               // 第 n 个不含 4 的数
  function countWithPrefix(prefix, remaining) {             // 前缀固定下的补全计数
    let total = 0;
    for (let len = 0; len <= remaining; len++)              // 各长度补全
      total += Math.pow(9, len);                            // 每位 9 种（无 4）
    return total;
  }
  let result = '', budget = n, prefixLen = 0;
  for (let pos = 0; pos < 10; pos++) {                      // 逐位确定
    for (let d = pos === 0 ? 1 : 0; d <= 9; d++) {          // 首位非零
      if (d === 4) continue;
      const cnt = countWithPrefix(result + d, 9 - pos);    // 以该前缀开头的总数
      if (budget > cnt) { budget -= cnt; continue; }       // 跳过该前缀块
      result += d;                                         // 固定该位
      break;
    }
  }
  return result;
}
// 通用套路：f(x) 计数 + 逐位贪心 = 数位 Kth
```
