---
title: [WEB-059] ESModule 和 CommonJS 的核心区别？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-059：ESModule 和 CommonJS 的核心区别？
**答**：
- 加载机制：ESM 是编译期静态分析，import/export 必须在顶层，可实现 Tree Shaking；CJS 是运行时加载 `module.exports` 对象，动态 require。
- 值语义：ESM 导出的是绑定引用（导出方修改后导入方可见），CJS 导出的是值的拷贝（基本类型拷贝后互不影响）。
- 运行环境：ESM 浏览器原生支持（`<script type="module">` 异步加载、严格模式、this 为 undefined）；CJS 是 Node 传统规范（同步 require、this 为 module.exports）。
- 互操作：Node 中 ESM 里 import CJS 能拿到 default 导出；CJS 里 require ESM 需要较新版本支持。工程上打包器都以 ESM 为准。

```javascript
// counter.cjs —— CommonJS：值的拷贝 + 动态加载
let count = 0;
setTimeout(() => { count = 100; }, 100); // 导出方稍后修改

module.exports = { count, inc: () => count++ };

// main.cjs
const counter = require('./counter.cjs'); // 同步、运行时加载
console.log(counter.count); // 0（加载时快照）
counter.inc();
setTimeout(() => {
  console.log(counter.count); // 1：外部拿到的 count 是拷贝，看不到内部变成 100
}, 200);
```

```javascript
// counter.mjs —— ESModule：绑定引用
export let count = 0;
setTimeout(() => { count = 100; }, 100); // 修改会实时反映到所有导入方
export const inc = () => count++;

// main.mjs
import { count, inc } from './counter.mjs'; // 静态分析、编译期确定依赖
console.log(count); // 0
inc();
setTimeout(() => {
  console.log(count); // 101：count 是对导出绑定的只读引用，实时同步
}, 200);

// 静态结构让打包器可以做 Tree Shaking：未导入的导出会被移除
// import { count } from './counter.mjs'; // inc 未使用，打包后不进产物
```
