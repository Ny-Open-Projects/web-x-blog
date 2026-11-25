---
title: [WCN-645] 笔试：实现 signal 测试时钟（可手动推进的调度器 + 异步 flush + 断言辅助）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-645：笔试：实现 signal 测试时钟（可手动推进的调度器 + 异步 flush + 断言辅助）

**答**：
- 需求：实现 TestClock：schedule(fn, delay) 按延迟入队；tick(ms) 推进虚拟时间并执行到期任务；flush() 执行全部；async flushAsync() 等待微任务。
- 思路：最小堆/排序数组存任务 {time, fn}；tick 维护 now 并执行 time<=now 的任务；flush 把 now 设为最大时间。
- 边界：任务中再 schedule 要正确排序；相同时间按插入序；取消任务返回 id。

```javascript
export class TestClock {
  constructor() { this.now = 0; this.tasks = []; this.seq = 0; }
  schedule(fn, delay = 0) {
    const task = { time: this.now + delay, seq: this.seq++, fn, cancelled: false };
    this.tasks.push(task);
    this.tasks.sort((a, b) => a.time - b.time || a.seq - b.seq);
    return task;
  }
  cancel(task) { if (task) task.cancelled = true; }
  tick(ms) {
    const target = this.now + ms;
    while (this.tasks.length && this.tasks[0].time <= target) {
      const t = this.tasks.shift();
      this.now = t.time;
      if (!t.cancelled) t.fn();
    }
    this.now = target;
  }
  flush() {
    if (this.tasks.length) this.tick(this.tasks[this.tasks.length - 1].time - this.now);
  }
  async flushAsync() { this.flush(); await Promise.resolve(); }
}
const clock = new TestClock();
clock.schedule(() => console.log('t=100'), 100);
clock.tick(100); // 精确触发，不依赖真实时间
```

**评分点**：
- 任务按 time+seq 排序，相同时间保持插入顺序（可预测）。
- tick 推进虚拟时间并执行到期任务，任务内新增任务能被处理。
- 支持 cancel（返回 task 句柄，取消后不执行）。
- flush/flushAsync 覆盖同步与微任务场景。
