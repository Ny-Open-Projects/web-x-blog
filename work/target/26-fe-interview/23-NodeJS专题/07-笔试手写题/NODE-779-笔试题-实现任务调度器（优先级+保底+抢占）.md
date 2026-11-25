---
title: [NODE-779] 笔试题——实现任务调度器（优先级 + 保底 + 超时抢占）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-779：手写任务调度器

**需求与边界**：
- 需求：任务队列调度（SCN-NODE-693）——① 多优先级队列（critical/high/low）；② 保底配额（每 10 个 high 跑 1 个 low——starvation 防御）；③ 任务超时抢占（超时任务终止——可中断任务协作式，SCN-NODE-628）；④ 并发上限（下游保护——SCN-NODE-643）。
- 边界：① 抢占的可中断性（任务定期检查中断信号——协作式取消，SCN-NODE-744）；② 超时任务的结果处理（标记失败可重试——SCN-NODE-736）；③ 优先级翻转防御（low 长期饿死的告警——最老 low 任务年龄监控）。

**答**：
```javascript
class PriorityScheduler {
  constructor({ concurrency = 10, floorEvery = 10 } = {}) { this.highRun = 0; }
  async pick() {
    if (this.critical.length) return this.critical.shift();
    if (++this.highRun >= this.floorEvery && this.low.length) {   // 保底配额（SCN-NODE-693）
      this.highRun = 0;
      return this.low.shift();                         // low 不饿死
    }
    return this.high.shift() ?? this.low.shift();
  }
  async run(task) {
    if (this.running >= this.concurrency) await slotAvailable();   // 并发上限（下游保护）
    this.running++;
    const ctrl = new AbortController();
    const timer = setTimeout(() => ctrl.abort('timeout'), task.timeout ?? 60_000);   // 超时抢占
    try {
      task.signal = ctrl.signal;                       // 协作式取消（任务定期检查）
      await handler(task);
    } catch (e) { markFailed(task, e); }               // 失败可重试（SCN-NODE-736）
    finally { clearTimeout(timer); this.running--; }
    if (oldestLowAge() > 3600_000) alert('LOW_STARVING');   // 饿死告警（SCN-NODE-693）
  }
}
```

**评分点**:
- 保底配额（每 N 个 high 跑 1 个 low——starvation 防御）。
- 协作式抢占（task.signal——可中断任务定期检查）。
- 并发上限（下游保护——SCN-NODE-643）。
- 饿死告警（最老 low 年龄——公平性监控）。
