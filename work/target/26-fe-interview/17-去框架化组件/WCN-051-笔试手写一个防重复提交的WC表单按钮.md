---
title: [WCN-051] 笔试：手写一个防重复提交的 WC 表单按钮（form-associated + 状态机）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, Web Components]
type: 笔试题
---

## WCN-051：笔试：手写一个防重复提交的 WC 表单按钮

**题目**：`<submit-btn>`：① form-associated，行为等同原生 submit button；② 点击后进入 loading 态（禁用 + 文案换成 loading），直到外部调用 `done()` / `fail()`；③ loading 期间点击/回车均无效；④ `form.requestSubmit()` 由组件触发而不是直接 `form.submit()`（保证原生校验先跑）；⑤ disabled attribute 时彻底不可用。

**答**：

```javascript
class SubmitBtn extends HTMLElement {
  static formAssociated = true;
  static observedAttributes = ['disabled'];
  #i = this.attachInternals();
  #state = 'idle'; // idle | loading | done | fail
  connectedCallback() {
    if (this.shadowRoot) return;
    const root = this.attachShadow({ mode: 'open' });
    root.innerHTML = `
      <style> button { padding:8px 16px } :host([disabled]) button { opacity:.5; pointer-events:none } </style>
      <button type="button" part="btn"><slot></slot></button>`;
    this.#btn = root.querySelector('button');
    this.#btn.addEventListener('click', () => this.#click());
  }
  #btn; #label;
  get form() { return this.#i.form; }
  #click() {
    if (this.#state === 'loading') return;               // 防重复提交
    const form = this.#i.form;
    if (!form) return;
    if (!form.checkValidity()) { form.reportValidity(); return; }  // 原生校验先行
    this.#enter('loading');
    form.requestSubmit();                                 // 交给表单原生提交流程
  }
  #enter(s) {
    this.#state = s;
    if (!this.#label) this.#label = this.textContent.trim() || '提交';
    this.#btn.textContent = s === 'loading' ? '提交中…'
      : s === 'done' ? '已提交' : s === 'fail' ? '重试' : this.#label;
    this.#btn.disabled = s === 'loading';
    this.#i.states.toggle('loading', s === 'loading');
  }
  done() { this.#enter('done'); setTimeout(() => this.#enter('idle'), 1500); }
  fail() { this.#enter('idle'); } // 失败回到 idle 允许重试（文案还原）
}
customElements.define('submit-btn', SubmitBtn);
```

**评分点**：
- formAssociated + `internals.form` 拿到宿主表单；用 `requestSubmit` 而非 `submit()`（保留校验与 submit 事件）。
- loading 状态机：点击守卫 + 按钮 disabled 双保险。
- `checkValidity/reportValidity` 在提交前主动触发原生校验。
- states 伪类（`:--loading`）暴露给样式层；`done/fail` 外部控制接口清晰。
- `:host([disabled])` 属性选择器禁用态。
