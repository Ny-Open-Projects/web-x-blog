---
title: [MFW-206] Next.js 多租户：域名驱动的租户路由怎么实现
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-206：Next.js 多租户的域名路由实现

**答**:
- 两种租户路由：域名制（acme.app.com——每个租户子域名）与路径制（app.com/acme）——域名制 SaaS 主流（品牌隔离）
- 域名制实现：Middleware 解析 Host header → 提取租户 slug → rewrite 到 `/[tenant]/...` 路由；租户数据在 layout 加载（generateMetadata 也要带租户上下文）
- 关键细节：通配域名 SSL（*.app.com 证书）、租户自定义域名（CNAME + 动态证书如 Vercel domains API）、缓存 key 必须含租户（否则跨租户串数据——多租户最大事故源）
- 数据层：每查询带 tenantId（RLS 行级安全是硬防线——前端租户解析只是路由，不是安全边界）

```javascript
// middleware.ts
export function middleware(req) {
  const host = req.headers.get('host')
  const sub = host.split('.')[0]
  if (sub !== 'www' && !isReserved(sub))
    return NextResponse.rewrite(new URL(`/${sub}${req.nextUrl.pathname}`, req.url))
}
// app/[tenant]/layout.tsx
export default async function TenantLayout({ children, params }) {
  const tenant = await getTenant(params.tenant)   // 查不到 → notFound()
  return <TenantProvider tenant={tenant}>{children}</TenantProvider>
}
```
