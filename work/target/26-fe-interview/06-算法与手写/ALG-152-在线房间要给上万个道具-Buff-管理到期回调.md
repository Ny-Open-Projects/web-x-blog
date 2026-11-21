---
title: [ALG-152] 在线房间要给上万个道具/Buff 管理到期回调，每个都 setTimeout 会让浏览器定时器爆炸。如何用时间轮思想管理大量定时器？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-152：在线房间要给上万个道具/Buff 管理到期回调，每个都 setTimeout 会让浏览器定时器爆炸。如何用时间轮思想管理大量定时器？
**答**：时间轮：只开 1 个系统级 tick（如 1s），把任务按「到期 tick 数」哈希到环形槽位；超过一圈的用 round 计数，每轮 tick 命中时 round 减到 0 才真正执行。添加 O(1)、tick 均摊 O(槽内任务数)，万个定时器只占 1 个系统定时器与 O(槽数 + 任务数) 内存。

```javascript
class TimingWheel {
  constructor(slots = 60, tickMs = 1000) {
    this.slots = Array.from({ length: slots }, () => []);
    this.tickMs = tickMs;
    this.current = 0;
    this.timer = setInterval(() => this.tick(), tickMs); // 全局唯一系统定时器
  }
  add(delayMs, fn) {
    const ticks = Math.ceil(delayMs / this.tickMs);
    const slot = (this.current + ticks) % this.slots.length;
    // 超过一圈的任务记 round 数，每轮命中减一，减到 0 才执行
    this.slots[slot].push({ fn, round: Math.floor(ticks / this.slots.length) });
  }
  tick() {
    const cur = this.slots[this.current];
    this.slots[this.current] = [];
    for (const job of cur) {
      if (job.round-- > 0) this.slots[this.current].push(job); // 未到轮数：放回
      else job.fn();
    }
    this.current = (this.current + 1) % this.slots.length;   // 指针步进
  }
}
```
