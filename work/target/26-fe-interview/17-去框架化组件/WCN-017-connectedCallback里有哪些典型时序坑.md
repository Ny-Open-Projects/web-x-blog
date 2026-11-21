---
title: [WCN-017] connectedCallback 里有哪些典型时序坑？为什么它可能被多次触发？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Web Components]
type: 面试题
---

## WCN-017：connectedCallback 里有哪些典型时序坑？为什么它可能被多次触发？

**答**：
- 多次触发：元素被移动（remove + append）或从隐藏容器（如 `display:none` 不会触发，但 iframe 间移动、拖拽重排会）中移入移出都会重新触发，所以"只初始化一次"的逻辑要自己加标志位。
- 坑：每次 connected 都 `attachShadow` 会抛错——shadow root 只能 attach 一次，正确姿势是在 constructor attach、connected 里只做数据绑定。
- 坑：connected 时属性可能还没到齐（见 upgrade 时序），依赖 attribute 的初始化要容忍 undefined 或等 attributeChangedCallback 驱动。
- 坑：在 connected 里同步读 `offsetWidth` 强制同步布局，长列表会放大成性能问题；批量场景应集中在 requestAnimationFrame。
- 移动场景：sortable 列表拖拽用 insertBefore 是"移动"不是"删除重建"，connected 会再次触发而 constructor 不会——资源初始化放 constructor、清理放 disconnected 才能正确配对。

```javascript
class SortableItem extends HTMLElement {
  constructor() {
    super();
    this.#root = this.attachShadow({ mode: 'open' }); // 只能一次，放 constructor
    this.#root.innerHTML = '<div part="item"><slot></slot></div>';
  }
  #boundDrag;
  connectedCallback() {
    if (this.#boundDrag) return;          // 防重复绑定
    this.#boundDrag = (e) => { /* drag 逻辑 */ };
    this.addEventListener('dragstart', this.#boundDrag);
  }
  disconnectedCallback() {
    this.removeEventListener('dragstart', this.#boundDrag);
    this.#boundDrag = null;
  }
  #root;
}
customElements.define('sortable-item', SortableItem);
```
