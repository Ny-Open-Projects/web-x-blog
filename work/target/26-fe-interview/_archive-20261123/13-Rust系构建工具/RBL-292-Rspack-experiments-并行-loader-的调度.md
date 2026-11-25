---
title: [RBL-292] Rspack 并行 loader 的调度与限制
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-292：Rspack 并行 loader 的调度与限制

**答**:
- JS loader 跑在 Node 侧（跨边界），Rust 内置 loader（swc 转译）在 Rust 线程池——「内置优先、JS 兜底」是性能关键
- JS loader 并行受 Node 单线程限制：串行队列 + worker 池实验能力（experiments.parallelLoader）——JS loader 数量决定并行收益上限
- 调度策略：按 loader 链拆分——链上任何一个 JS loader 就整条链进 Node；纯内置链全并行（这是「用 builtin:swc-loader 替代 babel-loader 提速」的原理）
- 度量：loader 总耗时 vs 并行化理论值（任务级 profile），差距 = 调度损耗

```javascript
// 链路设计
{ test: /\.ts$/, use: [{ loader: 'builtin:swc-loader' }] }   // 全 Rust 链 → 并行
// 链里混入自定义 JS loader → 整链进 Node 队列
// experiments: { parallelLoader: true }  ← JS loader worker 池（实验）
```
