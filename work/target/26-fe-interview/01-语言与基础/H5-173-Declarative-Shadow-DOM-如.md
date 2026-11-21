---
title: [H5-173] Declarative Shadow DOM 如何解决组件的 SSR/首屏/SEO？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-173：Declarative Shadow DOM 如何解决组件的 SSR/首屏/SEO？
**答**：
- DSD：HTML 里直接内联 `<template shadowrootmode="open">`，样式与结构随 HTML 一起到达——**无 JS 也有完整渲染**，爬虫与无 JS 环境可见。
- 客户端水合：`customElements.define` 时若 `this.shadowRoot` 已存在（DSD 创建的）就不再重建，直接复用。
- SSR 侧：旧 `innerHTML` 不解析 DSD，要用 `setHTMLUnsafe/parseHTMLUnsafe`；框架化方案是 lit 的 `@lit-labs/ssr` 自动注入 DSD。
- 附带收益：样式与 DOM 同到达，避免 FOUC；旧浏览器用 polyfill（遍历 template[shadowrootmode] 手动 attachShadow）。

```html
<!-- Declarative Shadow DOM：HTML 传输时自带 shadow 结构，无 JS 也有样式与封装 -->
<x-card>
  <template shadowrootmode="open">
    <style>
      :host { display: block; border: 1px solid #e5e7eb; border-radius: 8px;
              padding: 12px; }
      h3 { margin: 0 0 6px; color: #2563eb; }
    </style>
    <h3><slot name="title">默认标题</slot></h3>
    <p><slot></slot></p>
  </template>
  <span slot="title">服务端渲染的卡片</span>
  这段内容在 light DOM，爬虫与无 JS 环境都能读到
</x-card>
<script>
class XCard extends HTMLElement {
  connectedCallback() {
    // 水合：DSD 已创建 shadowRoot —— 只有不存在的（纯 CSR 场景）才补建
    if (this.shadowRoot) return;          // DSD 场景：直接复用，防重复注入
    this.attachShadow({ mode: 'open' }).innerHTML = `
      <style>h3 { color: #2563eb; }</style>
      <h3><slot name="title"></slot></h3><p><slot></slot></p>`;
  }
}
customElements.define('x-card', XCard);
</script>
<script>
// SSR 侧（Node）：手写解析 DSD 用 parseHTMLUnsafe，
// 旧 innerHTML 会把 template[shadowrootmode] 当普通模板忽略
const parsed = Document.parseHTMLUnsafe(
  '<x-card><template shadowrootmode="open"><style>:host{color:red}</style>' +
  'hi</template>content</x-card>');
console.log(parsed.querySelector('x-card').shadowRoot !== null);  // true

// 面试口径：
// 1) SEO 与首屏：内容与样式在 HTML 响应里完整可见，无 JS 也有首屏
// 2) 服务端用序列化器（lit 的 @lit-labs/ssr）自动注入 DSD
// 3) 水合：define 时检测 shadowRoot 已存在就复用，不重复 attach
// 4) 附带收益：样式与 DOM 同到达，避免 FOUC；旧浏览器用 polyfill 兜底
</script>
```

## 二十九、无障碍工程实践
