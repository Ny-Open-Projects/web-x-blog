---
title: [H5-042] Shadow DOM 里的事件是如何冒泡的？composed 是什么？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-042：Shadow DOM 里的事件是如何冒泡的？composed 是什么？
**答**：
- 影子树内部事件的冒泡对外部做了"重定向"：`event.target` 在越过 shadow 边界时被改写为宿主元素，保护内部结构。
- `event.composed === true` 的事件（如 click、focus、input）能穿越 shadow 边界继续冒泡；`composed: false` 的（如 mouseenter）到边界就停。
- 在影子树内监听时拿到的 target 是真实内部元素；外部监听宿主时拿到的是宿主。
- 自定义事件默认不 composed，跨边界派发要 `new CustomEvent(type, { bubbles: true, composed: true })`。

```javascript
class MyButton extends HTMLElement {
  connectedCallback() {
    const shadow = this.attachShadow({ mode: 'open' });
    shadow.innerHTML = `<button>点我</button>`;
    const btn = shadow.querySelector('button');

    // 影子树内：target 是真实内部 button
    btn.addEventListener('click', (e) => console.log('inner target:', e.target.tagName)); // BUTTON

    // 组件对外派发自定义事件：必须 composed 才能被页面收到
    btn.addEventListener('click', () => {
      this.dispatchEvent(
        new CustomEvent('my-press', { bubbles: true, composed: true, detail: { at: Date.now() } })
      );
    });
  }
}
customElements.define('my-button', MyButton);
```

```html
<my-button></my-button>

<script>
  // 页面侧：composed 事件穿透影子边界，target 已被改写为宿主
  document.querySelector('my-button').addEventListener('my-press', (e) => {
    console.log('outer target:', e.target.tagName); // MY-BUTTON，不是 BUTTON
    console.log('detail:', e.detail);
  });
</script>
```

## 九、性能加载与 SEO
