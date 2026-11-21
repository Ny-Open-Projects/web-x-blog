---
title: [RBL-212] Rolldown 的 Tree-Shaking 为什么能比 Rollup 更快
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-212：Rolldown 的 Tree-Shaking 为什么能比 Rollup 更快

**答**:
- 算法同源（ECMA 规范的 live-binding 分析），快在实现：Oxc 解析一次产出 AST + 符号表，分析在内存中原地做，无 JS 序列化开销
- 符号级而非语句级：引用图按符号（binding）建边，副作用标注（/*#__PURE__*/ 与 sideEffects 字段）参与剪枝
- 兼容性注意：sideEffects: false 的包语义与 Rollup/webpack 一致；CJS 互操作模块默认可摇（有静态分析的范围内）
- 验证方法：rolldown 打包前后对比产物符号（导出未引用的函数是否被剪），与 Rollup 产物 diff 建立基线

```javascript
// sideEffects 标注参与剪枝
// package.json: { "sideEffects": ["*.css"] }   ← css 保留，js 剪
// #__PURE__ 注解：IIFE 调用无副作用可剪
const config = /*#__PURE__*/ createConfig()
```
