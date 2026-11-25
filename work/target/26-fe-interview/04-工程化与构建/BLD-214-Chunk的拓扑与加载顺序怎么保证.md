---
title: [BLD-214] Chunk 的拓扑与加载顺序怎么保证？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-214：Chunk 拓扑怎么保证？
**答**：
- chunk 图：入口 chunk → 同步依赖 chunk（必须先行）→ 异步 chunk（按需）；共享 chunk 被多个入口引用时「提升」到公共层。
- 加载保证：runtime 按 chunk 依赖图生成加载顺序（父 chunk 内嵌依赖清单）；modulepreload 链条（SCN-ENG-325）保证网络层并行。
- 循环 chunk 依赖：打包器强制 chunk 图无环（模块分配阶段打破），环会导致加载死锁。
- 顺序错误的症状：「xxx is not defined」——共享 chunk 未先加载；排查看 runtime 的 chunk 依赖清单。
- 追问钩子：为什么打包器必须在「模块分配阶段」保证 chunk 图无环——runtime 按依赖序加载 chunk，环意味着 A 等 B、B 等 A，谁先加载都缺依赖——死锁；所以分包算法（如 rollup 的 chunk 分配）在 assign 阶段就把循环依赖的模块合并到同一 chunk 或提升到公共父级。

```javascript
// chunk 依赖图
{ main: { deps: ['vendor-react'] },
  'async-chart': { deps: ['vendor-d3', 'shared-ui'] } }
// 加载顺序保证：main 加载前 preload vendor-react
<link rel="modulepreload" href="vendor-react.js">
```
