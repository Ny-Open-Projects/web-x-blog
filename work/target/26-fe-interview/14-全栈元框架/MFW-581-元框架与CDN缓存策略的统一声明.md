---
title: [MFW-581] 元框架与 CDN 缓存策略的统一声明
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-581：CDN 缓存策略的统一声明

**答**:
- 元框架的缓存声明到 CDN 头的翻译：1) **路由段 config**（`export const revalidate = 60` → CDN 的 s-maxage=60——框架缓存与 CDN 缓存的统一声明）；2) **routeRules**（Nuxt：`{ '/blog/**': { cache: { swr: 3600 } } }` → s-maxage=3600 stale-while-revalidate）；3) **显式 header**（route handler 手动 Cache-Control——最高优先级）。
- 翻译的语义对齐：框架的 revalidate（Data Cache TTL）与 CDN s-maxage 是「两层缓存的两条 TTL」——统一声明让两层同步（revalidate=60 → s-maxage=60：CDN 与框架同过期——双缓存的一致性窗口）；「两层缓存不一致」（CDN 60s 框架 300s——CDN 短 TTL 保证用户 60s 内看到新数据（CDN 先过期回源，框架缓存还新鲜——快速返回）。
- 缓存头的产物审计（RBL-618 物料）：build 产物输出「每路由的预期 Cache-Control」（构建期推导——CDN 配置即产物 RBL-618 的元框架版）。
- 追问钩子：为什么「框架缓存与 CDN 缓存的 TTL 对齐」比「各自独立配置」更安全？——独立配置的失效错位：CDN 长缓存（1h）+ 框架短（60s）——CDN 缓存的旧 HTML 引用旧数据（框架缓存的新鲜数据没机会展示——CDN 屏蔽了框架层）；对齐让失效传播从「框架层」穿透到「CDN 层」（revalidate 时 s-maxage 同步到期）——多级缓存的失效传播一致性（RBL-637 缓存层级问题的 CDN 版）。

```javascript
// 路由段 config → CDN 头（Next）
// app/products/page.tsx
export const revalidate = 60;
// 响应头：Cache-Control: s-maxage=60, stale-while-revalidate
// routeRules 声明（Nuxt）
export default defineNuxtConfig({
  routeRules: {
    '/products': { swr: 60 },                            // s-maxage=60 swr
    '/api/**': { cache: false },                         // no-store
    '/admin/**': { headers: { 'cache-control': 'no-store' } },
  },
});
// 构建期产物：每路由的预期头
// .next/routes-manifest → CDN 配置文件（terraform/网关）
// 两层 TTL 对齐验证
function auditCacheAlignment(route, frameworkTtl, cdnTtl) {
  if (cdnTtl > frameworkTtl * 2)
    warn(`路由 ${route}: CDN TTL(${cdnTtl}s) >> 框架 TTL(${frameworkTtl}s)——CDN 屏蔽框架层失效`);
  return { route, cdnTtl, frameworkTtl };
}
```
