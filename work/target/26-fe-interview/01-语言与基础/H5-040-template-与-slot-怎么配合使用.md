---
title: [H5-040] template 与 slot 怎么配合使用？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-040：template 与 slot 怎么配合使用？
**答**：
- `<template>` 里的内容不渲染、不发请求（img 不加载），clone 后插入才生效，适合存放可复用的 DOM 模板。
- `<slot>` 是 Web Components 的"占位符"：分具名插槽与默认插槽两种，把使用者的子元素分发进影子树。
- 多个同名内容插入同一 slot 时按声明顺序排列；`slotchange` 事件监听分发变化。
- 与 Vue 的插槽概念一致，理解成本为迁移而来。

```html
<template id="tpl">
  <style>
    .root { padding: 8px; background: #f5f5f5; }
  </style>
  <div class="root">
    <h3><slot name="title">未命名</slot></h3>
    <div><slot>默认内容区</slot></div>
  </div>
</template>

<script>
  customElements.define('x-panel', class extends HTMLElement {
    connectedCallback() {
      const shadow = this.attachShadow({ mode: 'open' });
      // template 内容克隆后插入影子树
      shadow.appendChild(document.getElementById('tpl').content.cloneNode(true));
    }
  });
</script>

<x-panel>
  <span slot="title">订单详情</span>
  <p>这里是默认插槽分发的内容</p>
</x-panel>
```
