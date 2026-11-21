---
title: [WCN-222] 跨框架使用自定义元素时的调试手段？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-222：跨框架使用自定义元素时的调试手段？
**答**：
- 元素侧：getEventListeners(el)（控制台）检查监听堆积；`el.constructor.observedAttributes` 快查。
- 框架侧：React DevTools 看不到元素内部——元素自身实现 debug 属性（_debugState() 返回内部状态）。
- 性能侧：Performance 面板过滤 element render 任务；长任务归因到具体元素。
- 规范：元素库提供 devtools 钩子（注册 customElements.get 时的 debug 信息注入），生产构建剔除。

```javascript
class GoodsCard extends HTMLElement {
  _debugState() {          // 控制台：document.querySelector('goods-card')._debugState()
    return { sku: this._sku, count: this._count, loading: this._loading };
  }
}
r
```
