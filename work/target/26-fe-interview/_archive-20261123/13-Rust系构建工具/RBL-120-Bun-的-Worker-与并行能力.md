---
title: [RBL-120] Bun 的并行能力（Worker/线程/进程）与 Node 的对比？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-120：Bun 的并行能力（Worker/线程/进程）与 Node 的对比？
**答**：
- Bun 支持 Web 风格 Worker（new Worker(new URL('./w.ts', import.meta.url))），直接跑 TS，消息传递支持结构化克隆与可转移对象；CPU 密集任务用 Worker 池。
- 对比 Node worker_threads：语义相似（隔离堆 + 消息通信），Bun 的优势是免转译与更快的启动（JSC 轻量）；差异是生态兼容（Node 的 worker 特有 API 如 MessagePort 细节）。
- 单进程内的"并行"JS：JS 执行仍是单线程事件循环，并行靠 Worker；IO 并行靠原生异步（Zig 层）。
- 适用：图像处理、大 JSON 解析、压缩等 CPU 任务拆 worker；注意数据转移（Transferable/SharedArrayBuffer）减少拷贝。
- 追问钩子：并行设计的要点是"任务粒度"——worker 通信开销可能吃掉并行收益，先量化单任务耗时再拆。

```typescript
// main.ts
const workers = Array.from({ length: navigator.hardwareConcurrency }, () =>
  new Worker(new URL('./worker.ts', import.meta.url)));
const results = await Promise.all(
  chunks.map((c, i) => new Promise(res => {
    workers[i].postMessage(c);
    workers[i].onmessage = (e) => res(e.data);
  })));
// worker.ts
self.onmessage = (e) => self.postMessage(heavyCompute(e.data));
```
