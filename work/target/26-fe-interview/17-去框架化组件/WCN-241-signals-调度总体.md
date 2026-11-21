---
title: [WCN-241] Signals 的调度总体架构（写→标脏→批量 flush）是怎么工作的？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-241：Signals 的调度总体架构（写→标脏→批量 flush）是怎么工作的？
**答**：
- 写操作不立即执行 effect：只把受影响的 computed/effect 标记 dirty，统一在微任务（或显式 batch）里 flush。
- flush 时按依赖拓扑自底向上重算 computed，再执行 effect——保证每个 effect 只跑一次看到最终值。
- 层级去重是 Signals 性能的本质：N 个写入 + M 个订阅 = 一次批处理，不是 N×M 次。
- 各实现差异点：flush 时机（微任务/同步可选）、拓扑排序实现（深度标志位/优先级队列）。

```javascript
// 调度骨架
let pending = new Set<Effect>(); let scheduled = false;
function scheduleFlush() {
  if (scheduled) return; scheduled = true;
  queueMicrotask(() => { scheduled = false;
    const list = topoSort([...pending]);   // 依赖序
    pending = new Set();
    for (const e of list) if (e.dirty) e.run();   // 一次 flush 全收
  });
}
r
```
