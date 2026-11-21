---
title: [SCN-348] 协作评论 AI——AI 辅助回复评论的语气与上下文？
date: 2026-11-20
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-348：评论区 AI 辅助回复（根据评论生成回复草稿）怎么设计？

**答**:
- 触发与生成：评论框 AI 按钮（点击生成回复草稿——显式触发控成本）、上下文组装（评论内容+被评文本片段+历史对话+语气偏好——AGT-212 上下文压缩）、多候选生成（3 个候选：正式/简洁/详细——用户选风格）。
- 语气控制：语气预设（正式/轻松/感谢优先——按关系与场景默认）、公司语气规范注入（企业语气模板——SCN-321 prompt 资产复用）、敏感性检查（回复草稿过敏感词——避免 AI 语气失当）。
- 呈现与采纳：草稿卡片（可编辑后采纳——AI 是助手不是代答）、采纳率埋点（低采纳模板下线——SCN-483 反馈闭环）、重试与反馈（不满意重生成+理由反馈）。
- 边界：不自动发送（AI 只生成草稿——发送权在人）、评论内容的安全边界（涉及薪资/绩效等敏感主题→提示人工处理）。

```javascript
async function aiReply(comment) {
  const ctx = buildCtx({ comment, docSnippet: comment.anchor.text,
    thread: comment.thread, tone: user.tonePref });
  const drafts = await aiApi.reply(ctx, { n: 3,
    tones: ['formal', 'brief', 'detailed'] });
  showDraftPicker(drafts, { editable: true,   // 可编辑采纳
    onSend: (final) => sensitiveCheck(final) && send(final) });
}
// 采纳率：track('ai_reply', { tone, accepted }) →
//   <5% 的模板下线。
// 敏感主题：isSensitiveTopic(ctx) → 引导人工回复。
```
