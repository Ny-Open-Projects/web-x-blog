---
title: [BLD-261] 构建器的性能剖析（profiling）怎么做的？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-261：构建 profiling 怎么做？
**答**：
- 剖析维度：阶段耗时（resolve/transform/minify/emit）、模块耗时 TopN（哪些模块转换最慢）、插件耗时（每个 hook 的占用）、并行利用率（worker 空闲率）。
- 工具链：构建器自带 profile（webpack --profile/speed-measure/rspack trace）+ Node 火焰图（--cpu-prof——JS 层热点）+ Rust 工具的 trace（perf/tokio-console）。
- 剖析驱动优化的标准动作：Top 插件替换/收窄、慢模块的 include 收窄、压缩并行度调整——每次优化有 before/after 数据（SCN-ENG-221 方法论）。
- 剖析的常态化：剖析不是一次性诊断，随构建遥测（SCN-ENG-269）持续采样——性能劣化的哨兵数据源。
- 追问钩子：为什么「插件耗时」往往比「模块转换耗时」更容易藏住性能问题——模块转换有天然上限（每个文件毫秒级），而插件 hook 可能对全量资源做 O(n²) 操作（如一个在 emit 阶段遍历所有 chunk 组合的插件）——单个插件占构建 50% 不罕见；剖析按 hook 维度拆分才能发现这类「结构性慢」。

```javascript
// speed-measure 插件级剖析
const smp = new SpeedMeasurePlugin();
module.exports = smp.wrap({ plugins: [a, b, c] });    // 每个 plugin/loader 的耗时
// CPU 火焰图
node --cpu-prof --cpu-prof-dir=./prof build.js
// 持续采样（遥测）
telemetry.hooks = measuredHooks;   // 每个 hook 的耗时进遥测
```
