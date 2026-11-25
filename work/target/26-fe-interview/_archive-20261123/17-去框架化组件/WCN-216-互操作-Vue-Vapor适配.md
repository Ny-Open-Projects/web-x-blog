---
title: [WCN-216] Vue Vapor（无虚拟 DOM）模式下的自定义元素适配有什么变化？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-216：Vue Vapor（无虚拟 DOM）模式下的自定义元素适配有什么变化？
**答**：
- Vapor 编译为直接 DOM 操作——对自定义元素的 property 写入更直接（无 diff 开销）。
- defineCustomElement 在 Vapor 模式下仍在演进：关注响应式连接（effect 与元素生命周期绑定）。
- 事件绑定从 vnode props 变为直接 addEventListener——卸载清理由编译产物保证。
- 混合模式（同页 Vapor 组件 + 普通 WC）注意样式注入时序。

```javascript
// Vapor 适配要点：effect 生命周期
import { effect } from 'vue';
class Price extends HTMLElement {
  #stop?: () => void;
  connectedCallback() {
    this.#stop = effect(() => { this.textContent = String(this.#store.price); });
  }
  disconnectedCallback() { this.#stop?.(); }   // 与 Vapor 的 effectScope 对齐
}
r
```
