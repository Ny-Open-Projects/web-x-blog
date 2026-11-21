---
title: [HW-184] 手写富文本粘贴净化——ClipboardData 解析 text/html + DOMPurify 白名单净化 + 图片拦截确认
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

**答**：粘贴安全管线：paste 事件拦截 → 优先 text/html（保格式）→ DOMPurify 白名单净化（PER-202 Trusted Types 配合）→ 粘贴图片（clipboardData.files）弹确认（外部图片可能巨大/隐私）→ 纯文本兜底。

```javascript
editor.addEventListener('paste', (e) => {
  e.preventDefault();
  const cd = e.clipboardData;
  // 1. 图片：确认后插入（防"复制大图"意外上传）
  const file = [...(cd.files ?? [])].find((f) => f.type.startsWith('image/'));
  if (file) {
    if (confirm(`插入图片（${(file.size / 1048576).toFixed(1)}MB）？`)) insertImage(file);
    return;
  }
  // 2. 富文本：白名单净化（只保留安全标签与属性）
  const html = cd.getData('text/html');
  if (html && window.DOMPurify) {
    const clean = DOMPurify.sanitize(html, {
      ALLOWED_TAGS: ['p', 'br', 'b', 'i', 'em', 'strong', 'ul', 'ol', 'li', 'a', 'blockquote'],
      ALLOWED_ATTR: ['href'],
      FORBID_TAGS: ['style', 'script', 'img'],            // 图片单独确认流程，粘贴流禁 img
    });
    insertHTML(clean);                                    // 配合 Trusted Types policy（PER-202）
    return;
  }
  // 3. 纯文本兜底
  insertText(cd.getData('text/plain'));
});
// 净化清单的价值：从 Word/网页粘贴常带 <style> 全局污染/恶意 script/img 外链——白名单是唯一安全姿势
// FORBID img 的产品语义：粘贴图片走"确认上传"流程（转存自有 CDN），不是直接外链（防盗链/隐私）
```

**评分点**：
- text/html → DOMPurify 白名单 → 纯文本的净化管线——本题核心。
- 粘贴图片的确认流程（大小提示 + 转存）与粘贴流禁 img 的语义。
- Trusted Types 配合（PER-202）。
- ALLOWED_TAGS/ATTR 白名单的具体清单意识。
