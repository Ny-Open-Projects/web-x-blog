---
title: [H5-039] Shadow DOM 如何实现样式与结构隔离？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-039：Shadow DOM 如何实现样式与结构隔离？
**答**：
- `attachShadow({ mode: 'open' })` 创建影子树：内部 DOM 与样式对外部隐藏，页面 CSS 进不来、影子样式出不去（部分继承属性如 color/font 除外）。
- `mode: 'open'` 可通过 `el.shadowRoot` 访问，`closed` 则完全拿不到。
- 组件内样式用 `:host` 定义宿主自身样式、`::slotted()` 微调被分发子元素、CSS 自定义属性穿透传参。
- 收益：不依赖命名约定/前缀就能避免样式冲突，是"真"隔离（不同于 CSS Modules 的改名隔离）。

```javascript
class MyCard extends HTMLElement {
  connectedCallback() {
    const shadow = this.attachShadow({ mode: 'open' });

    shadow.innerHTML = `
      <style>
        /* 页面的 .title 样式影响不到这里 */
        :host { display: block; border: 1px solid #ddd; border-radius: 8px; }
        :host([hidden]) { display: none; }

        .title { color: #3367d6; }        /* 组件私有样式 */
        ::slotted(p) { margin: 0 12px; }  /* 修饰使用者塞进来的子元素 */
      </style>
      <div class="title"><slot name="title">默认标题</slot></div>
      <div class="body"><slot></slot></div>
    `;
  }
}
customElements.define('my-card', MyCard);
```

```html
<!-- 页面样式无论如何都污染不了组件内部 -->
<style> .title { color: red; } </style>

<my-card>
  <span slot="title">用户信息</span>
  <p>插槽内容样式由组件控制</p>
</my-card>

<script>
  // open 模式下外部可访问影子树
  console.log(document.querySelector('my-card').shadowRoot.querySelector('.title'));
</script>
```
