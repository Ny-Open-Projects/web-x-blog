---
title: [WCN-001] Web Components 三大标准是什么？它们如何配合实现"去框架化"组件？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Web Components]
type: 面试题
---

## WCN-001：Web Components 三大标准是什么？它们如何配合实现"去框架化"组件？

**答**：
- 三大标准：Custom Elements（自定义元素注册与生命周期）、Shadow DOM（DOM 与样式的封装隔离）、HTML Templates（`<template>` 惰性模板）。
- 配合方式：`<template>` 定义结构，`customElements.define` 注册元素类，元素在 `connectedCallback` 中把模板挂进 `attachShadow` 创建的影子树。
- 去框架化的意义：组件是浏览器原生能力，不依赖 React/Vue 运行时，可跨框架复用、可独立分发为单个 js 文件甚至直接 HTML 分发。
- 追问钩子：三大标准都不涉及状态管理，所以实践中常与 Signals（细粒度响应式）组合补齐"响应式"这块拼图。

```javascript
class UserBadge extends HTMLElement {
  connectedCallback() {
    const shadow = this.attachShadow({ mode: 'open' });
    // <template> 内容惰性存在，cloneNode 才会实例化
    const tpl = document.getElementById('user-badge-tpl');
    shadow.appendChild(tpl.content.cloneNode(true));
  }
}
customElements.define('user-badge', UserBadge);
```

```html
<template id="user-badge-tpl">
  <style>.name { font-weight: 600; }</style>
  <span class="name"><slot></slot></span>
</template>
<user-badge>张三</user-badge>
```
