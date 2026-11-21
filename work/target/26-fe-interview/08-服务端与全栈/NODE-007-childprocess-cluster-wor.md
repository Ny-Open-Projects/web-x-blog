---
title: [NODE-007] child_process、cluster、worker_threads 三者如何对比与选型？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-007：child_process、cluster、worker_threads 三者如何对比与选型？
**答**：
- **child_process**：创建独立 OS 进程（`spawn`/`exec`/`execFile`/`fork`），内存隔离最彻底，开销最大，进程间只能 IPC 或序列化通信；`exec` 会起 shell，有命令注入风险，传参务必用 `execFile`/`spawn`。
- **cluster**：基于 `child_process.fork` 的封装，多个进程 `fork` 同一个入口，主进程做负载均衡（默认 round-robin，Linux 下可 reuseport），用于**多核 HTTP 服务**；进程间不共享内存。
- **worker_threads**：**同一个进程内**的多线程，真正共享内存可用 `SharedArrayBuffer`，适合 CPU 密集任务（图片处理、加密计算），开销远小于进程；但一个 worker 崩溃不会拖垮主线程，而主线程异常仍影响 worker 的通信。
- 选型口诀：跑额外命令用 child_process；多核 Web 服务用 cluster/PM2；进程内 CPU 密集用 worker_threads。

```javascript
// worker_threads：CPU 密集任务不阻塞主线程
const { Worker, isMainThread, parentPort, workerData } = require('node:worker_threads');

if (isMainThread) {
  console.time('fib in worker');
  const worker = new Worker(__filename, { workerData: { n: 40 } });
  worker.on('message', (r) => { console.timeEnd('fib in worker'); console.log('result', r); });
  worker.on('error', (e) => console.error('worker error', e));
} else {
  // 子线程中执行递归 fib（故意 CPU 密集）
  const fib = (n) => (n <= 1 ? n : fib(n - 1) + fib(n - 2));
  parentPort.postMessage(fib(workerData.n));
}

// cluster：多核 HTTP 服务（对比参考）
// const cluster = require('node:cluster'); const http = require('node:http');
// if (cluster.isPrimary) {
//   for (let i = 0; i < require('node:os').cpus().length; i++) cluster.fork();
//   cluster.on('exit', (w) => cluster.fork()); // 进程守护自动拉起
// } else {
//   http.createServer((req, res) => res.end(`pid ${process.pid}`)).listen(3000);
// }
```
