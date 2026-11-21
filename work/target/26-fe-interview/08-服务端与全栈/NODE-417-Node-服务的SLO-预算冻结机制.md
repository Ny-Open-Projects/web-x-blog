---
title: [NODE-417] Node 服务的 SLO 错误预算与发布冻结机制如何运转？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-417：SLO 错误预算与发布冻结
**答**:
- 预算机制落地（ARC-354 服务端版）：SLO 定义（可用性/延迟 P99）→ 预算计算（按月）→ 燃烧监控（多窗口 NODE-404）→ 阈值动作：预算消耗 50% 提示、80% 减速发布（只允许修复类）、100% 冻结特性发布。
- 冻结的执行力：冻结状态写进发布平台（特性发布按钮禁用，只有 fix/hotfix 通道可走）；例外审批（业务关键发布需架构委员会批准并记录）。
- 预算恢复：新预算周期自动恢复；提前恢复需证明根因修复（改进项完成，ARC-407）。
- 避免博弈：冻结不是惩罚而是共同决策机制——冻结期间团队合力做稳定性（技术债清理），预算花完往往正是还债的时机。
- 透明度：预算看板公开（全团队可见），发布决策有数据依据而非主观争执。
```javascript
function releaseGate(slo) {
  const burn = slo.used / slo.budget;
  if (burn >= 1) return { allow: ['fix', 'hotfix'], freeze: true,
    resume: '改进项完成或下个预算周期' };
  if (burn >= 0.8) return { allow: ['fix', 'hotfix', 'lowRiskFeature'],
    note: '预算告急，非核心特性延后' };
  return { allow: '*' };
}
```
