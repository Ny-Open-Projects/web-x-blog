---
title: [JS-059] Set 有哪些典型应用？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-059：Set 有哪些典型应用？

**答**：
- 去重：`[...new Set(arr)]`，对基本类型直接有效。
- 集合运算：交集、并集、差集用 filter + has 实现。
- 成员存在性检查 O(1)，替代 `arr.includes` 的 O(n)。
- WeakSet 存对象标记“处理过”而不阻止回收。

```javascript
const arr = [1, 2, 2, 3, 'a', 'a'];
console.log([...new Set(arr)]); // [1, 2, 3, 'a']

const a = new Set([1, 2, 3]);
const b = new Set([2, 3, 4]);
const union     = new Set([...a, ...b]);
const intersect = new Set([...a].filter((x) => b.has(x)));
const diff      = new Set([...a].filter((x) => !b.has(x)));
console.log([...union], [...intersect], [...diff]);
// [1,2,3,4] [2,3] [1]

const big = new Set(Array.from({ length: 1e5 }, (_, i) => i));
console.time('set');
console.log(big.has(99999)); // O(1)
console.timeEnd('set');
```
