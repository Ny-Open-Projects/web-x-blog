---
title: [JS-097] Object.defineProperty 与 Proxy 的拦截能力差在哪？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-097：Object.defineProperty 与 Proxy 的拦截能力差在哪？

**答**：
- defineProperty 只能劫持“已存在的属性”的读写，监听不到新增属性、删除属性、数组索引赋值。
- Proxy 代理的是对象操作本身，新增/删除/has/枚举/函数调用全部可拦截（Vue3 弃用 defineProperty 的原因）。
- defineProperty 兼容性更好且性能开销更小；Proxy 无法 polyfill 到 ES5。
- defineProperty 改的是原对象，Proxy 返回代理对象，真实对象仍可被直接访问（要小心绕过）。

```javascript
// defineProperty：只针对"已有属性"
const legacy = { a: 1 };
Object.defineProperty(legacy, 'a', {
  get() { console.log('get a'); return 10; },
  set(v) { console.log('set a', v); },
});
legacy.a = 2;            // set a 2
legacy.b = 3;            // 新增属性：defineProperty 无法感知（Vue2 需要 $set）
console.log(legacy.b);   // 3 — 数据变了但拦截器没触发

// Proxy：拦截对象操作本身
const modern = new Proxy({ a: 1 }, {
  get(t, k, r)            { console.log('get', k); return Reflect.get(t, k, r); },
  set(t, k, v, r)         { console.log('set', k, v); return Reflect.set(t, k, v, r); },
  deleteProperty(t, k)    { console.log('delete', k); return Reflect.deleteProperty(t, k); },
});
modern.b = 1;    // set b 1 — 新增属性可拦截
delete modern.a; // delete a — 删除可拦截

// 数组差异
const arrProxy = new Proxy([], { set(t, k, v, r) { console.log('idx', k, v); return Reflect.set(t, k, v, r); } });
arrProxy[0] = 'x'; // idx 0 x — 数组索引赋值可拦截
```
