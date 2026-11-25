---
title: [BLD-222] Rollup 的 Scope Hoisting（作用域提升）原理是什么？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-222：Scope Hoisting 原理？
**答**：
- 原理：ESM 静态分析下，把多个模块的顶层作用域「拍平」进一个作用域（concatenated modules）——消除每模块的函数包装（webpack CJS wrapper 的开销）。
- 收益：减少函数调用与闭包创建（运行时性能）、体积显著缩小（无 wrapper 样板）、利于压缩器（同作用域内联）。
- 前提与失败：只有 ESM 才可 hoisting；CJS 模块/动态导出/顶层 this 依赖会「打破」拼接（该模块退回独立包装）。
- webpack 对应：optimization.concatenateModules（module concatenation plugin）。
- 追问钩子：为什么「顶层 this 指向」会打破作用域拼接——CJS 中 this === module.exports，ESM 顶层 this 是 undefined；拼接后多模块共享作用域，this 的语义无法统一——打包器把引用顶层 this 的模块排除出拼接单元，保留独立包装；这类「语义不可拍平」的场景是 hoisting 收益低于理论值的主因。

```javascript
// 拼接前（webpack wrapper）
/* 0 */ function (module, exports) { export const a = 1 }   // 伪码
/* 1 */ function (module, exports) { const b = a + 1 }
// 拼接后（rollup）
const a = 1; const b = a + 1;                        // 单作用域拍平
// 打破拼接：顶层 this / 动态 require / 修改 exports
```
