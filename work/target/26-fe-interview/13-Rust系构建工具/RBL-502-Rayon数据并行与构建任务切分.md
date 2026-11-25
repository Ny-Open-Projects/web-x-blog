---
title: [RBL-502] Rayon 数据并行：构建任务怎么切分给线程池
date: 2026-11-21
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-502：Rayon 数据并行：构建任务怎么切分给线程池

**答**：
- Rayon 是 Rust 的数据并行库（work-stealing 线程池）：`par_iter().map(...)` 把集合切分给线程池执行——构建器的天然并行点：模块转换（每模块独立）、压缩（每 chunk 独立）、SourceMap 生成。
- 任务切分的粒度问题：**过细（每模块一次任务调度）→ 调度开销占比高；过粗（整库一次任务）→ 无并行**。Rspack 的实践：模块级并行转换（粒度 = 模块）+ chunk 级并行压缩（粒度 = chunk）——两级粒度因为两阶段耗时分布不同。
- work-stealing 的意义：任务耗时不均（大模块 vs 小模块）时，空闲线程偷队列任务，负载自动均衡——比静态均分好，但「偷」有锁成本，任务队列要分本地/全局两级。
- 与 tokio 的分工：Rayon 管 CPU 密集（转换/压缩），tokio 管 IO 密集（文件读写/网络）——混用会饿死（CPU 任务占满 Rayon 线程阻塞 tokio runtime），Rspack 用独立 runtime 隔离。
- 追问钩子：并行的 Amdahl 定律约束——串行部分（模块图构建/依赖解析的拓扑排序）决定加速上限：并行化 90% 的部分 8 核只加速 ~4.7x——所以「先找串行瓶颈再并行」是构建器优化的顺序。

```javascript
// Rayon 并行与构建任务切分
use rayon::prelude::*;

// 模块级并行转换（粒度=模块）
let transformed: Vec<Module> = modules
  .par_iter()                       // work-stealing 线程池
  .map(|m| transform(m, &swc_options))
  .collect();

// chunk 级并行压缩（粒度=chunk，terser 换 swc 压缩器）
let minified: Vec<Chunk> = chunks
  .par_iter()
  .map(|c| minify(c))
  .collect();

// 串行瓶颈（Amdahl）：模块图拓扑排序无法并行
// 加速上限 = 1 / (serial + parallel/cores)
// 90% 并行化 @ 8 核 → 1/(0.1+0.9/8) ≈ 4.7x
// 顺序：先找串行瓶颈（图构建/解析）再并行转换
```
