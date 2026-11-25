---
title: [WCN-119] 笔试：手写 schema 驱动的 WC 表单生成器（JSON 配置 → 表单 + 校验 + 提交）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, 跨框架复用]
type: 笔试题
---

## WCN-119：笔试：手写 schema 驱动的 WC 表单生成器

**题目**：输入 schema：`[{ name:'name', label:'姓名', type:'text', required:true, max:20 }, { name:'age', type:'number', min:0, max:150 }, { name:'level', type:'select', options:['A','B'] }]`。实现 `<x-form .schema=${s}>`：① 按 schema 渲染行（label + 控件）；② 校验规则驱动（required/max/min/enum），错误文案内联显示；③ 对外派发 `form-valid-change`（detail.valid）与 `form-submit`（detail.values）；④ 值为受控对象，宿主可预填 `value`；⑤ schema 动态变更重建表单。

**答**：

```javascript
class XForm extends HTMLElement {
  #values = {}; #errors = {};
  set schema(s) { this.#schema = s; this.#values = {}; this.#render(); }
  set value(v) { this.#values = { ...v }; this.#render(); }
  #schema = [];
  connectedCallback() { if (!this.shadowRoot) { this.attachShadow({ mode: 'open' }); this.#render(); } }
  #render() {
    if (!this.shadowRoot || !this.#schema) return;
    const rows = this.#schema.map((f) => {
      const err = this.#errors[f.name];
      const ctrl = f.type === 'select'
        ? `<select name="${f.name}">${f.options.map((o) => `<option ${this.#values[f.name] === o ? 'selected' : ''}>${o}</option>`).join('')}</select>`
        : `<input name="${f.name}" type="${f.type === 'number' ? 'number' : 'text'}"
             value="${this.#values[f.name] ?? ''}">`;
      return `<label>${f.label}${ctrl}<em class="err">${err ?? ''}</em></label>`;
    }).join('');
    this.shadowRoot.innerHTML = `
      <style>.err{color:#dc2626;display:block;min-height:1em}</style>
      <form>${rows}<button type="submit">提交</button></form>`;
    const form = this.shadowRoot.querySelector('form');
    form.addEventListener('input', (e) => this.#validateField(e.target.name, e.target.value));
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      if (this.#validateAll()) this.#emitSubmit();
    });
  }
  #validateField(name, value) {
    const f = this.#schema.find((x) => x.name === name);
    const v = f.type === 'number' ? Number(value) : value;
    this.#values[name] = v;
    let err = '';
    if (f.required && (value === '' || value == null)) err = '必填';
    if (f.type === 'number' && (v < f.min || v > f.max)) err = `范围 ${f.min}-${f.max}`;
    if (f.max && typeof v === 'string' && v.length > f.max) err = `最长 ${f.max}`;
    this.#errors[name] = err;
    this.shadowRoot.querySelector(`input[name="${name}"] ~ .err, select[name="${name}"] ~ .err`).textContent = err;
    this.#emitValid();
  }
  #validateAll() {
    this.#schema.forEach((f) => this.#validateField(f.name, this.#values[f.name] ?? ''));
    return Object.values(this.#errors).every((e) => !e);
  }
  #emitValid() {
    this.dispatchEvent(new CustomEvent('form-valid-change', {
      bubbles: true, composed: true,
      detail: { valid: Object.values(this.#errors).every((e) => !e) },
    }));
  }
  #emitSubmit() {
    this.dispatchEvent(new CustomEvent('form-submit', {
      bubbles: true, composed: true, detail: { values: { ...this.#values } },
    }));
  }
}
customElements.define('x-form', XForm);
```

**评分点**：
- schema 单一驱动源：渲染/校验/错误文案全部由配置生成；schema setter 触发重建。
- 单字段即时校验 + 提交全量校验两阶段；number 类型转换。
- 两个对外事件 detail 结构清晰（valid 布尔 / values 快照）。
- 受控 value 入口（宿主预填）。
