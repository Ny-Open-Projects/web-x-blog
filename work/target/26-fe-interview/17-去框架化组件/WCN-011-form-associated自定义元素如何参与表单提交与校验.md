---
title: [WCN-011] form-associated 自定义元素如何参与表单提交与校验？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Web Components]
type: 面试题
---

## WCN-011：form-associated 自定义元素如何参与表单提交与校验？

**答**：
- 静态 `formAssociated = true` 使自定义元素注册进表单，成为"表单控件"：可被 FormData 收集、可用 `form.elements` 访问、支持 label 关联。
- 通过 `attachInternals()` 拿到 `ElementInternals`，用 `setFormValue(value, state)` 上报值——value 可传 FormData 以提交多个字段，state 用于重载恢复。
- 校验：`internals.setValidity({ valueMissing: true }, '请选择', anchor)` 声明校验状态；`:invalid`、`form.checkValidity()` 按原生控件一样工作。
- 生命周期钩子：`formAssociatedCallback(form)`、`formDisabledCallback`、`formResetCallback`、`formStateRestoreCallback` 处理表单事件。
- 交互属性：`static observedAttributes` 配合 `internals.states` 可加自定义状态伪类（如 `:--loading`）。

```javascript
class StarRating extends HTMLElement {
  static formAssociated = true;
  static observedAttributes = ['disabled'];
  #internals = this.attachInternals();
  #value = 0;
  connectedCallback() {
    this.attachShadow({ mode: 'open' }).innerHTML =
      Array.from({ length: 5 }, (_, i) => `<button data-v="${i + 1}" type="button">★</button>`).join('');
    this.shadowRoot.addEventListener('click', (e) => {
      if (e.target.matches('button')) this.#set(e.target.dataset.v | 0);
    });
    this.#internals.role = 'radiogroup';
  }
  attributeChangedCallback(_, o, n) { if (n !== o) this.#internals.setValidity({}); }
  formResetCallback() { this.#set(0); }
  formStateRestoreCallback(state) { this.#set(Number(state) | 0); }
  #set(v) {
    this.#value = v;
    this.#internals.setFormValue(String(v || ''));            // 空则不提交
    const ok = v > 0;
    this.#internals.setValidity(ok ? {} : { valueMissing: true }, ok ? '' : '请打分');
    [...this.shadowRoot.querySelectorAll('button')].forEach((b, i) => b.classList.toggle('on', i < v));
  }
}
customElements.define('star-rating', StarRating);
```
