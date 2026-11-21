---
title: [WCN-045] WC 里如何管理全局状态？跨组件通信方案（事件/store/context）怎么选？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Web Components]
type: 面试题
---

## WCN-045：WC 里如何管理全局状态？跨组件通信方案（事件/store/context）怎么选？

**答**：
- 方案一 DOM 事件：适合"子 → 父"通知（composed CustomEvent），缺点是"父 → 子"难做（要靠 attribute/property）。
- 方案二模块级 store（signals/observable）：全局共享读写，天然框架无关；组件 connected 订阅、disconnected 退订；跨页面（SPA）也一致。
- 方案三 context（沿树注入）：适合环境依赖（主题/i18n），适合多实例多主题共存场景。
- 组合惯例：服务器数据走 store（单一事实源），交互通知走事件（松耦合），环境注入走 context；禁止用事件传大数据流（事件无背压）。
- 坑：同一页面多版本组件库实例化两个 store —— store 要以"应用单例"方式打包（externalize 或挂 Symbol registry）避免双份。

```javascript
// store.js：模块级 signal store（去框架化）
import { signal, effect } from './mini-signals.js';
export const cart = signal([]);

export const cartApi = {
  add(item) { cart([...cart(), item]); },
  remove(id) { cart(cart().filter((i) => i.id !== id)); },
};

// 组件内订阅（生命周期配对）
class CartList extends HTMLElement {
  #disposer;
  connectedCallback() {
    this.attachShadow({ mode: 'open' }).innerHTML = '<ul id="l"></ul>';
    this.#disposer = effect(() => {
      this.shadowRoot.getElementById('l').innerHTML =
        cart().map((i) => `<li>${i.name}</li>`).join('');
    });
  }
  disconnectedCallback() { this.#disposer?.(); }
}
customElements.define('cart-list', CartList);
```
