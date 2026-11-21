---
title: [MP-278] 笔试：手写小程序 Worker 任务池（复用 + 超时 + 队列）
date: 2026-11-19
categories: [小程序]
tags: [前端面试, 笔试题, 19]
type: 笔试题
---

## MP-278：笔试：手写 Worker 任务池
**题**：实现 WorkerPool（上限 5 个 worker）：submit(taskFn 描述, data) 返回 Promise；空闲 worker 复用，无空闲排队；单任务超时（10s）reject 并销毁该 worker；页面卸载 terminateAll。

```javascript
class WorkerPool {
  constructor(size = 5) {
    this.size = size; this.idle = []; this.queue = []; this.busy = new Set()
  }
  _create() {
    const worker = wx.createWorker('workers/main.js')
    const entry = { worker, idle: false }
    worker.onMessage((msg) => entry.resolve?.(msg))
    return entry
  }
  submit(data, timeout = 10000) {
    return new Promise((resolve, reject) => {
      this.queue.push({ data, resolve, reject, timeout })
      this._pump()
    })
  }
  _pump() {
    while (this.idle.length < this.size && (this.idle.length === 0 || this.queue.length)) {
      if (!this.queue.length && this.idle.length >= 1) return
      const entry = this.idle.pop() || this._create()
      const task = this.queue.shift()
      if (!task) { this.idle.push(entry); return }
      this.busy.add(entry)
      entry.resolve = (msg) => { clearTimeout(entry.timer); entry.resolve = null; this.busy.delete(entry); this.idle.push(entry); task.resolve(msg); this._pump() }
      entry.timer = setTimeout(() => { entry.worker.terminate(); this.busy.delete(entry); task.reject(new Error('worker timeout')); this._pump() }, task.timeout)
      entry.worker.postMessage(task.data)
    }
  }
  terminateAll() { [...this.idle, ...this.busy].forEach(e => e.worker.terminate()); this.idle = []; this.busy.clear(); this.queue.forEach(t => t.reject(new Error('pool disposed'))); this.queue = [] }
}
```
**评分点**：
- 池化复用（wx.createWorker 上限 5 个，创建昂贵）。
- 超时销毁 worker（卡死任务不阻塞池）。
- 队列排队 + dispose 清理（防页面泄漏）。
- onMessage 与任务的配对（简化为单任务模式，能说出多任务需 msgId 配对加分）。
__zcode_status=$?
if [ "$__zcode_status" -eq 0 ]; then pwd -P > '/var/folders/0s/4tf1lwpd7817z10jldln1r4c0000h8/T/zcode-eaee2912-4fa9-462f-a14e-437dbd87948f-cwd'; fi
exit "$__zcode_status"
