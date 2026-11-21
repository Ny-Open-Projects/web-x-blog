---
title: [DP-250] 源码识别：前端调度器源码中的优先级队列与时间切片？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-250：源码识别：前端调度器源码中的优先级队列与时间切片？
**答**:
- 优先级队列：任务带优先级（urgent/normal/idle），两队列（同步优先立即执行 / idle 队列 rIC 消费）+ 饥饿防范（idle 任务老化提升，HW 系列讲过优先级老化）。
- 时间切片：每帧预算（如 8ms）内循环取任务，超时让路（shouldYield）——React Scheduler 同款（DP-221）。
- 观察者/命令：任务封装为 { run, cancel, priority } 命令对象，调度结果事件广播（onIdle）。
- 识别要点：能指出"idle 回调的超时 deadline 是把'空闲'变成硬约束的机制"（timeout 参数防饿死）。

```javascript
// 前端调度器（源码级简化）
class Scheduler {
  urgent = []; idle = [];
  schedule(task, priority = 'normal') {
    task.priority = priority;
    (priority === 'urgent' ? this.urgent : this.idle).push(task);
    if (priority === 'urgent') queueMicrotask(() => this.runUrgent());   // 立即
    else this.ensureIdleLoop();
  }
  ensureIdleLoop() {
    if (this.idleLooping) return; this.idleLooping = true;
    const loop = (deadline) => {
      let budget = 8;                                   // 时间切片
      while (this.idle.length && budget > 0) {
        const t = this.idle.shift();
        const start = performance.now();
        t.run();
        budget -= performance.now() - start;
      }
      this.ageTasks();                                  // 饥饿防范：老化提升
      this.idle.length ? requestAnimationFrame(loop) : (this.idleLooping = false);
    };
    requestAnimationFrame(loop);                        // 或 requestIdleCallback(loop, { timeout: 1000 })
  }
}
```
