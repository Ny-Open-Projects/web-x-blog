---
title: [WCN-032] WC 没有内置响应式系统怎么办？为什么业界常把 WC 与 Signals 组合？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Web Components]
type: 面试题
---

## WCN-032：WC 没有内置响应式系统怎么办？为什么业界常把 WC 与 Signals 组合？

**答**：
- 原生 WC 只有生命周期，没有"状态变了自动更新视图"的机制；选项有：手写 render + 手动调用（最简）、Lit 的响应式属性（`static properties` + requestUpdate）、接 Signals 库。
- Signals 优势：细粒度依赖追踪——只有真正读取了某个 signal 的 DOM 绑定才更新，无需 diff；与框架无关（Preact/Solid/Qwik/Vue 共享语义），正好契合 WC 的"去框架化"定位。
- 组合方式：组件内部建 `signal` 状态，`effect` 里做最小化 DOM 更新，connected 订阅、disconnected 释放 effect；跨组件共享时 signal 实例可作为"外部 store"注入。
- 对比 Lit 响应式属性：Lit 是"属性变化 → 全量 rerender 模板 + diff"，Signals 是"依赖变化 → 精确局部更新"，后者在长列表高频更新更省。
- 追问钩子：TC39 Signals 提案若落地，原生 WC + 原生 Signals 将形成无依赖的完整组件模型。

```javascript
// 独立 signals 实现（下一节展开），这里演示组合模式
import { signal, effect } from './mini-signals.js';

class CartBadge extends HTMLElement {
  #count = signal(0);
  #disposer;
  connectedCallback() {
    this.attachShadow({ mode: 'open' }).innerHTML = '<b id="n">0</b> 件';
    // 细粒度：只有文本节点更新，不重渲染整个影子树
    this.#disposer = effect(() => {
      this.shadowRoot.getElementById('n').textContent = String(this.#count());
    });
  }
  disconnectedCallback() { this.#disposer(); }
  add() { this.#count(this.#count() + 1); }
}
customElements.define('cart-badge', CartBadge);
```
