---
title: [ALG-430] 手写 Manacher 最长回文：用户名回文检测
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-430：手写 Manacher 最长回文：用户名回文检测

**答**：
- 题目：用户名风控——检测「高度回文」昵称（如 abcdcba，常见于刷号）。Manacher O(n) 求最长回文。
- 思路：插入 # 统一奇偶（aba → #a#b#a#）；p[i] = 以 i 为中心的最大回文半径；利用已算 p[mirror] 初始化（i 在右边界内 → p[i] ≥ min(p[2c-i], r-i)）再扩展。
- 评分点：# 插入统一奇偶；mirror 复用；O(n) 复杂度证明（边界只前进）。

```javascript
function manacher(s) {
  const t = '#' + [...s].join('#') + '#';                  // 统一奇偶
  const p = new Array(t.length).fill(0);
  let c = 0, r = 0;                                        // 中心与右边界
  for (let i = 0; i < t.length; i++) {
    if (i < r) p[i] = Math.min(p[2 * c - i], r - i);       // mirror 复用
    while (i - p[i] - 1 >= 0 && i + p[i] + 1 < t.length
      && t[i - p[i] - 1] === t[i + p[i] + 1]) p[i]++;      // 暴力扩展
    if (i + p[i] > r) { c = i; r = i + p[i]; }             // 更新边界
  }
  let best = 0, center = 0;
  for (let i = 0; i < t.length; i++)
    if (p[i] > best) { best = p[i]; center = i; }
  return { maxLength: best, substring: s.slice((center - best) >> 1, (center - best) >> 1 + best) };
}
function isSuspiciousUsername(u) {
  const { maxLength } = manacher(u);
  return maxLength >= Math.floor(u.length * 0.8);          // 80% 回文判可疑
}
```
