---
title: [JS-138] 手写 call/apply/bind 完整版要注意什么？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 笔试题, 04]
type: 笔试题
---

## JS-138：手写 call/apply/bind 完整版要注意什么？

**答**：
- call/apply 细节：this 为 null/undefined 时指向 globalThis；原始值要 Object 包装；用 Symbol 做临时键避免覆盖已有属性；用 defineProperty 避免 enumerable 污染 for-in。
- bind 细节：预设参数拼在实参前；`new bound()` 时 this 是新实例，必须把 this 透传给原函数而不是绑定的 ctx。
- new 兼容：`bound.prototype = Object.create(fn.prototype)`，让 `new bound()` 的实例 instanceof 原函数成立。
- 返回值都要透传。

```javascript
Function.prototype.myCall = function (ctx, ...args) {
  ctx = ctx == null ? globalThis : Object(ctx); // null/undefined → 全局；原始值包装
  const key = Symbol('fn');                     // 不覆盖已有属性
  Object.defineProperty(ctx, key, {             // 不可枚举，不污染 for-in
    value: this, enumerable: false, configurable: true, writable: true,
  });
  const result = ctx[key](...args);
  delete ctx[key];
  return result;
};

Function.prototype.myApply = function (ctx, args = []) {
  return this.myCall(ctx, ...(args ?? [])); // 复用 call，args 兜底空数组
};

Function.prototype.myBind = function (ctx, ...preset) {
  const fn = this;
  function bound(...args) {
    // new bound() 时 this 是新实例 → 透传给原函数；普通调用 → 用绑定的 ctx
    return fn.apply(this instanceof bound ? this : ctx, [...preset, ...args]);
  }
  if (fn.prototype) {
    bound.prototype = Object.create(fn.prototype); // new bound() 的原型链接回 fn
  }
  return bound;
};

function greet(g1, g2) { return `${this.name}: ${g1} ${g2}`; }
console.log(greet.myCall({ name: 'A' }, 'hi', 'yo'));    // A: hi yo
console.log(greet.myApply({ name: 'B' }, ['a', 'b']));   // B: a b
console.log(greet.myCall(null, 'x', 'y'));               // undefined: x y（globalThis.name）

// bind 的 new 兼容验证
const BoundGreet = greet.myBind({ name: 'C' }, 'hey');
console.log(new BoundGreet('z') instanceof greet); // true
// 普通调用走 ctx，new 调用走新实例
```
