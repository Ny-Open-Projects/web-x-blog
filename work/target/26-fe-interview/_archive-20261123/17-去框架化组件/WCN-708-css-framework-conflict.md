---
title: [WCN-708] WC 与宿主 Tailwind/Bootstrap 的全局样式优先级冲突如何治理？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-708：WC 与宿主 Tailwind/Bootstrap 的全局样式优先级冲突如何治理？

**答**：
- 结论：Shadow DOM 本身隔离了大多数组件样式，冲突主要发生在「::part 暴露的元素」和「slotted 内容」；用 CSS 自定义属性作为主题接口，避免直接依赖宿主全局类。
- 为 slotted 内容提供显式的 ::slotted 兜底样式并提升特异性（如 `:host ::slotted(.btn)`）；用 `@layer` 与 `all: revert` 切断继承链。
- 追问钩子：宿主 `* { box-sizing: border-box }` 会影响 Shadow 内元素吗？考察对 CSS 继承与通用选择器边界的理解。

```javascript
class DsCard extends HTMLElement {
  connectedCallback() {
    const root = this.attachShadow({ mode: 'open' });
    root.innerHTML = `
      <style>
        :host { --ds-pad: 16px; all: initial; display: block; }
        .body { padding: var(--ds-pad, 16px); }
        /* 提升 ::slotted 特异性，压过宿主全局类 */
        :host ::slotted(.btn) { border-radius: 6px !important; }
      </style>
      <div class="body"><slot></slot></div>`;
  }
}
customElements.define('ds-card', DsCard);
```
