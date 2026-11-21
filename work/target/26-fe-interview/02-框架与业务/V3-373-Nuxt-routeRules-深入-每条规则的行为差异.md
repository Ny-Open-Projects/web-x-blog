---
title: [V3-373] Nuxt routeRules 深入：各条规则的行为差异是什么？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-373：Nuxt routeRules 深入：各条规则的行为差异是什么？
**答**：
- `prerender: true`：构建期生成静态 HTML，运行时零服务端开销；适合营销页、文档页。
- `ssr: false`：SPA 模式，服务端只出壳；适合登录后内部工具页。
- `isr: 3600`：增量静态再生，服务端缓存 HTML 定时失效（需支持的 preset，如 Nitro + Redis/Vercel）。
- `swr: 60`：stale-while-revalidate HTML 缓存，先回旧页后台刷新，适合内容页。
- `cache` / `headers` / `redirect`：接口级缓存、自定义响应头（CSP/HSTS）、路由重定向。
- 组合建议：首页 swr、详情 isr、后台 ssr:false、活动页 prerender——一个配置文件完成「按路由选渲染策略」。
```javascript
routeRules: {
  '/': { swr: 60 },
  '/goods/**': { isr: 3600 },
  '/admin/**': { ssr: false },
  '/promo/**': { prerender: true }
}
```
