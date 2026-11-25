---
title: [RBL-259] monorepo 构建编排的可观测面板怎么建
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-259：monorepo 构建编排的可观测面板怎么建

**答**:
- 核心看板四块：总时长趋势（P50/P95 按分支）、缓存命中率（按任务类型）、关键路径分解（哪条依赖链最长）、flaky 与失败分布（按包/按原因）
- 采集：编排器每任务上报（name/耗时/缓存命中/内存峰值），CI 侧聚合入库——数据模型先行，工具换成数据不丢
- 诊断场景：「昨天起 build 变慢」→ 任务耗时 diff → 定位到具体包/commit（关联 git）——面板必须支持时间对比视图
- 告警联动：总时长 P95 超基线 20% 自动开 issue 带 diff 分析——可观测的终点是自动行动

```text
面板字段：task / duration / cacheHit / memPeak / commit / branch / timestamp
视图：趋势线 + 对比 diff + 关键路径瀑布图
告警：p95 总时长超基线 20% → auto issue
```
