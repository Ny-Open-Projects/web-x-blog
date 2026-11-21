---
title: [ALG-117] 手写 Function.prototype.bind：组件事件回调要永久绑定组件实例，还要支持预设参数（偏函数），并且 `new bound()` 时不能被绑死的 this 干扰？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-117：手写 Function.prototype.bind：组件事件回调要永久绑定组件实例，还要支持预设参数（偏函数），并且 `new bound()` 时不能被绑死的 this 干扰？
**答**：bind 返回一个闭包函数：调用时用 `fn.apply(ctx, [...预置参数, ...实参])`。两个易错点：① 用 `new` 调用 bound 函数时，this 是新实例，优先级高于 bind 的 ctx（ES5 用 `instanceof` 检测，原生通过 new.target 判断）；② bound 的 prototype 要链接回原函数原型，保证 `new bound()` 的实例 instanceof 原构造函数。时间 O(1)。

```javascript
Function.prototype.myBind = function (ctx, ...preArgs) {
  const fn = this;
  const bound = function (...args) {
    // new 调用时 this 是新实例，优先级高于 bind 的 ctx
    return fn.apply(this instanceof bound ? this : ctx, [...preArgs, ...args]);
  };
  // 维持原型链：new bound() 的实例 instanceof 原构造函数成立
  if (fn.prototype) bound.prototype = Object.create(fn.prototype);
  return bound;
};
// 场景：事件回调永久绑定组件实例 + 预设行号
const onRowClick = handleClick.myBind(component, rowIndex);
```
