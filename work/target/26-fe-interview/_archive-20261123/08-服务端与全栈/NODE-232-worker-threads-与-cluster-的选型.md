---
title: [NODE-232] worker_threads 与 cluster 的选型？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-232：worker_threads 与 cluster 的选型？
**答**：
- 维度对比：内存（worker 同进程共享 V8 基座，cluster 每进程独立内存）、隔离性（worker 崩溃可能波及主线程，cluster 完全隔离）、通信成本（worker 低，cluster IPC 序列化）、适用对象（worker = CPU 任务卸载，cluster = 服务多核扩容）。
- 组合形态（生产常见）：cluster/PM2 起多进程扩容吞吐 + 每进程内 worker pool 处理 CPU 任务（NODE-25x PM2 章节）。
- 决策口诀："多核扩容用 cluster，单进程内 CPU 卸载用 worker；两者不互斥"。
- 容器环境：K8s 单容器单进程 + 水平扩副本时 cluster 退位，worker 仍适用。

```javascript
// 组合形态示意
// 主进程（cluster master / PM2）→ N 个 worker 进程（每个是完整 HTTP server）
// 每个 HTTP server 进程内：
import Piscina from 'piscina';
const pool = new Piscina({ filename: './cpu-tasks.js', maxThreads: 2 });   // 该进程内 CPU 卸载
app.post('/resize', async (req, res) => {
  res.json(await pool.run(req.body));           // CPU 任务进线程池
});
// 面试表达：cluster 是"进程级水平扩展"，worker 是"进程内任务并行"——层次不同
```
