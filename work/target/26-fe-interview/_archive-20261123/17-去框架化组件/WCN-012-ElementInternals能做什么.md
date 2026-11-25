---
title: [WCN-012] ElementInternals 提供了哪些能力？如何用它实现自定义状态伪类与 ARIA 默认值？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Web Components]
type: 面试题
---

## WCN-012：ElementInternals 提供了哪些能力？如何用它实现自定义状态伪类与 ARIA 默认值？

**答**：
- 表单能力：`setFormValue` / `setValidity` / `checkValidity` / `reportValidity`，以及 `form`、`labels`、`willValidate` 等只读属性。
- 状态伪类：`internals.states.add('checked')` 对应 CSS `:--checked`（注意是双冒号风格 `:--name`），可在影子树里写 `button:--checked`，比 data 属性更语义化。
- ARIA 默认值：`internals.role = 'slider'` 与 `aria*` 反射属性可设默认语义，用户在宿主元素上显式写的 `role`/`aria-*` 会覆盖默认值。
- 布局能力：`shadowRoot` 访问、`target`（delegateFocus 相关）以及 `getTargetComputedStyle`（部分实现）等辅助 API。
- 限制：`attachInternals()` 每个元素只能调一次，重复调用抛错；调用后不能再 `attachShadow`（反之亦然——已 attachShadow 的元素不能再 attachInternals？实际可以，但不能两次 attachInternals）。

```css
/* 影子树内：配合 internals.states */
button:--active { outline: 2px solid #2563eb; }
```

```javascript
class ToggleChip extends HTMLElement {
  static formAssociated = true;
  #i = this.attachInternals();
  #on = false;
  connectedCallback() {
    this.attachShadow({ mode: 'open' }).innerHTML = `<button part="chip">chip</button>`;
    const btn = this.shadowRoot.querySelector('button');
    btn.addEventListener('click', () => {
      this.#on = !this.#on;
      this.#i.states.toggle('active', this.#on);   // 自定义状态伪类
      this.#i.role = 'switch';                     // 默认 ARIA，可被外部 role 覆盖
      this.#i.ariaChecked = String(this.#on);
      this.#i.setFormValue(this.#on ? 'on' : null);
    });
  }
}
customElements.define('toggle-chip', ToggleChip);
```
