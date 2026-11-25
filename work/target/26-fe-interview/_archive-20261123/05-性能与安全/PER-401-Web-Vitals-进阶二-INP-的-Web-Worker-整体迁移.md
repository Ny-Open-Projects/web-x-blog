---
title: [PER-401] 什么时候值得把整块业务逻辑迁进 Worker（Off-main-thread 架构）？迁移成本与收益边界？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-401：什么时候值得把整块业务逻辑迁进 Worker？迁移成本与收益边界？

**答**：
- 判断标准：主线程持续被非 UI 计算占用 > 30%（LoAF 聚合数据可算出），且计算与 DOM 解耦（纯数据变换/校验/协议解析）——满足两条才考虑 off-main-thread 架构。典型场景：协同编辑引擎（OT/CRDT 计算）、行情计算、大表单校验引擎。
- 收益上限：主线程只留 UI 更新，INP 的 processing 段趋近于零；但 input delay 与 presentation 段不受影响——Worker 化救不了"渲染贵"的页面。
- 迁移成本：状态同步架构（单一数据源在 Worker，主线程订阅变更——类似 WebWorker 状态库模式）；调试复杂度（DevTools 的 Worker 调试/断点体验较弱）；序列化成本治理（PER-386：数据常驻 + 指令通信）；框架生态缺位（React/Vue 的渲染仍在主线程，Worker 只接管"状态与计算"，渲染 dispatch 回主线程）。
- 渐进路径：先 Worker 化最热的 3~5 个纯函数（热点函数排行驱动，PER-298），验证收益与成本后再评估整块迁移；整块迁移是"架构决策"要过性能评审。

```text
Off-main-thread 决策：
前提：LoAF 数据显示主线程非 UI 计算 > 30% + 计算与 DOM 解耦
架构：状态单源在 Worker（计算/校验/协议）→ 变更 diff 派发主线程 → 框架渲染
收益：processing 段 → 0；不改善 input delay 与 presentation
成本：状态同步架构、调试复杂度、序列化治理（数据常驻+指令通信）
路径：热点函数 Worker 化试点（Top3 纯函数）→ 验证 → 整块迁移过性能评审
反例：渲染贵的页面迁 Worker —— presentation 段不动，收益为零
```
