---
title: [JS-298] 笔试：手写 Set 集合运算工具函数
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 笔试题, 数据结构]
type: 笔试题
---

## JS-298：笔试：手写 Set 集合运算

**题目**：在 ES2025 原生方法可用前，实现 union/intersection/difference/symmetricDifference/isSubsetOf 五个工具：入参可为任意可迭代对象；返回新 Set。

**答**：
```javascript
const toSet = (it) => it instanceof Set ? it : new Set(it);

const union = (a, b) => new Set([...toSet(a), ...toSet(b)]);
const intersection = (a, b) => {
  const B = toSet(b);
  return new Set([...toSet(a)].filter(x => B.has(x)));
};
const difference = (a, b) => {
  const B = toSet(b);
  return new Set([...toSet(a)].filter(x => !B.has(x)));
};
const symmetricDifference = (a, b) => new Set([
  ...difference(a, b), ...difference(b, a),
]);
const isSubsetOf = (a, b) => {
  const B = toSet(b);
  return [...toSet(a)].every(x => B.has(x));
};

const a = new Set([1, 2, 3]), b = new Set([2, 3, 4]);
union([1], b);                     // 可迭代入参 {1,2,3,4}
intersection(a, b);                // {2,3}
symmetricDifference(a, b);         // {1,4}
isSubsetOf(new Set([2, 3]), a);    // true
```

**评分点**：
- 迭代入参的兼容（toSet 归一化）
- 小集合在「小侧」遍历的优化意识（先算 size 择优，加分）
- symmetricDifference 的两次 difference 组合
- 对照 ES2025 原生方法的迁移说明（加分）
