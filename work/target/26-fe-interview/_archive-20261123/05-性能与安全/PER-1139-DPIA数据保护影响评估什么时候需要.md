---
title: [PER-1139] DPIA（数据保护影响评估）什么时候需要做
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1139：DPIA（数据保护影响评估）什么时候需要做

**答**：
- 触发条件：大规模处理敏感数据、系统性监控（行为画像/追踪）、自动化决策（评分/风控自动拒绝）、新技术引入（指纹/AI 分析）。
- 内容：处理目的与合法性、必要性论证（能否更少数据达成）、风险与缓解措施、残余风险接受。
- 工程角色：提供技术事实（数据流/保留期/加密状态），法务主导评估结论。
- 轻量化：常规功能用 checklist 快筛，命中触发条件才做完整 DPIA。

```javascript
// DPIA 快速筛查
const TRIGGERS = [
  f => f.sensitiveData?.length > 0,
  f => f.systematicMonitoring,
  f => f.automatedDecision,
  f => f.newTech?.some(t => ['fingerprint', 'ai-scoring'].includes(t)),
];
function dpiaScreen(feature) {
  const hit = TRIGGERS.map((t, i) => t(feature) ? i : null).filter(v => v !== null);
  return { needFullDPIA: hit.length > 0, triggers: hit,
    note: hit.length ? '走完整 DPIA 流程（法务主导）' : 'checklist 备案即可' };
}
```
