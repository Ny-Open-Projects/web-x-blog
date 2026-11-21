---
title: [WCN-058] 笔试：手写带 slot 分发与空态检测的卡片容器 WC
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, Web Components]
type: 笔试题
---

## WCN-058：笔试：手写带 slot 分发与空态检测的卡片容器 WC

**题目**：`<card-container>`：① 具名插槽 header/footer + 默认插槽；② 默认插槽无内容时显示空态（用 `assignedNodes` 判断，忽略纯空白文本节点）；③ footer 无内容时隐藏 footer 区；④ slotchange 响应宿主动态增删子节点；⑤ 对外派发 `content-change`（detail.count）。

**答**：

```javascript
class CardContainer extends HTMLElement {
  connectedCallback() {
    if (this.shadowRoot) return;
    const root = this.attachShadow({ mode: 'open' });
    root.innerHTML = `
      <style>
        .hd, .ft { padding: 8px 12px; background: #f9fafb; }
        .ft[hidden] { display: none; }
        .empty { padding: 32px; text-align: center; color: #9ca3af; }
      </style>
      <div class="hd" part="header"><slot name="header"></slot></div>
      <div class="bd" part="body">
        <slot id="body"></slot>
        <div class="empty">暂无内容</div>
      </div>
      <div class="ft" part="footer" hidden><slot name="footer"></slot></div>`;
    this.#bodySlot = root.getElementById('body');
    this.#footerSlot = root.querySelector('slot[name=footer]');
    this.#empty = root.querySelector('.empty');
    this.#sync();
    this.#bodySlot.addEventListener('slotchange', () => this.#sync());
    this.#footerSlot.addEventListener('slotchange', () => this.#sync());
  }
  #bodySlot; #footerSlot; #empty;
  #sync() {
    // 忽略纯空白文本节点，只统计有效内容
    const nodes = (this.#bodySlot.assignedNodes())
      .filter((n) => n.nodeType === 1 || (n.nodeType === 3 && n.textContent.trim()));
    this.#empty.hidden = nodes.length > 0;
    const fNodes = this.#footerSlot.assignedNodes().filter((n) => n.nodeType === 1);
    this.#footerSlot.parentElement.hidden = fNodes.length === 0;
    this.dispatchEvent(new CustomEvent('content-change', {
      bubbles: true, composed: true, detail: { count: nodes.length, hasFooter: fNodes.length > 0 },
    }));
  }
}
customElements.define('card-container', CardContainer);
// 动态：host.append(节点) 或 host.querySelector('li').remove() 均会触发 slotchange
```

**评分点**：
- 空态判定过滤空白文本节点（常见踩坑点）。
- slotchange 覆盖增删/移动子节点与 slot 属性迁移。
- footer 空时隐藏容器而非只隐藏 slot（避免占位背景）。
- 事件 composed + detail 统计口径清晰；connected 里先手动 #sync 一次（初始分配不触发 slotchange）。
