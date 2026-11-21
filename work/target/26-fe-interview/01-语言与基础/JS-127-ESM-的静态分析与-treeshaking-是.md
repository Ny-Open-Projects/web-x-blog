---
title: [JS-127] ESM 的静态分析与 tree-shaking 是什么关系？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-127：ESM 的静态分析与 tree-shaking 是什么关系？

**答**：
- ESM 的 import/export 必须在顶层、路径必须是静态字符串 → 构建期即可确定完整依赖图。
- 依赖图确定后，打包器标记"导入了但未使用"的导出并在压缩时移除，即 tree-shaking。
- 破坏 shaking 的常见写法：动态属性访问 `utils[name]()`、模块顶层副作用、把导出挂到对象上再解构。
- `package.json` 的 `sideEffects: false` 与 `/*#__PURE__*/` 注释帮助打包器安全删除。

```javascript
// utils.js
// export const used   = () => 'use';
// export const unused = () => 'never';  // 未被引用 → 打包产物中消失

// main.js
import { used } from './utils.js'; // 静态可分析 → unused 被摇掉
console.log(used());

// 会破坏 tree-shaking 的写法：
// 1. 动态访问：静态分析不知道会用到哪个导出 → 全保留
//    import * as utils from './utils.js';
//    const fn = utils[name];
// 2. 顶层副作用：删除模块可能改变程序行为
//    utils.js 顶部：window.__init__ = true;
// 3. CommonJS：require 是运行时调用，无静态结构 → 无法摇

// package.json 声明（让打包器放心删除无引用文件）：
// {
//   "name": "lib",
//   "sideEffects": ["*.css", "./src/polyfill.js"], // 白名单外均无副作用
// }

// 副作用函数也可用内联注释标记可安全删除：
// const result = /*#__PURE__*/ createSomething();
```
