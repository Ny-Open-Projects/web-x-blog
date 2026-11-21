---
title: [ALG-115] 手写 Function.prototype.call：埋点函数要借用任意模块的 this 记录来源，且不能污染目标对象？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-115：手写 Function.prototype.call：埋点函数要借用任意模块的 this 记录来源，且不能污染目标对象？
**答**：原理是隐式绑定——把函数临时挂到目标对象上再调用，this 自然指向它。要点：① target 为 null/undefined 时绑到 globalThis（非严格模式）；② 用 `Symbol` 作临时 key 避免覆盖已有属性；③ 调完删除临时属性。apply 只是参数形式不同（数组展开），O(n)。

```javascript
Function.prototype.myCall = function (ctx, ...args) {
  ctx = ctx == null ? globalThis : Object(ctx);  // null/undefined 兜底，原始值包对象
  const key = Symbol('fn');                      // 唯一 key，不覆盖已有属性
  // configurable: true 必须显式声明：defineProperty 默认不可配置，严格模式下 finally 的 delete 会 TypeError
  Object.defineProperty(ctx, key, { value: this, enumerable: false, configurable: true });
  try {
    return ctx[key](...args);                    // 隐式绑定：作为方法调用
  } finally {
    delete ctx[key];                             // 用完删除，不留痕迹
  }
};
// 场景：日志函数借用模块对象记录来源
function log(tag) { console.log(tag, this.name); }
log.myCall({ name: 'order-module' }, '[order]'); // '[order] order-module'
```
