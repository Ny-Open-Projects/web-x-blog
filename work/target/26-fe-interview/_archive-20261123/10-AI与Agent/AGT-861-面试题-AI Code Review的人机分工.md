---
title: [AGT-861] AI Code Review 进了流程，人与 AI 的审查分工怎么划（谁看什么/谁负责什么）？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-861：AI Code Review 进了流程，人与 AI 的审查分工怎么划（谁看什么/谁负责什么）

**答**：
- 分工原则：AI 管「机械面」（风格/类型/明显 bug/测试缺口/安全模式匹配，秒级反馈），人管「语义面」（架构合理性/业务正确性/权衡取舍）。AI 意见分置信级：高置信问题阻塞合并，低置信进"可选建议"不抢注意力。
- 责任归属：AI 意见是提示不是豁免——合并者对代码负全责；反过来 AI 漏报不免除人工审查义务（AI 是增强不是替代）。
- 反馈闭环：开发者对 AI 意见的采纳/拒绝信号回流，持续校准 AI 的误报率——误报高的检查项自动降级为建议。

```javascript
function reviewFlow(pr) {
  const ai = aiReview(pr);
  return {
    blocking: ai.issues.filter(i => i.confidence > 0.9),   // 阻塞合并
    suggestions: ai.issues.filter(i => i.confidence <= 0.9),
    humanFocus: pr.diff.riskyAreas(),              // 人工看语义面
    feedbackLoop: (id, adopt) => calibrate(id, adopt),     // 校准
  };
}
```

