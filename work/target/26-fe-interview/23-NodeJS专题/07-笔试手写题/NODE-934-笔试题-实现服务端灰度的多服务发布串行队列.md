---
title: [NODE-934] 笔试题——实现多服务发布串行队列（互斥 + 插队）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-934：手写发布队列

**需求与边界**：
- 需求：发布队列（SCN-联想-934/ENG-276）——① 同服务互斥（串行队列——SCN-ENG-276）；② hotfix 插队（灰度收口——SCN-联想-934）；③ 跨服务并行（不同服务可并行——SCN-OPS-214）；④ 队列死锁检测（SCN-联想-934）。
- 边界：① 互斥的粒度（per 服务——SCN-OPS-214 隔离）；② 插队的审计（SCN-OPS-220）；③ 死锁的检测周期（SCN-联想-934）。

**答**：
```javascript
class ReleaseQueue {
  constructor() { this.queues = new Map(); }           // per 服务（SCN-OPS-214）
  enqueue(plan) {                                      // hotfix 插队（SCN-联想-934）
    const q = this.queues.get(plan.app) ?? [];
    if (plan.hotfix) {
      graySettle(q.running);                           // 灰度收口（SCN-联想-934）
      q.unshift(plan); audit({ insert: 'hotfix', plan: plan.id });
    } else q.push(plan);
  }
  deadlockCheck() {                                    // 周期检测（SCN-联想-934）
    for (const [app, q] of this.queues)
      if (circularDep(q)) alert({ type: 'QUEUE_DEADLOCK', app });
  }
}
```

**评分点**:
- per 服务互斥队列（SCN-ENG-276）。
- hotfix 插队 + 灰度收口（SCN-联想-934）。
- 死锁检测周期（SCN-联想-934）。
- 审计（SCN-OPS-220）。
