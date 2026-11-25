---
title: [OPS-271] 发布事件溯源（编排器的事件溯源架构）怎么设计？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## OPS-271：发布事件溯源怎么设计？
**答**：
- 事件溯源架构：发布编排状态不直接存「当前状态」，而是存事件流（PlanCreated/StepStarted/StepSucceeded/RollbackTriggered）——状态 = 事件重放结果。
- 价值：完整审计（SCN-OPS-220 天然满足）、时间旅行（重放到任意时刻看状态）、事后分析（发布过程的事件序列可挖掘模式）、崩溃恢复（重放即恢复，SCN-OPS-212 的架构级解法）。
- 快照优化：事件流长时定期快照（重放加速），快照与事件混合重放。
- 只追加语义：事件不可修改不可删除——与发布留痕的合规要求天然一致。
- 追问钩子：为什么事件溯源是「发布编排」的天然架构——发布的本质是「一系列带顺序的决策动作」，事后最常被问的是「当时发生了什么、为什么这么做」；事件流完整保留决策序列，让审计/恢复/复盘三个需求共享同一份数据源——状态表方案需要三处冗余记录，事件溯源一份搞定。

```javascript
// 事件流
const events = [
  { type: 'PlanCreated', planId, by, ts },
  { type: 'StepStarted', step: 'sdk@2.0' },
  { type: 'StepSucceeded', step: 'sdk@2.0', artifacts: {...} },
  { type: 'RollbackTriggered', reason, by },           // 只追加不可改
];
const stateAt = (n) => events.slice(0, n).reduce(applyEvent, initialState);   // 时间旅行
// 快照加速
if (events.length > 1000) snapshot(stateAt(events.length));
```
