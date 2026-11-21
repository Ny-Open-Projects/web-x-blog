---
title: [H5-103] form-associated custom elements 怎么让自定义控件接入原生表单？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-103：form-associated custom elements 怎么让自定义控件接入原生表单？
**答**：
- 三件套：静态 `formAssociated = true` → `attachInternals(this)` 拿 `ElementInternals` → 用 `setValidity/setFormValue` 把自定义控件"变成"真正的表单字段。
- 接入后组件获得原生待遇：参与表单提交序列化、`form.reset()`、`:invalid` 匹配、form 属性跨表单关联、label 点击聚焦。
- `internals.setFormValue(value, state?)`：value 进提交数据，state 存还原状态（如多字段组合控件）；值为 null 则该字段不提交。
- 校验：`internals.setValidity({ valueMissing: true }, '请选择日期')` 标错；`checkValidity/reportValidity` 走原生链路。
- 生命周期扩展：`formAssociatedCallback/formDisabledCallback/formResetCallback` 响应表单级变化。

```html
<form id="f">
  <label for="rating">评分</label>
  <!-- 自定义控件：看起来是星星，提交时是真正的 rating 字段 -->
  <star-rating id="rating" name="rating" required></star-rating>
  <button>提交</button>
</form>

<script>
  customElements.define('star-rating', class extends HTMLElement {
    static formAssociated = true;            // 1) 声明关联

    constructor() {
      super();
      this.internals = this.attachInternals();  // 2) ElementInternals
      this.attachShadow({ mode: 'open' }).innerHTML = `
        <span role="radiogroup" aria-label="评分">
          ${[1,2,3,4,5].map(n =>
            `<button type="button" data-v="${n}" aria-label="${n} 星">★</button>`).join('')}
        </span>`;
      this.shadowRoot.addEventListener('click', (e) => {
        const v = e.target.dataset?.v;
        if (v) this.value = v;
      });
      this._value = '';
    }

    get value() { return this._value; }
    set value(v) {
      this._value = v;
      // 3) 值进表单序列化
      this.internals.setFormValue(v);
      // 4) 校验接入原生体系
      this.internals.setValidity(
        this.required && !v ? { valueMissing: true } : {},
        this.required && !v ? '请选择评分' : ''
      );
      this.#paint(v);
    }

    get required() { return this.hasAttribute('required'); }
    #paint(v) {
      [...this.shadowRoot.querySelectorAll('button')].forEach(b =>
        b.style.opacity = b.dataset.v <= v ? 1 : 0.25);
    }

    // 表单级生命周期
    formResetCallback() { this.value = ''; }
    formDisabledCallback(disabled) {
      this.shadowRoot.style.pointerEvents = disabled ? 'none' : '';
    }
  });
</script>

<script>
  // 组件获得原生待遇：checkValidity、label 关联全部可用
  const rating = document.getElementById('rating');
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    if (!rating.checkValidity()) return rating.reportValidity(); // 原生气泡
    console.log(new FormData(form).get('rating'));               // 序列化成功
  });
</script>
```
