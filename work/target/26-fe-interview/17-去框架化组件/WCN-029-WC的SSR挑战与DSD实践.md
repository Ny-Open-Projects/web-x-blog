---
title: [WCN-029] WC 的 SSR 有哪些挑战？如何在 Next/Nuxt 中配合 Declarative Shadow DOM 输出？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Web Components]
type: 面试题
---

## WCN-029：WC 的 SSR 有哪些挑战？如何在 Next/Nuxt 中配合 Declarative Shadow DOM 输出？

**答**：
- 挑战一：服务端无真实浏览器，`attachShadow`/customElements 依赖 DOM 环境；直接 import 组件 JS 会挂，需要 Node 端 DOM shim（如 happy-dom/@lit-labs/ssr）。
- 挑战二：客户端 JS 负责行为，但服务端必须负责"结构+样式"的输出，否则白屏/FOUC——解法是输出 DSD 标记（`<template shadowrootmode>`）。
- Lit 的官方方案 `@lit-labs/ssr`：在 Node 里渲染组件为 DSD 字符串；Next.js 通过 route handler / 自定义 renderToPipeableStream 介入，Nuxt 可用 Nitro 插件处理。
- 水合模型：define 在客户端执行时浏览器升级已有元素（connectedCallback 再次触发），行为层接管；注意避免重复渲染（connected 里判断 shadowRoot 是否已有内容）。
- 坑：DSD 里的 `<script>` 不执行，事件绑定全靠客户端 define；样式若走外部 `<link rel=stylesheet>` 需确保域名可达。

```javascript
// Node 侧：用 @lit-labs/ssr 渲染组件为 DSD（示意）
import { render } from '@lit-labs/ssr';
import { collectResultSync } from '@lit-labs/ssr/lib/collect-result-sync.js';
import './stat-card.js'; // Lit 组件可在 Node 渲染（无真实 DOM 副作用）

export function renderCard(props) {
  return collectResultSync(render`<stat-card value="${props.value}">${props.label}</stat-card>`);
}
// 输出形如：
// <stat-card value="1280"><template shadowrootmode="open">...styles+DOM...</template>今日访问</stat-card>

// 客户端：懒 define，升级已有元素，不重渲染
import('./stat-card.client.js');
```
