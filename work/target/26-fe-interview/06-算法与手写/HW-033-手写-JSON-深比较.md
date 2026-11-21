---
title: [HW-033] 手写 JSON 深比较
date: 2026-11-17
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-033：手写 JSON 深比较

**答**：
- 评分点：同引用 `a === b` 短路；类型不同直接 false（用 `typeof` + Array.isArray 区分对象与数组，数组 vs 对象结构不同必不等）；key 长度不同直接 false（比逐 key 比较更快的剪枝）；NaN 用 `Object.is` 或「都不等于自身」处理；纯 JSON 数据不涉及循环引用，但要能说出若含环需要 WeakMap 记忆化路径；复杂度 O(n)（n 为节点总数）。

```javascript
// ===== 5 分钟速写版 =====
function jsonEqual(a, b) {
  if (a === b) return true; // 同引用（含原始值）
  if (typeof a !== typeof b) return false;
  if (a === null || b === null || typeof a !== 'object') {
    return Number.isNaN(a) && Number.isNaN(b); // NaN 之间视为相等
  }
  if (Array.isArray(a) !== Array.isArray(b)) return false;
  const keysA = Object.keys(a), keysB = Object.keys(b);
  if (keysA.length !== keysB.length) return false;
  return keysA.every(k => jsonEqual(a[k], b[k]));
}

// ===== 标准完整版（含边界处理）=====
function jsonEqualPro(a, b, seen = new Map()) {
  if (Object.is(a, b)) return true; // 同引用 / NaN / ±0 区分
  if (a === null || b === null) return false;
  if (typeof a !== 'object' || typeof b !== 'object') return false;
  if (Array.isArray(a) !== Array.isArray(b)) return false;
  // 循环引用保护：同一对节点比较中再次相遇 → 视为相等（各自内部环结构一致）
  const pairKey = a;
  if (seen.get(pairKey) === b) return true;
  seen.set(pairKey, b);
  const keysA = Reflect.ownKeys(a);
  const keysB = Reflect.ownKeys(b);
  if (keysA.length !== keysB.length) return false;
  return keysA.every(k => {
    if (!Object.prototype.hasOwnProperty.call(b, k)) return false; // key 集合必须一致
    return jsonEqualPro(a[k], b[k], seen);
  });
}
// 追问：与 JSON.stringify(a) === JSON.stringify(b) 的区别 ——
// 序列化法受 key 顺序、undefined 丢失、循环引用报错影响，不可靠；递归比较是标准答案。
```

---
