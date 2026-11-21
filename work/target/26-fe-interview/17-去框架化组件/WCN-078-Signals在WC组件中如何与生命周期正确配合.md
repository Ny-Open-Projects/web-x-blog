---
title: [WCN-078] Signals 在 WC 组件中如何与生命周期正确配合？effect 何时创建、何时释放？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Signals]
type: 面试题
---

## WCN-078：Signals 在 WC 组件中如何与生命周期正确配合？effect 何时创建、何时释放？

**答**：
- 创建时机：优先在 `connectedCallback`（DOM 就绪、绑定目标存在）；在 constructor 里创建 effect 若引用影子树节点会拿到 null。
- 释放时机：`disconnectedCallback` 调用 effect 的 dispose——否则元素移除后 effect 仍在响应全局 signal 变化，泄漏并浪费更新。
- 配对原则：connected/disconnected 可能多次触发（元素被移动），effect 创建也要防重（已存在直接复用）。
- 作用域选择：组件私有状态用组件内 signal；跨组件共享用模块级 store，但订阅仍随组件生命周期。
- 批处理与渲染时机：effect 默认微任务批处理，正好在浏览器绘制前完成 DOM 更新，与 `requestAnimationFrame` 对齐良好；强制同步读布局的场景才需要 rAF 包装。

```javascript
import { signal, effect } from './mini-signals.js';

const theme = signal('light');   // 模块级共享

class ThemeableCard extends HTMLElement {
  #dispose;
  connectedCallback() {
    if (!this.shadowRoot) {
      this.attachShadow({ mode: 'open' }).innerHTML = '<style>:host{display:block}</style><div part="body"><slot></slot></div>';
    }
    this.#dispose ??= effect(() => {           // 防重创建
      this.shadowRoot.part.getAttribute?.('x');
      this.setAttribute('data-theme', theme.value); // 细粒度：只改一个属性
    });
  }
  disconnectedCallback() {
    this.#dispose?.();
    this.#dispose = undefined;
  }
}
customElements.define('themeable-card', ThemeableCard);
```
