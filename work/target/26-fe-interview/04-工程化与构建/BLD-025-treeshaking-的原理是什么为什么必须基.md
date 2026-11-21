---
title: [BLD-025] tree-shaking 的原理是什么？为什么必须基于 ESM？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-025：tree-shaking 的原理是什么？为什么必须基于 ESM？
**答**：
- 前提一（静态结构）：ESM 的 import/export 是编译期语法，导入导出在 AST 阶段就确定，可以建立"导出绑定 → 使用处"的静态关系；CJS 的 require 是运行时函数调用，无法静态穷举。
- 前提二（usedExports 分析）：webpack 对每个模块做导出使用标记（普通用法、re-export 链、动态访问），未被使用的导出在 terser 压缩时被判定为死代码删除。
- 连锁效果：usedExports + ConcatenatedModules（作用域提升）后，"只用了库中一个函数"时其余函数因未被引用被整体消除。
- 边界：有副作用的代码不能删（IIFE、polyfill、CSS import），所以需要 sideEffects 标记配合；`export default` 整对象导出会让分析失效（要具名导出）。

```javascript
// webpack.config.js：开启 tree-shaking 的完整配置
module.exports = {
  mode: 'production', // 生产模式自动开启 usedExports + minimize
  optimization: {
    usedExports: true,                  // 标记未使用的导出（dev 可开 以便观察标记）
    minimize: true,                     // terser 执行真正删除
    concatenateModules: true,           // 作用域提升 增强消除效果
    sideEffects: true,                  // 读取 package.json sideEffects 字段
    providedExports: true,
  },
};

// src/utils.js —— 正确导出方式（具名）
export function deepClone(obj) { return JSON.parse(JSON.stringify(obj)); }
export function formatDate(d) { return d.toISOString(); } // 未被使用 将被 shake

// src/index.js
import { deepClone } from './utils'; // 只引入具名导出
console.log(deepClone({ a: 1 }));
// 产物验证：grep formatDate dist/main.js 应无结果
```
