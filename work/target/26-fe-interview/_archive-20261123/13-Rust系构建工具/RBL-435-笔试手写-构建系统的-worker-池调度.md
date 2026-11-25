---
title: [RBL-435] 笔试：手写构建系统的 Worker 池调度
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-435：手写 Worker 池调度
**需求**：实现 `createWorkerPool({ size })`：1) 池化 worker 进程（spawn 预热，任务通过 IPC 分发）；2) 任务分发：空闲 worker 优先 + 任务队列（FIFO）；3) worker 崩溃恢复：exit 事件检测 → 该 worker 在途任务重新入队（任务不丢）→ 新 worker 补位；4) 内存阈值：worker RSS 超限强制 recycle（防 worker 内存泄漏累积）；5) `run(task)` Promise 化 + 超时；6) pool.stats() 活跃/队列/回收数。

```javascript
import { fork } from 'node:child_process'

export function createWorkerPool({ size = 4, workerPath, recycleMB = 2048 } = {}) {
  const idle = [], busy = new Map(), queue = []
  let recycled = 0

  function spawnWorker() {
    const w = fork(workerPath)
    w.on('message', ({ taskId, result, error }) => {
      const { resolve, reject } = busy.get(taskId) ?? {}
      busy.delete(taskId); idle.push(w)
      error ? reject(new Error(error)) : resolve(result)
      pump()
    })
    w.on('exit', () => {
      for (const [taskId, task] of busy) {                       // 崩溃任务重入队
        if (task.worker === w) { busy.delete(taskId); queue.push(task) }
      }
      if (!stopped) spawnWorker()                                // 补位
      pump()
    })
    return w
  }

  let stopped = false
  for (let i = 0; i < size; i++) idle.push(spawnWorker())

  function pump() {
    while (idle.length && queue.length) {
      const w = idle.pop()
      // 内存回收检查
      if (w.memoryUsageMB?.() > recycleMB) { w.kill(); recycled++; idle.push(spawnWorker()); continue }
      const task = queue.shift()
      busy.set(task.id, { ...task, worker: w })
      w.send({ ...task })
    }
  }

  function run(task, timeoutMs = 120_000) {
    return new Promise((resolve, reject) => {
      const timer = setTimeout(() => {
        queue.splice(queue.findIndex((t) => t.id === task.id), 1)
        reject(new Error(`task ${task.id} timeout`))
      }, timeoutMs)
      queue.push({ ...task, resolve: (v) => { clearTimeout(timer); resolve(v) },
        reject: (e) => { clearTimeout(timer); reject(e) } })
      pump()
    })
  }

  return {
    run,
    stats: () => ({ idle: idle.length, busy: busy.size, queued: queue.length, recycled }),
    dispose: () => { stopped = true; [...idle, ...busy.keys()].forEach((w) => w.kill()) },
  }
}
```
**评分点**：
- 池化生命周期（预启 + 空闲复用 + 崩溃补位）
- 崩溃任务重入队（任务不丢——worker 池可靠性核心）
- 内存阈值 recycle（长跑泄漏治理）
- 超时与清理（超时任务从队列移除防幽灵任务）
