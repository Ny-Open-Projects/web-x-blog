---
title: [AIC-282] AI 评审发现高风险变更已合入主干，如何给出「可执行的回滚建议」？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-282：AI 评审发现高风险变更已合入主干，如何给出「可执行的回滚建议」？
**答**：
- 回滚建议三要素：回滚方式（revert commit / 开关关闭 / 降级到旧版本）、影响面（关联 PR/模块）、验证步骤（回滚后检查什么）。
- 提前备好：高风险 PR 合入时就生成「预签名的回滚方案」，出事时直接执行不现想。
- 能力开关优先于代码回滚：feature flag 一键关闭是首选路径。
- 回滚演练：季度用 AI 生成模拟故障场景演练回滚流程，验证方案可执行。

```javascript
const rollbackPlan = (pr: PR) => ({
  prefer: pr.hasFlag ? `关闭开关 ${pr.flag}，秒级生效` : `git revert ${pr.mergeSha}`,
  impact: impactedModules(pr),        // AI 从 diff 推导
  verify: ['回归核心链路冒烟', '观察错误率 5 分钟'],
  prerolled: true,                    // 合入时生成，出事即用
});
r
```
