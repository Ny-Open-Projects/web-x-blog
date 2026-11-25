---
title: [WCN-620] Shadow DOM 中的 ARIA 有哪些陷阱？金融级无障碍验收如何过关？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-620：Shadow DOM 中的 ARIA 有哪些陷阱？金融级无障碍验收如何过关？

**答**：
- 结论：最大陷阱是跨 Shadow 边界的 ID 引用失效（aria-labelledby/aria-controls 引用 shadow 外的 id 无法解析）以及焦点管理。
- 做法：ARIA 引用尽量在同一 shadow 树内闭合；确实要跨边界时同步维护 id；用 ElementInternals 暴露 ARIA 状态（ariaLabel/role）；焦点用 delegatesFocus + tabindex 管理。
- 追问钩子：如何验收？ axe-core 在 Shadow DOM 下需特殊配置 + 读屏软件（NVDA/VoiceOver）实测——考察对「自动化不能覆盖全部」的认知。

```javascript
class DsDialog extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open', delegatesFocus: true });
    this.internals = this.attachInternals();
    this.internals.role = 'dialog';
  }
  connectedCallback() {
    const titleId = 'ds-dialog-title';
    this.shadowRoot.innerHTML = `
      <h2 id="${titleId}">标题</h2>
      <div role="document" aria-labelledby="${titleId}"><slot></slot></div>
      <button tabindex="0">关闭</button>`;
    this.internals.ariaLabel = '提示对话框';
  }
  focus() { this.shadowRoot.querySelector('button')?.focus(); }
}
customElements.define('ds-dialog', DsDialog);
```
