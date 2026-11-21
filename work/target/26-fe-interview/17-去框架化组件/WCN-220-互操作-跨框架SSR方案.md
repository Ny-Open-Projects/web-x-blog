---
title: [WCN-220] 多框架宿主（React+Vue 同仓）下统一 WC 的 SSR 输出方案？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-220：多框架宿主（React+Vue 同仓）下统一 WC 的 SSR 输出方案？
**答**：
- 统一在「元素层」做 DSD 渲染：元素提供 renderDSD(props) → HTML 片段（框架无关）。
- 各框架 SSR 适配只负责「把元素标签与 DSD 模板嵌进自己的流」。
- 水合一致：DSD 内容即客户端注册后渲染的初始态（同一渲染函数双端跑）。
- 关键约束：渲染函数必须纯净（无 window/document 访问）。

```javascript
// 元素库统一 SSR 渲染
export function renderGoodsCardDSD({ sku, price }: Props) {
  return `<goods-card sku="${sku}">
<template shadowrootmode="open">
<style>…</style><div class="price">${escape(price)}</div>
</template></goods-card>`;
} // React/Vue/Nuxt 的 SSR 适配层都消费这一函数
r
```
