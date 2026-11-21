---
title: [V3-267] Nuxt 的流式渲染与 SSR 降级（客户端接管）策略是怎样的？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-267：Nuxt 的流式渲染与 SSR 降级（客户端接管）策略是怎样的？
**答**：
- 流式：实验性 `nuxt experimental streamSsr`/组件级 Suspense 流式，外壳先出，慢区块后补；适合首页多数据源场景。
- 降级链路：服务端渲染抛错时（接口超时/渲染异常），框架输出"客户端渲染标记"，浏览器全量客户端渲染（CSR fallback），页面不白屏。
- 分级降级设计：关键路径接口设置短超时（200~500ms）+ 熔断到默认数据；非关键区块放 ClientOnly/懒加载，直接不参与 SSR。
- 监控：上报 SSR 失败率、fallback 率、渲染耗时；fallback 率 > 2% 说明服务端依赖不稳，优先治理接口。
- 追问钩子：客户端接管后 hydration 与 SEO 的代价——CSR 内容爬虫可能读不到，重要内容务必保证 SSR 成功率。

```typescript
// nuxt.config.ts
export default defineNuxtConfig({
  experimental: { payloadExtraction: true },
  nitro: {
    render: {                                    // 自定义渲染器：失败降级
      onError(event, error) {
        event.res.setHeader('x-nuxt-fallback', 'csr'); // 标记客户端接管
        return renderCsrShell(event);           // 输出纯 SPA 壳
      },
    },
  },
});
// 组件侧：非关键区块主动退出 SSR
// <ClientOnly><HeavyWidget /></ClientOnly>  或 definePageMeta({ ssr: false })
```
