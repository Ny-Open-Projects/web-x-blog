---
title: [JS-130] 顶层 await 的使用场景与限制是什么？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-130：顶层 await 的使用场景与限制是什么？

**答**：
- 顶层 await 允许在 ESM 模块顶层直接 await，模块求值会暂停到 promise 结算。
- 语义：父模块等待所有依赖模块的顶层 await 完成后才求值——依赖链会被阻塞。
- 限制：只能在 ESM 中用（CJS 语法错误）；公共依赖慎用，会造成加载瀑布。
- 配合动态 import：调用方 `await import('./x.mjs')` 等待的是整个模块图完成求值。

```javascript
// config.mjs —— 模块自身变成异步求值
// const res = await fetch('/config.json');      // 顶层 await
// export const config = await res.json();

// main.mjs —— 拿到的 config 一定已就绪
// import { config } from './config.mjs';
// console.log(config.apiBase); // 不需要再 await

// 依赖链被阻塞的示意：
// main.mjs
//   import { config } from './config.mjs'; // 等待中
//   import { util } from './util.mjs';     // ← 无关模块也被推迟执行！
// 解法：config.mjs 导出 promise 而不是 await 它
//   export const configPromise = fetch('/config.json').then((r) => r.json());
//   // 需要配置的模块自己 await configPromise，无关模块不被阻塞

// 限制 1：CJS 中报错
// const data = await fetch('/x'); // SyntaxError（.cjs / require 链中）

// 限制 2：动态 import 的等待范围是整个模块图
async function boot() {
  const mod = await import('./config.mjs'); // 等到顶层 await 全部完成
  console.log('模块图就绪', Object.keys(mod));
}
boot();

// 典型应用：DB 连接、WASM 实例化、top-level 资源初始化
// const wasm = await WebAssembly.instantiateStreaming(fetch('/engine.wasm'));
// export const engine = wasm.instance;
```
