---
title: [V3-261] Nuxt 的渲染模式切换：prerender/ISR/SSR/SPA 按 path 怎么选？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-261：Nuxt 的渲染模式切换：prerender/ISR/SSR/SPA 按 path 怎么选？
**答**：
- prerender（SSG）：内容构建期确定（营销页/文档/首页），CDN 全静态，TTFB 极低。
- ISR/swr：内容低频变化（商品详情），首次 SSR 后缓存，`swr: N` 秒后台再生，兼顾新鲜度与性能。
- SSR：个性化强、必须实时（用户中心/购物车），每请求渲染，注意缓存头与边缘函数成本。
- ssr:false（SPA）：纯交互后台（admin），无需 SEO 与首屏服务端渲染。
- 组合决策依据三问：SEO 需求？内容个性化程度？更新频率？——三问答案直接映射上表，这是回答"为什么这么配"的万能框架。

```typescript
routeRules: {
  '/':                { prerender: true },                    // 首页：构建期生成
  '/blog/**':         { isr: true, cache: { maxAge: 3600 } }, // 博客：低频再生
  '/product/**':      { swr: 300 },                           // 商品：300s SWR
  '/account/**':      { ssr: true, headers: { 'cache-control': 'no-store' } }, // 实时个性化
  '/admin/**':        { ssr: false },                         // 内部后台 SPA
  '/old-site/*':      { redirect: { to: '/new/*', statusCode: 301 } },
}
```
