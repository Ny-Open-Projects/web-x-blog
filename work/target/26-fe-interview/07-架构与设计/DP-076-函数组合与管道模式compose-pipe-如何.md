---
title: [DP-076] 函数组合与管道模式：compose/pipe 如何实现？
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-076：函数组合与管道模式：compose/pipe 如何实现？
**答**：
- 组合：`compose(f, g)(x) = f(g(x))`（从右向左）；管道：`pipe(f, g)(x) = g(f(x))`（从左向左，更符合阅读顺序）。
- 前端应用：数据加工流水线（清洗→校验→格式化）、中间件/拦截器合成、redux 的 `compose(middleware)(createStore)`、HOC 组合。
- 与职责链关系：职责链是"请求在对象链中流动"，compose 是"数据在函数链中流动"——函数式版的职责链。
- 加分：类型安全的 pointfree 风格、Promise 版 composeP。

```javascript
// compose：从右向左；pipe：从左向右
const compose = (...fns) => (x) => fns.reduceRight((acc, fn) => fn(acc), x);
const pipe = (...fns) => (x) => fns.reduce((acc, fn) => fn(acc), x);

// 数据加工流水线
const trim = (s) => s.trim();
const toLower = (s) => s.toLowerCase();
const slugify = (s) => s.replace(/\s+/g, '-');
const normalizeSlug = pipe(trim, toLower, slugify); // 声明流水线：顺序即执行顺序
console.log(normalizeSlug('  Hello World  ')); // hello-world

// 异步管道：每步可能是 Promise
const pipeP = (...fns) => (x) => fns.reduce((p, fn) => p.then(fn), Promise.resolve(x));
const fetchUser = (id) => Promise.resolve({ id, name: 'tom', age: 17 });
const assertAdult = (u) => { if (u.age < 18) throw new Error('未成年'); return u; };
const toView = (u) => ({ name: u.name.toUpperCase() });
pipeP(fetchUser, assertAdult, toView)(1).then(console.log).catch((e) => console.log('拦截', e.message));

// redux 源码对照：compose 用于增强 store
// export default function compose(...fns) {
//   if (fns.length === 0) return (arg) => arg;
//   if (fns.length === 1) return fns[0];
//   return fns.reduce((a, b) => (...args) => a(b(...args)));
// }
const enhance = compose((next) => ( reducer) => next(reducer), (next) => next); // 增强器叠加示意
console.log(typeof compose()); // function —— 空组合是恒等函数
```
