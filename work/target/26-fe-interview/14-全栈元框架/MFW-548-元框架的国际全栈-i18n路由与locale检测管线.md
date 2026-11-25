---
title: [MFW-548] 国际化全栈：i18n 路由结构与 locale 检测管线
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-548：i18n 路由与 locale 检测管线

**答**:
- i18n 路由结构：`[locale]/` 段路由（app/[locale]/page.tsx——locale 是动态段：URL /en/products /zh/products）——locale 进 URL = 缓存键含 locale（RBL-598：每种 locale 独立产物）；「locale 检测」：middleware 读 Accept-Language/cookie → 重定向到带 locale 的 URL（规范化：无 locale 路径 308 到检测 locale）。
- 检测的顺序优先级：URL 显式 > cookie 用户偏好 > Accept-Language > 默认——「检测只在无 URL locale 时」（middleware 逻辑）；「cookie 与 URL 的循环」（cookie=zh 访问 /en → 尊重 URL 还是 cookie？——URL 优先：用户显式选择语言即意图）。
- 翻译资源加载：全量 vs 按命名空间（RBL-695 管线——locale chunk 独立缓存）；server 组件的 i18n（next-intl 的 getRequestConfig——ALS 上下文携带 locale RBL-519 多租户模式同构）。
- 追问钩子：为什么 locale 必须进 URL 而不是只靠 cookie？——URL = 可分享/可缓存/可 SEO（每种 locale 独立 URL 才能被搜索引擎索引——hreflang 对）；cookie-only locale = 缓存键缺失（CDN 缓存会串 locale——不同用户看到不同语言缓存的同一 URL = 灾难）；「状态进 URL」原则（RBL-936 的 state）在 i18n 的必然性：用户可见状态必须可寻址。

```javascript
// middleware：locale 检测与重定向
export function middleware(req) {
  const { pathname } = req.nextUrl;
  if (locales.some(l => pathname.startsWith(`/${l}`))) return NextResponse.next();
  const locale = pickLocale(req);                        // cookie > Accept-Language > default
  return NextResponse.redirect(new URL(`/${locale}${pathname}`, req.url));  // 308 语义
}
// [locale] 段路由：缓存键含 locale
// app/[locale]/products/page.tsx
export async function generateStaticParams() {
  return locales.map(l => ({ locale: l }));              // 每 locale 预渲染
}
// server 组件的 i18n 上下文（ALS 模式 RBL-519）
// i18n/request.ts
export const getRequestConfig = async () => {
  const locale = (await tenantContext.getStore())?.locale ?? 'en';
  return { messages: (await import(`../messages/${locale}.json`)).default };
};
// hreflang（SEO）
<link rel="alternate" hrefLang="zh" href="https://x.com/zh/products" />
```
