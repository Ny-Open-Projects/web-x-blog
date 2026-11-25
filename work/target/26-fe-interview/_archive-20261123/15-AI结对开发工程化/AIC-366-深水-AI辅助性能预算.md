---
title: [AIC-366] 如何把「性能预算」体系与 AI 开发结合，防止 AI 产出把包体积/指标写崩？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-366：如何把「性能预算」体系与 AI 开发结合，防止 AI 产出把包体积/指标写崩？
**答**：
- 预算文件化：budgets.json（首屏 JS ≤ 170KB/LCP ≤ 2.5s/依赖新增需审批），AI 上下文必带。
- CI 硬门禁：体积/指标超预算直接 block，AI 产出与人工产出同标准。
- AI 超预算应对：门禁失败时 AI 给「达预算方案」（代码分割/换轻依赖），人确认后重提。
- 预算变更治理：调预算 = 架构决策，需要性能负责人审批并记录理由。

```javascript
const perfBudgetGate = {
  budgets: { firstLoadJS: '170KB', lcp: '2.5s', newDep: 'requires-approval' },
  onFail: 'AI 生成达标方案（分割/轻量替代）→ 人确认 → 重提',
  change: '调预算 = 架构决策 + 性能 owner 审批',
};
r
```
