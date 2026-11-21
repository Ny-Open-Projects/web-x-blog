---
title: [WCN-049] 笔试：手写一个 hash 驱动的迷你 WC 路由（动态 import + 生命周期清理）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, Web Components]
type: 笔试题
---

## WCN-049：笔试：手写一个 hash 驱动的迷你 WC 路由

**题目**：实现 `<wc-router>`：① 影子树内有 `<main>` 出口；② `routes` property（`{ '/a': () => import('./a.js'), ... }`）；③ 监听 hashchange，`#/a` 时把 `a-page`（由 loader 返回的类）渲染进出口；④ 切换路由时销毁旧页面（调用其 `dispose?.()` 并清空出口）；⑤ 未匹配路由渲染 404；⑥ 首次渲染不依赖 hashchange 事件。

**答**：

```javascript
class WcRouter extends HTMLElement {
  routes = {};
  #current;
  connectedCallback() {
    if (!this.shadowRoot) {
      this.attachShadow({ mode: 'open' }).innerHTML = '<main part="out"></main>';
    }
    this.#out = this.shadowRoot.querySelector('main');
    window.addEventListener('hashchange', this.#onChange = () => this.#render());
    this.#render(); // 首次：不依赖事件
  }
  disconnectedCallback() { window.removeEventListener('hashchange', this.#onChange); }
  #out; #onChange;
  async #render() {
    const path = location.hash.replace(/^#/, '') || '/';
    const loader = this.routes[path];
    this.#destroy();
    if (!loader) { this.#out.textContent = '404'; return; }
    const mod = await loader();
    const Ctor = mod.default ?? Object.values(mod).find((v) => v.prototype instanceof HTMLElement);
    if (!Ctor) { this.#out.textContent = '404'; return; }   // 异步期间路由又变了要防竞态
    const now = location.hash.replace(/^#/, '') || '/';
    if (now !== path) return;   // 异步期间路由又变了：放弃本次结果（防竞态）
    const page = new Ctor();
    this.#current = page;
    this.#out.append(page);
    this.dispatchEvent(new CustomEvent('route-change', { bubbles: true, composed: true, detail: { path } }));
  }
  #destroy() {
    this.#current?.dispose?.();   // 页面可自定义清理
    this.#current?.remove();
    this.#current = null;
    this.#out.replaceChildren();  // 兜底清空
  }
}
customElements.define('wc-router', WcRouter);
```

**评分点**：
- 首次渲染主动调用 #render，hashchange 只负责后续（启动时序）。
- disconnected 移除 hashchange 监听（泄漏意识）。
- 异步 loader 期间路由切换的竞态防护（判断当前 hash 是否仍是目标）。
- 旧页面 dispose 钩子 + replaceChildren 双保险清理。
- 404 分支覆盖。
