---
title: [JS-128] 循环依赖在 ESM 与 CommonJS 中的行为差异？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-128：循环依赖在 ESM 与 CommonJS 中的行为差异？

**答**：
- ESM：模块提升 + 活绑定（live binding），循环不报错，但访问"未初始化"的绑定会抛 TDZ ReferenceError。
- CJS：同步执行，第二次 require 命中缓存拿到"半成品 exports"的快照，不报错但可能拿到 undefined。
- 规避方式一致：循环双方都不要在模块顶层直接使用对方导出，延迟到函数调用时再访问。
- ESM 的活绑定：导出值变化后，导入方读到的永远是最新值；CJS 是值拷贝。

```javascript
// ===== 差异一：活绑定 vs 值快照 =====
// counter.mjs
//   export let count = 0;
//   export function inc() { count += 1; }
// main.mjs
//   import { count, inc } from './counter.mjs';
//   inc(); console.log(count); // 1 — 读到最新值（活绑定）

// counter.cjs
//   let count = 0;
//   module.exports = { count, inc() { count += 1; } };
// main.cjs
//   const { count, inc } = require('./counter.cjs');
//   inc(); console.log(count); // 0 — 解构拿到的是当时的值拷贝

// ===== 差异二：循环依赖输出题 =====
// a.mjs
//   import { b } from './b.mjs';
//   export const a = 'A';
//   console.log('a 执行，读到 b =', b);
// b.mjs
//   import { a } from './a.mjs';
//   export const b = 'B';
//   console.log('b 执行，读到 a =', a);   // ← TDZ！此刻 a.mjs 还没执行到 export const a

// 入口 import './a.mjs' 的求值顺序：
// a.mjs 开始 → 触发 b.mjs 求值 → b.mjs 顶层读 a → a 在 TDZ → ReferenceError
// 修复：b.mjs 改为函数内延迟访问
//   export function printA() { console.log(a); } // 调用时 a 已初始化 → 'A'

// ===== CJS 的循环：拿半成品快照 =====
// a.cjs: exports.a = 1; const { b } = require('./b.cjs'); console.log('a', b);
// b.cjs: const { a } = require('./a.cjs'); // 命中缓存，拿到 { a: 1 }
//        exports.b = 2;
// 特点：require('./a.cjs') 时 a.cjs 未执行完，此时它后续设置的导出拿不到
```
