---
title: [MFW-209] Next.js 国际化路由三种方案对比
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-209：国际化路由三种方案

**答**:
- 方案一：路径前缀（/en/about /zh/about）——SEO 最优（每语言独立 URL）、实现成熟（[lang] 动态段 + Middleware Accept-Language 重定向）；方案二：域名分区域（en.site.com / zh.site.com）——region 部署友好；方案三：cookie/header 无 URL 变化——SEO 最差（不推荐公开站点）
- [lang] 段实现：app/[lang]/layout.tsx 校验 lang 合法（notFound 兜底）、字典按语言分包懒加载、generateStaticParams 枚举语言（SSG 每语言产物）
- Middleware 语言协商：cookie > Accept-Language > 默认——协商只在「无语言路径」时重定向（防循环）
- 缓存与失效：语言进缓存 key（fetch tags 带 lang）、hreflang 标签 SEO 配套

```javascript
// middleware.ts：语言协商
if (!/^\/(en|zh)/.test(req.nextUrl.pathname)) {
  const lang = req.cookies.get('lang')?.value
    ?? negotiate(req.headers.get('accept-language')) ?? 'en'
  return NextResponse.redirect(new URL(`/${lang}${req.nextUrl.pathname}`, req.url))
}
```
