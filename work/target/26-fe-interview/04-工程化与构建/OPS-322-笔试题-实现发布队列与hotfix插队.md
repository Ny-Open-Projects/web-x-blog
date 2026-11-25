---
title: [OPS-322] 笔试题——实现发布队列与 hotfix 插队（灰度收口联动）？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## OPS-322：手写发布队列插队

**需求与边界**：
- 需求：同应用发布互斥队列（串行）——① hotfix 插队时强制「灰度收口」（当前灰度全量或回滚，SCN-OPS-263）；② 队列可视化（谁在等谁）；③ 队列死锁检测（互相依赖的发布）。
- 边界：① 收口方式由灰度指标决定（指标健康全量，异常回滚）；② 插队记录（被插队的发布计划状态保留，可恢复）；③ 死锁检测周期性。

**答**：
```javascript
class ReleaseQueue {
  constructor(app) { this.app = app; this.queue = []; this.running = null; }
  async enqueue(plan, { isHotfix = false } = {}) {
    if (isHotfix) return this.jump(plan);              // 插队
    this.queue.push(plan); return { position: this.queue.length };
  }
  async jump(hotfix) {
    if (this.running?.gray?.active) {
      // 强制收口：指标健康全量，异常回滚
      const settle = this.running.gray.hardMetrics.ok ? 'FULL' : 'ROLLBACK';
      await graySettle(this.running, settle);
      audit({ action: 'gray-settle', mode: settle, by: 'hotfix-jump' });
    }
    this.queue.unshift(hotfix);                        // 插到队首
    return { jumped: true, settled: true };
  }
  deadlockCheck() {                                    // 周期性死锁检测
    const waiting = this.queue.filter(p => p.dependsOn);
    const cycle = waiting.find(p => circularDep(p));
    if (cycle) alert({ type: 'QUEUE_DEADLOCK', plan: cycle.id });
  }
  status() { return { running: this.running?.id, waiting: this.queue.map(p => p.id) }; }
}
```

**评分点**:
- hotfix 插队强制收口（指标健康决定全量/回滚——SCN-OPS-263）。
- 收口审计（谁/何种模式）。
- 死锁检测（互相依赖的发布）。
- 队列可视化 status()。
