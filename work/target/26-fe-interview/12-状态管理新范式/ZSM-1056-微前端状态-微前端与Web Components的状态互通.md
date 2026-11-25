---
title: [1056] Web Components 子应用的状态互通（属性/事件/上下文）
date: 2026-11-17
categories: [状态管理新范式]
tags: [前端面试, 面试题, 微前端]
type: 面试题
---

## 1056：Web Components 子应用的状态互通（属性/事件/上下文）

**答**：
- 互通三通道：attributes/properties（初始化数据——字符串/对象属性）、Custom Events（对外发布变更——emit 带 payload，冒泡被宿主捕获）、Context API（provide/inject 式——宿主 provide 上下文 wc 内 consume）。
- 状态边界：WC 内部状态私有（shadow DOM 内 store），对外只暴露「属性入 + 事件出」——WC 是天然的状态封装边界（比框架组件更严格）。
- 框架无关的代价：WC 内部用什么状态管理（Lit 的 reactive properties/轻量 store）与宿主无关——宿主只按协议交互；跨框架复用（React/Vue 宿主都可用）。
- 追问钩子：为什么 WC 的「属性入+事件出」协议比共享 store 更适合跨框架？——属性与事件是平台标准（所有框架都支持——协议不受框架版本/生态约束）；共享 store 要求宿主与 WC 用同一状态库实例（跨框架几乎不可能保证单例）。

```js
class AddressBlock extends HTMLElement {
  static properties = { value: { type: Object } };      // 属性入
  setFields(f) { this._store.set(f); }                  // 方法接口
  validate() { return this._store.validate(); }
  _onChange(f) {
    this.dispatchEvent(new CustomEvent('address-change',
      { detail: f, bubbles: true }));                   // 事件出
  }
}
customElements.define('address-block', AddressBlock);
```
