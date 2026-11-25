---
title: [BLD-212] 打包器的并行化（worker 池）怎么运作？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-212：并行化怎么运作？
**答**：
- 并行层级：模块转换并行（babel-loader 多进程/原生多线程）、入口级并行（多 entry 并发构建）、压缩并行（terser 按 chunk 分片多进程）。
- worker 通信成本：序列化 AST/源码的开销——粒度太小（每模块一个任务）通信开销吞掉收益；批量化（每 worker 处理一批模块）是关键。
- 原生实现的碾压：Rspack/esbuild 在 Rust/Go 内部多线程，无序列化开销——JS 层 worker 池是历史方案，原生并行是现在。
- 并行与缓存协同：worker 结果直接写持久缓存（SCN-BLD-211），下次跳过。
- 追问钩子：为什么 babel-loader 开 thread-loader 有时反而更慢——每模块任务经 IPC 序列化传输（源码+options），小模块的传输开销超过转换本身；并行收益的阈值是「单模块转换耗时 > 通信开销」，所以 thread-loader 对大文件项目有效、小模块海量项目负收益——粒度决定并行有效性。

```javascript
// webpack 历史方案（现多为原生替代）
{ loader: 'thread-loader', options: { workers: 4, poolTimeout: 2000 } },   // 批处理池
{ loader: 'babel-loader' }
// 压缩并行
new TerserPlugin({ parallel: 4, terserOptions: {...} })
```
