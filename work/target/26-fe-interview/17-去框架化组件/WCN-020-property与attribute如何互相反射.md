---
title: [WCN-020] WC 组件的 property 与 attribute 如何互相反射？为什么复杂对象只能走 property？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Web Components]
type: 面试题
---

## WCN-020：WC 组件的 property 与 attribute 如何互相反射？为什么复杂对象只能走 property？

**答**：
- attribute 只能是字符串、走 HTML 声明式书写（SSR 友好）；property 可承载任意值、走 JS API。两者是同一配置的两个视图，框架绑定（Vue 的 `:prop`、React 的 props）实际都在 set property 或 attribute。
- 反射约定：getter/setter 内部互转——`set` property 时若为原始值则 `setAttribute`，`attributeChangedCallback` 里再解析回 property；对象/数组/函数只存 property 并跳过 attribute。
- `reflect: true` 式行为需要手写（Lit 提供 `@property({ reflect: true })`），原生自定义元素没有自动反射。
- 坑：property 初始值要在 constructor 定义，否则升级前的 "early set" 值不会被搬运到升级后的实例。
- 性能：高频更新（拖拽坐标）走 property 避免字符串序列化与 attributeChanged 开销；低频配置（disabled、size）走 attribute 便于 SSR 与 no-JS 展示。

```javascript
class Gauge extends HTMLElement {
  static observedAttributes = ['max', 'label'];
  #value = 0; // 私有字段承载 property 真值
  get value() { return this.#value; }
  set value(v) {
    this.#value = Number(v) || 0;
    // 原始值反射到 attribute，SSR/no-JS 可见；复杂值不反射
    if (typeof v === 'number') this.setAttribute('value', String(v));
    this.render();
  }
  attributeChangedCallback(name, o, n) {
    if (n === o) return;
    if (name === 'value') this.#value = Number(n) || 0; // attribute → property
    this.render();
  }
  options = { unit: 'ms' }; // 复杂对象：仅 property，外部 this.options = {...} 赋值
  render() { /* 使用 this.#value 与 this.getAttribute('max') 渲染 */ }
}
customElements.define('x-gauge', Gauge);
```
