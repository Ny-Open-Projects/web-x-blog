---
title: [AGT-514] AI 新功能（新模型/新提示词）前端如何做灰度分流与实验分组展示？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-514：AI 新功能（新模型/新提示词）前端如何做灰度分流与实验分组展示

**答**：
- AI 实验的特殊点：分流要「会话级粘性」（同一会话始终同组，否则同一段对话前后模型不一致，体验和统计都乱）。
- 分组信息要透传到埋点：每条消息记录实验分组、模型版本、提示词版本，否则效果评估无从归因。
- UI 上灰度差异要可观测：调试面板显示当前命中的实验与版本，客服排障时能一眼定位。

```javascript
function assignGroup(sessionId, exp) {
  return stickyBucket(exp.key, sessionId)  // 会话级粘性分桶
    ?? hash(exp.key + sessionId) % 100 < exp.ratio ? 'treat' : 'ctrl';
}
function trackTurn(msg, group) {   // 每轮消息带完整归因维度
  track('ai_turn', { ...msg.meta, exp: exp.key, group,
    modelVer: msg.modelVersion, promptVer: msg.promptVersion });
}
```

