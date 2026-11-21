---
title: [JS-063] Proxy 与 Object.defineProperty 的区别？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-063：Proxy 与 Object.defineProperty 的区别？

**答**：
- defineProperty 只能劫持**已知属性**的读写，新增/删除属性无法感知（Vue2 需 $set）。
- Proxy 劫持整个对象级别操作：新增删除、has、ownKeys、函数调用都可拦截。
- defineProperty 兼容性更好（IE9+），Proxy 是 ES6（IE 不支持）。
- 数组索引与 length：defineProperty 处理繁琐，Proxy 天然支持。

```javascript
// Object.defineProperty：只能监听已有属性
const vue2like = {};
let inner = 0;
Object.defineProperty(vue2like, 'count', {
  get() { return inner; },
  set(v) { inner = v; console.log('dep update'); },
  enumerable: true,
});
vue2like.count = 1;      // 触发
vue2like.newKey = 2;     // 无法被监听

// Proxy：对象级监听
const vue3like = new Proxy({ count: 0 }, {
  set(t, k, v) {
    t[k] = v;
    console.log(`update ${String(k)}`);
    return true;
  },
  deleteProperty(t, k) {
    console.log(`remove ${String(k)}`);
    return delete t[k];
  },
});
vue3like.newKey = 2;   // update newKey
delete vue3like.count; // remove count

// 数组
const arrProxy = new Proxy([1, 2], { set(t, k, v) { t[k] = v; console.log('arr set', k, v); return true; } });
arrProxy[5] = 9;       // arr set 5 9
```

## 九、模块化
