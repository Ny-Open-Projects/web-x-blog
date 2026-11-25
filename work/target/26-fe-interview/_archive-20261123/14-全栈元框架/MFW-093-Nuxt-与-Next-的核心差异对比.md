---
title: [MFW-093] Nuxt 与 Next 的核心差异是什么？各自适合什么团队？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-093：Nuxt 与 Next 的核心差异是什么？各自适合什么团队？
**答**：
- 心智模型：Next 是 **React Server Components 优先**，数据与组件在服务端一体执行；Nuxt 是 **Vue 全家桶 + 明确的 useFetch/useAsyncData 数据层**，组件仍是同构的 Vue 组件，数据请求显式声明。
- 渲染策略配置：Nuxt 的 routeRules 一张表管全站（swr/isr/prerender/ssr:false），Next 要逐页 export + Middleware 组合；Nuxt 配置面更集中，Next 粒度更细（PPR/Suspense 分层更成熟）。
- 服务端引擎：Nuxt 的 Nitro 是独立可部署层（多 preset、storage 抽象）；Next 绑定 Vercel 生态更深，自托管要靠 standalone/OpenNext。
- 选型结论：Vue 团队无脑 Nuxt；React 团队且重度依赖 RSC/Server Action 心智选 Next；混合部署到自有 K8s 时 Nitro 的多目标产物更省事。两者都在向「类型安全 + 流式 + 可插拔缓存」收敛。

```ts
// 同一「商品页 + 缓存」两框架写法对比

// ===== Next（RSC：数据取数即组件代码） =====
// app/products/[id]/page.tsx
export const revalidate = 600;
export default async function Page({ params }: { params: Promise<{ id: string }> }) {
  const product = await db.product.findUnique({ where: { id: use(params).id } });
  return <h1>{product?.name}</h1>;
}

// ===== Nuxt（数据层显式 + routeRules 集中配置） =====
// app/pages/products/[id].vue
// nuxt.config: routeRules['/products/**'] = { swr: 600 }
// <script setup>
// const { data: product } = await useFetch(`/api/products/${useRoute().params.id}`);
// </script>
// <template><h1>{{ product?.name }}</h1></template>
```
