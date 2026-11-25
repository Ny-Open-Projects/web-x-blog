---
title: [WCN-803] 监管行业（金融/医疗）落地 WC 组件库有哪些合规红线？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-803：监管行业（金融/医疗）落地 WC 组件库有哪些合规红线？

**答**：
- 结论先行：监管行业落 WC，红线不在技术本身，而在「可审计、可追溯、数据不出域」——组件库必须把合规能力做成默认开启的基建，而不是业务方各自实现。
- 数据合规：表单类组件禁止把敏感值（卡号/病历）写入 attribute（会留在 DOM 与监控里），用 property + ElementInternals，并配脱敏渲染；埋点事件默认脱敏上报。
- 可访问性合规：WCAG 2.1 AA 是强制项，影子树内焦点顺序、aria 关联、键盘可达要做成组件契约，并自动生成 a11y 审计报告供合规留存。
- 供应链与完整性：组件产物上 SRI、锁定版本、CDN 来源可审计，禁止运行时从不可信源动态注入脚本（Trusted Types + CSP）。
- 变更可追溯：每次组件发布要有 ADR、变更日志、审批记录，支持「某线上页面用的是哪个组件版本」的反向追责。
- 追问钩子：面试官会问「影子树是不是给审计造成盲区」——要答到用 ElementInternals 暴露可访问状态、把所有交互事件桥到可监听的 CustomEvent，保证审计工具能穿透观测。

```javascript
// 合规表单基类：敏感值走 property + 脱敏渲染，不落 attribute/DOM
class SecureField extends HTMLElement {
  static observedAttributes = ['label'];
  #value = '';                          // 私有字段，绝不反射到 attribute
  constructor() {
    super();
    this.attachShadow({ mode: 'open' }).innerHTML = `<label part="label"></label><input part="input" />`;
  }
  set value(v) { this.#value = v; this.render(); }
  get value() { return this.#value; }
  connectedCallback() { this.setAttribute('label', this.getAttribute('label') || ''); this.render(); }
  attributeChangedCallback() { this.render(); }
  render() {
    this.shadowRoot.querySelector('label').textContent = this.getAttribute('label') || '';
    // 脱敏：只显示后四位，完整值留在内存 property 中
    this.shadowRoot.querySelector('input').value = this.#value.replace(/\d(?=\d{4})/g, '•');
  }
  // 审计友好的事件：不带原始敏感值
  reportChange() {
    this.dispatchEvent(new CustomEvent('secure-change', {
      bubbles: true, composed: true, detail: { changed: true, len: this.#value.length },
    }));
  }
}
customElements.define('secure-field', SecureField);
```
