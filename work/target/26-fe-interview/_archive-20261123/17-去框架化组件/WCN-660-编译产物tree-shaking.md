---
title: [WCN-660] 编译产物如何设计才能对 tree-shaking 友好？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-660：编译产物如何设计才能对 tree-shaking 友好？

**答**：
- 结论：用 ESM 静态导入、纯函数、无顶层副作用；指令/组件按独立模块导出，让打包器能摇掉未用部分。
- 做法：编译生成 import { helperA } from 'runtime' 而非整体导入；用 /*#__PURE__*/ 标注纯调用；避免 IIFE 与动态属性访问。
- 追问钩子：为什么副作用是 tree-shaking 的敌人？因为打包器无法证明删除是否安全——考察对「副作用标注」的实践认知。

```javascript
// 不友好：整体导入 + 顶层副作用
// import * as runtime from 'runtime'; runtime.init();
// 友好：按需导入 + 纯标注
import { createElement as h, createEffect as e } from './runtime.js';
export function Comp(props) {
  const el = /*#__PURE__*/ h('div');
  /*#__PURE__*/ e(() => { el.textContent = props.text(); });
  return el;
}
// 未用到的 helper 可被摇掉；/*#__PURE__*/ 告诉打包器"此调用无副作用"
```
