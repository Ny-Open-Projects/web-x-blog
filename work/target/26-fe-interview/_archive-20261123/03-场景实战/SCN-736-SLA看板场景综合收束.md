---
title: [SCN-736] SLA 看板场景综合收束：一条主线讲清可观测看板方法论？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-736：SLA 看板场景综合收束
**答**：
- 指标主线：SLI→SLO→错误预算闭环，指标「有 owner 有 SLO 可行动」才上板，口径版本化 + 双跑切换（SCN-703/704/710）。
- 数据主线：采样策略与还原、t-digest 多级聚合（分位数不可平均）、数据管道多级物化、补录排除管道故障时段（SCN-709/712/724/725）。
- 行动主线：值班视图三要素、告警认领闭环、发布静默与回滚联动、预算燃尽行动线、改进项追踪（SCN-706/707/722/727/717）。
- 治理主线：看板即代码、指标归属裁决、看板自身健康、成本指标不作考核（SCN-718/732/731/729）。
- 面试答法：以「一次 P95 劣化从发现到闭环」串全流程——异常检测标注 → 区域热力定位 → 发布对账归因 → 告警认领处置 → 周报复盘 → 改进项验证。

```javascript
const slaMethodology = {
  metrics: ['slo-loop', 'owner-and-actionable', 'calVer-dual-run'],
  data: ['sampling-restore', 't-digest-merge', 'materialized-only', 'backfill-exclude'],
  action: ['oncall-view', 'claim-loop', 'deploy-silence', 'budget-burn-lines'],
  governance: ['board-as-code', 'ownership-ruling', 'self-health', 'cost-advisory'],
};
```
