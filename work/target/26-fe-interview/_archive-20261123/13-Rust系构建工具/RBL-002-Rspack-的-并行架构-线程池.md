---
title: [RBL-002] Rspack 的并行架构是怎么设计的？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-002：Rspack 的并行架构是怎么设计的？
**答**：
- 总体是"JS 宿主 + Rust 核心"的混合架构：Rspack 进程里跑一个 Node 宿主负责读取配置、执行 JS Loader/Plugin，Rust 核心负责模块图、解析、生成产物。
- 并行主引擎是 Rayon 工作窃取线程池：parse、transform、minify 等"可按模块切分"的任务提交进池，默认线程数等于 CPU 核数。
- JS 与 Rust 之间的边界用 FFI（napi-rs）：JS 侧回调（loader、plugin 钩子）被调度回 libuv 线程执行，执行结果再封包传回 Rust；这类跨边界调用是主要串行化点，所以 Rspack 建议减少 JS loader/plugin 数量。
- 任务类型区分：CPU 密集（编译、压缩）进 Rayon；IO 密集（读文件、写产物）用 tokio 异步运行时，互不阻塞。
- 追问钩子：这也是"为什么 Rspack 不实现全部 webpack 插件 API"的根因——很多 webpack 插件依赖在任意时机同步改 JS 对象图，跨 FFI 频繁同步代价过高。

```text
Node 宿主进程
├── JS 侧：读 rspack.config.js、执行 JS loader/plugin（libuv 线程）
│     ↑↓ napi-rs FFI（数据封包 + 回调调度，串行化瓶颈点）
└── Rust 核心
      ├── tokio 异步任务：文件 IO、监听
      └── Rayon 线程池（N = CPU 核数）
            ├── 并行 parse（swc_ast → 模块元信息）
            ├── 并行 transform（loader 的 Rust 内置实现）
            ├── 并行 minify（内置 swc 压缩器）
            └── 模块图构建 / chunk 生成（图算法，部分可并行）
关键点：JS loader 越多，FFI 往返越多，并行度越低 → 迁移优先换内置 loader
```
