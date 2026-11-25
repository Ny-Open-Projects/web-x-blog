---
title: [SCN-1227] AI 产品的多语言界面与翻译辅助
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1227：AI 产品的多语言界面与翻译辅助

**答**：
- 多语言：界面 i18n + 对话内容实时翻译（消息级翻译按钮）。
- 方向：RTL 语言（阿拉伯语）布局镜像适配。
- 质量：AI 翻译标注"机器翻译"，关键内容建议人工。

```javascript
// 消息翻译
async function translateMessage(msgId, to) {
  const r = await api('/translate', { msgId, to });
  return { translated: r.text,
    machine: true,                                     // 机器翻译标注
    original: showToggle(msgId) };                     // 原文切换
}
function showToggle(id) { return true; }
```
