---
title: [WCN-724] WC 内部抛异常如何做错误边界，避免拖垮整个宿主页面？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-724：WC 内部抛异常如何做错误边界，避免拖垮整个宿主页面？

**答**：
- 结论：每个 WC 在 connectedCallback/事件处理器外层包 try/catch，捕获后渲染降级 UI（fallback slot 或静态内容），并通过自定义事件上报；异常不应冒泡到 document。
- 关键异步路径（Promise、setTimeout、effect）也要 catch；用全局 `window.onerror`/`unhandledrejection` 作为最后兜底。
- 追问钩子：Shadow DOM 内的错误能被宿主的 window.onerror 捕获吗？考察 composed 错误事件与错误传播边界。

```javascript
const withBoundary = (fn, fallback) => (...args) => {
  try { return fn(...args); }
  catch (err) {
    console.error('[wc boundary]', err);
    fallback(err);
  }
};
class DsWidget extends HTMLElement {
  connectedCallback() {
    withBoundary(() => this.render(), (err) => {
      this.innerHTML = `<div role="alert">组件加载失败，请重试</div>`;
      this.dispatchEvent(new CustomEvent('wc-error', { detail: String(err), bubbles: true, composed: true }));
    })();
  }
  render() { throw new Error('模拟渲染异常'); }
}
customElements.define('ds-widget', DsWidget);
```
