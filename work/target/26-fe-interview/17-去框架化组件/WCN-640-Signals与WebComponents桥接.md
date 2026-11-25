---
title: [WCN-640] Signals 与 Web Components 桥接有哪几种模式？各有什么代价？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-640：Signals 与 Web Components 桥接有哪几种模式？各有什么代价？

**答**：
- 结论：三种模式——① Signal→Property 直写（最简）② 元素内建 signal 并在 connectedCallback 绑定 effect（内聚）③ 通过上下文对象跨组件共享（适合树形组件）。
- 代价：模式①需框架侧同步；模式②要求每个元素自己管理 dispose；模式③增加间接层但可观测性好。
- 追问钩子：哪种最适合设计系统？通常②+③组合：元素内建 signal 保证自治，context 解决跨组件（如 Tabs 与 Tab）联动。

```javascript
// 模式②：元素内建 signal + 自动绑定/清理
function bindSignal(el, sig, apply) {
  let dispose;
  const run = () => { apply(sig.get()); };
  const obs = new MutationObserver(() => {
    if (!el.isConnected) { dispose?.(); obs.disconnect(); }
  });
  obs.observe(el.parentNode || document.body, { childList: true });
  dispose = effect(run);
  return () => { dispose(); obs.disconnect(); };
}
class DsCounter extends HTMLElement {
  connectedCallback() {
    this.count = signal(0);
    this.attachShadow({ mode: 'open' });
    this.shadowRoot.innerHTML = '<span></span>';
    this._stop = bindSignal(this, this.count,
      v => this.shadowRoot.querySelector('span').textContent = v);
  }
  disconnectedCallback() { this._stop?.(); }
}
```
