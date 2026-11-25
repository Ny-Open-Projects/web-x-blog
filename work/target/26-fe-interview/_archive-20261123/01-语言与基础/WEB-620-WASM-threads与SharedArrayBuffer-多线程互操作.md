---
title: [WEB-620] WASM threads 与 SharedArrayBuffer：多线程互操作
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 面试题, WebAssembly]
type: 面试题
---

## WEB-620：WASM threads 与 SharedArrayBuffer：多线程互操作

**答**：
- WASM threads 模型：主 wasm 模块 + 多个 wasm worker 共享同一 SharedArrayBuffer 线性内存，线程间用 Atomics（wait/notify/compareExchange）同步
- 前提硬性：页面必须 crossOriginIsolated（COOP+COEP），否则 SharedArrayBuffer 不可用——这是 WASM 多线程上线的前置工程
- 与 JS 交互的关键：worker 里的 wasm 实例要用共享内存实例化（import 的 memory 是 SAB），每个线程独立实例但共享内存段
- 坑：主线程把 SharedArrayBuffer postMessage 给 worker 是转移语义中的特殊情形（SAB 不转移所有权而是共享）；非 SAB 的 ArrayBuffer 才是转移
- 实战建议：线程数不超过 navigator.hardwareConcurrency，任务粒度要远大于线程同步成本；调试用 Atomics 输出 + 控制台约定格式

```javascript
// 主线程: 创建共享内存并分发给 workers
const memory = new WebAssembly.Memory({ initial: 64, maximum: 256, shared: true });
const sab = memory.buffer; // SharedArrayBuffer
const workers = Array.from({ length: navigator.hardwareConcurrency - 1 }, () => {
  const w = new Worker('wasm-worker.js');
  w.postMessage({ wasmUrl, sab }, [/* SAB 不转移, 直接传 */]);
  return w;
});
// wasm-worker.js: 用同一 SAB 实例化, Atomics 同步
// const { instance } = await WebAssembly.instantiateStreaming(fetch(wasmUrl),
//   { env: { memory: new WebAssembly.Memory({ initial: 64, shared: true }) } });
```
