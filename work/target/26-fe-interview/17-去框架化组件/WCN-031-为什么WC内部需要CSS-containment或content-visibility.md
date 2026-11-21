---
title: [WCN-031] WC 列表渲染慢时如何用 CSS containment / content-visibility 优化？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Web Components]
type: 面试题
---

## WCN-031：WC 列表渲染慢时如何用 CSS containment / content-visibility 优化？

**答**：
- `contain: content`（或 layout/style/paint 细分）：告诉浏览器元素内部变化不影响外部布局，缩小重排范围；列表行组件在 `:host { contain: content }` 上声明。
- `content-visibility: auto` + `contain-intrinsic-size`：视口外的行跳过渲染/布局/绘制，长列表首屏成本接近虚拟滚动且零 JS；进入视口才真正渲染。
- 两者关系：content-visibility 自带 contain 效果（跳过时）；纯 contain 不跳过渲染只限制影响域。
- 注意坑：content-visibility 依赖 intrinsic-size 占位，尺寸不稳会导致滚动条跳动；需要精确测量或给稳定预估高度。
- 与虚拟滚动取舍：数据量千级、行结构简单 → content-visibility 优先（无 JS 维护成本）；行内含重交互/无限增长 → 虚拟滚动（DOM 数量本身是瓶颈时它不可替代）。

```css
/* 影子树内 */
:host {
  contain: content;              /* 行级布局影响域收敛 */
  content-visibility: auto;      /* 视口外跳过渲染 */
  contain-intrinsic-size: auto 72px; /* 屏外占位高度，进入后用真实尺寸 */
}
```

```javascript
class FeedRow extends HTMLElement {
  connectedCallback() {
    this.attachShadow({ mode: 'open' }).innerHTML = `
      <style>:host{contain:content;content-visibility:auto;contain-intrinsic-size:auto 72px}
      .row{display:flex;height:72px;align-items:center}</style>
      <div class="row"><slot name="avatar"></slot><b><slot name="title"></slot></b></div>`;
  }
}
customElements.define('feed-row', FeedRow);
// 外层容器再配 contain-intrinsic-root / overflow auto，万级列表滚动即可用性达标
```
