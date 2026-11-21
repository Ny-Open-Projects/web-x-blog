---
title: [MFW-103] SvelteKit 的 load 依赖追踪与 invalidate 是怎么工作的？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-103：SvelteKit 的 load 依赖追踪与 invalidate 是怎么工作的？
**答**：
- 导航时 SvelteKit 只重跑「受影响」的 load：URL 变化 → 依赖 `url` 参数的 load 重跑；`params` 变化 → 依赖 params 的重跑；两者都没依赖则直接复用上次结果。这是框架级的细粒度复用。
- 手动失效：`invalidate(url)` 按 URL 前缀失效、`invalidateAll()` 失效所有 load（默认 `use:enhance` 成功后就是 invalidateAll）、`depends('app:cart')` + `invalidate('app:cart')` 自定义依赖标记。
- 与 React Query/SWR 对照：SvelteKit 把失效做在「路由数据层」，没有独立缓存库；跨组件共享请求要靠 load + 全局 state 或另接 TanStack Query。
- `invalidateAll` 的代价：mutation 后所有页面数据重新拉取，重页面会闪 loading——精确 invalidate 是优化点。

```js
// +page.js —— 声明依赖
export async function load({ fetch, depends, params }) {
  depends('app:cart'); // 自定义依赖标记
  return { items: await fetch(`/api/products/${params.id}`).then((r) => r.json()) };
}
```

```svelte
<!-- 加购后精确失效，而不是 invalidateAll -->
<script>
  import { invalidate } from '$app/navigation';

  async function addToCart(id) {
    await fetch('/api/cart', { method: 'POST', body: JSON.stringify({ id }) });
    await invalidate('app:cart');       // 只重跑声明了该依赖的 load
    // await invalidateAll();           // 粗粒度替代：全量重跑
  }
</script>
```

```js
// 依赖追踪生效规则示例
// +page.js: export function load({ url }) {...}    -> 依赖 url
//   ?page=2 导航时：url 变了 -> 重跑
//   同 URL 任意点击 -> 复用，不重跑
// +page.js: export function load() {...}            -> 无依赖
//   导航到同路由不同参数 -> 仍复用（需手动 invalidate）
```
