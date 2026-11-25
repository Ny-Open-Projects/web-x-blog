---
title: [SCN-1224] AI 产品的生成内容导出（Markdown/图片/PDF）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1224：AI 产品的生成内容导出（Markdown/图片/PDF）

**答**：
- 导出：会话导出（Markdown 全文/带样式截图/PDF），长会话分段导出。
- 格式：导出保留代码块/引用/公式（格式保真）。
- 分享：会话分享链接（只读快照，脱敏选项）。

```javascript
// 会话导出
async function exportConversation(sessionId, format) {
  const msgs = await api(`/session/${sessionId}/messages`);
  if (format === 'md')
    return download(mdOf(msgs), 'conversation.md');
  if (format === 'pdf')
    return pdfRender(msgs);
  return shareLink(sessionId, { readonly: true, masked: true });
}
function mdOf(msgs) {
  return msgs.map(m => `## ${m.role}\n\n${m.content}`).join('\n\n');
}
function download(text, name) { return text.length; }
function pdfRender(msgs) { return 'pdf'; }
function shareLink(id, o) { return `/s/${id}`; }
```
