---
title: [BLD-126] useBuiltIns 的 entry / usage / false 三种 polyfill 注入模式产物差异。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-126：useBuiltIns 的 entry / usage / false 三种 polyfill 注入模式产物差异。
**答**：
- **entry**：入口手写 `import 'core-js/stable'; import 'regenerator-runtime/runtime';`，构建时替换为按目标浏览器需要的**全量 API 垫片**——与代码是否用到无关，产物最大但"一次垫齐"。
- **usage（主流）**：不需要手写 import，babel 扫描每个文件**实际用到的 API**（如代码里有 `Promise.allSettled` 才注入对应模块），按需注入、产物最小；缺点是依赖第三方包时看不到其内部使用（需要 transform-runtime 配合）。
- **false**：不注入任何 polyfill，只转语法——目标浏览器较新或有独立 polyfill 服务（如 cdn polyfill.io? 已不推荐，通常自管）时使用；产物最小且零重复。
- 重复风险：usage + 第三方库自带 core-js 会双实例（`Symbol.hasInstance` 判断失效等），库禁止带 polyfill——这也是"应用用 usage，库用 transform-runtime"的根本原因。

```javascript
// 同一段源码在三种模式下的产物差异
// 源码：Promise.allSettled([p1, p2]).then(rs => rs.includes(undefined))

// ── useBuiltIns: 'entry'（入口写 import 'core-js/stable'）──
// 构建时被替换为（按 browserslist 目标展开，可能与业务无关的 API 也全垫）：
// require("core-js/modules/es.promise.all-settled.js");
// require("core-js/modules/es.array.includes.js");
// require("core-js/modules/es.array.iterator.js");
// require("core-js/modules/es.object.to-string.js");   // ...数量与目标浏览器成反比

// ── useBuiltIns: 'usage'（入口无任何手写 import）──
// 每个用到的文件顶部按需注入，只垫"这份代码用到的"：
// require("core-js/modules/es.promise.all-settled.js");   // 因为代码里有 allSettled
// require("core-js/modules/es.array.includes.js");        // 因为代码里有 includes

// ── useBuiltIns: false ──
// 无任何注入；targets 较旧时运行时直接报 Promise.allSettled is not a function
// 需要自己在 HTML 里引统一 polyfill 或接受目标限制
```
