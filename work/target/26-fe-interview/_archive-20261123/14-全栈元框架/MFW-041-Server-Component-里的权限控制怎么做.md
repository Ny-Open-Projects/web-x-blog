---
title: [MFW-041] Server Component 里的权限控制（布局级与数据级）怎么做？
date: 2026-11-17
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-041：Server Component 里的权限控制（布局级与数据级）怎么做？
**答**：
- 双层防护：**路由级**用 middleware 或 layout 里校验 session（未登录直接 `redirect('/login')`）；**数据级**在每次查询前校验归属（`where: { userId }`），防止水平越权（IDOR）。
- Server Component 读 session 用 `cookies()`（Auth.js 等库的 auth() 也是基于此）；**绝不能把鉴权判断交给 Client Component**——客户端代码全部可篡改，服务端必须自己验。
- `notFound()` 抛 404 比返回 403 更稳（不泄露资源存在性）；对「存在但无权」的资源统一 404 是安全惯例。
- middleware 层适合做**粗粒度**拦截（URL 前缀 + session 存在性）；细粒度（角色、数据归属）要在渲染与查询处做，因为 middleware 无法可靠拿到用户身份细节（Edge 里也碰不到 DB）。
- Server Action 同样要重复鉴权——它是独立入口，绕过了页面渲染流程。

```tsx
// app/admin/layout.tsx —— 布局级：进入即校验
import { redirect } from 'next/navigation';
import { getSession } from '@/lib/auth';

export default async function AdminLayout({ children }) {
  const session = await getSession(); // 读 cookie 校验
  if (!session) redirect('/login?from=/admin');
  if (session.role !== 'admin') notFound(); // 无权统一 404：不泄露 /admin 存在性
  return <div className="admin-shell">{children}</div>;
}
```

```tsx
// app/orders/[id]/page.tsx —— 数据级：归属校验防 IDOR
import { notFound } from 'next/navigation';

export default async function Order({ params }) {
  const { id } = await params;
  const session = await getSession();
  // 必须带 userId 条件：任何登录用户拿别人订单 ID 都查不到
  const order = await db.order.findFirst({
    where: { id, userId: session.userId },
    include: { items: true },
  });
  if (!order) notFound();
  return <OrderView order={order} />;
}
```
