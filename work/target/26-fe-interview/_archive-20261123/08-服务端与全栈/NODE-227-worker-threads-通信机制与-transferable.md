---
title: [NODE-227] worker_threads 通信机制与 transferable？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-227：worker_threads 通信机制与 transferable？
**答**：
- postMessage 结构化克隆：对象深拷贝（大 Buffer 成本高）；transferList（ArrayBuffer/MessagePort）零拷贝转移所有权——大 Buffer 传 worker 必用。
- MessageChannel：worker 间直连（不经主线程中转）——环形拓扑的任务分发。
- workerData vs postMessage：初始化数据（启动时一次）用 workerData；运行时消息用 postMessage。
- 陷阱：transfer 后主线程的 Buffer 变空（所有权转移）；未 transfer 的大对象序列化卡顿（主线程阻塞——用了 worker 却还在卡）。

```javascript
import { Worker, MessageChannel } from 'node:worker_threads';
// transferable：零拷贝
const buf = Buffer.from(await fs.readFile('image.raw'));
worker.postMessage(buf, [buf.buffer]);        // ArrayBuffer 所有权转移给 worker
// 主线程 buf 现在不可用（length 0）——转移语义
// worker 侧返回也要 transfer：
// parentPort.postMessage(result, [result.buffer]);
// MessageChannel：worker 直连
const { port1, port2 } = new MessageChannel();
w1.postMessage({ port: port2 }, [port2]);     // port2 转移给 w1
w2.postMessage({ port: port1 }, [port1]);
// 此后 w1/w2 直接互发，主线程不再中转（大结果直传）
```
