---
title: [MFW-030] 笔试：手写 i18n 语言协商 Middleware（含 cookie 优先级与回退）
date: 2026-11-17
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-030：笔试：手写 i18n 语言协商 Middleware（含 cookie 优先级与回退）
**题目**：支持 locales `['zh','en','ja']`，默认 `zh`。规则：用户已访问过则尊重 `NEXT_LOCALE` cookie；否则按 Accept-Language 协商；都不命中用默认。URL 无语言前缀时 307 重定向到 `/{locale}{path}`（保留 query）；`/_next`、静态资源与 API 不处理。

```typescript
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

const LOCALES = ['zh', 'en', 'ja'];
const DEFAULT_LOCALE = 'zh';
const COOKIE = 'NEXT_LOCALE';

function negotiate(acceptLanguage: string | null): string {
  if (!acceptLanguage) return DEFAULT_LOCALE;
  // 解析 q 值排序：'zh-CN,en;q=0.8,ja;q=0.5'
  const parsed = acceptLanguage
    .split(',')
    .map((part) => {
      const [tag, q] = part.trim().split(';q=');
      return { tag: tag.toLowerCase(), q: q ? parseFloat(q) : 1 };
    })
    .sort((a, b) => b.q - a.q);
  for (const { tag } of parsed) {
    const base = tag.split('-')[0]; // zh-CN -> zh
    if (LOCALES.includes(base)) return base;
  }
  return DEFAULT_LOCALE;
}

export function middleware(req: NextRequest) {
  const { pathname, search } = req.nextUrl;

  // 静态资源 / API 直接放行
  if (pathname.startsWith('/_next') || pathname.startsWith('/api') || pathname.includes('.')) {
    return NextResponse.next();
  }

  // 已经带语言前缀：写回 cookie 供下次使用
  const [, first] = pathname.split('/');
  if (LOCALES.includes(first)) {
    const res = NextResponse.next();
    if (req.cookies.get(COOKIE)?.value !== first) {
      res.cookies.set(COOKIE, first, { maxAge: 31536000, path: '/' });
    }
    return res;
  }

  // 无前缀：cookie 优先，其次协商
  const locale = req.cookies.get(COOKIE)?.value ?? negotiate(req.headers.get('accept-language'));
  const url = req.nextUrl.clone();
  url.pathname = `/${locale}${pathname === '/' ? '' : pathname}`; // 保留 query：clone 自带
  return NextResponse.redirect(url, 307); // 307 保方法，避免 POST 被 308 改写语义争议
}

export const config = { matcher: ['/((?!_next|api).*)'] };

// **评分点**
// 1. 优先级正确：cookie > Accept-Language > 默认值。
// 2. Accept-Language 解析处理 q 值与 zh-CN -> zh 主子标签归一。
// 3. 重定向保留原 query（clone nextUrl），307/308 选择有说法。
// 4. matcher/守卫排除 _next 与带点路径（静态文件），避免死循环重定向。
```
