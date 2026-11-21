---
title: [H5-232] Worker 消息传递为什么慢：structured clone
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, Worker]
type: 面试题
---

## H5-232：Worker 消息传递为什么慢：structured clone

**答**：
- postMessage 默认对数据做 structured clone（深拷贝），大数据（几 MB 的数组/对象）拷贝一次几十毫秒，主线程与 Worker 双向都卡
- 函数/DOM 节点/Error 等不可克隆，静默丢失或报错（DataCloneError）
- 加速手段一：Transferable 对象（ArrayBuffer/MessagePort/ImageBitmap）零拷贝转移所有权，传后原线程失效
- 加速手段二：SharedArrayBuffer 共享内存，零拷贝共享读写（需要 Atomics 同步，且要求 COOP/COEP 头）
- 工程建议：频繁大数据交互的场景用「SharedArrayBuffer + 帧号协议」或 Comlink 的代理模式降低心智负担

```javascript
// 100MB 数组：clone vs transfer 差距巨大
const big = new Float32Array(25 * 1024 * 1024); // ~100MB
worker.postMessage(big.buffer, [big.buffer]);   // transfer：微秒级，原线程变 null
// worker.postMessage(big.buffer);               // clone：几十 ms，两边各自持有副本
```
