---
title: [WCN-009] slot 插槽与 slotchange 事件如何监听"分布式节点"？assignedNodes 是什么？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Web Components]
type: 面试题
---

## WCN-009：slot 插槽与 slotchange 事件如何监听"分布式节点"？assignedNodes 是什么？

**答**：
- slot 是 Shadow DOM 的"投影点"：子节点不会被移动，只是在渲染时被分配到匹配的 slot 位置（light DOM 仍留在宿主下）。
- 具名 slot：子节点带 `slot="name"` 分配到 `<slot name="name">`；默认内容落到无名 `<slot>`（默认插槽）。
- `slotchange` 事件在"分配集合"变化时触发（添加/删除/移动子节点或改 slot 属性），初始分配不会触发。
- `slot.assignedNodes({ flatten })` 获取实际分配的节点；`flatten: true` 会把空 slot 的 fallback 内容也算进来。反向可用 `node.assignedSlot`。
- 坑：slotchange 拿到的 `e.target.assignedNodes()` 是 light DOM 节点，修改它们会影响外部文档；分布式节点的样式要用 `::slotted()` 或让外部自己管。

```javascript
class DockLayout extends HTMLElement {
  connectedCallback() {
    const root = this.attachShadow({ mode: 'open' });
    root.innerHTML = `
      <header part="header"><slot name="header"></slot></header>
      <main><slot></slot></main>
      <footer><slot name="footer">默认页脚</slot></footer>`;
    root.querySelectorAll('slot').forEach((slot) => {
      slot.addEventListener('slotchange', (e) => {
        const nodes = e.target.assignedNodes().filter(n => n.nodeType === 1);
        console.log('slot 变化:', e.target.name || 'default', nodes);
        // 例：header 区为空时折叠 header
        if (e.target.name === 'header') e.target.parentElement.hidden = nodes.length === 0;
      });
    });
  }
}
customElements.define('dock-layout', DockLayout);
```
