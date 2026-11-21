---
title: [ENG-028] Tree-shaking 的原理是什么？sideEffects 有什么用？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-028：Tree-shaking 的原理是什么？sideEffects 有什么用？
**答**：
- 原理：基于 ESM 的静态结构，标记模块中未被使用的 export，压缩阶段删除死代码。
- 只对静态可分析的 import/export 有效，CJS 的动态 require 无法摇掉。
- package.json 的 sideEffects: false 告诉打包器"所有文件都无副作用"，未引用的模块可整体删除。
- 有副作用的文件必须显式列入数组（如 CSS、带 polyfill 的模块），否则误删出 bug。

```javascript
// utils.js
export function used() {
  return 1;
}

export function unused() {
  return 2; // 未被任何入口 import，生产构建中会被移除
}

// package.json 中配合声明：
// "sideEffects": ["*.css", "*.scss"]
// 表示除样式文件外全部无副作用，可放心 tree-shaking
```
