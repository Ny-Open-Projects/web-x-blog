---
title: [WCN-267] Signals 应用的性能剖析方法（依赖图热点定位）？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-267：Signals 应用的性能剖析方法（依赖图热点定位）？
**答**：
- 依赖图快照：导出当前图（节点/边/订阅数/重算次数）——找重算次数异常的节点。
- 写放大检测：一次写引发的 effect 执行数（理想 = 受影响数，异常 = 图设计问题）。
- 工具：dev-mode 计数器（每次 computed/effect 执行计数）+ 场景复现统计。
- 优化路径：减少中间 computed 层/提升 equal 粒度/拆分大信号。

```javascript
const stats = graph.stats();
// { computedRuns: 5000, effects: 3, writeAmplification: 1666 } → 写放大异常
// 优化：a→b→c→d 链条中 d 只依赖 a 的部分字段 → 拆分信号
r
```
