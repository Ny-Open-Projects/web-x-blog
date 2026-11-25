---
title: [NODE-104] 线程池被大文件 I/O 阻塞的经典案例？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-104：线程池被大文件 I/O 阻塞的经典案例？
**答**：
- libuv 线程池默认 **4 个线程**，且 fs、`dns.lookup`、`crypto.randomBytes/pbkdf2`、zlib 共用——一处堵塞全线遭殃。
- 案例：接口 A 并发读 8 个 500MB 日志，4 个线程全被占住；接口 B 只想算个 pbkdf2 摘要也要排队，P99 飙升但 CPU 不高。
- 特征：**CPU 利用率低 + 事件循环 lag 不高 + I/O 类接口集体变慢** = 线程池饥饿。
- 对策：`UV_THREADPOOL_SIZE=16` 扩容；超大文件改分块流式；密码摘要等重计算挪 worker_threads；域名解析改 `dns.resolve`（不走线程池）。

```javascript
const fs = require('fs');
const crypto = require('crypto');

// 复现排队：8 个大文件读 + 1 个小 pbkdf2 同时发起
const t0 = Date.now();
for (let i = 0; i < 8; i++) fs.readFile('/data/big.log', () => {});
crypto.pbkdf2('pwd', 'salt', 1e5, 32, 'sha256', () =>
  console.log('pbkdf2 观测耗时 ms =', Date.now() - t0));
// 输出远大于其真实计算耗时，差值就是线程池排队时间

// 定量观测：事件循环不受影响（lag 低），但所有线程池 API 变慢
const { monitorEventLoopDelay } = require('perf_hooks');
const h = monitorEventLoopDelay({ resolution: 20 }); h.enable();
setInterval(() => {
  console.log('eventloop p99 ms =', (h.percentile(99) / 1e6).toFixed(1));
  h.reset();
}, 2000).unref();
// 启动：UV_THREADPOOL_SIZE=16 node server.js 可显著缓解
```
