---
title: [ALG-019] 不允许直接调用 `String.prototype.indexOf`，在富文本编辑器里实现"查找下一个关键字"功能，手写 indexOf 核心逻辑？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-019：不允许直接调用 `String.prototype.indexOf`，在富文本编辑器里实现"查找下一个关键字"功能，手写 indexOf 核心逻辑？
**答**：朴素匹配：主串每个位置 i 尝试对齐模式串，逐字符比较，全部匹配则返回 i；比较失败移动到 i+1。可用"首字符不匹配直接跳过"剪枝。面试可追问 KMP：利用失配表把主串指针不回退，优化到 O(n + m)。时间 O(n × m)，空间 O(1)。

```javascript
function myIndexOf(haystack, needle) {
  if (needle === '') return 0;
  const n = haystack.length, m = needle.length;
  if (m > n) return -1;
  for (let i = 0; i + m <= n; i++) {
    if (haystack[i] !== needle[0]) continue; // 首字符剪枝
    let j = 1;
    while (j < m && haystack[i + j] === needle[j]) j++;
    if (j === m) return i;
  }
  return -1;
}
```
