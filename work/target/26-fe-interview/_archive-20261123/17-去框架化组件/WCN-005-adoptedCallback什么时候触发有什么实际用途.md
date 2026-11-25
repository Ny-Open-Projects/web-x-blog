---
title: [WCN-005] adoptedCallback 什么时候触发？在跨 iframe 组件迁移中有什么实际用途？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Web Components]
type: 面试题
---

## WCN-005：adoptedCallback 什么时候触发？在跨 iframe 组件迁移中有什么实际用途？

**答**：
- 仅当元素通过 `document.adoptNode()`（或 appendChild 跨文档）从一个 Document 迁移到另一个 Document 时触发，源文档触发 disconnected、目标文档触发 adopted 再 connected。
- 典型场景：编辑器/低代码平台把 iframe 预览里的组件"提出"到主文档；或 SSR 水合时把片段从模板文档迁到主文档。
- 用途一：迁移后重建与原文档绑定的资源——在旧文档上注册的事件监听、ResizeObserver、定时器要迁移到新 document 域。
- 用途二：更新 `this.ownerDocument` 相关逻辑，例如在新文档里重新注册 form-associated、重新获取 CSSStyleSheet。
- 注意：adoptedCallback 触发顺序早于新文档的 connectedCallback，且同一元素生命周期里可多次触发。

```javascript
class DraggableCard extends HTMLElement {
  adoptedCallback(oldDoc, newDoc) {
    // 事件监听绑定在旧 document 上，迁移后需要解绑重绑
    oldDoc.removeEventListener('keydown', this._onKey);
    newDoc.addEventListener('keydown', this._onKey);
    // ResizeObserver 跟随 window，需在新文档重建
    this._ro?.disconnect();
    this._ro = new newDoc.defaultView.ResizeObserver(() => this.render());
    this._ro.observe(this);
  }
  render() { /* ... */ }
}
customElements.define('draggable-card', DraggableCard);
```
