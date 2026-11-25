---
title: [WCN-915] slot 与 children 语义差异：React children 与 WC 具名 slot 怎么互转
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-915：slot 与 children 语义差异：React children 与 WC 具名 slot 怎么互转

**答**：
- 结论先行：WC 用 `<slot>` 做内容投影（含具名 slot），React 用 `children` prop；跨框架桥接时要把「children/具名插槽」映射到对应 slot 属性。
- 默认 slot：React 的 children 直接放进 WC 的 light DOM，WC 内 `<slot>` 接管渲染；注意 light DOM 节点不会被 React 管理样式，token/CSS 变量要能穿透。
- 具名 slot：React 用 `slot="header"` 属性标记子节点，或封装 `<Slot name="header">` 组件；Vue 用 `v-slot` 需转成带 slot 属性的 DOM 节点。
- 响应式 children：React re-render 会重建 children，导致 WC 内 slot 内容闪烁；稳定 key + memo 减少重挂载，或用 signal 驱动内容而非频繁换 DOM。
- 追问钩子：面试官问「slotchange 事件怎么用」——答：监听 `slotchange` 感知投影内容变化，做懒初始化或尺寸测量，但不要在里面反复派发导致循环。

```javascript
// React 侧把具名 children 映射到 WC 的 slot 属性
function DsCard({ header, children, footer }) {
  return <ds-card>
    <div slot="header">{header}</div>
    <div slot="default">{children}</div>
    <div slot="footer">{footer}</div>
  </ds-card>;
}
// WC 内部：
class DsCard extends HTMLElement {
  connectedCallback() {
    const root = this.attachShadow({ mode: 'open' });
    root.innerHTML = `
      <header><slot name="header"></slot></header>
      <main><slot></slot></main>
      <footer><slot name="footer"></slot></footer>`;
    root.querySelector('slot').addEventListener('slotchange', e =>
      console.log('slot 内容变化', e.target.name));
  }
}
customElements.define('ds-card', DsCard);
```
