---
title: [OPT-034] Web Worker 通信与 Transferable Objects 如何落地？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-034：Web Worker 通信与 Transferable Objects 如何落地？

**答**：
- 主线程与 Worker 通信默认是 structured clone（深拷贝），传 100MB 数据本身就耗时数百 ms，反而造成卡顿。
- Transferable Objects 解决该问题：`ArrayBuffer`、`MessagePort`、`OffscreenCanvas`、`ReadableStream` 等支持**移交所有权**，零拷贝，但移交后原线程不能再访问。
- 更进一步用 `SharedArrayBuffer`（需跨域隔离头 COOP/COEP）+ `Atomics` 真正共享内存。
- 典型场景：大 JSON 解析、图片/视频处理、加解密、WebSocket 心跳外的数据加工。

```javascript
// 一一对应：Transferable 零拷贝移交 vs structured clone 对比
// main.js
const worker = new Worker('worker.js');

// 方式一：structured clone，100MB 数据拷贝一次，主线程被阻塞
const cloned = bigArrayBuffer;
worker.postMessage({ buf: cloned });

// 方式二：Transferable，零拷贝瞬时移交，主线程侧原 buffer 变为不可用
const buf = new ArrayBuffer(100 * 1024 * 1024);
const view = new Float64Array(buf);
for (let i = 0; i < view.length; i++) view[i] = i;

console.time('transfer');
worker.postMessage({ buf }, [buf]); // 第二个参数是转移列表
console.timeEnd('transfer');        // 几乎 0ms
console.log(buf.byteLength);        // 0 —— 所有权已移交

// worker.js：接收后直接可用
// self.onmessage = ({ data }) => {
//   const arr = new Float64Array(data.buf);
//   let sum = 0;
//   for (let i = 0; i < arr.length; i++) sum += arr[i];
//   self.postMessage(sum);
// };
```
