---
title: [H5-264] 剪贴板 API：navigator.clipboard 的权限与降级
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, PWA]
type: 面试题
---

## H5-264：剪贴板 API：navigator.clipboard 的权限与降级

**答**：
- 写入 clipboard.writeText：需 https + 用户手势（或已授权）；读取 clipboard.readText 需权限弹窗，用户拒绝是常态
- 权限查询：`navigator.permissions.query({ name: 'clipboard-read' })` 提前判断
- 复制富文本：ClipboardItem + write（text/html 与 text/plain 多格式一起写入）
- 降级方案：document.execCommand('copy')（已废弃但仍是老浏览器兜底）——需要先创建选区；iframe hack 处理 iOS 兼容
- 坑：异步 clipboard API 在非手势上下文（setTimeout 回调）调用会失败，要在事件处理函数同步链路内调用

```javascript
async function copyRich(node) {
  const html = node.outerHTML, text = node.textContent;
  if (navigator.clipboard && window.ClipboardItem) {
    await navigator.clipboard.write([new ClipboardItem({
      'text/html': new Blob([html], { type: 'text/html' }),
      'text/plain': new Blob([text], { type: 'text/plain' }),
    })]);
  } else fallbackExecCommand(text); // 老浏览器兜底
}
```
