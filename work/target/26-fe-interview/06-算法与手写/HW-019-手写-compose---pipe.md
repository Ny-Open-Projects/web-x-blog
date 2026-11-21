---
title: [HW-019] 手写 compose / pipe
date: 2026-11-17
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-019：手写 compose / pipe

**答**：
- 评分点：compose 是**从右往左**执行（`compose(f, g)(x) === f(g(x))`），pipe 从左往右；实现用 `reduceRight` / `reduce` 一行搞定，但要说清 reduce 传入的是函数而非值（函数式组合的关键）；首个函数可接收多参数，后续函数一律单参数（上一环节的结果）；能扩展异步版本 composeP / 支持多参透传是加分项。

```javascript
// ===== 5 分钟速写版 =====
const compose = (...fns) =>
  x => fns.reduceRight((acc, fn) => fn(acc), x); // 从右往左
const pipe = (...fns) =>
  x => fns.reduce((acc, fn) => fn(acc), x);      // 从左往右
// compose(toUpper, getName)(user) 等价 toUpper(getName(user))

// ===== 标准完整版（含边界处理）=====
function composePro(...fns) {
  if (fns.some(fn => typeof fn !== 'function')) {
    throw new TypeError('all arguments must be functions');
  }
  if (fns.length === 0) return x => x; // identity 兜底
  return function (...args) {
    // 首个函数支持多参；后续单参串联
    return fns.reduceRight((acc, fn, i) =>
      i === fns.length - 1 ? fn(...args) : fn(acc), undefined);
  };
}
function pipePro(...fns) {
  if (fns.some(fn => typeof fn !== 'function')) {
    throw new TypeError('all arguments must be functions');
  }
  if (fns.length === 0) return x => x;
  return function (...args) {
    return fns.reduce((acc, fn, i) => (i === 0 ? fn(...args) : fn(acc)), undefined);
  };
}
// 异步组合版：每个 fn 返回 Promise
const composeAsync = (...fns) =>
  x => fns.reduceRight((acc, fn) => Promise.resolve(acc).then(fn), Promise.resolve(x));
// 追问：中间件洋葱模型（Koa）本质就是带 next 参数的 compose 变体。
```

---
