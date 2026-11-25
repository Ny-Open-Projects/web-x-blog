---
title: [RBL-560] Rust 构建器的并行模型：rayon 数据并行 vs tokio 任务并发的分工
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-560：Rust 构建器的并行模型：rayon 数据并行 vs tokio 任务并发的分工

**答**：
- 构建器里两类并行要分开：**CPU 密集**（transform/minify/chunk 生成）用 rayon 数据并行（work-stealing 线程池按核数满载）；**IO/等待密集**（读文件/网络 resolve/插件回调）用 tokio 异步任务——混用会导致线程池互相饿死。
- 分工原则：模块图的解析阶段是「fan-out IO」（上千个文件 stat/read）→ tokio spawn 并发读；拿到源码后的 transform 阶段是纯 CPU → `par_iter` 分发到 rayon；两者交接用 channel（如 tokio mpsc → rayon scope）。
- 线程池隔离的理由：rayon 默认假设任务短且 CPU-bound，若塞进 await 会阻塞 worker 让并行度崩塌；反过来 IO 任务占满 tokio 池也会拖慢事件循环。SWC 的 n_threads 配置、rolldown 的并行 transform 都是这个模型。
- 同步原语选择：模块图结构用 `RwLock<ModuleGraph>` 或更细的 per-module 锁（dashmap）——粗粒度全局锁是并行扩展性的头号杀手；写少读多场景优先 snapshot + COW。
- 追问钩子：为什么不全异步？——Rust 的 async 对 CPU 任务无收益（没有线程切换的让出点），且 async fn 里的阻塞会传染；「IO 用 async、CPU 用 rayon」是生态共识（如 turbopack 也是混合运行时）。

```javascript
// 概念示意：构建管线的并行分层（Rust 伪代码）
// 阶段1 IO：tokio 并发读取
let sources = futures::stream::iter(paths)
  .map(|p| async move { fs::read(p).await })
  .buffer_unordered(256).collect::<Vec<_>>().await;

// 阶段2 CPU：rayon 并行 transform
let outputs: Vec<Module> = sources
  .into_par_iter()
  .map(|src| swc_transform(src))       // 纯 CPU，无 await
  .collect();

// 阶段3：模块图更新（细粒度锁）
// graph: DashMap<ModuleId, ModuleState>  // per-module 锁，避免全局 RwLock 串行化

// 反模式示例（面试考点）：
// rayon::spawn(async { io().await })  // ✗ await 阻塞 rayon worker
// tokio::task::spawn_blocking 里做全量 minify 后又回 async 串行收集 // ✗ 白并行
```
