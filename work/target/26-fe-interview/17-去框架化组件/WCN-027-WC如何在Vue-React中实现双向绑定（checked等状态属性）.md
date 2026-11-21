---
title: [WCN-027] WC 组件在框架里如何实现 v-model/受控双向绑定？value 与 change 事件要怎么约定？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Web Components]
type: 面试题
---

## WCN-027：WC 组件在框架里如何实现 v-model/受控双向绑定？value 与 change 事件要怎么约定？

**答**：
- 核心约定：提供 `value` property getter/setter + 对外派发 `input`/`change` 事件（detail 带 value），原生输入控件语义在框架包装层可直接映射。
- Vue3：`defineCustomElement` 产物可用 `v-model:value`；组件需要 `props: ['value']` + `emit('update:value')`，WC 场景对应 property + CustomEvent。
- React 19：对 custom element 的 props 直传 property（对象/函数不再丢），受控用法是 `<my-input value={v} onChange={(e)=>setV(e.detail.value)}>`，关键在事件命名映射 React 的 onChange。
- 受控回写防抖动：setter 内如果值与内部当前值相等应直接 return，避免"事件→框架 setState→回写 property→再次触发渲染"循环。
- 对象型复杂状态（如 options 数组）：只走 property；受控传引用时组件内部不得直接修改传入对象（单向数据流）。

```javascript
class MyInput extends HTMLElement {
  #value = '';
  static observedAttributes = ['placeholder'];
  connectedCallback() {
    const root = this.attachShadow({ mode: 'open' });
    root.innerHTML = '<input part="input">';
    const input = root.querySelector('input');
    input.addEventListener('input', () => {
      this.value = input.value; // setter 会回写 & 通知
      this.dispatchEvent(new CustomEvent('input', {
        bubbles: true, composed: true, detail: { value: this.#value },
      }));
    });
  }
  get value() { return this.#value; }
  set value(v) {
    v = String(v ?? '');
    if (v === this.#value) return;      // 防循环回写
    this.#value = v;
    this.shadowRoot.querySelector('input').value = v;
  }
}
customElements.define('my-input', MyInput);
// React 受控：<my-input value={val} onChange={(e) => setVal(e.detail.value)} />
```
