---
title: [WEB-602] 笔试：手写 rAF + requestIdleCallback 任务分片调度
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 笔试题, 性能]
type: 笔试题
---

## WEB-602：笔试：手写 rAF + requestIdleCallback 任务分片调度

**答**：实现 `Scheduler`：① `addTask(fn, { priority })`：高优先级任务在下一帧 rAF 执行，低优先级在 requestIdleCallback 空闲期执行；② 每个 idle 回调内任务总耗时不超过 deadline 剩余的 80%，剩余任务排队到下一空闲期；③ 无 requestIdleCallback 环境（Safari）降级 setTimeout(0) + 每批 16ms 预算；④ 支持任务取消。写出核心实现。

```javascript
class Scheduler {
  constructor() {
    this.tasks = new Set(); this.cancelled = new Set();
    this.hasRIC = typeof requestIdleCallback === 'function';
  }
  addTask(fn, { priority = 'low' } = {}) {
    const t = { fn, priority };
    this.tasks.add(t);
    if (priority === 'high') requestAnimationFrame(() => this._runOne(t));
    else this._scheduleIdle();
    return () => this.cancelled.add(t);
  }
  _scheduleIdle() {
    if (this._pending) return;
    this._pending = true;
    const drain = (deadline) => {
      this._pending = false;
      const budget = deadline ? () => deadline.timeRemaining() > 2
        : () => performance.now() - start < 16; // 降级按 16ms 预算
      const start = performance.now();
      for (const t of [...this.tasks]) {
        if (this.cancelled.has(t)) { this.tasks.delete(t); this.cancelled.delete(t); continue; }
        if (!budget()) break;
        this.tasks.delete(t);
        try { t.fn(); } catch (e) { console.error(e); }
        if (this.tasks.size) this._scheduleIdle(); // 剩余排队
        break;
      }
    };
    if (this.hasRIC) requestIdleCallback(drain);
    else setTimeout(() => drain(null), 0);
  }
  _runOne(t) {
    if (this.cancelled.has(t)) return;
    this.tasks.delete(t);
    t.fn();
  }
}
```

**评分点**：
- 高/低优先级分别走 rAF 与 idle 通道，理解两者调度时机差异
- idle 分片按 timeRemaining 预算控制，剩余任务重新排队
- Safari 降级路径用 16ms 帧预算模拟
- 取消语义完整（含未执行队列清理）
