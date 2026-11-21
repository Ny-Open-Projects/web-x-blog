---
title: [ALG-125] 埋点 SDK 要求各业务方调用 `track(category, action, label)`，但多数调用点 category 固定。如何用柯里化让业务方少传重复参数？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-125：埋点 SDK 要求各业务方调用 `track(category, action, label)`，但多数调用点 category 固定。如何用柯里化让业务方少传重复参数？
**答**：柯里化把多参函数转成逐参收集：参数凑齐 `fn.length` 就执行，否则返回收集器继续等。要点：① 以 `fn.length`（形参数）为准，含默认值/剩余参数的函数需特殊处理；② 递归收集而不是嵌套箭头写死参数个数；③ 场景价值——预置通用参数生成"特化函数"。时间 O(1) 每次收集。

```javascript
function curry(fn) {
  return function curried(...args) {
    if (args.length >= fn.length) return fn.apply(this, args); // 参数凑齐则执行
    return (...rest) => curried(...args, ...rest);             // 否则继续收集
  };
}
// 场景：埋点预置 category
const track = curry((category, action, label) => send({ category, action, label }));
const orderTrack = track('order');
orderTrack('submit', 'btn-top');    // 部分调用
orderTrack('cancel', 'btn-side');   // 复用同一特化函数
// track('order', 'submit', 'btn-top') 一次传全也支持
```
