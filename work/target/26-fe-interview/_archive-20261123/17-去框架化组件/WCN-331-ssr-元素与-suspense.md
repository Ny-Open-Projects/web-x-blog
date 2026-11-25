---
title: [WCN-331] 元素与框架 Suspense 边界的协同（元素异步内容挂起）？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-331：元素与框架 Suspense 边界的协同（元素异步内容挂起）？
**答**：
- 元素内部异步数据：元素自身管理（skeleton → content）——不依赖框架 Suspense（shadow 内组件框架不可见）。
- 混合：元素作为 Suspense 的同步子（元素本身同步渲染骨架，内部异步自治）。
- 事件：元素内容就绪派发 ready 事件 → 宿主可驱动 Suspense 状态。
- 规范：元素异步自治优先（框架无关），只在需要统一 loading 编排时用 ready 事件。

```javascript
class DsChart extends HTMLElement {
  async connectedCallback() {
    this._renderSkeleton();
    this._data = await load();
    this._renderChart();
    this.dispatchEvent(new CustomEvent('ready', { bubbles: true, composed: true }));
  }
}
r
```
