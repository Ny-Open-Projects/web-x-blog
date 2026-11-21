---
title: [MFW-106] SvelteKit 怎么做流式渲染和错误处理？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-106：SvelteKit 怎么做流式渲染和错误处理？
**答**：
- 流式：load 返回值里放**未 await 的 promise**，页面组件用 `{#await}` 消费——服务端会先 flush 页面骨架，promise resolve 后通过流式 chunk 补上数据（配合 Suspense 式体验，但 Svelte 用原生 await 块）。
- 错误分层：load 里 `throw error(404, 'msg')`（预期错误，渲染 +error.svelte）vs 意外异常（进 handleError 上报）；`+error.svelte` 沿路由层级就近接管，最外层是根 `+layout.svelte` 旁的 `+error.svelte`。
- 关键区别：流式 promise 一旦在服务端 reject，数据以错误形态发给客户端再抛出；而页面级致命错误发生在首字节之前，直接整页错误响应。
- 与 Next 对照：SvelteKit 用 promise 字段 ≈ Next 的 `<Suspense>` 包 await 组件；+error.svelte ≈ error.tsx。

```js
// +page.server.js —— 流式：慢数据不 await
export function load({ params }) {
  return {
    product: getProduct(params.id),          // Promise（不 await）：流式
    critical: getStock(params.id),           // await 的快数据先出
  };
}

export async function getProduct(id) {
  await new Promise((r) => setTimeout(r, 800));
  return db.product.findUnique({ where: { id } });
}
```

```svelte
<!-- +page.svelte -->
<script>
  export let data;
</script>

<h1>{data.critical.stock > 0 ? '现货' : '缺货'}</h1>

{#await data.product}
  <p>商品信息加载中…</p>
{:then product}
  <h2>{product.name}</h2>
{:catch err}
  <p>加载失败：{err.message}</p>
{/await}
```

```svelte
<!-- +error.svelte —— 就近错误页 -->
<script>
  import { page } from '$app/state';
</script>

<h1>{page.status}</h1>
<p>{page.error?.message}</p>
```
