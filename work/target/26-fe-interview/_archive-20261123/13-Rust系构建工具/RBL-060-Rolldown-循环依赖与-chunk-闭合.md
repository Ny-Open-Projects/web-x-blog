---
title: [RBL-060] Rolldown 如何处理循环依赖与 chunk 依赖闭合？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-060：Rolldown 如何处理循环依赖与 chunk 依赖闭合？
**答**：
- 循环依赖基础处理与 rollup 一致：模块图中环存在时按"模块执行顺序"做 hoist，ESM 的 live binding 语义保证引用最终拿到值；CJS 环则可能拿到 undefined（导出尚未赋值）。
- chunk 化后的新问题：抽 chunk 可能把环切开（A 环里 a、b 被分进不同 chunk），造成 chunk 间循环 import，浏览器加载顺序敏感时出错。
- rolldown 的处理：chunk 分割算法保证依赖闭合（closed chunks）——与循环相关联的模块要么合并进同一 chunk，要么抽出公共部分，避免跨 chunk 环。
- manualChunks 的典型事故：把环上模块强行分到两个 chunk → 运行时 "Cannot access before initialization"；advancedChunks 的闭合计算规避此问题。
- 排查手段：rolldown 会报 circular dependency 警告，先修源码再谈分割。
- 追问钩子：ESM 的 TDZ 与 live binding 是理解这类运行时错误的理论基础。

```javascript
// 循环依赖示例
// a.js: import { b } from './b'; export const a = () => b() + 1;
// b.js: import { a } from './a'; export const b = () => a() + 1;
// manualChunks 若把 a/b 分进两个 chunk → chunk 间循环 import
// rolldown advancedChunks：a/b 依赖闭合 → 自动合进同一 chunk
console.log('规则：chunk 分割不得切开循环依赖（closure 保证）');
```
