---
title: [JS-065] CommonJS 与 ESM 的核心区别？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-065：CommonJS 与 ESM 的核心区别？

**答**：
- 加载时机：CJS 运行时同步 require，可条件加载；ESM 编译期静态分析，声明必须顶层。
- 输出：CJS 值的**拷贝**，导出后变化不可见；ESM 值的**只读引用**（live binding）。
- this：CJS 顶层 this 是 exports 对象；ESM 顶层 this 是 undefined。
- 循环依赖：两者都靠缓存缓解，ESM 靠静态结构提前暴露绑定，行为更可控。

```javascript
// counter.cjs —— CommonJS
let count = 0;
function inc() { count += 1; }
module.exports = { count, inc };

// main.cjs
const { count, inc } = require('./counter.cjs');
inc();
console.log(count); // 0，值拷贝，不随内部变化

// counter.mjs —— ESM
export let count = 0;
export function inc() { count += 1; }

// main.mjs
import { count, inc } from './counter.mjs';
inc();
console.log(count); // 1，live binding

// 条件加载差异
if (process.env.DEV) {
  const dev = require('./dev.cjs'); // CJS 可以
}
// const dev = await import('./dev.mjs'); // ESM 用动态 import
```
