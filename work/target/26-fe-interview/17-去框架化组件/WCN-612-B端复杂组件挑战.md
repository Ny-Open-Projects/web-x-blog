---
title: [WCN-612] B 端中后台里表格/弹窗/富文本类复杂组件，用 WC 封装有哪些特殊挑战？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-612：B 端中后台里表格/弹窗/富文本类复杂组件，用 WC 封装有哪些特殊挑战？

**答**：
- 结论：复杂组件的价值在「契约稳定 + 跨项目复用」，挑战集中在 Shadow DOM 与第三方生态（虚拟滚动/富文本/弹层）的集成。
- 典型坑：弹窗需要 append 到 body（teleport）否则被 overflow 裁剪；富文本的浮层定位要处理 shadow 坐标系；表格的列插槽需要 slot 分发而非 props 传 JSX。
- 追问钩子：设计要不要支持「无 Shadow 渲染」？对强定制场景提供 light DOM 模式可降低集成成本——考察权衡思维。

```javascript
class DsModal extends HTMLElement {
  connectedCallback() {
    this.attachShadow({ mode: 'open' });
    this.shadowRoot.innerHTML = '<slot></slot>';
    // 弹层挂到 body 的 portal，避免被祖先 overflow:hidden 裁剪
    this.portal = document.createElement('div');
    this.portal.className = 'ds-modal-portal';
    this.portal.appendChild(this.shadowRoot);
    document.body.appendChild(this.portal);
  }
  open() { this.portal.style.display = 'block'; }
  close() { this.portal.style.display = 'none'; }
  disconnectedCallback() { this.portal?.remove(); }
}
customElements.define('ds-modal', DsModal);
```
