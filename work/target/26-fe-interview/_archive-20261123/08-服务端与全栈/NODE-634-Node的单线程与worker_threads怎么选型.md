---
title: [NODE-634] Node 的单线程模型与 worker_threads/child_process 怎么选型？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-634：并发模型怎么选型？
**答**：
- 三层模型：事件循环单线程（IO 并发——主战场，async IO 零成本并发）+ worker_threads（CPU 密集/阻塞库——真并行，共享内存 SharedArrayBuffer）+ child_process（独立进程隔离/复用二进制——崩溃隔离与进程级沙箱）。
- 选型判断：任务类型——IO 密集留在主线程；CPU 密集 >10ms 且高频 → worker 池（piscina）；需要隔离（不可信代码/内存泄漏防护/独立崩溃域）→ 子进程；需要共享大内存计算 → worker + SharedArrayBuffer。
- worker 成本：启动 ~30ms + 每实例独立 V8 heap——池化复用（worker 池不是每任务新建）；通信结构化克隆成本（大数据用 Transferable/SharedArrayBuffer 零拷贝）。
- 反模式：用 worker 做 IO（浪费——主线程 async 更高效）；用子进程做高频小任务（进程启动成本远超任务）。
- 追问钩子：为什么「CPU 密集放 worker」不能解决所有慢接口——worker 解决计算但增加通信与调度开销；慢接口的根因如果是「阻塞式同步 IO」（如 fs.readFileSync 在请求路径），worker 只是把阻塞搬走而非消除——正确解法是消除阻塞调用本身；worker 是兜底不是万能。

```javascript
// worker 池（piscina 模式）
const Piscina = require('piscina');
const pool = new Piscina({ filename: './cpu-task.js', maxThreads: os.cpus().length - 1 });
app.post('/render', async (req, res) =>
  res.send(await pool.run(req.body)));               // CPU 密集进池
// 大数据零拷贝
const sab = new SharedArrayBuffer(1024 * 1024);
worker.postMessage({ buf: sab }, [sab]);              // Transferable
```
