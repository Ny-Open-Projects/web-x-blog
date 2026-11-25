---
title: [NODE-431] Node 服务的 SLO 多层级联（请求级→服务级→业务级）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-431：SLO 多层级联
**答**:
- 三层 SLO：请求级（单接口 P99/错误率——定位用）、服务级（服务整体可用性——发布冻结用 ARC-417）、业务级（核心链路端到端：下单成功率——与业务对齐用）。上级 SLI 由下级聚合，但业务级要独立度量（端到端拨测/真实流量）不能纯推导。
- 级联预算分配：业务级预算按链路分摊（下单链路 = 网关 + BFF + 订单 + 库存各分到子预算——哪层烧完哪层负责修复，避免互相甩锅）。
- 依赖方的 SLO 契约：BFF 依赖下游，下游 SLO 不足会导致 BFF 超预算——依赖对齐会（NODE-405）把 SLO 要求写进依赖声明（ 高 SLA 调用方获得优先容量与告警）。
- 权衡设计：不是所有接口都设 SLO（维护成本）——核心接口全量 SLO、长尾接口只监控告警。
- 面向用户的正确性：SLO 用真实用户流量（RUM/服务端真实请求）度量而非拨测（拨测只保底检测）。
```javascript
// 业务级 SLI：下单成功率（端到端）
const sli = (orders) => ({
  success: orders.filter(o => o.status === 'paid').length / orders.length,
  degrade: orders.filter(o => o.status === 'paid' && o.lag > 3).length // 降级成功（超时但最终成）单列
});
// 预算分摊：链路预算 0.1% → 网关 0.02 / bff 0.03 / order 0.03 / stock 0.02（10% 冗余给重试）
```
