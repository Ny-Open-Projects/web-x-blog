---
title: [H5-105] Web Components 在 Vue/React 中如何互操作？有哪些已知坑？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-105：Web Components 在 Vue/React 中如何互操作？有哪些已知坑？
**答**：
- 通用前提：自定义元素在框架看来是"普通 DOM 标签"，**属性传字符串、事件靠 addEventListener**，与框架数据流存在阻抗失配。
- Vue 3 原生支持最好：`compilerOptions.isCustomElement` 声明后可直接模板使用，props/attrs 自动透传，`@event` 监听自定义事件正常工作。
- React 19 起原生支持自定义元素（属性可传对象/函数、事件监听）；React 18 及以前需手写 ref + addEventListener 的 wrapper 组件。
- 高频坑一：复杂数据只能走 **property** 而非 attribute，框架如果默认设 attribute 会导致 `[object Object]`——组件内应同时实现 attribute 反序列化或框架侧强制 property。
- 高频坑二：shadow 内样式与框架 CSS 隔离，框架的全局 reset 不会进入组件，必要时用 adoptedStyleSheets 注入主题变量。

```javascript
// ===== React 18：手写 wrapper（React 19 可省略此包装）=====
import { useEffect, useRef } from 'react';

function ReactWrapper({ value, onChange, children }) {
  const ref = useRef(null);
  useEffect(() => {
    const el = ref.current;
    const handler = (e) => onChange?.(e.detail);
    el.addEventListener('value-change', handler);      // 自定义事件监听
    return () => el.removeEventListener('value-change', handler);
  }, [onChange]);
  useEffect(() => {
    ref.current.value = value;                          // 复杂数据走 property
  }, [value]);
  return <my-color-picker ref={ref}>{children}</my-color-picker>;
}

// ===== Vue 3：声明后直接用 =====
// main.js
// const app = createApp(App);
// app.config.compilerOptions.isCustomElement = (tag) => tag.startsWith('my-');

// 组件模板中：
// <my-color-picker :value="color" @value-change="color = $event.detail" />

// ===== 组件侧配合：attribute 序列化 + property 双通道 =====
customElements.define('my-color-picker', class extends HTMLElement {
  set value(v) { this._v = v; this.#render(v); }
  get value() { return this._v; }
  // attribute 只承载可序列化形态（React18/Vue 传字符串时的兜底）
  static get observedAttributes() { return ['value']; }
  attributeChangedCallback(_, old, val) {
    if (old !== val && typeof val === 'string') this.value = val;
  }
  #render(v) {
    this.dispatchEvent(new CustomEvent('value-change', {
      detail: v, bubbles: true, composed: true,
    }));
  }
});
```

## 十九、可访问性与国际化深入
