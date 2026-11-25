---
title: [WCN-036] WC 组件库怎么构建与分发？裸自定义元素与 Lit 封装各怎么打包？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Web Components]
type: 面试题
---

## WCN-036：WC 组件库怎么构建与分发？裸自定义元素与 Lit 封装各怎么打包？

**答**：
- 分发形态：每个组件一个 ESM 入口（`import 'lib/my-card.js'` 自动 define）+ 可选"仅类不注册"入口（`MyCard` 类导出，宿主自定义 tag 名与注册时机）。
- Lit 组件打包：编译阶段用 `@lit/reactive-element`，产物必须包含 runtime；要小心多实例重复注册问题——库里 define 一次，宿主 bundle 若也带 Lit 会出现两份装饰器基础设施（版本对齐或 externalize）。
- 构建工具链：esbuild/rolldown 打包 ESM + 生成 d.ts；样式若用 `.css` 文件，构建时内联为 `css` 模板字符串或 adoptedStyleSheets 注入；SSR 场景额外产出 DSD 渲染入口。
- 版本共存：允许页面同时加载 v1/v2 组件库 → tag 名加版本段（`my-card-v2`）或提供 `register(tag?)` 工厂而不是顶层自动 define。
- 产物要求：sideEffect: false 便于 tree-shaking；组件文件之间禁止隐式 define（副作用注册会破坏按需加载）。

```javascript
// 每组件入口：my-card.js（自动注册版）
import { MyCard } from './my-card.element.js';
if (!customElements.get('my-card')) customElements.define('my-card', MyCard);
export * from './my-card.element.js';

// my-card.element.js：仅类，宿主可自定义注册
export class MyCard extends HTMLElement { /* ... */ }

// 工厂注册：支持多版本共存
export function registerMyCard(tag = 'my-card') {
  if (!customElements.get(tag)) customElements.define(tag, MyCard);
  return customElements.whenDefined(tag);
}
```

```json
{ "name": "@lib/wc-cards", "type": "module",
  "exports": { ".": "./my-card.js", "./element": "./my-card.element.js" },
  "sideEffects": ["*.define.js"] }
```
