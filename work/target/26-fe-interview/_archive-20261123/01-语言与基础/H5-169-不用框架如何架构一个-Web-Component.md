---
title: [H5-169] 不用框架如何架构一个 Web Components 组件库？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-169：不用框架如何架构一个 Web Components 组件库？
**答**：
- 样式层：**constructable stylesheet**（`new CSSStyleSheet()` + `adoptedStyleSheets`）全库共享一份样式表，省内存且可热替换；主题用 CSS 变量穿透 Shadow DOM，变体只是改变量值。
- 组件层：统一基类封装 attribute↔property 映射、批渲染、事件解绑这些模板代码（这就是手写一个微型 lit）；对外用 `::part` 暴露样式钩子。
- 工程层：TS + 构建产 ESM，`package.json exports` 按组件分包支持 tree-shaking；测试用 @open-wc/testing + Playwright 快照。
- SSR：提供 Declarative Shadow DOM 服务端渲染（见 H5-173）；文档用 demo 页/Storybook。

```javascript
// 无框架组件库：样式层 + 基类层 + 主题变量

// 1) 样式层：constructable stylesheet 全库共享一份
const sheet = new CSSStyleSheet();
sheet.replaceSync(`
  :host { display: inline-block;
          --btn-bg: #2563eb; --btn-fg: #fff; --btn-radius: 6px; }
  button { background: var(--btn-bg); color: var(--btn-fg);
           border: 0; padding: 8px 16px; border-radius: var(--btn-radius);
           cursor: pointer; font: inherit; }
  button:hover { filter: brightness(1.1); }
`);

// 2) 基类：封装 attribute 映射 / 批渲染 / 事件绑定（手写微型 lit）
class XElement extends HTMLElement {
  #props = {};
  #scheduled = false;
  constructor() {
    super();
    this.attachShadow({ mode: 'open' });
    this.shadowRoot.adoptedStyleSheets = [sheet];
    this.shadowRoot.addEventListener('click', (e) => {
      const act = e.target.closest('[data-action]')?.dataset.action;
      if (act) this[act]?.();
    });
  }
  connectedCallback() { this.#flush(); }
  #flush() {
    if (this.#scheduled) return;
    this.#scheduled = true;
    queueMicrotask(() => {
      this.#scheduled = false;
      this.shadowRoot.innerHTML = this.render();
    });
  }
  render() { return ''; }
}

// 3) 具体组件：变体只是切 CSS 变量值，样式规则不变
class XButton extends XElement {
  static observedAttributes = ['variant'];
  attributeChangedCallback(_, __, variant) {
    this.style.setProperty('--btn-bg',
      variant === 'danger' ? '#ef4444' : variant === 'ghost' ? '#94a3b8' : '#2563eb');
  }
  render() {
    return `<button part="main" data-action="click"><slot></slot></button>`;
  }
  click() { this.dispatchEvent(new CustomEvent('x-click', { bubbles: true })); }
}
customElements.define('x-button', XButton);

// 组件库清单（面试要点）：
// 1) constructable stylesheet 复用 + CSS 变量主题 + ::part 样式钩子
// 2) 基类统一管理 attribute/property 映射与批渲染 —— 这就是手写微型 lit
// 3) 构建：TS + esbuild 产 ESM，exports 按组件分包支持 tree-shaking
// 4) SSR 提供 Declarative Shadow DOM（见 H5-173）；文档 demo 页 / Storybook
```
