---
title: [MFW-861] TanStack Start 的 beforeLoad 与 loader 职责差异，鉴权该放哪
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-861：TanStack Start 的 beforeLoad 与 loader 职责差异，鉴权该放哪

**答**：
- 结论：beforeLoad 在 loader 之前运行，负责鉴权/重定向/预取依赖，其结果进入 context 供子路由 loader 用；loader 专职取数据。
- 鉴权落点放 beforeLoad——在取数前拦截，避免无谓查询；loader 只信任 beforeLoad 建立的 context。
- 追问钩子：beforeLoad 会重复执行吗？——默认每次导航都跑，可用 staleTime 缓存；子路由自动继承父级 beforeLoad。

```javascript
export const Route = createFileRoute('/admin/_layout')({
  beforeLoad: async ({ location, context }) => {
    const user = await context.auth.getUser();
    if (!user) throw redirect({ to: '/login', search: { redirect: location.href } });
    if (!user.isAdmin) throw redirect({ to: '/403' });
    return { user };                                 // 进入 context，子路由可用
  },
  loader: async ({ context }) => {
    // context.user 由 beforeLoad 保证存在，直接信任
    return db.admin.dashboard(context.user.id);
  }
});
```
