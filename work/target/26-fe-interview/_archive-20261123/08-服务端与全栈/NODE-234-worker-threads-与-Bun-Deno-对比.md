---
title: [NODE-234] worker_threads 与 Bun/Deno 的并发模型对比？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-234：worker_threads 与 Bun/Deno 的并发模型对比？
**答**：
- 三家一致的底座：单线程事件循环 + 线程池卸载 CPU。
- Node：worker_threads（V8 实例 per worker）+ libuv 线程池（fs/crypto 默认并行）。
- Bun：Worker API（Web 标准）+ JSC 隔离（每 worker 独立 isolate），启动比 V8 worker 快。
- Deno：Web Worker（标准 API）+ ops 桥接；最近强调 worker pool 库。
- 迁移视角：Web 标准 API（Worker/MessageChannel/SharedArrayBuffer）三家通用——代码尽量落在标准面，平台特化（worker_threads 细节）隔离在适配层。

```javascript
// 跨运行时适配层示意
function createCpuPool() {
  if (typeof WorkerGlobalScope !== 'undefined' && globalThis.Worker) {
    // Bun / Deno / 浏览器：Web Worker
    return new WebWorkerPool(new URL('./worker.js', import.meta.url));
  }
  return new Piscina({ filename: './worker.js' });     // Node：worker_threads
}
// 标准面：postMessage / MessageChannel / Atomics 三家语义一致
// 特化面：Node 的 transferList 细节、Bun 的快速启动、Deno 的 permission 模型
```
