---
title: [BLD-221] Rspack 与 Webpack 的架构差异（快在哪）？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-221：Rspack 快在哪？
**答**：
- 三大差异：① 原生实现（Rust 多线程无 GC 停顿 vs JS 单线程+GC）；② 增量编译内建（模块级失效图一等公民 vs webpack 需 watch 模式）；③ 并行无序列化开销（原生共享数据 vs JS worker IPC）。
- 兼容策略：webpack API 兼容层（loader/大部分插件可直接用）——迁移成本主要在少数深度依赖 tapable 内部行为的插件。
- 差异代价：原生扩展门槛高（Rust 插件）——纯 JS 生态的复杂插件是迁移短板。
- 选型判断：webpack 大仓构建慢 → Rspack 收益大；强依赖 webpack 特有插件生态 → 先混合（dev 用 rspack）。
- 追问钩子：为什么「JS 单线程 + GC」是 webpack 慢的结构性原因而非优化不足——webpack 的核心循环（模块图遍历/转换调度）在 JS 里跑，数千模块的图操作产生大量临时对象（GC 压力）且只能单线程（JS 限制）；Rust 无 GC + 数据竞争安全的并行是语言级优势——这不是配置优化能追平的差距。

```javascript
// rspack.config.js —— webpack 兼容
module.exports = {
  resolve: { alias: {...} },                          // 大部分配置直接复用
  plugins: [new HtmlWebpackPlugin()],                 // 兼容插件
  experiments: { css: true },
};
// benchmark: webpack 90s → rspack 9s（10× 量级）
```
