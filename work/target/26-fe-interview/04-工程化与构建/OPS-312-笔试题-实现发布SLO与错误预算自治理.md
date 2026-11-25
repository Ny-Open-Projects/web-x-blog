---
title: [OPS-312] 笔试题——实现发布系统 SLO 错误预算（自治理冻结）？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## OPS-312：手写发布系统错误预算

**需求与边界**：
- 需求：发布系统三 SLO 维度（可用性/时效/正确性）各自维护错误预算；预算消耗事件归类（编排器故障/flag 服务故障/回滚超时）；预算烧完触发自治理动作（冻结发布系统功能开发，SCN-OPS-285）；预算按月重置。
- 边界：① 正确性类 SLO（产物完整性）错误预算为 0（任何违规即烧穿——硬约束）；② 自治理动作自动执行 + 人工解除（防永久冻结）；③ 预算消耗事件与事故关联（归因）。

**答**：
```javascript
function releaseErrorBudget(slos, month) {
  const budgets = {
    availability: (1 - slos.availability) * monthMs(month),   // 可用性预算
    latency: slos.rollbackP95 breaches * allowance,           // 时效违规次数预算
    correctness: 0,                                           // 硬约束：零预算
  };
  const burn = {
    availability: downtimeMs(month) / budgets.availability,
    latency: latencyBreaches(month) / budgets.latency,
    correctness: correctnessViolations(month),                // 任何违规 = 烧穿
  };
  const exhausted = Object.entries(burn).filter(([k, b]) =>
    k === 'correctness' ? b > 0 : b >= 1);
  if (exhausted.length) {
    freezeFeatures('release-system');                  // 自治理：冻结功能开发
    notifyPlatform({ exhausted, incidents: linkedIncidents(exhausted) });
    return { frozen: true, exhausted, note: '人工可解除（防永久冻结）' };
  }
  return { frozen: false, burn };
}
```

**评分点**:
- 三维度预算（正确性零预算——硬约束不同于可用性软目标）。
- 烧穿自动冻结功能开发（自治理——SCN-OPS-285）。
- 预算消耗事件与事故关联（归因闭环）。
- 人工解除通道（防永久冻结——自动化兜底人工刹车）。
