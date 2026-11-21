---
title: [AIC-373] 「这个 PR 可能引发线上事故」——AI 事故预测能做吗？怎么做才靠谱？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-373：「这个 PR 可能引发线上事故」——AI 事故预测能做吗？怎么做才靠谱？
**答**：
- 基于历史模式：从历史事故的 diff 特征（改了配置/动了支付链路/无测试覆盖高风险路径）学预测规则。
- 预测输出必须可解释：列出触发的历史事故先例（哪几个 PR 相似）——纯分数没人信。
- 精准率优先：预测宁可少报，误报多了「狼来了」，只保留精准率 > 50% 的规则。
- 闭环验证：预测命中记录 vs 实际事故对照，季度校准规则。

```javascript
async function predictIncident(pr: PR) {
  const similar = await findSimilarPastPRs(pr.diff, { inIncidents: true });
  if (similar.length && precision(similar) > 0.5)
    return { warn: true, precedents: similar, reason: '带先例的可解释预警' };
  return { warn: false };
}
r
```
