---
title: [BLD-218] ESM 与 CJS 的打包互操作边界在哪里？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-218：互操作边界在哪？
**答**：
- 核心不对称：CJS 允许条件 require / 导出任意结构（exports 可变）；ESM 静态——打包器把 CJS 视为「黑盒」（无法 tree-shake），把 ESM 的 default/named 映射进 CJS 语义。
- 常见断点：CJS 包「模块级副作用 + 动态 require」（bundled 全量）；ESM 导入 CJS 的 named import（打包器静态分析 CJS 导出——cjs-module-lexer 启发式，动态导出抓不到）。
- exports 条件的双生态：import 条件给 ESM 消费者、require 给 CJS——双构建产物必须语义一致（dual package hazard：同包两实例）。
- 解法：包作者提供 ESM 入口 + 使用者强制单实例（alias 统一入口/resolve 条件一致）。
- 追问钩子：为什么 dual package hazard（双实例）在 monorepo 特别高发——pnpm 严格隔离下，A 包走 require 条件拿到 CJS 实例、B 包走 import 拿到 ESM 实例——同一 npm 包两个实例（instanceof 失败/单例失效）；解法是全仓统一 resolve 条件或包本身只提供单一 ESM 入口。

```javascript
// cjs-module-lexer 的启发式
exports.foo = 1; module.exports.bar = 2;            // 可静态分析
Object.defineProperty(exports, 'x', { get() {...} }); // 不可分析 → named import 失败
// dual hazard 解法
resolve: { conditionNames: ['import'] }              // 全仓统一条件
```
