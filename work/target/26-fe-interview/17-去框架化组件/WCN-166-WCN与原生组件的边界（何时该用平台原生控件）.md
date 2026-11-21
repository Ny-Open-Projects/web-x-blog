---
title: [WCN-166] WCN 与平台原生控件的边界：哪些交互应该直接用原生标签而不是自研组件？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 选型与工程落地]
type: 面试题
---

## WCN-166：WCN 与平台原生控件的边界：哪些交互应该直接用原生标签而不是自研组件？

**答**：
- 原生优先清单：`<details>/<summary>`（折叠）、`<dialog>`（模态）、`<input type=date/color/file>`（采集类）、`<select>`（除非设计硬约束）、`<video>`（+ 自绘控制条）、popover 属性元素——原生自带可达性、键盘、触控与平台一致性，自研等于重复实现一堆 a11y 陷阱。
- WCN 的正确姿势：组件作为"壳"包装原生控件做样式统一（如 `<acme-switch>` 内部用 `<input type=checkbox role=switch>`），而不是从 div 手搓开关；form-associated 让壳无缝进表单。
- 判断标准：该交互的平台成熟度（a11y/触控/输入法覆盖）与设计还原度的冲突程度——冲突小用原生，冲突大才自研且必须补 a11y 测试。
- 平台新能力跟进：popover、`@starting-style`、CSS anchor positioning 逐年替代第三方弹层/定位库——组件依赖清单定期评审下线自研轮子。

```javascript
// 壳包装原生控件的正确模式
class AcmeSwitch extends HTMLElement {
  static formAssociated = true;
  #i = this.attachInternals();
  connectedCallback() {
    this.attachShadow({ mode: 'open' }).innerHTML = `
      <style>:host{display:inline-block} label{display:flex;gap:8px}</style>
      <label><slot></slot><input type="checkbox" role="switch"></label>`;
    const input = this.shadowRoot.querySelector('input');
    input.addEventListener('change', () => {
      this.#i.setFormValue(input.checked ? 'on' : null);   // 原生控件兜底全部 a11y
      this.dispatchEvent(new CustomEvent('acme-switch-change',
        { bubbles: true, composed: true, detail: { checked: input.checked } }));
    });
  }
}
customElements.define('acme-switch', AcmeSwitch);
```
