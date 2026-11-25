---
title: [MFW-869] TanStack Start 的 server function 中间件链和 Next Middleware 有什么差异
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-869：TanStack Start 的 server function 中间件链和 Next Middleware 有什么差异

**答**：
- 结论：TanStack 的 server function 中间件是函数级装饰器链（.middleware([...])），紧邻业务逻辑；Next Middleware 是路由级边缘层，在渲染前统一拦截。
- 落地：鉴权/日志/限流在 Start 用 serverFn 中间件复用，在 Next 用 middleware（边缘）或 RSC 层；粒度与执行时点不同。
- 追问钩子：全局鉴权放哪？——Start 用 beforeLoad + serverFn 双层，Next 用 middleware 粗粒度 + RSC 细粒度。

```javascript
// TanStack：函数级中间件链（紧邻业务）
const fn = createServerFn()
  .middleware([authMiddleware, logMiddleware, rateLimitMiddleware])
  .handler(async ({ context }) => {
    return db.getData(context.user.id);
  });

// Next：路由级边缘层（统一拦截所有请求）
export function middleware(req) {
  const token = req.cookies.get('token');
  if (!token) return NextResponse.redirect('/login');
  return NextResponse.next();
}
// 差异：Start 粒度到单个函数、与业务同处；Next 是请求入口的统一屏障
```
