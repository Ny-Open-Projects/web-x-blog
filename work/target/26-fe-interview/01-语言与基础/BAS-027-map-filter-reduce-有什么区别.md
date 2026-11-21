---
title: [BAS-027] map、filter、reduce 有什么区别？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-027：map、filter、reduce 有什么区别？
**答**：
- map：一一映射，返回等长新数组；filter：条件筛选，返回子集；reduce：把数组归约为任意值（数字、对象、数组）。
- 三者都不修改原数组；map 和 filter 都可以用 reduce 实现。
- 常见错误：map 里忘写 return 得到一堆 undefined；不需要新数组时该用 forEach 而不是 map。

```javascript
const nums = [1, 2, 3, 4];
nums.map((n) => n * 2);              // [2, 4, 6, 8] 等长映射
nums.filter((n) => n % 2 === 0);     // [2, 4] 子集
nums.reduce((sum, n) => sum + n, 0); // 10 归约
nums.reduce(
  (acc, n) => { acc[n % 2 ? 'odd' : 'even'].push(n); return acc; },
  { odd: [], even: [] },             // reduce 还能归约出对象
);
```
