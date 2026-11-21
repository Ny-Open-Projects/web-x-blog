---
title: [HW-011] 手写 call / apply / bind
date: 2026-11-17
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-011：手写 call / apply / bind

**答**：
- 评分点：call/apply 的核心是「把函数临时挂到目标对象上再调用」，用 `Symbol` 做 key 避免属性名冲突与污染；null/undefined 的 this 要回落到 globalThis，原始值要 `Object()` 包装（严格模式差异可作为加分讨论）；apply 与 call 唯一区别是参数是数组（要校验非数组报错）；bind 返回**新函数**且要支持 `new` 调用——new 时 this 指向实例而非绑定对象，原型要挂到原函数原型上（`Object.create(fn.prototype)`）；bind 还要支持预设参数柯里化拼接。

```javascript
// ===== 5 分钟速写版 =====
Function.prototype.myCall = function (ctx, ...args) {
  ctx = ctx === null || ctx === undefined ? globalThis : Object(ctx);
  const key = Symbol('fn');            // 唯一 key 防止覆盖对象已有属性
  ctx[key] = this;
  const res = ctx[key](...args);
  delete ctx[key];
  return res;
};
Function.prototype.myBind = function (ctx, ...preset) {
  const fn = this;
  function bound(...later) {
    // new bound() 时 this instanceof bound 成立 → this 优先于绑定的 ctx
    return fn.apply(this instanceof bound ? this : ctx, [...preset, ...later]);
  }
  bound.prototype = Object.create(fn.prototype); // 保持 new bound 时原型链正确
  return bound;
};

// ===== 标准完整版（含边界处理）=====
Function.prototype.myCallPro = function (ctx, ...args) {
  if (typeof this !== 'function') throw new TypeError('myCall must be called on a function');
  ctx = ctx === null || ctx === undefined ? globalThis : Object(ctx);
  const key = Symbol('fn');
  ctx[key] = this;
  const res = ctx[key](...args);
  delete ctx[key];
  return res;
};
Function.prototype.myApplyPro = function (ctx, args = []) {
  if (typeof this !== 'function') throw new TypeError('myApply must be called on a function');
  if (args !== null && args !== undefined && typeof args[Symbol.iterator] !== 'function') {
    throw new TypeError('second argument must be array-like');
  }
  ctx = ctx === null || ctx === undefined ? globalThis : Object(ctx);
  const key = Symbol('fn');
  ctx[key] = this;
  const res = ctx[key](...args);       // apply 与 call 只差参数展开方式
  delete ctx[key];
  return res;
};
Function.prototype.myBindPro = function (ctx, ...preset) {
  if (typeof this !== 'function') throw new TypeError('myBind must be called on a function');
  const fn = this;
  function bound(...later) {
    // 1. new 调用：this 是 bound 的实例，优先级最高
    // 2. 普通调用：绑定到 ctx
    return fn.apply(this instanceof bound && fn.prototype.isPrototypeOf(this) ? this : ctx,
                    [...preset, ...later]);
  }
  // 用中间层避免直接修改 bound.prototype 影响原函数原型（不污染 fn.prototype）
  bound.prototype = Object.create(fn.prototype);
  return bound;
};
```

---
