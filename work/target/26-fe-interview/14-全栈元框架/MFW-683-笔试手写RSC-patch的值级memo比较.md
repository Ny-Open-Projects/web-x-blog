---
title: [MFW-683] 笔试：手写 RSC patch 的值级 memo 比较
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-683：笔试：手写值级 memo 比较

**答**：实现 `shallowEqualProps(prev, next, { ignore })`。规则：1) 浅比较顶层键（值相等——对象/数组/函数引用比较（默认浅）；原始值 === 比较）；2) **ignore 列表**：跳过的键（timestamp——每次不同的抖动字段 RBL-794 规范化）；3) **深度字段比较**（指定键做深比较——product 对象的值比较（RBL-682 修正方案））；4) 返回 boolean（true = props 相等可跳过 re-render）。边界：prev/next null（null === null true）；键数不同（false）；undefined 值的键（undefined === undefined true——但 Object.keys 不含 undefined？——显式键比较）。

```javascript
function shallowEqualProps(prev = {}, next = {}, { ignore = [], deep = [] } = {}) {
  const pk = Object.keys(prev).filter(k => !ignore.includes(k));
  const nk = Object.keys(next).filter(k => !ignore.includes(k));
  if (pk.length !== nk.length) return false;
  for (const k of pk) {
    if (deep.includes(k)) {
      if (!deepEqValue(prev[k], next[k])) return false;    // 深比较指定键
      continue;
    }
    if (prev[k] !== next[k]) return false;                 // 浅比较
  }
  return true;
}
function deepEqValue(a, b) {
  if (a === b) return true;
  if (a == null || b == null) return false;
  if (typeof a !== 'object' || typeof b !== 'object') return a === b;
  if (Array.isArray(a) !== Array.isArray(b)) return false;
  const ka = Object.keys(a), kb = Object.keys(b);
  if (ka.length !== kb.length) return false;
  return ka.every(k => deepEqValue(a[k], b[k]));
}

// 自测
// 浅比较：原始值
console.log(shallowEqualProps({ id: 1, name: 'x' }, { id: 1, name: 'x' }) === true);
// 引用不同但值同的对象 → false（浅比较）
console.log(shallowEqualProps({ p: { id: 1 } }, { p: { id: 1 } }) === false);
// deep 修正
console.log(shallowEqualProps({ p: { id: 1 } }, { p: { id: 1 } }, { deep: ['p'] }) === true);
// ignore 抖动
console.log(shallowEqualProps({ ts: 1, v: 'x' }, { ts: 2, v: 'x' },
  { ignore: ['ts'] }) === true);
// 键数不同
console.log(shallowEqualProps({ a: 1 }, { a: 1, b: 2 }) === false);
// null
console.log(shallowEqualProps(null, null) === true);
// 数组深比较
console.log(shallowEqualProps({ items: [1, 2] }, { items: [1, 2] }, { deep: ['items'] }) === true);
console.log(shallowEqualProps({ items: [1, 2] }, { items: [1, 3] }, { deep: ['items'] }) === false);
```

**评分点**：
- 浅比较 + ignore（抖动字段）+ deep 指定键（RBL-682 的修正方案落地）
- deepEqValue 的递归实现（数组/对象/null 边界）；键数不等快速失败
- 边界（null/undefined 键/数组）；性能语义（浅 O(键) / 深 O(子树)——比较成本 vs re-render 成本）
- 能说清「RSC patch 的 Flight 反序列化 = 引用不稳定——memo 需值级比较辅助（deep 指定键）」属于加分
