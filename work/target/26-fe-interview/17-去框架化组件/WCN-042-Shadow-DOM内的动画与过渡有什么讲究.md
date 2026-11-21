---
title: [WCN-042] Shadow DOM 里的动画与过渡有什么讲究？keyframes 作用域与 View Transitions 怎么用？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Web Components]
type: 面试题
---

## WCN-042：Shadow DOM 里的动画与过渡有什么讲究？keyframes 作用域与 View Transitions 怎么用？

**答**：
- @keyframes 定义在影子树内就是作用域化的，同名 keyframes 不会与文档冲突；但反过来，影子内引用文档级 keyframes 是不行（不继承），需在影子树内重新声明。
- :host 上做过渡会受外部 `display` 影响吗：`:host { transition }` 生效于宿主元素本身，可配合外部 class 切换实现"组件级"过渡。
- 动画性能：优先 transform/opacity；WC 里可用 `:host { contain: paint }` 收敛重绘范围；影子树不影响合成层规则。
- View Transitions：`document.startViewTransition` 可为 WC 切换动画，配合 `view-transition-name` 命名影子内元素实现共享元素过渡；影子边界不影响 VT，因为 VT 作用于渲染快照。
- 入场动画触发：新 define 的元素渲染在首帧，CSS animation 会自动播放；JS 驱动用 `element.animate()`（WAAPI），无需 keyframes 注入。

```javascript
class FlipCard extends HTMLElement {
  flip() {
    // WAAPI：keyframes 由 JS 提供，天然作用域安全
    this.shadowRoot.querySelector('.front').animate(
      [{ transform: 'rotateY(0)' }, { transform: 'rotateY(180deg)' }],
      { duration: 300, easing: 'ease-in-out', fill: 'forwards' });
  }
  #render() {
    this.attachShadow({ mode: 'open' }).innerHTML = `
      <style>
        :host { display:block; perspective: 600px; contain: paint; }
        .front { transition: transform .3s; transform-style: preserve-3d; }
        @keyframes fade { from { opacity: 0 } }  /* 作用域内的 keyframes */
        .enter { animation: fade .2s ease-out; }
      </style>
      <div class="front enter"><slot></slot></div>`;
  }
}
customElements.define('flip-card', FlipCard);
```
