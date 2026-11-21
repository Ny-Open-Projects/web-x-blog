---
title: [CSS-188] 样式隔离方案有哪些？从 iframe 到 Shadow DOM 怎么选？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-188：样式隔离方案有哪些？从 iframe 到 Shadow DOM 怎么选？

**答**：
- 隔离强度排序：iframe（文档级）> Shadow DOM（树级）> CSS Modules/Scoped（编译期改名）> BEM/namespace（纯约定）。
- iframe：最强隔离与最贵成本（多文档、内存、通信、弹窗裁剪），适合微前端与富文本编辑器。
- Shadow DOM：运行时真隔离，但全局继承属性（color 等）、@font-face、选择器穿透（:host、::part）需要专门处理。
- 选型：微前端用 iframe/Shadow；组件库用 CSS Modules 或 Shadow；应用内部用 BEM + @layer。

```javascript
// 1. Shadow DOM：树级隔离
class MyWidget extends HTMLElement {
  connectedCallback() {
    const root = this.attachShadow({ mode: 'open' });
    root.innerHTML = `
      <style>
        :host { display: block; }       /* 宿主元素自身的样式出口 */
        p { color: red; }               /* 与外部完全隔离 */
        ::slotted(span) { color: blue; } /* 插槽内容的有限控制 */
      </style>
      <p>隔离内容</p>
      <slot></slot>`;
  }
}
customElements.define('my-widget', MyWidget);
// 暴露主题钩子：外部用 my-widget::part(title) { ... } 定制内部

// 2. CSS Modules：构建期 hash，同文档但类名唯一
// import s from './widget.module.css'  →  s.title === "Widget_title__x1"

// 3. iframe：文档级隔离，适合完全不受宿主样式影响的场景
// iframe.srcdoc = '<style>p{color:red}</style><p>独立文档</p>'
```
