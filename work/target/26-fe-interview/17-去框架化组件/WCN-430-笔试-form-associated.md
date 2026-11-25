---
title: [WCN-430] 笔试：实现 formAssociated 表单控件（值/校验/FormData 集成）。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-430：笔试：实现 formAssociated 表单控件（值/校验/FormData 集成）。
**答**：`DsRating extends HTMLElement, formAssociated`：内部 input[type=range] 同步 value；setFormValue 上报；ValidityState 转发（required 语义）；重置响应。

```javascript
class DsRating extends HTMLElement {
  static formAssociated = true;
  #internals;
  constructor() {
    super();
    this.#internals = this.attachInternals();
    this._value = 0;
  }
  set value(v) { this._value = v; this.#internals.setFormValue(String(v));
    this.#internals.setValidity(v > 0 ? this.#internals.validity : { valueMissing: true },
      v > 0 ? '' : '请评分'); this._render(); }
  get value() { return this._value; }
  formResetCallback() { this.value = 0; }
}
customElements.define('ds-rating', DsRating);

```

**评分点**：
- static formAssociated = true + attachInternals。
- value property ↔ internals.setFormValue。
- 校验：internals.setValidity(validity, message)。
- formResetCallback 恢复默认。
