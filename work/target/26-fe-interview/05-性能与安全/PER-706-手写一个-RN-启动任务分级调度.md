---
title: [PER-706] 手写一个 RN 启动任务分级调度器：同步最小集 + 交互后任务 + 空闲任务，带优先级与超时兜底
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-706：手写一个 RN 启动任务分级调度器：同步最小集 + 交互后任务 + 空闲任务，带优先级与超时兜底

**答**：
- 调度器：`schedule(task, tier)` 三档队列——sync 立即、afterInteract 用 InteractionManager、idle 用 requestIdleCallback；每任务带优先级与超时（idle 任务超时升级到交互后执行，防饿死）。
- 要点：afterInteract 队列按优先级排序执行；idle 任务的单个执行要限时（>16ms 的拆分）；任务失败不影响后续；执行统计（各档任务耗时/是否超时升级）。
- 边界：调度器自身在启动最早期安装；任务间依赖声明（DAG 简化为 deps 数组，前置完成才执行）。
- 评分点：超时升级防饿死与依赖声明。

```javascript

import { InteractionManager } from 'react-native';
class StartupScheduler {
  constructor() {
    this.afterQueue = []; this.idleQueue = []; this.done = new Set();
    InteractionManager.runAfterInteractions(() => this.drainAfter());
    const idle = () => requestIdleCallback((deadline) => {
      while (this.idleQueue.length && deadline.timeRemaining() > 8) {  // 单任务限时
        const t = this.idleQueue.shift();
        if (!this.ready(t)) { this.idleQueue.push(t); break; }        // 依赖未完成
        this.run(t);
      }
      if (this.idleQueue.length) idle();
    });
    idle();
  }
  schedule(task, tier = 'idle', { priority = 0, timeoutMs = 5000, deps = [] } = {}) {
    const item = { ...task, priority, timeoutMs, deps, addedAt: Date.now() };
    if (tier === 'sync') this.run(item);
    else if (tier === 'afterInteract') { this.afterQueue.push(item); this.afterQueue.sort((a, b) => b.priority - a.priority); }
    else this.idleQueue.push(item);
  }
  ready(t) { return t.deps.every(d => this.done.has(d)); }
  run(t) {
    try { t.fn(); } catch (e) { warn(`task ${t.name} failed`, e); }
    this.done.add(t.name);
    if (Date.now() - t.addedAt > t.timeoutMs) track('startup-task-timeout', t.name); // 超时统计
  }
  drainAfter() {
    while (this.afterQueue.length) {
      const t = this.afterQueue.shift();
      if (this.ready(t)) this.run(t); else this.afterQueue.push(t);
    }
    // idle 队列里超时任务升级执行
    this.idleQueue = this.idleQueue.filter(t => {
      if (Date.now() - t.addedAt > t.timeoutMs * 2) { this.run(t); return false; }
      return true;
    });
  }
}
```
