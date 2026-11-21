---
title: [NODE-506] Node 服务的内部 SLA 协商（上下游对齐延迟预算）流程如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-506：内部 SLA 协商
**答**:
- 问题：BFF 需要下游 200ms，下游默认 SLA 500ms——预算不协商到落地时互相甩锅。SLA 协商机制：调用方提需求（接口/预算/QPS/错误容忍）→ 提供方评估（容量/成本）→ 达成写入依赖声明（NODE-505）。
- 协商产物：每依赖关系的 SLA 条目（P99 目标/错误率上限/QPS 配额/超时降级约定）——数据驱动协商（历史 trace 数据：现在实际 P95 是 180ms，要求 200ms 合理；要求 100ms 需成本评估）。
- 动态调整：SLA 不是一次谈死——季度 review（业务变化/流量增长重新对齐 NODE-433 容量联动）、违约处理（持续违约 → 升级：容量投入/架构优化/调用方降级容忍）。
- 与降级联动：SLA 里写清楚"违约时调用方怎么办"（降级策略——协商的一部分而非事后甩锅）。
- 度量：SLA 达标率（协商条款的实际达成——依赖画像 NODE-467 的契约对齐视图）、协商周期（需求到生效的时长——协商机制的效率）。
```yaml
# SLA 条目（依赖声明扩展）
- caller: trade-bff, provider: inventory-svc, route: /internal/stock
  sla: { p99: 200ms, errRate: 0.5%, qps: 3000, onBreach: 'caller-degrade-cache' }
  basis: { currentP95: 120ms, headroom: 40% }   # 数据驱动协商
review: quarterly
```
