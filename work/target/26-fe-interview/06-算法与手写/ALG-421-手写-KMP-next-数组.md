---
title: [ALG-421] 手写 KMP next 数组：日志模式匹配
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-421：手写 KMP next 数组：日志模式匹配

**答**：
- 题目：在审计日志流中找某模式串（如「ERROR:timeout」）的所有出现位置，日志量大需要线性算法。手写 KMP 的 next（失配指针）数组。
- 思路：next[i] = 模式串 [0..i] 的最长相等前后缀长度；构建：自身与自身错位匹配（p[next[i-1]] == p[i] 则延续，否则跳 next[next[i-1]]）。
- 评分点：next 定义准确；构建的跳转回退；匹配主循环失配时 j = next[j-1] 而非回退 i。

```javascript
function buildNext(p) {
  const next = new Array(p.length).fill(0);
  let k = 0;                                               // 当前最长相等前后缀
  for (let i = 1; i < p.length; i++) {
    while (k > 0 && p[i] !== p[k]) k = next[k - 1];        // 失配：回退 next 链
    if (p[i] === p[k]) k++;
    next[i] = k;
  }
  return next;
}
function kmpSearch(text, p) {
  const next = buildNext(p);
  const hits = [];
  let j = 0;
  for (let i = 0; i < text.length; i++) {
    while (j > 0 && text[i] !== p[j]) j = next[j - 1];     // 主串失配：j 回退，i 不回退
    if (text[i] === p[j]) j++;
    if (j === p.length) { hits.push(i - j + 1); j = next[j - 1]; }   // 命中：找重叠匹配
  }
  return hits;                                             // O(n + m) 线性
}
```
