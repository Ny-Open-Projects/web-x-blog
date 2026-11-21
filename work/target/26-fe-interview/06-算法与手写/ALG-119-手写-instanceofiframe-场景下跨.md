---
title: [ALG-119] 手写 instanceof：iframe 场景下跨 window 的对象用原生 instanceof 会失效，需要沿原型链手查？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-119：手写 instanceof：iframe 场景下跨 window 的对象用原生 instanceof 会失效，需要沿原型链手查？
**答**：instanceof 的语义是：沿对象的原型链逐层上溯，任何一层严格等于构造函数的 `prototype` 即为 true。手写用 `Object.getPrototypeOf` 循环，终点是 null。注意：① 右操作数必须是函数；② 原始值直接 false；③ 跨 iframe 用原生 instanceof 会因为两个 window 各有一套构造函数而失效，手查原型链可绕开构造函数比对。时间 O(原型链深度)。

```javascript
function myInstanceof(obj, Ctor) {
  if (obj == null || typeof Ctor !== 'function') return false;
  if (typeof obj !== 'object' && typeof obj !== 'function') return false; // 原始值直接 false
  let proto = Object.getPrototypeOf(obj);
  while (proto) {
    if (proto === Ctor.prototype) return true; // 沿原型链逐层比对
    proto = Object.getPrototypeOf(proto);
  }
  return false;
}
// myInstanceof([], Array) => true；myInstanceof('s', String) => false（原始值）
// myInstanceof(new Date(), Object) => true（Date.prototype 在 Object.prototype 链上）
```
