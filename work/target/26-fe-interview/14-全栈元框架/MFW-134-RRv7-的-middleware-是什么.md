---
title: [MFW-134] RRv7 的 middleware（unstable_middleware）是什么？放在哪一层？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-134：RRv7 的 middleware（unstable_middleware）是什么？放在哪一层？
**答**：
- RRv7 的 middleware（v7.3 起 unstable）：在路由匹配后、loader/action 执行前运行的包装函数，可以**按路由树分层声明**——根路由的 middleware 对全站生效，子路由的只对该分支生效，执行顺序是树序（外层先入、后出，洋葱模型）。
- 上下文传递：middleware 通过 `context.set/get` 构建请求级上下文（如鉴权后的 user），loader/action 从 `context` 参数读取——替代了 Remix 时代「loader 里各自查 session」的重复。
- 与 Next Middleware 对比：Next 的 middleware.ts 是全局单文件（网络层），RRv7 是路由树分层（洋葱）；RRv7 能拿到路由级上下文做更精细的编排。
- 状态：unstable 前缀意味着 API 可能变化，生产使用要锁定版本并关注 changelog。

```tsx
// app/routes.ts —— 声明层
import { route } from '@react-router/dev/routes';
export default [
  route('/', 'routes/layout.tsx', [
    { index: true, file: 'routes/home.tsx' },
    route('admin', 'routes/admin-layout.tsx', { middleware: ['./middleware/auth.ts#adminOnly'] }),
  ]),
] satisfies RouteConfig;
```

```ts
// app/middleware/auth.ts —— 洋葱模型的鉴权中间件
import { unstable_createMiddleware } from 'react-router';

export const logger = unstable_createMiddleware(async ({ request, context }, next) => {
  const t0 = Date.now();
  await next();
  console.log(`${request.method} ${request.url} ${Date.now() - t0}ms`);
});

export const adminOnly = unstable_createMiddleware(async ({ request, context }, next) => {
  const user = await requireUser(request); // 解析 cookie/token
  if (user.role !== 'admin') throw new Response('Forbidden', { status: 403 });
  context.set('user', user);  // 写入请求级上下文
  await next();
});
```

```tsx
// app/routes/admin.tsx —— loader 里取上下文
export async function loader({ context }: any) {
  const user = context.get('user'); // middleware 已鉴权，这里免重复查
  return { adminPanel: await db.adminData(user.id) };
}
```
