---
title: [BLD-028] /*#__PURE__*/ 纯注解的作用和正确用法是什么？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-028：/*#__PURE__*/ 纯注解的作用和正确用法是什么？
**答**：
- 纯注解告诉压缩器"这次函数调用的返回值若未被使用，则整个调用（含副作用）可以整体删除"，是给 terser/esbuild 的语义提示，不是 webpack 特性。
- 典型场景：类表达式 `var a = /*#__PURE__*/ (function () { ... })()`、JSX 转译产物、`const el = /*#__PURE__*/ createElement()`——调用本身无全局副作用。
- 常见错误：给有副作用的调用标 PURE（如日志上报、注册逻辑），会被错误删除，且只在压缩后暴露，极难排查。
- 生产验证手段：压缩前后 diff 产物、NODE_ENV=production 重复 grep 关键标识符。
- babel 的 @babel/plugin-transform-react-jsx 自动为 JSX 生成 PURE 注解，这就是"未渲染组件不产生运行时开销"的来源之一。

```javascript
// 有副作用的调用 不能加 PURE 会被删
const result = pureHeavyCompute();      // 若结果未使用且标记 PURE 整个调用被移除

// 正确示例：纯构造
const app = /*#__PURE__*/ createApp(App); // 若 app 未使用 createApp 连同副作用整体删除

// 误用示例（危险）：
// /*#__PURE__*/ initTracker();          // 上报埋点被删除 线上数据缺失
// /*#__PURE__*/ registerElement('x-foo'); // 组件注册被删除 标签不生效

// webpack.config.js：确认压缩器保留注解语义
module.exports = {
  optimization: {
    minimizer: ['...'], // webpack 5 默认 terser 会尊重 /*#__PURE__*/ 注解
  },
};
```
