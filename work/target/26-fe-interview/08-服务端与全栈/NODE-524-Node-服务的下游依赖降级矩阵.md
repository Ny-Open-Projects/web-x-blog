---
title: [NODE-524] Node 服务的下游依赖降级矩阵（每依赖的降级预案）如何维护？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-524：下游依赖降级矩阵
**答**:
- 矩阵结构：每依赖一行（依赖名/调用它的接口清单/各接口的降级策略/降级数据来源/恢复探测）——全服务依赖的降级预案一览（NODE-390 降级框架的数据视图）。
- 策略类型谱系：缓存兜底（上次成功响应）、静态默认（预置数据）、裁剪降级（去掉该模块返回其余）、功能关闭（入口隐藏）、异步补偿（暂拒 + 稍后重试队列）、快速失败（核心链路显式报错——ARC-460 涉资不静默）。
- 矩阵维护机制：声明即入矩阵（依赖声明时必须填降级策略——NODE-505 声明制的字段）、演练状态列（每条预案最近演练时间/结果——超期未演练标红 NODE-408）、owner 列（预案责任人）。
- 应急视角：故障时按矩阵查预案（"recommend-svc 挂了 → 影响接口 /home,/detail → 各自降级策略 X/Y"——值班直接执行 NODE-429 Runbook 引用矩阵）。
- 反模式治理：无预案依赖（矩阵空格 = 风险敞口——数量必须趋零）、预案与实现不符（声明 cache 但代码没实现——CI 声明与实现一致性校验）。
```yaml
# 降级矩阵
deps:
  recommend-svc:
    usedBy: [/api/home, /api/detail]
    degrade:
      /api/home: { type: static-default, data: hot-list }
      /api/detail: { type: hide-module }
    probe: half-open 30s
    lastDrill: 2026-11-10   # > 90d 未演练标红
```
