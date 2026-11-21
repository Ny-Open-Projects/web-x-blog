---
title: [PER-281] 长任务（Long Task）的定义是什么？它如何伤害 INP/TBT？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-281：长任务（Long Task）的定义是什么？它如何伤害 INP/TBT？

**答**：
- 定义：主线程上超过 50ms 的任务即为 Long Task（50ms 阈值来自 RAIL 模型：100ms 内响应输入，任务必须短到能穿插输入处理）。
- 伤害路径一（INP）：用户点击时主线程正在跑长任务 → 事件排队等它跑完才开始处理（input delay）→ 交互延迟从 0 变成"等长任务"。
- 伤害路径二（TBT）：Lighthouse 用 Total Blocking Time 衡量加载期——所有 >50ms 任务超出 50ms 的部分之和。TBT 高 = 加载期主线程忙 = INP 也差。TBT 是 INP 的实验室代理指标。
- 排查与治理：Performance 面板看红色任务块 / longtask observer 线上采集；治理三板斧——代码切片（scheduler.yield）、降优先级（把非关键任务挪到 idle）、Worker 隔离（纯计算）。目标：主线程无 >50ms 任务，特别是加载后 3 秒与高频交互路径上。

```javascript
// 线上长任务采集：计数 + 总阻塞时长 + 归因
let stats = { count: 0, blocking: 0 };
new PerformanceObserver((list) => {
  for (const e of list.getEntries()) {
    stats.count++;
    stats.blocking += Math.max(0, e.duration - 50);   // TBT 语义：超出 50ms 的部分
    if (e.duration > 300) report({ type: 'long-task', dur: Math.round(e.duration),
                                   at: e.name, ts: Math.round(e.startTime) });
  }
}).observe({ type: 'longtask', buffered: true });
// TBT（加载期）：performance.now() 在 load 事件后的累计 blocking
// 验收：TBT < 200ms；长任务 > 300ms 的样本单独上报并归因
```
