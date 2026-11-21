---
title: [WCN-040] WC 的弹层/下拉组件如何处理 z-index 与裁剪问题？top layer 与 Popover API 怎么用？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Web Components]
type: 面试题
---

## WCN-040：WC 的弹层/下拉组件如何处理 z-index 与裁剪问题？top layer 与 Popover API 怎么用？

**答**：
- 传统痛点：下拉/弹层放影子树里会被祖先 `overflow:hidden` 裁剪、被 z-index 压住；portal 到 body 又脱离组件上下文、样式与 slot 断开。
- 现代解法：Popover API（`popover` 属性 + `showPopover()`）把元素提升到浏览器 top layer，无视裁剪与 z-index，且自带 Esc 关闭、点击外部关闭（light dismiss）、`::backdrop` 伪元素；元素仍留在原 DOM 位置，slot 与事件都正常。
- `<dialog>.showModal()` 同样进 top layer，适合模态；Popover 适合非模态（下拉、tooltip、toast）。
- top layer 内的定位：popover 是 fixed 语义，需自己算锚点位置（CSS Anchor Positioning `anchor()` 正在普及，可用 polyfill）。
- 兜底方案：老浏览器用 `position: fixed` + 计算 viewport 坐标，或 portal 到 body 后用 context/slot 回传数据。

```javascript
class WcDropdown extends HTMLElement {
  connectedCallback() {
    const root = this.attachShadow({ mode: 'open' });
    root.innerHTML = `
      <style> [popover] { inset:auto; border:1px solid #e5e7eb; border-radius:8px;
        box-shadow:0 8px 24px rgba(0,0,0,.12); padding:8px; } </style>
      <button popovertarget="menu">选项</button>
      <ul id="menu" popover><slot></slot></ul>`;
    // top layer：不受任何 overflow/z-index 影响；Esc/点外自动关闭
    root.getElementById('menu').addEventListener('toggle', (e) => {
      this.dispatchEvent(new CustomEvent('wc-open-change', {
        bubbles: true, composed: true, detail: { open: e.newState === 'open' },
      }));
    });
  }
}
customElements.define('wc-dropdown', WcDropdown);
```
