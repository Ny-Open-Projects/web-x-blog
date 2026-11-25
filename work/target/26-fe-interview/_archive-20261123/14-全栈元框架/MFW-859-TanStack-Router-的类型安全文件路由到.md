---
title: [MFW-859] TanStack Router 的类型安全文件路由到 routeTree.gen.ts 是怎么生成的
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-859：TanStack Router 的类型安全文件路由到 routeTree.gen.ts 是怎么生成的

**答**：
- 结论：构建期扫描 routes 目录，把文件路径映射为嵌套路由树，生成带精确类型的 routeTree.gen.ts（每个路由的 params / loaderData / search 类型）。
- 与 RRv7 typegen 差异：TanStack「文件即类型源」+ 生成代码参与编译，search params 也强类型，推导更强。
- 追问钩子：生成文件要不要提交？——通常提交以保证 IDE 即时类型与 CI 可复现，或用 CI 校验「生成后无 diff」。

```javascript
// 目录：routes/__root.tsx, routes/posts/$postId.tsx
// 生成：routeTree.gen.ts（示意）
export interface FileRoutesByPath {
  '/posts/$postId': {
    params: { postId: string };                     // 参数强类型
    loaderData: Post;                                // loader 返回类型
    search: { tab: 'info' | 'comments' };            // search 也强类型
  };
}
// 使用：跳转时参数类型受检
navigate({ to: '/posts/$postId', params: { postId: '42' } }); // ✓
navigate({ to: '/posts/$postId', params: {} });               // ✗ 编译报错
```
