---
title: [AIC-333] AI 如何做 oncall 辅助（值班时的快速定位）？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-333：AI 如何做 oncall 辅助（值班时的快速定位）？
**答**：
- 告警富化：告警触发时 AI 自动聚合上下文（最近变更/相关面板/相似历史告警的处理记录）。
- runbook 检索：按告警类型匹配 runbook 步骤并跟踪执行状态。
- 历史相似度：用 embedding 检索「同症状历史事故」的根因与解法，给排障起点。
- 边界：AI 只做信息聚合与建议，执行操作（扩容/回滚）必须人触发——避免自动化误操作放大事故。

```javascript
async function oncallAssist(alert: Alert) {
  const ctx = await Promise.all([recentChanges(alert.service), similarIncidents(alert.signature),
                                 runbookFor(alert.type)]);
  return { brief: ctx, suggestedSteps: ctx[2].steps, execute: 'human-only' };
}
r
```
