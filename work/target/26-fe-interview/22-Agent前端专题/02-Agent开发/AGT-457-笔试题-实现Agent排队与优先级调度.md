---
title: [AGT-457] 笔试题——实现任务排队调度（优先级老化+公平防饿死）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-457：手写任务调度：多优先级队列、老化提权、公平性保障

**需求与边界**：
- 输入：任务 {priority, enqueuedAt}、并发容量；输出：取任务的顺序决策。
- 边界要求：① 高优先级先执行；② 老化机制（等待超时逐级提权防饿死）；③ 同级按先来先服务；④ 队列深度监控与背压（超长队列拒绝新任务）。

**答**：
```javascript
class PriorityScheduler {
  constructor({ capacity = 10, agingMs = 60000 }) {
    this.queues = { high: [], normal: [], low: [] };
    this.capacity = capacity; this.agingMs = agingMs;
  }
  enqueue(task) {
    if (this.length() > this.capacity * 2)
      return { rejected: true, reason: 'queue_full' };  // 背压
    this.queues[task.priority ?? 'normal'].push(task);
    return { rejected: false, position: this.length() };
  }
  next() {
    this.age();                                    // 先老化再取
    for (const level of ['high', 'normal', 'low']) {
      const q = this.queues[level];
      if (q.length) return q.shift();              // 同级 FIFO
    }
    return null;
  }
  age() {                                          // 等待超时逐级提权
    const now = Date.now();
    const promote = (from, to) => {
      const q = this.queues[from];
      for (let i = q.length - 1; i >= 0; i--)
        if (now - q[i].enqueuedAt > this.agingMs) {
          this.queues[to].push({ ...q.splice(i, 1)[0],
            promoted: true });
        }
    };
    promote('low', 'normal');
    promote('normal', 'high');
  }
  length() { return Object.values(this.queues)
    .reduce((s, q) => s + q.length, 0); }
  stats() {                                        // 深度监控
    return { high: this.queues.high.length,
      normal: this.queues.normal.length,
      low: this.queues.low.length,
      utilization: this.length() / (this.capacity * 2) };
  }
}
```

**评分点**:
- 三级优先级 + 同级 FIFO，取任务顺序正确。
- 老化提权（等待超时 low→normal→high）防饿死，promoted 标记可观测。
- 背压：队列超 2 倍容量拒绝新任务（不无限堆积）。
- stats 深度监控供扩容决策。
