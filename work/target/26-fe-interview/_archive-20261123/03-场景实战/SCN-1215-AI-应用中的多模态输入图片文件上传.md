---
title: [SCN-1215] AI 应用中的多模态输入（图片/文件上传理解）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1215：AI 应用中的多模态输入（图片/文件上传理解）

**答**：
- 输入：图片（拖拽粘贴/截图上传）、文件（PDF/Word 解析后注入上下文）。
- 渲染：输入区缩略图/文件卡片（解析状态），大文件分块解析进度。
- 限制：文件大小/页数限制与超限提示。

```javascript
// 多模态输入
async function multimodalUpload(file) {
  if (file.size > 20 * 1024 * 1024)
    return { ok: false, reason: '文件超过 20MB' };
  const parsed = file.type.startsWith('image/')
    ? { type: 'image', url: await toDataURL(file) }
    : await parseDocument(file);                       // PDF 分块解析
  return { ok: true, ...parsed,
    progress: parsed.pages ? `解析中 ${parsed.pages} 页` : null };
}
async function parseDocument(f) { return { type: 'doc', pages: 10 }; }
async function toDataURL(f) { return URL.createObjectURL(f); }
```
