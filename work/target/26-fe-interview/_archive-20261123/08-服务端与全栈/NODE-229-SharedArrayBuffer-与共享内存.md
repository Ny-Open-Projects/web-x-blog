---
title: [NODE-229] SharedArrayBuffer 与共享内存？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-229：SharedArrayBuffer 与共享内存？
**答**：
- SharedArrayBuffer：worker 间真正的共享内存（零拷贝双向），配合 Atomics（原子操作）实现锁/计数器/信号量。
- 使用姿势：SAB + Atomics.wait/notify（worker 阻塞等待，主线程 notify）——手写互斥锁的基础。
- 适用：大数据集只算不传（百万级浮点矩阵）、高频小消息（消息环形缓冲区）。
- 风险：竞态条件——Atomics 是唯一安全访问方式；无 GC 越界问题但要自己管理长度（Atomics.load/store）。

```javascript
// const { SharedArrayBuffer } = require('node:worker_threads'); // 或全局（Node 22 全局可用）
// 主线程
const sab = new SharedArrayBuffer(1024);
const counter = new Int32Array(sab);
const worker = new Worker('./w.js', { workerData: { sab } });
Atomics.store(counter, 0, 0);
Atomics.notify(counter, 0);                    // 唤醒等待的 worker
// worker（w.js）
const counter = new Int32Array(workerData.sab);
Atomics.wait(counter, 0, 0);                   // 阻塞直到 counter[0] ≠ 0
const v = Atomics.load(counter, 0);
Atomics.add(counter, 0, 1);                    // 原子自增：无竞态
parentPort.postMessage(v);
```
