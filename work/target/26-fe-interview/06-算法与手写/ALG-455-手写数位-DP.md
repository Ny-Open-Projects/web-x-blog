---
title: [ALG-455] 手写数位 DP：回文数计数（编号回文筛选）
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-455：手写数位 DP：回文数计数（编号回文筛选）

**答**：
- 题目：统计 [L, R] 内回文数个数。数位 DP 处理回文的对称性：从两端往中间填。
- 思路：改「从中间向两边填」或「枚举前半段 + 构造回文再判界」——工程上后者更简单：枚举前半长度与前半内容，构造完整回文，计数落在区间内的。
- 评分点：对称结构的数位 DP 变形；枚举前半构造法；边界判断（奇偶长度）。

```javascript
function countPalindromes(L, R) {                          // 枚举前半构造
  let count = 0;
  for (let len = String(L).length; len <= String(R).length; len++) {
    const half = Math.ceil(len / 2);
    const start = half === 1 ? 1 : Math.pow(10, half - 1);
    const end = Math.pow(10, half) - 1;
    for (let h = start; h <= end; h++) {                   // 枚举前半段
      const hs = String(h);
      const pal = len % 2 === 0
        ? hs + [...hs].reverse().join('')
        : hs + [...hs.slice(0, -1)].reverse().join('');
      const v = +pal;
      if (v >= L && v <= R) count++;                       // 落在区间内
    }
  }
  return count;
}
// 复杂度：O(√R × 位数)——回文数本身只有 O(√R) 个，构造枚举天然高效
// 教学点：标准数位 DP 处理回文需「双向填数」状态，工程上枚举构造更简
```
