---
title: [MFW-108] SvelteKit 与 Next、Nuxt 对比，各自立足点是什么？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-108：SvelteKit 与 Next、Nuxt 对比，各自立足点是什么？
**答**：
- 立足点一句话：Next 卖 RSC 服务端心智；Nuxt 卖 Vue 生态 + Nitro 部署自由；SvelteKit 卖**最小运行时**——编译期消解框架，客户端负担最小，水合最快。
- 数据层哲学：SvelteKit 是最「web 标准」的（form actions、load、fetch 都是显式 web API 风格）；Next 用 RSC/Action 抽象；Nuxt 用 composable 数据层。SvelteKit 的显式分层对初学者更友好。
- 生态权重：React 生态是 Next 的护城河，Svelte 生态最小但质量高（组件库、图标类够用）；团队招人市场上 React 明显占优。
- 适用判断：性能敏感的营销/文档/中小应用、追求精简 bundle 的团队选 SvelteKit；大型 React 团队与复杂服务端组件化需求选 Next；Vue 团队选 Nuxt。

```js
// 三框架「同一页面」的代码密度对比（伪代码摘要）

// ===== SvelteKit：load 显式 + 组件极简 =====
// +page.server.js: export const load = ({ params }) => ({ product: getProduct(params.id) });
// +page.svelte: <h1>{data.product.name}</h1>

// ===== Next：组件即取数（RSC） =====
// export default async function Page({ params }) {
//   const product = await getProduct((await params).id);
//   return <h1>{product.name}</h1>;
// }

// ===== Nuxt：composable 数据层 =====
// const { data: product } = await useFetch(`/api/products/${useRoute().params.id}`);
// <h1>{{ product?.name }}</h1>
```
