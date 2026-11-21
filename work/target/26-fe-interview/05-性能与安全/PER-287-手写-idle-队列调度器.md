---
title: [PER-287] 笔试题：手写基于 requestIdleCallback 的空闲任务队列（优先级 + 超时 + deadline 预算）
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-287：手写基于 requestIdleCallback 的空闲任务队列（优先级 + 超时 + deadline 预算）

**题目**：实现 `IdleQueue`：① `push(fn, { priority = 0, timeout = 3000 })` 入队；② rIC 回调里按 deadline.timeRemaining() 预算执行，优先级高的先跑；③ 每个任务带 timeout——超时后即使不空闲也用 setTimeout 强制执行（防饿死）；④ 返回 Promise；⑤ 页面隐藏时暂停空闲调度，恢复可见时重启。

**答**：rIC 的两个坑要处理：Safari 不支持（降级 setTimeout 1ms 模拟）、低优先级任务可能长期被挤（超时兜底）。deadline 预算让"一次 idle 回调跑多个小任务"。

```javascript
class IdleQueue {
  constructor() {
    this.queue = []; this.running = false;
    document.addEventListener('visibilitychange', () => {
      if (document.visibilityState === 'visible') this.#schedule();
    });
  }
  push(fn, { priority = 0, timeout = 3000 } = {}) {
    return new Promise((resolve, reject) => {
      const item = { fn, priority, timeout, resolve, reject, at: Date.now() };
      this.queue.push(item);
      this.queue.sort((a, b) => b.priority - a.priority);       // 高优在前
      if (!this.running) this.#schedule();
      setTimeout(() => {                                        // 超时兜底：强制执行防饿死
        const idx = this.queue.indexOf(item);
        if (idx !== -1) { this.queue.splice(idx, 1); this.#exec(item); }
      }, timeout);
    });
  }
  #schedule() {
    if (!this.queue.length || document.visibilityState !== 'visible') return;
    const ric = window.requestIdleCallback || ((f) => setTimeout(() => f({ timeRemaining: () => 12, didTimeout: false }), 1));
    ric((deadline) => {
      while (this.queue.length && deadline.timeRemaining() > 2) {   // 预算内连续执行
        this.#exec(this.queue.shift());
      }
      if (this.queue.length) this.#schedule();                      // 预算用尽，下一轮 idle
    });
  }
  #exec(item) { try { item.resolve(item.fn()); } catch (e) { item.reject(e); } }
}
// 用法：idleQueue.push(() => flushLogs(), { priority: 0, timeout: 2000 })
```

**评分点**：
- deadline 预算循环（timeRemaining > 2 连续执行），单次 idle 跑多个任务。
- 超时兜底完整：setTimeout 强制执行并从队列移除（防重复执行——先移除再 exec）。
- 优先级排序与降级路径（无 rIC 用 setTimeout 模拟）。
- 隐藏暂停/可见重启，不空转。
