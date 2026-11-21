---
title: [HW-165] 手写 ElementInternals 自定义表单控件——WC 参与 form 校验（formAssociated + setValidity）
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

**答**：自定义表单控件（WC）原生参与 form：static formAssociated = true + attachInternals——setValidity({valid: false}, '消息', anchor) 让控件接进原生校验体系（form.reportValidity/`:invalid` 伪类/checkValidity 全部生效），form.reset 与 FormData 收集自动工作。

```javascript
class EmailInput extends HTMLElement {
  static formAssociated = true;
  #internals; #input;
  constructor() {
    super();
    this.#internals = this.attachInternals();
    this.#internals.setFormValue('');
    const shadow = this.attachShadow({ mode: 'open' });
    shadow.innerHTML = `<input part="input" type="email" aria-label="邮箱">`;
    this.#input = shadow.querySelector('input');
    this.#input.addEventListener('input', () => {
      this.#internals.setFormValue(this.#input.value);
      const valid = /^\S+@\S+$/.test(this.#input.value);
      this.#internals.setValidity(
        valid ? {} : { patternMismatch: true },
        valid ? '' : '请输入合法邮箱',
        this.#input,                                        // anchor：错误提示锚点
      );
      this.dispatchEvent(new CustomEvent('x-valid', { detail: valid, bubbles: true }));
    });
  }
  // form 关联自动获得：
  // form.checkValidity() / reportValidity() 包含本控件
  // :invalid 伪类作用于 <x-email-input>
  // FormData 自动收集（name 属性 + setFormValue）
  static get observedAttributes() { return ['value']; }
  attributeChangedCallback(_, old, v) { if (this.#input && v !== null) this.#input.value = v; }
}
customElements.define('x-email-input', EmailInput);
// <form><x-email-input name="email"></x-email-input><button type="submit">提交</button></form>
// form.onsubmit = (e) => { e.preventDefault(); console.log(new FormData(form).get('email')); }
// 对比手动方案（隐藏 input + 手动校验）：ElementInternals 接进原生体系——表单级 UI/键盘/读屏全部免费获得
```

**评分点**：
- formAssociated + attachInternals + setValidity 的参与原生校验机制——本题核心。
- anchor 元素（错误提示定位）；patternMismatch 等 validity flags 正确使用。
- FormData 收集与 form.reset 自动工作。
- 与"隐藏 input"手动方案的对比（原生校验 UI/键盘/a11y 免费获得）。
