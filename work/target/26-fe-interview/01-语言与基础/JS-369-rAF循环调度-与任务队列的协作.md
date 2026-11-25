---
title: [JS-369] rAF 循环调度：与任务队列的协作
date: 2026-11-21
categories: [JavaScript]
tags: [前端面试, 面试题, 并发]
type: 面试题
---

## JS-369：rAF 循环调度：与任务队列的协作

**答**：
- rAF 的语义：每帧渲染前回调，与屏幕刷新对齐；页面隐藏自动暂停（省电）——它是「渲染节拍器」不是通用定时器，逻辑计时勿用 rAF
- 帧内预算分配：rAF 回调里应控制在 <10ms（留渲染时间）——重计算放 rAF 之外（idle/Worker），rAF 只做「读布局 → 写样式」的同步段
- 与 idle 协作：rAF 处理视觉必要更新，requestIdleCallback 处理非紧急（预计算/清理）；两者构成「帧内两阶段」——渲染优先，空闲补作业
- 多循环合并：页面多个动画各自 rAF 是反模式（回调风暴）——统一 ticker（一个 rAF 循环分发到订阅者），暂停语义按订阅者
- 长动画暂停恢复：切后台回来 rAF 时间戳跳变——dt 钳制（min(dt, 50ms)）防物理模拟爆冲；计数器类动画按绝对进度算而不是累加

```javascript
// 统一 ticker
class Ticker {
  #subs = new Map(); #raf = 0; #last = 0;
  add(id, fn) { this.#subs.set(id, fn); this.#start(); return () => { this.#subs.delete(id); this.#stopIfIdle(); }; }
  #start() {
    if (this.#raf) return;
    this.#last = performance.now();
    const loop = (t) => {
      const dt = Math.min(t - this.#last, 50);   // dt 钳制
      this.#last = t;
      for (const fn of this.#subs.values()) fn(dt, t);
      this.#raf = requestAnimationFrame(loop);
    };
    this.#raf = requestAnimationFrame(loop);
  }
  #stopIfIdle() { if (!this.#subs.size && this.#raf) { cancelAnimationFrame(this.#raf); this.#raf = 0; } }
}
```
