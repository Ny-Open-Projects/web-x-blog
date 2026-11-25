---
title: [MFW-111] Astro 是什么？Islands 架构解决什么问题？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-111：Astro 是什么？Islands 架构解决什么问题？
**答**：
- Astro 是**内容优先**的元框架：默认零 JS（纯 HTML/CSS 输出），组件可以用 React/Vue/Svelte/Solid 任意混写，构建期渲染成静态 HTML。
- Islands 架构：页面整体是静态 HTML，只有需要交互的组件「岛」才带 JS 并按需水合——解决了传统 SPA「整页 hydrate」的水合税：哪怕只有一个按钮要交互，React SPA 也要下发整个组件树运行时。
- 量化收益：90% 内容页 0 KB JS；交互岛只加载自身代码+框架运行时。LCP/TTI 接近纯静态站。
- 边界：交互密集型应用（后台、IM）岛占比上升，优势退化，此时选 Next/Refine 类更合适——Astro 的甜区是内容站+局部交互。

```astro
---
// src/pages/index.astro —— 构建期执行，输出纯 HTML
import ProductCard from '../components/ProductCard.astro';
import CartButton from '../components/CartButton.react.jsx';

const products = await fetch('https://api.example.com/products').then((r) => r.json());
---
<html>
  <body>
    <h1>热销商品</h1>
    {products.map((p) => <ProductCard product={p} />)}  <!-- 静态：0 JS -->

    <!-- 岛：仅这个按钮带 React 运行时，且滚动进视口才加载 -->
    <CartButton client:visible productId="p_1001" />
  </body>
</html>
```
