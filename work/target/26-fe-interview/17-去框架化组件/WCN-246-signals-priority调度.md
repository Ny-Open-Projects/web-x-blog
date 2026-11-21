---
title: [WCN-246] Signals 的优先级调度（高优交互先更新）如何实现？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-246：Signals 的优先级调度（高优交互先更新）如何实现？
**答**：
- 思路：flush 时按订阅者优先级分两轮——交互类 effect 立即轮，渲染类 effect 延迟轮。
- 实现：dirty 集合按优先级分桶，microtask 先清高优桶，低优桶进 idle/macro。
- 风险：两轮之间读到「半新半旧」——需要 read-consistent 设计（读取锁定轮次版本）。
- 务实做法：多数场景不需要信号级优先级——把优先级交给框架渲染调度层。

```javascript
function flushPrioritized() {
  const hi = [...pendingHigh].sort(topo); const lo = [...pendingLow];
  for (const e of hi) e.run();                 // 微任务：交互
  queueIdleTask(() => { for (const e of lo) e.run(); });   // idle：渲染
}
r
```
