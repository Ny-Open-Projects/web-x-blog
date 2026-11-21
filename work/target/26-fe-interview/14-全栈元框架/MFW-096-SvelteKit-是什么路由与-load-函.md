---
title: [MFW-096] SvelteKit 是什么？路由和 load 函数的心智模型是什么？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-096：SvelteKit 是什么？路由和 load 函数的心智模型是什么？
**答**：
- SvelteKit 是 Svelte 的官方全栈框架：文件路由（`src/routes`）+ SSR/SSG/SPA 可切换 + `+server.ts` API 层 + adapter 部署体系。
- 核心心智：**load 函数负责取数**，组件只管渲染。`+page.js`（同构 load，服务端与客户端都能跑）与 `+page.server.js`（仅服务端，可碰密钥/DB）分离，边界比 RSC 更显式。
- 数据流：嵌套路由每个段可有自己的 `+layout.js/+page.js`，导航时只重新运行**变化段**的 load（依赖追踪决定），未变段数据复用。
- 与 Next 对照：`+page.server.js` ≈ RSC 的服务端组件 + fetch，但没有「组件即服务端代码」的混合心智，取数与渲染明确分层。

```
src/routes/
├── +layout.svelte          # 根布局
├── +layout.server.js       # 全站服务端数据（如用户信息）
├── products/
│   ├── +page.server.js     # 列表页服务端 load
│   └── [id]/
│       ├── +page.server.js # 详情页服务端 load
│       └── +page.svelte    # 详情组件
└── api/
    └── products/+server.ts # GET /api/products
```

```js
// +page.server.js —— 仅服务端：可以连 DB、用密钥
export async function load({ params, url, locals }) {
  const page = Number(url.searchParams.get('page') ?? 1);
  const product = await db.product.findUnique({ where: { id: params.id } });
  if (!product) throw error(404, '商品不存在');
  return { product, page };
}
```

```svelte
<!-- +page.svelte —— 组件只消费 data -->
<script>
  export let data; // load 返回值自动注入
</script>

<h1>{data.product.name}</h1>
<p>¥{data.product.price}</p>
```
