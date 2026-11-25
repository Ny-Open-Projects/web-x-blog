---
title: [ARC-288] 灰度与 AB 的成本治理：实验泛滥怎么管？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-288：灰度与 AB 的成本治理：实验泛滥怎么管？
**答**：
- 实验泛滥的代价：分桶层资源耗尽（新实验挤不进）、代码里 flag 永不清理（组合测试爆炸）、分析带宽被低价值实验占据、用户体验碎片化（一半用户活在新旧功能杂交态）。
- 治理机制：实验准入评审（预期效应量 MDE 达不到显著性所需的样本量 → 不批）、强制结束期（到期未显著自动关闭并通知）、层容量审计（每层最多 N 个活跃实验）、代码回收 SLA（实验关闭后 flag 2 周内删除，CI 扫描未清理 flag）。
- ROI 度量：每个实验记录"结论采纳率"——长期采纳率低的团队收紧配额，让实验资源流向高价值方向。
- 分层治理数据：每季度输出"层使用率/僵尸 flag 数/实验平均周期"看板，向技术负责人汇报。

```typescript
// 实验生命周期治理
const exp = { name: 'newFeed', mde: 0.02, requiredN: 80000, endsAt: '2026-11-30', status: 'running' };
function auditExperiments(today) {
  const expired = exps.filter(e => e.endsAt < today && e.status === 'running');
  expired.forEach(e => { e.status = 'auto-closed'; notify(e.owner, '实验到期未显著，已关闭，请 2 周内删除 flag'); });
  ci.scanFlags({ deleteAfterDays: 14 });       // flag 未清理 → CI error
}
// 准入：estimateRequiredN(mde, baseline) > layerRemaining(layer) → 拒绝申报
```
