---
title: [NODE-348] Node 服务的进程模型：cluster 与 worker_threads 如何分工？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-348：cluster 与 worker_threads 分工
**答**:
- 分工原则：cluster（多进程）用于扩展 HTTP 吞吐与故障隔离（单 worker 崩溃不影响其他）；worker_threads 用于进程内 CPU 密集任务（不影响事件循环）。两者正交：K8s 场景每 Pod 单进程 + HPA 扩容，替代 cluster。
- worker_threads 细节：传 ArrayBuffer 用 transferList 零拷贝；SharedArrayBuffer 共享大数据（配 Atomics 同步）；每 worker 独立事件循环，创建有成本（池化复用）；消息传递是结构化克隆（大对象序列化成本，改传 buffer）。
- cluster 细节：请求分发默认 round-robin（Linux）；端口共享由 master 转发；session/缓存不共享（各进程独立——共享状态外置 Redis）；master 不做重业务（只做守护）。
- 崩溃策略：worker uncaughtException → 记录快照 → 重启（退避防风暴，ARC-308）；重启预算（每分钟重启次数上限）防死循环。
- 何时都不用：IO 密集（Node 天然擅长）；CPU 密集才考虑下沉。
```javascript
// worker 池（CPU 任务）
import { Worker } from 'worker_threads';
class WorkerPool {
  constructor(size) { this.idle = Array.from({ length: size }, () => new Worker('./cpu-worker.js')); }
  run(buf) {
    const w = this.idle.pop();
    return new Promise((res, rej) => {
      w.postMessage(buf, [buf]);                                  // 零拷贝转移
      w.once('message', r => { this.idle.push(w); res(r); });
      w.once('error', rej);
    });
  }
}
```
