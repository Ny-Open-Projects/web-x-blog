---
title: [H5-172] Shadow DOM 内的表单控件如何参与校验与提交？ElementInternals？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-172：Shadow DOM 内的表单控件如何参与校验与提交？ElementInternals？
**答**：
- 问题：Shadow DOM 里包一个真 input，`FormData` 拿不到值、原生校验也不认识这个自定义元素。
- 解法：元素声明 `static formAssociated = true`，构造器里 `attachInternals()` 拿到与表单的内部通道。
- 四个能力：`setFormValue()` 参与提交与 FormData；`setValidity(validity, message, anchor)` 把内部 input 的校验状态上抛（anchor 指向真实输入框，原生气泡定位正确）；`formResetCallback` 联动重置；`formDisabledCallback` 联动禁用。
- 效果：`<x-input required>` 像原生控件一样被 `checkValidity/reportValidity/:invalid/:user-invalid` 识别，无障碍语义完整。

```html
<form id="f">
  <x-input name="email" required></x-input>
  <button>提交</button>
</form>
<script>
// ElementInternals：自定义控件接入原生表单体系
class XInput extends HTMLElement {
  static formAssociated = true;          // 1) 声明为 form-associated
  #internals;
  #input;
  constructor() {
    super();
    this.#internals = this.attachInternals();   // 2) 拿到与表单的内部通道
    this.attachShadow({ mode: 'open' }).innerHTML = `
      <style>
        input { border: 1px solid #ccc; padding: 6px; border-radius: 4px; }
        :host(:invalid) input { border-color: #ef4444; }
      </style>
      <input type="email" placeholder="邮箱"/>`;
    this.#input = this.shadowRoot.querySelector('input');
    this.#input.addEventListener('input', () => this.#sync());
  }
  #sync() {
    // 3) 参与提交：值写入表单，FormData 能取到
    this.#internals.setFormValue(this.#input.value);
    // 4) 参与校验：把内部 input 的校验状态"上抛"给宿主元素
    //    anchor 指向真实输入框，浏览器错误气泡会正确定位
    const v = this.#input.validity;
    this.#internals.setValidity(
      v, v.valid ? '' : this.#input.validationMessage, this.#input);
  }
  // 表单重置联动
  formResetCallback() { this.#input.value = ''; this.#sync(); }
  // 禁用联动：宿主所在的表单禁用时同步到内部 input
  formDisabledCallback(disabled) { this.#input.disabled = disabled; }
}
customElements.define('x-input', XInput);

// 现在它就是"原生控件"：FormData / checkValidity / :invalid / reportValidity 全部工作
document.getElementById('f').onsubmit = (e) => {
  e.preventDefault();
  console.log(new FormData(e.target).get('email'));   // x-input 的值
  if (!e.target.checkValidity()) e.target.reportValidity();
};
</script>
```
