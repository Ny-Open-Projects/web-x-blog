---
title: [FRP-391] 笔试：手写 Web Component 包装层（内核 → WC 协议）
date: 2026-11-21
categories: [框架原理]
tags: [前端面试, 笔试题, 架构]
type: 笔试题
---

## FRP-391：笔试：手写 WC 包装层

**答**：实现 `defineWC(name, kernelFactory, { props, events, styles })`：① 自定义元素类：observedAttributes 声明响应属性、attributeChangedCallback 同步内核；② 事件协议：内核回调 → CustomEvent（detail 带业务数据，composed: true）；③ shadow DOM：adoptedStyleSheets 注入样式（幂等共享）+ slot 支持；④ 生命周期：connected/disconnected 对应内核 start/stop；⑤ 与 React/Vue 的集成说明（属性传对象用 property 赋值协议）。写出实现。

```javascript
export function defineWC(name, kernelFactory, { props = {}, events = [], styles } = {}) {
  const propNames = Object.keys(props);
  const sheet = (() => { const s = new CSSStyleSheet(); s.replaceSync(styles ?? ''); return s; })();
  customElements.define(name, class extends HTMLElement {
    static get observedAttributes() { return propNames; }
    #kernel = null; #cleanups = [];
    connectedCallback() {
      this.attachShadow({ mode: 'open' });
      this.shadowRoot.adoptedStyleSheets = [sheet];  // 幂等共享(CSSStyleSheet 单例)
      this.shadowRoot.innerHTML = `<div part="root"><slot></slot></div>`;
      // 内核启动: props 从 attribute/property 读取
      this.#kernel = kernelFactory(this.#readProps());
      this.#cleanups.push(
        this.#kernel.sub(() => this.#render()),
        ...events.map((ev) => this.#kernel.on(ev, (detail) =>
          this.dispatchEvent(new CustomEvent(`${name}-${ev}`, { detail, composed: true, bubbles: true })))));
      this.#render();
    }
    disconnectedCallback() { this.#cleanups.forEach((c) => c()); this.#kernel?.stop?.(); this.#cleanups = []; }
    attributeChangedCallback(k, _, nv) { this.#kernel?.setProp?.(k, props[k](nv)); }
    #readProps() { return Object.fromEntries(propNames.map((k) => [k, props[k](this.getAttribute(k))])); }
    #render() { /* 内核快照 → shadow DOM 更新(或暴露给框架层) */ }
  });
}
// React19 集成: <my-widget prop-a="1" on-widget-change={(e) => ...}/> — 原生属性/事件映射
// 对象 props: el.propA = obj (property 赋值, 不走 attribute 序列化)
```

**评分点**：
- adoptedStyleSheets 幂等共享（多实例单一样式表）
- 事件协议（CustomEvent composed + 命名空间）
- 生命周期映射（connected→start, disconnected→stop + cleanups）
- property vs attribute 的对象传递协议
