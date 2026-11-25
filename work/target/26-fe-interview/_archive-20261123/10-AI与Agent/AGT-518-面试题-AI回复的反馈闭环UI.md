---
title: [AGT-518] 点赞点踩之外，AI 回复的反馈体系怎么设计才能真正支撑迭代？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-518：点赞点踩之外，AI 回复的反馈体系怎么设计才能真正支撑迭代

**答**：
- 反馈要结构化：点踩时弹标签（答非所问/内容错误/过时/格式差）+ 可选文字，比裸点踩信息量大十倍。
- 负反馈自动关联诊断数据：traceId、引用来源、模型版本一起入库，评估组能直接把反馈变成评测用例。
- 反馈状态要回给用户：被采纳的反馈（"已修复"）推送回来，形成闭环才会持续有反馈。

```javascript
async function submitFeedback(msgId, { type, tags, comment }) {
  const turn = getTurn(msgId);
  await api.feedback({ msgId, type, tags, comment,
    traceId: turn.traceId, modelVer: turn.modelVersion,
    sources: turn.sources?.map(s => s.id) });  // 归因上下文一起带走
  if (tags.includes('内容错误')) {
    evalQueue.add({ from: 'feedback', turn });  // 直接进评测用例候选池
  }
}
```

