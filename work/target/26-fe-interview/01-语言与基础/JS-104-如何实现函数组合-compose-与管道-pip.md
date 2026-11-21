---
title: [JS-104] 如何实现函数组合 compose 与管道 pipe？有哪些应用场景？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-104：如何实现函数组合 compose 与管道 pipe？有哪些应用场景？

**答**：
- compose：从右到左执行，`compose(f, g)(x) = f(g(x))`，数学风格。
- pipe：从左到右执行，与数据流向一致，可读性更好，前端更常用。
- 实现：`reduce`（pipe）或 `reduceRight`（compose）串联函数。
- 场景：数据清洗链、表单校验链、中间件、状态转换（Redux reducer 前置处理）。

```javascript
const compose = (...fns) => (x) => fns.reduceRight((acc, fn) => fn(acc), x);
const pipe = (...fns) => (x) => fns.reduce((acc, fn) => fn(acc), x);

// 数据清洗链：每一步都是单一职责的纯函数
const trim    = (s) => s.trim();
const toLower = (s) => s.toLowerCase();
const wrap    = (s) => `<p>${s}</p>`;

const normalize = pipe(trim, toLower, wrap);
console.log(normalize('  Hello World  ')); // <p>hello world</p>
console.log(compose(wrap, toLower, trim)('  Hi  ')); // <p>hi</p>

// 增强版：支持第一个函数多参数
const pipeN = (...fns) => (...args) =>
  fns.reduce((acc, fn, i) => (i === 0 ? fn(...acc) : fn(acc)), args);
const pow = (a, b) => a ** b;
const double = (n) => n * 2;
console.log(pipeN(pow, double)(2, 3)); // 18

// 异步管道：每个环节允许返回 Promise
const pipeAsync = (...fns) => (x) =>
  fns.reduce((p, fn) => p.then(fn), Promise.resolve(x));
pipeAsync(
  () => Promise.resolve('user-1'),
  (id) => Promise.resolve({ id, name: 'tom' }),
  (u) => u.name.toUpperCase()
).then(console.log); // TOM
```
