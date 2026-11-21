---
title: [ARC-271] 大促 AB 与灰度在大促期间如何调整策略？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-271：大促 AB 与灰度在大促期间如何调整策略？
**答**：
- 原则：大促期间**实验让位于稳定**。T-3 起新实验冻结（存量实验只观察不下线，避免分桶变化引入指标噪声）；大促数据用作"长期实验"的观察窗口而非决策窗口。
- 灰度收紧：发布灰度比例上限下调（ARC-263），且灰度分桶必须与实验分桶隔离（正交分层），避免灰度流量叠加实验桶造成局部压力集中。
- 大促特有的 AB：玩法效果验证（A/B 两种优惠呈现）属于"大促专属实验"，用短周期 + 强指标（转化率/GMV）快进快出，T-0 前出结论。
- 分桶一致性：同一用户的实验桶跨天/跨端保持稳定（分桶因子用 userId 而非 sessionId），否则大促跨日数据没法归因。

```typescript
// 正交分层分桶
function bucket(userId: string, layer: string, salt: string) {
  const h = hash(`${layer}:${salt}:${userId}`) % 100;      // 层间独立，层内互斥
  return h;
}
// 冻结期：experimentService.newLaunches(disabled) —— 只读存量
// 大促专属实验：{ window: ['11-01','11-10'], metric: 'gmvPerUser', minSample: 50000, autoStopOnSignificance: true }
```
