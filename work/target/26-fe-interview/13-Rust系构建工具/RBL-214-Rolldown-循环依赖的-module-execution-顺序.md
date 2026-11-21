---
title: [RBL-214] Rolldown 怎么处理循环依赖的执行顺序
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-214：Rolldown 怎么处理循环依赖的执行顺序

**答**:
- ESM 循环依赖语义：模块提升 hoisting（函数声明可用），绑定 live binding（TDZ 内访问报错）——Rolldown 按 ESM 规范保证与 Rollup/浏览器原生行为一致
- chunk 闭合规则：循环依赖的模块尽量落在同一 chunk，避免跨 chunk 循环（加载顺序复杂化）；无法闭合时保持执行顺序标注
- 实践排查：循环依赖导致 undefined 报错的，先用 madge/depcruise 找环，再决定打破（依赖倒置）还是合并 chunk
- CJS 循环更宽松（部分导出对象），互操作时 Rolldown 保留 CJS 语义——混合 ESM/CJS 项目重点回归场景

```javascript
// a.js ↔ b.js 循环：函数声明 OK，顶层求值 TDZ 风险
// a.js
import { bFn } from './b.js'
export function aFn() { return bFn() }        // ✓ 延迟调用
// export const aVal = bFn()                   // ✗ 初始化期 TDZ
```
