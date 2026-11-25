---
title: [MFW-743] Nuxt Route Rules 声明式缓存
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-743：Nuxt Route Rules 声明式缓存

**答**:
- Route Rules 的声明式缓存（RBL-530 Nitro 扩展）：1) **routeRules**（nuxt.config 的路由级缓存/重定向/headers——`{ '/blog/**': { swr: 3600 } }`）；2) **策略类型**：prerender（构建期生成）/ swr（stale-while-revalidate）/ isr（增量再生）/ cache（存储缓存——unstorage 后端 RBL-530）；3) headers/redirect/proxy（非缓存的路由规则——重定向/代理/自定义头）。
- Route Rules 到 HTTP 头的翻译：swr: 3600 → `Cache-Control: s-maxage=3600, stale-while-revalidate`（RBL-582 的 Nuxt 版）；isr：类似但框架内缓存（Nitro 的 route cache）；「声明式 → 头」的翻译与 Next 的 revalidate 对齐（RBL-526 的统一语义）。
- 优先级：routeRules 的匹配（glob 通配——`/api/**` 与 `/api/specific` 的匹配优先级：specific 优先于通配）。
- 追问钩子：为什么「声明式缓存」优于「每页面手动设置」？——声明式 = 路由级别的统一策略（`/blog/**` 一条规则覆盖所有 blog 页）；手动 = 每页面单独设置（遗漏/不一致——200 页面 200 种缓存策略）；「声明的中心化」：缓存策略在一个文件（review 一次看全局）——配置的中心化是治理的基础（RBL-677 共享配置的 Nuxt 版）。

```typescript
// nuxt.config.ts
export default defineNuxtConfig({
  routeRules: {
    // 静态化
    '/': { prerender: true },
    // ISR（Nitro 内缓存）
    '/blog/**': { swr: 3600 },                          // s-maxage=3600 swr
    '/products/**': { isr: 60 },
    // API 不缓存
    '/api/**': { cache: false, cors: true },
    // 重定向
    '/old': { redirect: { to: '/new', statusCode: 302 } },
    // 代理
    '/proxy/**': { proxy: 'https://backend.com/**' },
    // 自定义头
    '/admin/**': { headers: { 'x-robots-tag': 'noindex' } },
  },
});
// 翻译到 HTTP 头（RBL-582）
// '/blog/**': swr:3600 → Cache-Control: s-maxage=3600, stale-while-revalidate
// 优先级：specific > 通配
// { '/blog/**': swr: 3600, '/blog/featured': swr: 0 }    ← featured 用 0（实时）
```
