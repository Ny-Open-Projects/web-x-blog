---
title: [AGT-363] 记忆压缩策略——什么信息摘要、什么信息必须保留？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-363：压缩上下文时，怎么决定什么摘要、什么原文保留？

**答**:
- 保留优先级（永不摘要）：用户显式约束与决策（"必须用方案 B"）、关键数字与实体（金额/日期/ID——摘要改数字=事故，AGT-212）、安全红线（AGT-288 锚定）、任务目标本身。
- 可摘要项：过程性对话（怎么讨论出来的）、工具原始输出（保留结论与引用指针）、寒暄与重复内容。
- 摘要纪律：摘要输出结构化（决策/事实/待办三段）、摘要标注"由 AI 生成"（回溯时知道非原文）、关键项摘要后保留引用指针（"详见第 N 轮原文"——需要时可回查）。
- 分层执行：先规则筛选（数字/约束正则提取强制保留），再 LLM 摘要剩余部分——规则保关键，模型压缩其余，混合管线比纯 LLM 摘要可靠。

```javascript
async function smartCompact(history) {
  const mustKeep = extractByRule(history,
    { numbers: true, constraints: true, decisions: true });
  const rest = history.filter(m => !mustKeep.has(m));
  const summary = await llm(`按 {决策/事实/待办} 压缩，
    不得改写数字与实体。`, rest);
  return [
    { role: 'system', content: '关键约束（原文）：' + mustKeep },
    { role: 'system', content: '早期纪要（AI 摘要）：' + summary },
    ...recent(history, 6),   // 近期原文保留
  ];
}
```
