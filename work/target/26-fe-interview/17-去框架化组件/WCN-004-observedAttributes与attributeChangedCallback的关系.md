---
title: [WCN-004] 为什么必须用静态 observedAttributes 声明？attributeChangedCallback 有哪些时序坑？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Web Components]
type: 面试题
---

## WCN-004：为什么必须用静态 observedAttributes 声明？attributeChangedCallback 有哪些时序坑？

**答**：
- 浏览器按静态字段 `static observedAttributes` 建立观察白名单，未声明的 attribute 变化不会回调，这是为了性能避免任意 attribute 都派发回调。
- 坑一：解析 HTML 时，属性在元素"升级"前就已存在，升级瞬间会对每个已存在的 observed attribute 各触发一次 `attributeChangedCallback`，且早于 `connectedCallback`。
- 坑二：`setAttribute(name, '')` 的 newV 是空字符串不是 null；`removeAttribute` 时 newV 为 `null`，旧值可能为 `''`，判断"是否第一次"不能靠 old 为 null。
- 坑三：回调里同步 `setAttribute` 同名属性会递归触发，需用 oldV !== newV 守卫或 microtask 合并。
- 实践：attribute 只承载字符串配置（低频），复杂数据走 property + attribute 反射封装。

```javascript
class ConfigPanel extends HTMLElement {
  static observedAttributes = ['size', 'disabled'];
  attributeChangedCallback(name, oldV, newV) {
    // 坑三守卫：值真正变化才处理
    if (oldV === newV) return;
    // 坑二：'' 与 null 语义区分 —— removeAttribute 得到 null
    this._cfg ??= {};
    this._cfg[name] = newV === null ? undefined : newV;
    if (this.isConnected) this.render();
  }
  connectedCallback() { this.render(); }
  render() { this.shadowRoot.textContent = JSON.stringify(this._cfg ?? {}); }
}
customElements.define('config-panel', ConfigPanel);
```
