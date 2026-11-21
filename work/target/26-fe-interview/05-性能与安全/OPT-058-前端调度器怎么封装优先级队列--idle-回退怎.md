---
title: [OPT-058] 前端调度器怎么封装？优先级队列 + idle 回退怎么做？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-058：前端调度器怎么封装？优先级队列 + idle 回退怎么做？

**答**：
- 调度器要回答两个问题：**什么时候跑**（rAF 对齐渲染 / idle 兜底）和**先跑谁**（优先级队列）。
- 分四档优先级：`immediate`（同步）、`high`（本帧 rAF）、`normal`（下一帧）、`idle`（requestIdleCallback + timeout 防饿死）。
- 同帧任务合并执行，单帧超预算立即把剩余任务降到下一帧，避免调度器自己变成长任务。
- 典型应用：埋点上报、图表重算、缓存清理都压到 idle 档；交互反馈走 high 档。

```javascript
// 一一对应：优先级调度器（四档优先级 + 单帧预算控制 + idle 防饿死）
class Scheduler {
  constructor(frameBudget = 12) {
    this.queues = { high: [], normal: [], idle: [] };
    this.frameBudget = frameBudget;
    this.scheduled = false;
  }
  push(task, priority = 'normal') {
    this.queues[priority].push(task);
    if (!this.scheduled) this._schedule();
  }
  _schedule() {
    this.scheduled = true;
    // high/normal 对齐 rAF：一次回调里按预算消费多档队列
    requestAnimationFrame(() => this._runFrame());
    // idle 档单独走 idle，timeout=2000 防止页面一直忙导致任务饿死
    requestIdleCallback((dl) => this._runIdle(dl), { timeout: 2000 });
  }
  _runFrame() {
    const start = performance.now();
    while (this.frameBudget > performance.now() - start) {
      const q = this.queues.high.length ? this.queues.high
        : this.queues.normal.length ? this.queues.normal : null;
      if (!q) break;
      q.shift()(); // 消费一个任务，超预算立即停，剩余留到下帧
    }
    this.scheduled = this.queues.high.length + this.queues.normal.length > 0;
    if (this.scheduled) requestAnimationFrame(() => this._runFrame());
  }
  _runIdle(deadline) {
    // 只在空闲时间足够时跑 idle 任务，timeRemaining 不足就留给下一轮 timeout
    while (deadline.timeRemaining() > 5 && this.queues.idle.length) {
      this.queues.idle.shift()();
    }
  }
}

// 使用：上报进 idle，输入高亮进 high
const sched = new Scheduler();
input.addEventListener('input', (e) => {
  sched.push(() => highlight(e.target.value), 'high');
  sched.push(() => report('search-input', e.target.value.length), 'idle');
});
```
