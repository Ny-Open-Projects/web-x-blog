---
title: [WCN-015] Declarative Shadow DOM 是什么？它解决了 SSR 场景的什么问题？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Web Components]
type: 面试题
---

## WCN-015：Declarative Shadow DOM 是什么？它解决了 SSR 场景的什么问题？

**答**：
- 用 `<template shadowrootmode="open">` 直接在 HTML 里声明影子树，浏览器解析时即创建 shadow root，无需等 JS。
- 解决的问题：传统 WC 必须等 JS 下载执行 `attachShadow`，SSR 输出的 HTML 首屏无样式无结构（FOUC）；DSD 让服务端 HTML 自带完整影子结构与样式，首屏即可渲染。
- SSR 流程：服务端渲染时把组件的 shadow 模板序列化为 DSD 标记输出，客户端 JS 只注册行为（升级已有元素），不重复渲染。
- `shadowrootmode` 必须写（不提倡旧名 `shadowroot`/`shadowrootdelegatesfocus` 的裸模式属性）；`shadowrootclonable`、`shadowrootdelegatesfocus` 是可选修饰。
- 注意：DSD 模板里的 `<script>` 不会在解析时执行（防止 SSR 注入），样式与内容会；客户端可按需 lazy define 对应 custom element。

```html
<!-- 服务端直出的 HTML，无 JS 也完整渲染 -->
<product-card sku="A1">
  <template shadowrootmode="open">
    <style>.title { font-weight: 600 } .price { color: #16a34a }</style>
    <div class="title">无线耳机</div>
    <div class="price">¥299</div>
    <slot></slot>
  </template>
  <span slot>黑色 / 主动降噪</span>
</product-card>

<script type="module">
  // 按需水合：注册后浏览器自动升级上面已存在的元素
  customElements.define('product-card', class extends HTMLElement {
    connectedCallback() { /* 绑定交互、加购按钮事件等 */ }
  });
</script>
```
