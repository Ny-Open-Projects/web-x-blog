---
title: [WCN-232] 框架（React 19/Vue）如何水合带 DSD 的自定义元素而不重复渲染？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-232：框架（React 19/Vue）如何水合带 DSD 的自定义元素而不重复渲染？
**答**：
- DSD 内容已在 DOM 中——元素注册时检测「已有 DSD 模板」则跳过首渲染（hydrate 模式）。
- lit 的 ssr 层原生处理；自研元素需实现「hydrateFromDSD()」：采用现 DOM、只绑事件。
- 关键：事件绑定不重建 DOM（避免闪烁与焦点丢失）。
- 验证：首屏到可交互期间无 DOM 替换（MutationObserver 断言）。

```javascript
connectedCallback() {
  const tpl = this.querySelector('template[shadowrootmode]');
  if (tpl && !this.shadowRoot) {
    // 浏览器已解析 DSD 时 shadowRoot 已存在；polyfill 场景手动采用
    this.attachShadow({ mode: 'open' }).appendChild(tpl.content.cloneNode(true));
  }
  this._bindEvents();   // 只绑事件，不重建 DOM
}
r
```
