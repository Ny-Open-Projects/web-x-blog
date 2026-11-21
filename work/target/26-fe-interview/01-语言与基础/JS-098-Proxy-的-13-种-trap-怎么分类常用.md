---
title: [JS-098] Proxy 的 13 种 trap 怎么分类？常用组合是哪些？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-098：Proxy 的 13 种 trap 怎么分类？常用组合是哪些？

**答**：
- 对象基本操作 6 个：get / set / has / deleteProperty / defineProperty / getOwnPropertyDescriptor。
- 原型与枚举 3 个：getPrototypeOf / setPrototypeOf / ownKeys（Object.keys、for-in 的底层）。
- 函数专属 3 个：apply / construct / 以及 targets 为函数时的调用拦截。
- 扩展控制 2 个：isExtensible / preventExtensions；13 种 trap 与 Reflect 的 13 个静态方法一一对应。

```javascript
const target = { a: 1 };
const handler = {
  // —— 基本操作 ——
  get(t, k, r)                { return Reflect.get(t, k, r); },            // p.k / p[k]
  set(t, k, v, r)             { return Reflect.set(t, k, v, r); },         // p.k = v
  has(t, k)                   { return Reflect.has(t, k); },               // 'a' in p
  deleteProperty(t, k)        { return Reflect.deleteProperty(t, k); },    // delete p.k
  defineProperty(t, k, d)     { return Reflect.defineProperty(t, k, d); }, // Object.defineProperty(p,...)
  getOwnPropertyDescriptor(t, k) { return Reflect.getOwnPropertyDescriptor(t, k); },
  // —— 原型与枚举 ——
  getPrototypeOf(t)           { return Reflect.getPrototypeOf(t); },       // Object.getPrototypeOf
  setPrototypeOf(t, p)        { return Reflect.setPrototypeOf(t, p); },
  ownKeys(t)                  { return Reflect.ownKeys(t); },              // Object.keys/for-in 底层
  // —— 函数专属：仅当 target 是函数时触发 ——
  apply(t, thisArg, args)     { return Reflect.apply(t, thisArg, args); }, // p()
  construct(t, args, nt)      { return Reflect.construct(t, args, nt); },  // new p()
  // —— 扩展控制 ——
  isExtensible(t)             { return Reflect.isExtensible(t); },         // Object.isExtensible
  preventExtensions(t)        { return Reflect.preventExtensions(t); },
};

const proxy = new Proxy(target, handler);
proxy.b = 2;
console.log('a' in proxy, Object.keys(proxy), Reflect.ownKeys(handler));

// 常用组合一：只读代理（set 与 deleteProperty 都抛错）
const readonly = new Proxy(target, {
  set() { throw new TypeError('只读对象'); },
  deleteProperty() { throw new TypeError('只读对象'); },
});

// 常用组合二：函数代理做日志/鉴权
const api = new Proxy(function rpc(path) { return `call ${path}`; }, {
  apply(t, thisArg, args) {
    console.log('调用前校验', args);
    return Reflect.apply(t, thisArg, args);
  },
});
console.log(api('/user')); // 调用前校验 ['/user'] → call /user
```
