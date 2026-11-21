---
title: [WCN-038] `::slotted()` 与 `::part` 有什么区别？分别覆盖哪类定制需求？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Web Components]
type: 面试题
---

## WCN-038：`::slotted()` 与 `::part` 有什么区别？分别覆盖哪类定制需求？

**答**：
- `::slotted(selector)`：作用于"被 slot 投影的 light DOM 节点"（组件使用者写的子元素），但只能命中节点本身，不能命中它的后代；只有直接被分配的顶层节点受控。
- `::part(name)`：作用于"影子树内部的节点"（组件作者导出的部件），可配合 `::part(a b)` 跨层级穿透到子组件导出的 part。
- 方向相反：::slotted 是"组件管外面的内容"，::part 是"外面管组件的内部"。
- 限制：::slotted 的选择器不能组合后代（`::slotted(.a .b)` 无效）；::part 不能用结构关系选择器（`::part(title) span` 无效），只能加属性过滤 `::part(btn)[data-x]`。
- 都不可用时兜底：CSS 自定义属性（传 token）或让外部直接持有 light DOM 节点自行加 class。

```javascript
class CardList extends HTMLElement {
  connectedCallback() {
    this.attachShadow({ mode: 'open' }).innerHTML = `
      <style>
        /* 定制使用者投进来的 li（仅顶层，不能到 li 的子节点） */
        ::slotted(li) { border-top: 1px solid #e5e7eb; }
        ::slotted(li:first-child) { border-top: 0; }
        /* 定制自己的内部部件 */
        .hd { padding: 12px; }
      </style>
      <div class="hd" part="header"><slot name="title"></slot></div>
      <ul><slot></slot></ul>`;
  }
}
customElements.define('card-list', CardList);
```

```html
<style>
  /* 外部视角 */
  card-list::part(header) { background: #f9fafb; }
  card-list li { color: #374151; }  /* li 子节点样式：light DOM 本来就在外部文档，可直接管 */
</style>
<card-list><span slot="title">商品</span><li>耳机</li><li>键盘</li></card-list>
```
