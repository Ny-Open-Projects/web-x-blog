---
title: [WCN-592] 平台化「文档即产品」：如何把文档站做成可交互 playground + 版本切换 + 反馈闭环？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-592：平台化「文档即产品」：如何把文档站做成可交互 playground + 版本切换 + 反馈闭环？

**答**：
- 结论：文档站 = 内容层（MDX）+ 交互层（在线编辑器）+ 版本层（多版本文档）+ 反馈层（问题上报）。
- playground：内置在线编译器，实时把示例代码渲染进隔离 iframe，错误捕获后展示。
- 版本切换：URL 带版本号，文档与示例都从对应版本产物加载，避免「文档新版、示例旧版」。
- 追问：如何保证 playground 示例不污染主站？（答：iframe sandbox + 独立源，限制 postMessage 白名单）

```javascript
function createPlayground(code, version) {
  const iframe = document.createElement('iframe');
  iframe.sandbox = 'allow-scripts allow-same-origin';
  iframe.srcdoc = `<script type="module">
    import { bootstrap } from '/ds/${version}/core.js';
    try { ${code} } catch (e) { parent.postMessage({ type:'error', msg:String(e) }, '*'); }
  <\/script>`;
  window.addEventListener('message', e => { if (e.data.type === 'error') showError(e.data.msg); });
  return iframe;
}
```
