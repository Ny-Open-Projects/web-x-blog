---
title: [WCN-202] 框架把 prop 同步到自定义元素的机制差异（React/Vue/Svelte）？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-202：框架把 prop 同步到自定义元素的机制差异（React/Vue/Svelte）？
**答**：
- Vue 3：自动判断——元素有对应 property 则设 property，否则 setAttribute；事件用 @event 原生支持。
- React 19：启发式（props 名以 on 开头且元素有该 property 则绑定），复杂值默认 property。
- Svelte：始终设 property（更可预测），attribute 需显式 attribute:xxx。
- 通用建议：自定义元素用「显式属性白名单」文档声明每个 prop 走 property 还是 attribute。

```javascript
class GoodsCard extends HTMLElement {
  static observedAttributes = ['sku'];
  set count(v) { this._count = v; this._render(); }   // property 路径
  get count() { return this._count; }
  attributeChangedCallback(_n, _o, sku) { this._sku = sku; this._render(); }
}
// Vue: <goods-card :sku="sku" :count="n" />  → sku 走 attribute（有 observed）count 走 property
r
```
