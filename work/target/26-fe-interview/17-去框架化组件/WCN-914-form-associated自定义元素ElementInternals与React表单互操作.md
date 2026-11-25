---
title: [WCN-914] form-associated 自定义元素（ElementInternals）与 React 表单库怎么互操作
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-914：form-associated 自定义元素（ElementInternals）与 React 表单库怎么互操作

**答**：
- 结论先行：普通 WC 对表单是「黑盒」，form-associated custom elements 用 ElementInternals + `static formAssociated = true` 让它像原生 input 一样参与表单校验与提交。
- 关键 API：`attachInternals()` 拿到 internals，用 `setFormValue(value)` 写入提交值、`setValidity()` 报告校验状态、`willValidate` 参与原生校验；并在 form 事件里同步。
- React 互操作坑：React 的受控表单依赖 value/onChange，而 WC 的值在 internals 里；需用 ref 读 `el.internals` 或监听 `formdata`/自定义事件桥接，不能只靠 props。
- 校验联动：WC 的 `checkValidity()` 要和 React Hook Form / Formik 的校验器对齐，避免「WC 内部通过但表单库认为无效」的双重标准（结算表单常见）。
- 追问钩子：面试官问「浏览器兼容性怎么办」——答：ElementInternals 在老浏览器需 polyfill，且 polyfill 无法完美模拟原生表单参与，要提供降级（隐藏原生 input 兜底）。

```javascript
// form-associated 自定义元素
class DsAmount extends HTMLElement {
  static formAssociated = true;
  constructor() {
    super();
    this._internals = this.attachInternals();
    this._internals.setFormValue('0');
  }
  set value(v) {
    this._v = v;
    this._internals.setFormValue(v);
    const ok = Number(v) >= 0;
    this._internals.setValidity(ok ? {} : { rangeUnderflow: true }, '不能为负', this);
  }
  get value() { return this._v || '0'; }
}
customElements.define('ds-amount', DsAmount);
const form = document.createElement('form');
form.innerHTML = '<ds-amount name="amount"></ds-amount>';
const el = form.querySelector('ds-amount');
el.value = '99';
console.log(new FormData(form).get('amount')); // 99（原生表单可见）
```
