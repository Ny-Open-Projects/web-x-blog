---
title: [WCN-149] WCN 组件的错误边界与监控埋点怎么做？影子树内的异常如何捕获归因？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 选型与工程落地]
type: 面试题
---

## WCN-149：WCN 组件的错误边界与监控埋点怎么做？

**答**：
- 捕获层：window.onerror/unhandledrejection 全局兜底；组件级用"每个生命周期回调包 try/catch"的基类（相当于 WC 的 error boundary），出错时渲染降级 UI 并派发 `wc-error` 事件。
- 归因：异常对象附 `component: tagName + version`（构建时注入 __WC_VERSION__），监控平台按组件维度聚合；影子树内部节点用 `composedPath()` 还原组件归属。
- 埋点模式：组件对外事件即埋点（统一在 adapters 层监听 composed 事件上报），core 不感知监控 SDK——保持去框架化纯净。
- 性能埋点：define 耗时、首次渲染耗时（connected → 首个 effect 完成）打 performance.mark，上报组件级 TTFB/TBT。
- 版本追踪：加载器上报 tag→version 映射，线上问题可直接定位到灰度版本并回滚（WCN-114）。

```javascript
// 错误边界基类
class SafeElement extends HTMLElement {
  #guard(fn) {
    try { fn(); }
    catch (e) {
      e.__wc = { tag: this.tagName.toLowerCase(), version: this.constructor.__WC_VERSION__ };
      reportError(e);                                     // 上报（含组件归因）
      this.dispatchEvent(new CustomEvent('wc-error', { bubbles: true, composed: true, detail: { message: e.message } }));
      this.shadowRoot.innerHTML = '<div class="fallback">组件暂不可用</div>';
    }
  }
  connectedCallback() { this.#guard(() => this.safeConnected?.()); }
  attributeChangedCallback(...a) { this.#guard(() => this.safeAttrChange?.(...a)); }
}
// adapters 层统一监听：
// document.addEventListener('wc-error', (e) => track('wc_error', e.detail))
```
