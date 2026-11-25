---
title: [RBL-023] Rspack 中 loader 执行顺序与 pitch 机制如何工作？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-023：Rspack 中 loader 执行顺序与 pitch 机制如何工作？
**答**：
- 常规阶段：use 数组从后往前执行——最后声明的 loader 先处理源码，处理结果作为前一个 loader 的输入，形成流水线。
- pitch 阶段：从前往后先执行各 loader 的 pitch；某个 loader 的 pitch 返回非 undefined 值则跳过后续 pitch 与常规阶段，直接回跳执行前面 loader 的常规阶段（拦截语义）。
- 经典用例：style-loader 的 pitch 把 CSS 注入 DOM 并返回空串拦截后续；babel-loader cacheDirectory 在 pitch 里先查缓存，命中直接返回跳过编译。
- 与 webpack 的一致性：Rspack 保留 pitch 与拦截语义，迁移自 webpack 的 loader 一般不用改；但组合了冷门 pitch 行为的 loader 需要回归。
- 调试方法：在每个 loader 里打 `this.resourcePath` 与输入长度，确认顺序；或用 Rsdoctor 的 loader 耗时视图。
- 追问钩子：loader 是无状态函数，跨模块共享状态要通过 this.data（同一 loader 请求内传递）而不是模块级可变全局。

```javascript
// cache-loader 语义的手写示例（演示 pitch 拦截）
const fs = require('fs');
module.exports = function (source) {
  return source; // 常规阶段：真正转换
};
module.exports.pitch = function () {
  const cache = `/tmp/cache-${this.resourcePath.replace(/\W/g, '_')}.js`;
  if (fs.existsSync(cache)) {
    return fs.readFileSync(cache, 'utf8'); // 命中缓存 → 拦截，常规阶段不再执行
  }
};
```
