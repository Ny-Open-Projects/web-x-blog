---
title: [ALG-097] 组件 props 变更检测、测试断言都需要"两个对象内容是否完全相等"的 deepEqual，且要兼容循环引用。如何实现？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-097：组件 props 变更检测、测试断言都需要"两个对象内容是否完全相等"的 deepEqual，且要兼容循环引用。如何实现？
**答**：先走 `===` 快路径（原始值与同引用）；任一方非对象即 false；用 `WeakMap<对象, 已比较过的对象>` 处理循环引用——配对重复出现视为相等（引用比较语义）；再比较键数量后逐键递归。`===` 同引用短路让大部分调用 O(1)，最坏 O(n)，空间 O(n)。

```javascript
function deepEqual(a, b, seen = new WeakMap()) {
  if (a === b) return true; // 含原始值与同引用
  if (a === null || b === null || typeof a !== 'object' || typeof b !== 'object') {
    return false;
  }
  if (seen.get(a) === b) return true; // 循环引用配对已确认
  seen.set(a, b);
  if (Array.isArray(a) !== Array.isArray(b)) return false;
  const ka = Object.keys(a), kb = Object.keys(b);
  if (ka.length !== kb.length) return false;
  return ka.every(k => deepEqual(a[k], b[k], seen));
}
```
