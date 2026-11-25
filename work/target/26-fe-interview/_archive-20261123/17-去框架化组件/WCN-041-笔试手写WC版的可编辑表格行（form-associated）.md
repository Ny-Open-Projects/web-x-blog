---
title: [WCN-041] 笔试：手写一个 form-associated 的评分输入 WC（ElementInternals + 校验）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, Web Components]
type: 笔试题
---

## WCN-041：笔试：手写一个 form-associated 的评分输入 WC

**题目**：`<wc-rating name="score" required max="5">`：① 注册进表单，`FormData` 提交 `score`；② 必填校验（未选报错文案）；③ `disabled` attribute 使按钮禁用且不可提交；④ `form.reset()` 复位；⑤ 键盘可达（方向键改分值）。

**答**：

```javascript
class WcRating extends HTMLElement {
  static formAssociated = true;
  static observedAttributes = ['disabled', 'max', 'required'];
  #i = this.attachInternals();
  #value = 0;
  connectedCallback() {
    if (this.shadowRoot) return;
    const max = Number(this.getAttribute('max')) | 0 || 5;
    const root = this.attachShadow({ mode: 'open' });
    root.innerHTML =
      Array.from({ length: max }, (_, i) =>
        `<button type="button" data-v="${i + 1}" aria-label="${i + 1} 星">☆</button>`).join('');
    root.style = 'display:inline-flex;gap:2px';
    root.addEventListener('click', (e) => {
      if (this.hasAttribute('disabled')) return;
      const b = e.target.closest('button'); if (!b) return;
      this.#set(Number(b.dataset.v));
    });
    root.addEventListener('keydown', (e) => {
      if (this.hasAttribute('disabled')) return;
      if (e.key === 'ArrowRight') this.#set(Math.min(max, this.#value + 1));
      if (e.key === 'ArrowLeft') this.#set(Math.max(0, this.#value - 1));
    });
    this.#validate();
  }
  attributeChangedCallback() { if (this.shadowRoot) this.#validate(); }
  formDisabledCallback(d) { d ? this.setAttribute('disabled', '') : this.removeAttribute('disabled'); }
  formResetCallback() { this.#set(0); }
  #set(v) {
    this.#value = v;
    [...this.shadowRoot.querySelectorAll('button')].forEach((b) => {
      const n = Number(b.dataset.v);
      b.textContent = n <= v ? '★' : '☆';
    });
    this.#validate();
  }
  #validate() {
    this.#i.setFormValue(this.#value ? String(this.#value) : null);
    const missing = this.hasAttribute('required') && !this.#value;
    this.#i.setValidity(
      missing ? { valueMissing: true } : {},
      missing ? '请评分' : '',
      this.shadowRoot.querySelector('button'));
  }
}
customElements.define('wc-rating', WcRating);
```

**评分点**：
- `static formAssociated` + `attachInternals` + `setFormValue` 三件套齐全。
- required 校验用 `setValidity({ valueMissing })`，且提供 anchor 与中文文案。
- `formResetCallback` / `formDisabledCallback` 两个钩子都实现（题目硬性要求）。
- 键盘方向键支持且尊重 disabled。
- shadowRoot 重复 attach 防御（元素被移动时不崩）。
