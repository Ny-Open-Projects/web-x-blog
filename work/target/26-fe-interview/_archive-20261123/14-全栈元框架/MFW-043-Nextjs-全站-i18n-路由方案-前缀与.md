---
title: [MFW-043] App Router 的 i18n 路由方案怎么做（URL 前缀 vs cookie）？
date: 2026-11-17
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-043：App Router 的 i18n 路由方案怎么做（URL 前缀 vs cookie）？
**答**：
- App Router 不再有内置 i18n 路由，主流方案：**URL 前缀法**（/zh、/en 成为路径一部分）——SEO 友好（每语言独立 URL），配合 middleware 协商首次跳转。
- 协商优先级：用户主动切换（cookie NEXT_LOCALE）> Accept-Language > 默认语言；已带前缀的 URL 不再重定向。
- 词典加载：语言包按命名空间拆分，Server Component 直接 import（不打进客户端），Client Component 只带用到的词条——避免全量词典进 bundle。
- hreflang：sitemap 或 metadata 里给每页声明 `<link rel="alternate" hreflang>`；`generateStaticParams` 预渲染所有语言版本。
- cookie 法（无前缀）实现简单但 SEO 差（所有语言同 URL），只适合后台类产品。

```ts
// middleware.ts —— 首次访问协商语言前缀
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

const LOCALES = ['zh', 'en'];
export function middleware(req: NextRequest) {
  const [, seg] = req.nextUrl.pathname.split('/');
  if (LOCALES.includes(seg)) return NextResponse.next();
  const cookieLocale = req.cookies.get('NEXT_LOCALE')?.value;
  const locale = cookieLocale && LOCALES.includes(cookieLocale)
    ? cookieLocale
    : (req.headers.get('accept-language')?.startsWith('zh') ? 'zh' : 'en');
  const url = req.nextUrl.clone();
  url.pathname = `/${locale}${req.nextUrl.pathname}`;
  return NextResponse.redirect(url);
}
export const config = { matcher: ['/((?!api|_next|.*\\..*).*)'] };
```

```tsx
// app/[locale]/layout.tsx —— 词典按需注入
import { notFound } from 'next/navigation';

export async function generateStaticParams() {
  return LOCALES.map((locale) => ({ locale })); // 全语言静态化
}

export default async function LocaleLayout({ children, params }) {
  const { locale } = await params;
  if (!LOCALES.includes(locale)) notFound();
  const dict = (await import(`@/dictionaries/${locale}.json`)).default; // 只加载当前语言
  return (
    <html lang={locale}>
      <body><Nav dict={dict.nav} />{children}</body>
    </html>
  );
}
```
