---
title: [WCN-056] WC 组件如何做国际化与 RTL？文案从哪来（context/attribute/CSS logical 属性）？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Web Components]
type: 面试题
---

## WCN-056：WC 组件如何做国际化与 RTL？文案从哪来（context/attribute/CSS logical 属性）？

**答**：
- 文案来源三选：① attribute/slot（宿主传文案，组件最中性，推荐）；② context（沿树注入 i18n 实例，多语言块级切换）；③ 组件内置字典 + `lang` 属性选择（独立分发 SDK 场景）。
- RTL：影子树内不要写 left/right，统一用 CSS logical 属性（margin-inline-start、inset-inline、padding-block）；`dir` 属性继承穿透 shadow 边界，宿主设置 `<html dir="rtl">` 组件自动翻转。
- 需要感知方向时用 `:host([dir])` 拿不到——正确做法是 CSS `:dir(rtl)` 伪类（现代浏览器影子树内可用）或监听宿主 dir 变化。
- 数字/日期格式化：组件内用 `Intl.NumberFormat`，locale 从 `this.lang`（继承自宿主 lang 属性）读取，不硬编码。
- 复数/占位符：简单场景 `t('key', { n })` 字符串替换即可；重度 i18n 需求建议文案全部外置、组件零字典。

```javascript
class PriceTag extends HTMLElement {
  static observedAttributes = ['value', 'currency'];
  connectedCallback() {
    this.attachShadow({ mode: 'open' }).innerHTML = `
      <style>:host{display:inline-block}
      /* 全部 logical 属性：RTL 自动翻转 */
      b { margin-inline-end: 4px } .old { text-decoration: line-through; inset-inline-start: 0 }</style>
      <b id="p"></b><slot name="note"></slot>`;
    this.#sync();
  }
  attributeChangedCallback() { if (this.shadowRoot) this.#sync(); }
  #sync() {
    const locale = this.lang || navigator.language;          // 继承宿主 lang
    const nf = new Intl.NumberFormat(locale, {
      style: 'currency', currency: this.getAttribute('currency') ?? 'CNY',
    });
    this.shadowRoot.getElementById('p').textContent =
      nf.format(Number(this.getAttribute('value')) || 0);
  }
}
customElements.define('price-tag', PriceTag);
// 宿主：<html lang="ja" dir="rtl"> 下组件自动日语格式化 + 布局翻转
```
